import time
from netmiko import ConnectHandler
import requests
import json
import warnings
from datetime import date


warnings.filterwarnings("ignore")


# this function is to update the switch commands sheet with the ise details
def update_line(file_name, line_num, new_text):
    lines = []
    with open(file_name, "r") as f:
        lines = f.readlines()
    lines[line_num - 1] = new_text + "\n"
    with open(file_name, "w") as f:
        f.writelines(lines)


# write the existing configuration to memory and export the configuration with old acs user account
def take_switch_backup_before_configuration(switch, backup_location):
    try:
        connect_to_switch = ConnectHandler(**switch)
        hostname = connect_to_switch.send_command('show run | include hostname', expect_string=r'#', read_timeout=40)
        switch_name = hostname.split("hostname")[1]
        print(f"Exporting switch configuration before starting for {switch_name}")
        write_result = connect_to_switch.send_command('write mem', expect_string=r'#', read_timeout=40)
        command_result = connect_to_switch.send_command('show run', expect_string=r"#", read_timeout=40)
        switch_check = open(f'{backup_location}/{str(switch["ip"])}_switch_{switch_name}_old_config_{str(switch["ip"])}_{date.today()}.txt', 'w')
        switch_check.write(command_result)
        switch_check.close()
        connect_to_switch.disconnect()
        return 'pass'

    except Exception as error:
        print('Failed to take configuration backup before starting the on boarding process with the below error:')
        print(error)
        return 'fail'


# write the existing configuration to memory and export the configuration after successfully ISE boarding check
def take_switch_backup_after_configuration(switch, backup_location):
    try:
        connect_to_switch = ConnectHandler(**switch)
        switch_name = connect_to_switch.send_command('show run | include hostname',expect_string=r"#",read_timeout=40)
        hostname = switch_name.split("hostname")[1]
        print(f"Exporting switch configuration after successfully ISE boarding check {switch_name}")
        write_result = connect_to_switch.send_command('write mem',expect_string=r'#',read_timeout=40)
        command_result = connect_to_switch.send_command('show run', expect_string=r"#",read_timeout=40)
        switch_check = open(f'{backup_location}/{str(switch["ip"])}_switch_{hostname}_new_config_{str(switch["ip"])}_{date.today()}.txt', 'w')
        switch_check.write(command_result)
        switch_check.close()
        connect_to_switch.disconnect()
        return 'pass'

    except Exception as error:
        print(error)
        return 'fail'


# remove the switch from ISE network device in case of failure
def remove_networkdevice_from_ise(ISE_IP, ISE_authorization_header, network_device_id):
    try:
        url = f"https://{ISE_IP}:9060/ers/config/networkdevice/{network_device_id}"
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
        requests.request("DELETE", url, headers=headers, auth=ISE_authorization_header, verify=False)
        print("switch removed from ISE network devices")

    except Exception as error:
        print('Failed to remove switch from ISE')
        return error


# Add switch to ISE network devices
def add_networkdevice_to_ise(switch, ISE_IP, ISE_authorization_header, TACACS_KEY, switch_group_location, switch_type_location):
    try:
        with open('network_device.json', 'r') as f:
            network_device = json.load(f)
        connect_to_switch = ConnectHandler(**switch)
        hostname = connect_to_switch.send_command('show run | include hostname', expect_string=r'#', read_timeout=40).split("hostname")[1]
        connect_to_switch.disconnect()
        print(f"Adding {hostname} switch to ISE network devices")
        # Prepare network device json file to post it to ISE
        network_device['NetworkDevice']['name'] = hostname.strip()
        network_device['NetworkDevice']['description'] = f'{hostname}-{switch["ip"]}-api'
        network_device['NetworkDevice']['NetworkDeviceIPList'][0]['ipaddress'] = switch["ip"]
        network_device['NetworkDevice']['tacacsSettings']['sharedSecret'] = TACACS_KEY
        network_device['NetworkDevice']['tacacsSettings']['previousSharedSecret'] = TACACS_KEY
        network_device['NetworkDevice']['NetworkDeviceGroupList'] = [
            f"Location#All Locations{switch_group_location}",
            "IPSEC#Is IPSEC Device#No",
            f"Device Type#All Device Types{switch_type_location}"
        ]
        url = f"https://{ISE_IP}:9060/ers/config/networkdevice"
        payload = json.dumps(network_device)
        headers = {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload, auth=ISE_authorization_header, verify=False)
        # keep the newly created network device ID in case of failure to remove it from ISE
        network_device_id = response.headers['Location'].split('networkdevice/')[1]
        if response.status_code != '400':
            return f'pass**{network_device_id}'
        else:
            return 'fail'

    except Exception as error:
        print("Failed to add network device to ISE")
        print(error)
        return 'fail'


# configure the switch with aaa commands defined in ISE-Commands file
def configure_switch_ise_aaa(switch):
    try:
        connect_to_switch = ConnectHandler(**switch)
        # this command will reload the switch in 3 min in case of failure so we can still have access to the switch
        connect_to_switch.send_command('reload in 3', expect_string=r"confirm",
                                       strip_prompt=False, strip_command=False)
        connect_to_switch.send_command('y', expect_string=r"#",
                                       strip_prompt=False, strip_command=False)
        time.sleep(3)
        connect_to_switch.send_command('configure terminal', expect_string=r"#")

        # this will start configuring the switch with the AAA new-model commands in the ISE-Commands file
        with open('ise_switch_commands.txt', 'r') as commands:
            print('Configuring the switch with the ISE-AAA commands set')
            for command in commands:
                switch_command = command.strip()
                connect_to_switch.send_command(switch_command, expect_string=r"#")

        with open('old_acs_aaa_configuration.txt', 'r') as commands:
            print('Removing old ACS-AAA configuration')
            for command in commands:
                switch_command = command.strip()
                connect_to_switch.send_command(switch_command, expect_string=r"#")

        connect_to_switch.disconnect()
        return 'pass'

    except Exception as error:
        print('Failed to run switch aaa commands the below error ,switch will reload in 3 min and switch will be removed from ISE')
        print(error)
        return 'fail'


# Check if we can now authenticate user from ISE
def sanity_check_configuration(switch, ISE_check_username, ISE_check_password):
    try:
        connect_to_switch = ConnectHandler(**switch)
        # test ISE user to check if the configuration is successful
        authentication_result = connect_to_switch.send_command(f'test aaa group ISE-TACACS {ISE_check_username} {ISE_check_password} legacy')
        if authentication_result.__contains__('successfully'):
            # cancel the  switch reload which was initiated before starting the ISE-AAA configuration
            connect_to_switch.send_command('reload cancel')
            print('##### Attempting authentication test to server-group ISE-TACACS using tacacs+ was successfully authenticated #####')
            return 'pass'
        else:
            return 'fail'

    except Exception as error:
        print('ISE user authentication failed with the below error ,switch will reload in 3 min and switch will be removed from ISE')
        print(error)
        return 'fail'


# Start the on-boarding process for the switch
def start_onboarding_process(switch_ip, onboarding_requirements):
    try:
        print("=" * 100)
        print(f"Starting configuration process for {switch_ip}")
        print("=" * 100)
        # prepare the configuration requirements from the provided information in the on-boarding requirements json file
        config_backup_folder = onboarding_requirements['config_backup_folder']
        switches_local_username = onboarding_requirements['switches_local_username']
        switches_local_user_password = onboarding_requirements['switches_local_user_password']
        ISE_IP = onboarding_requirements['ISE_IP']
        TACACS_KEY = onboarding_requirements['TACACS_KEY']
        ISE_TACACS_check_username = onboarding_requirements['ISE_username_check']
        ISE_TACACS_check_password = onboarding_requirements['ISE_password_check']
        ACS_username = onboarding_requirements['ACS_username']
        ACS_password = onboarding_requirements['ACS_password']
        ISE_authorization_header = (onboarding_requirements['ISE_username'], onboarding_requirements['ISE_password'])
        switch_group_location = onboarding_requirements['network_device_group_location']
        switch_type_location = onboarding_requirements['network_device_group_type']


        # switch details ro run ISE-AAA commands
        switch = {'device_type': 'cisco_ios', 'ip': switch_ip,
                  'username': switches_local_username, 'password': switches_local_user_password}

        # switch details to take backup before start
        switch_acs_credentials = {'device_type': 'cisco_ios', 'ip': switch_ip,
                  'username':  ACS_username, 'password': ACS_password}

        ###
        # each process will run only if the previous process succeeded
        # if any process failed at any time the configuration will be reverted
        # local username and password with privilege 15 and loging directly to the exec is required
        ###

        # start by writing the configuration to memory and take configuration backup
        if take_switch_backup_before_configuration(switch_acs_credentials, config_backup_folder) == 'pass':
            # Adding the switch to ISE network devices and save the network device id in case of reverting back
            configure_ise = add_networkdevice_to_ise(switch, ISE_IP, ISE_authorization_header, TACACS_KEY, switch_group_location, switch_type_location)
            if configure_ise.__contains__('pass'):
                network_device_id = configure_ise.split('**')[1]
                # configuring switch with ISE-AAA new-model commands as fail-safe control reload command is initiated
                if configure_switch_ise_aaa(switch) == 'pass':
                    # check if the ISE-USER provided in on-boarding requirements successfully authenticated with ISE
                    if sanity_check_configuration(switch, ISE_TACACS_check_username, ISE_TACACS_check_password) == 'pass':
                        # cancel reload , write memory, export the configuration
                        take_switch_backup_after_configuration(switch, config_backup_folder)
                    else:
                        # remove switch from ISE and the switch will reload
                        remove_networkdevice_from_ise(ISE_IP, ISE_authorization_header, network_device_id)
                        print('>>>> Check if the provided ISE username and password in the on-boarding requirements are correct <<<<')
                else:
                    # remove switch from ISE and the switch will reload
                    remove_networkdevice_from_ise(ISE_IP, ISE_authorization_header, network_device_id)
                    print('>>> Check if the provided local user credentials and privilege in the on-boarding requirements file are correct <<<<')
            else:
                print('>>>> Check if ISE details in the on-boarding requirements are correct <<<<')
        else:
            print('>>> Check if the provided ACS user credentials and privilege in the on-boarding requirements file are correct <<<<')

    except Exception as error:
        print(error)


# main on-boarding function for the switches list in requirements file
def ISE_ONboarding_switches():
    try:
        with open('onboarding_requirements.json', 'r') as f:
            onboarding_requirements = json.load(f)

        # update the ise command list with the provided information from on-boarding requirements json file
        TACACS_KEY = onboarding_requirements['TACACS_KEY']
        ISE_IP = onboarding_requirements['ISE_IP']
        source_vlan = onboarding_requirements['switches_source_interface_vlan']
        update_line("ise_switch_commands.txt", 3, f"server {ISE_IP}")
        update_line("ise_switch_commands.txt", 4, f"ip tacacs source-interface {source_vlan}")
        update_line("ise_switch_commands.txt", 8, f"ip tacacs source-interface {source_vlan}")
        update_line("ise_switch_commands.txt", 26, f"address ipv4  {ISE_IP}")
        update_line("ise_switch_commands.txt", 27, f"key {TACACS_KEY}")
        update_line("ise_switch_commands.txt", 29, f"tacacs-server host {ISE_IP}")
        update_line("ise_switch_commands.txt", 30, f"tacacs-server key {TACACS_KEY}")
        update_line("ise_switch_commands.txt", 32, f"address ipv4  {ISE_IP}")
        update_line("ise_switch_commands.txt", 33, f"key {TACACS_KEY}")

        # switches to configure for on-boarding to ISE
        excluded_switches = onboarding_requirements['exclude_switch_list']
        first_switch_ip = onboarding_requirements['start_ip']
        last_switch_ip = onboarding_requirements['end_ip']
        ip_list = [".".join(first_switch_ip.split(".")[:3]) + "." + str(i) for i in
                   range(int(first_switch_ip.split(".")[-1]), int(last_switch_ip.split(".")[-1]) + 1)]
        for ip in ip_list:
            if ip in excluded_switches:
                continue
            else:
                start_onboarding_process(ip, onboarding_requirements)

    except Exception as error:
        print('failed to start the on boarding process for switch with the below error:')
        print(error)
        print('>>>> check if all the requirements in the on-boarding process is correct <<<<')


ISE_ONboarding_switches()






