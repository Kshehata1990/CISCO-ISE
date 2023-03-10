 

***
# Cisco ISE switches onboarding readiness guide

## Table  of  Contents 
- [Introduction](#Introduction)
- [Cisco ISE Preparation](#cisco-ise-configuration)
- [Cisco Switch Preparation](#cisco-switch-configuration)
- [ON-Boarding requirements](#file-requirements)
- [Installation and Usage](#installation)
- [Conclusion](#conclusion)


<div align="right">
<a href="https://youtube.com/@ArabHackSploit/"> 
 <em>Created By: Karim Shehata 26 FEB 2023</em>
</a> 
</div>

***

## Introduction <a name="Introduction"></a>  
<p align="justify">
 
This project aims to facilitate the process of onboarding Cisco switches to Cisco ISE for network device administration using TACACS+ through automation using Python code. For organizations with a large number of switches, this can greatly improve efficiency and reduce the likelihood of errors and inconsistencies.

It is important to note that before attempting to automate the process, it is highly recommended to start by adding at least one switch manually and following <a href="https://github.com/Kshehata1990/CISCO-ISE/blob/main/Network devices Tacacs configurations/1- Manual configuration/README.md"> manual configuration guide </a> provided in this repository. This will help ensure that the process is properly understood and that any issues are identified and addressed early on.

This document provides a comprehensive guide on the prerequisite preparations required to onboard Cisco switches to Cisco ISE using a Python script. The document outlines the steps necessary to prepare the environment, Cisco switches, and Cisco ISE for the onboarding process, including configuring the necessary settings and setting up the required credentials.

To successfully run the Python script, it is essential to ensure that the environment is appropriately configured and that the Cisco switches and Cisco ISE are correctly set up. This document provides step-by-step instructions for preparing the environment, configuring the Cisco switches, configuring Cisco ISE, and running the Python script.
  
</p>  

***   

## Cisco  ISE  Preparation  <a name="cisco-ise-configuration"></a>  
<p align="justify">
Enabling external RESTful services on Cisco ISE is essential for allowing the Python script to interact with Cisco ISE and perform necessary tasks such as creating network access devices and managing policies.

Creating a user with the appropriate group permissions is crucial to ensure that the Python script has the necessary permissions to access and modify Cisco ISE's settings.

Performing a basic readiness test allows you to verify that the RESTful service is properly configured and that the user has the appropriate permissions to perform the required tasks.

In this section of the document, you will find step-by-step instructions with screenshots for configuring Cisco ISE, including enabling external RESTful services, creating a user with the appropriate group permissions, and performing a basic readiness test. By following these instructions, you will be able to configure Cisco ISE to work with the Python script and onboard your Cisco switches successfully.  
</p>

### 1. Login to Cisco ISE and navigate to Administration >> Settings

![Step 3 screenshot](https://images.tango.us/workflows/875f1bff-2400-482c-8055-8a6bc3ee3d9f/steps/52123f06-c2de-4f51-acc4-965597a30789/b8ff98c2-df45-4be6-8b3c-f52ec3e6adf8.png?crop=focalpoint&fit=crop&fp-x=0.5000&fp-y=0.5000&w=1200&blend-align=bottom&blend-mode=normal&blend-x=800&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmsucG5n)


### 2. Go to ERS Settings and enable ERS Setting for primary administration node

![Step 4 screenshot](https://images.tango.us/workflows/875f1bff-2400-482c-8055-8a6bc3ee3d9f/steps/c5b6936d-8a00-432a-90e0-9ceb0ad9b331/1541214c-9f9b-4f47-964d-115f62d668e5.png?crop=focalpoint&fit=crop&fp-x=0.5000&fp-y=0.5000&w=1200&blend-align=bottom&blend-mode=normal&blend-x=800&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmsucG5n)


### 3. Navigate to Admin Access >> Admin Groups >> ERS Admin

![Step 5 screenshot](https://images.tango.us/workflows/875f1bff-2400-482c-8055-8a6bc3ee3d9f/steps/08702983-c861-4ea2-bde5-1aaa4fefddab/4fe81084-4faf-4a36-9935-21c7adcf2756.png?crop=focalpoint&fit=crop&fp-x=0.5000&fp-y=0.5000&w=1200&blend-align=bottom&blend-mode=normal&blend-x=800&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmsucG5n)


### 4. Add user to the ERS admin group and save the configuration

![Step 6 screenshot](https://images.tango.us/workflows/875f1bff-2400-482c-8055-8a6bc3ee3d9f/steps/baebbba0-c6e8-456c-bf84-51e6930506ea/568c6a46-a3a3-472f-90fe-d7bb6807f5ea.png?crop=focalpoint&fit=crop&fp-x=0.5000&fp-y=0.5000&w=1200&blend-align=bottom&blend-mode=normal&blend-x=800&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmsucG5n)


### 5. Access ERS SDK on "https://ise:9060/ers/sdk"

![Step 7 screenshot](https://images.tango.us/workflows/875f1bff-2400-482c-8055-8a6bc3ee3d9f/steps/7fc120ec-3520-4e3e-bb20-5f0cb99901ce/1e4c6a5d-ee71-47df-90c5-d0e9c31715df.png?crop=focalpoint&fit=crop&fp-x=0.5000&fp-y=0.5000&w=1200&blend-align=bottom&blend-mode=normal&blend-x=800&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmsucG5n)


### 6. Verify the configuration by Postman and python script  
```python
import requests

url = "https://<ISE-IP>:9060/ers/config/networkdevice"
headers = {'Accept': 'application/json'}
response = requests.request("GET", url, headers=headers,  verify=False, auth=('<ERS_ADMIN_username>', '<ERS_ADMIN_password>'))
print(response.text)
```
![Step 8 screenshot](https://images.tango.us/workflows/875f1bff-2400-482c-8055-8a6bc3ee3d9f/steps/720ec1d8-6083-4485-947f-cc692e5ae231/72186a46-e6b6-4714-8256-6394b246d081.png?crop=focalpoint&fit=crop&fp-x=0.5000&fp-y=0.5000&w=1200&blend-align=bottom&blend-mode=normal&blend-x=800&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmsucG5n)  

***


## Cisco Switch Preparation  <a name="cisco-switch-configuration"></a>  
<p align="justify"> 
Cisco switches should be prepared for onboarding by configuring the necessary settings. Remote accessibility via SSH should be enabled, and a local user account for configuration purposes should be created. Additionally, it is recommended that the local user account is set up to log in directly to exec mode and not enable mode.

If a local user account is not present on the Cisco switch, a Python script can be used to create one. This ensures that a user account with the appropriate permissions is in place to configure the switch.
</p>  

###  Python script to add local user on the switches  
```python
from netmiko import ConnectHandler

first_switch_ip = '<switch_IP>'
last_switch_ip = '<switch_IP>'
ip_list = [".".join(first_switch_ip.split(".")[:3]) + "." + str(i) for i in
           range(int(first_switch_ip.split(".")[-1]), int(last_switch_ip.split(".")[-1]) + 1)]
for ip in ip_list:
    try:
 
        if ip in [<list of ips you want to execlude>]:
            continue
        else:
            print(f'configuring username and password for {ip}')
            local_username = "<>"
            locol_password = "<>"
            login_username = '<>'
            login_password = '<>'
            switch = {'device_type': 'cisco_ios', 'ip': ip, 'username': login_username,'password': login_password}
            connect_to_switch = ConnectHandler(**switch)
            connect_to_switch.send_command('configure terminal', expect_string=r"#")
            connect_to_switch.send_command(f'username {local_username} privilege 15 secret {local_password}', expect_string=r"#",strip_prompt=False)
            connect_to_switch.disconnect()
            
    except Exception as error:
        print(error)
        continue
```

***  

## ONBoarding requirements file  <a name="file-requirements"></a>  

### Before running the Python script to onboard your Cisco switches to Cisco ISE, you need to ensure that you have the following prerequisites in place:
<p align="justify">

${\textcolor{green} {1. \ Configuration \ backup \ folder:}}$ The folder where the switch configurations will be backed up before and after the deployment process is specified.    
${\textcolor{green} {2. \ Switches \ Local \ Username:}}$ The username of a local user account on the switch with privilege level 15 is required.    
${\textcolor{green} {3. \ Switches \ Local \ User \ Password:}}$  The password for the local user account on the switch is necessary.    
${\textcolor{green} {4. \ Switches \ Source \ Interface \ VLAN:}}$ The VLAN interface on the switch that will be used to communicate with Cisco ISE must be defined.   
${\textcolor{green} {5. \ ACS \ Username:}}$ The username for the Cisco ACS or local user account used to authenticate users and devices needs to be provided.  
${\textcolor{green} {6. \ ACS \ Password:}}$ The password for the Cisco ACS or local user account must be specified.  
${\textcolor{green} {7. \ TACACS \ Key:}}$ The secret key used for TACACS+ authentication between the switch and Cisco ISE should be defined.  
${\textcolor{green} {8. \ ISE \ IP \ Address:}}$ The IP address for the Cisco ISE must be provided and should be reachable from the switch.  
${\textcolor{green} {9. \ ISE \ ERSADMIN \ Username:}}$ The ERSADMIN username used to login to ISE must be defined.  
${\textcolor{green} {10. \ ISE \ ERSADMIN \ Password:}}$ The ERSADMIN password used to login to ISE should be specified.  
${\textcolor{green} {11. \ Network \ Device \ Group \ Location:}}$ The location to add the network device, keeping in mind the tree representation should be represented by the "#" sign, must be specified.  
${\textcolor{green} {12. \ Network \ Device \ Group \ Type:}}$ The type to add the network device, keeping in mind the tree representation should be represented by the "#" sign, must be defined.  
${\textcolor{green} {13. \ ISE \ TACACS \ Username \ for \ Verification:}}$ The TACACS username configured on ISE for verifying the configuration should be provided.  
${\textcolor{green} {14. \ ISE \ TACACS \ Password \ for \ Verification:}}$ The TACACS password for the configured username on ISE for verifying the configuration must be defined.  
${\textcolor{green} {15. \ Exclude \ Switch \ List:}}$ The list of switches' IP addresses to be excluded from onboarding, if any, should be provided.  
${\textcolor{green} {16. \ Start \ IP:}}$ The start IP address for the switches list must be specified.   
${\textcolor{green} {17. \ End \ IP:}}$ The end IP address for the switches list must be specified.  
 
Ensure that you have all the required parameters before running the Python script for onboarding your Cisco switches to Cisco ISE . Failure to provide these parameters may result in errors or unsuccessful onboarding of the switches. 
</p>   

***  

## Installation and Usage <a name="installation"></a>
  
 This project aims to facilitate the process of onboarding Cisco switches to Cisco ISE for network device administration using TACACS+ through automation using Python code. For organizations with a large number of switches, this can greatly improve efficiency and reduce the likelihood of errors and inconsistencies.

It is important to note that before attempting to automate the process, it is highly recommended to start by adding at least one switch manually and following <a href="https://github.com/Kshehata1990/CISCO-ISE/blob/main/Network devices Tacacs configurations/1- Manual configuration/README.md"> manual configuration guide </a> provided in this repository. This will help ensure that the process is properly understood and that any issues are identified and addressed early on.  

To install this project, you need to have Python 3 and the requests library installed on your system. You also need to have access to a Cisco ISE server with administrator credentials.  
 
![code trace](https://github.com/Kshehata1990/CISCO-ISE/blob/main/Network%20devices%20Tacacs%20configurations/2-Configuration%20Automation/1-%20ISE%20switches%20onboarding%20code%20trace.png)  

 

### To install this project, clone this repository and run the following command:

```bash
pip install -r requirements.txt  
```

### update the onboarding requirements json file 

```json  
{
  "config_backup_folder": "<backup folder to save the configuration before and after deployment>",
  "switches_local_username": "<username of a local user with privilege 15>",
  "switches_local_user_password": "<password of a local user>",
  "switches_source_interface_vlan": "<sitches interface vlan to communicate with ise(SVI name)>",
  "ACS_username": "<cisco acs  or local username>",
  "ACS_password": "<cisco acs or local password>",
  "TACACS_KEY": "<tacacs secret key>",
  "ISE_IP": "<ISE ip address and must be reachable from the switch>",
  "ISE_ERSADMIN_username": "<ERSADMIN username to login to ISE>",
  "ISE_ERSADMIN_password": "<ERSADMIN password to login to ISE>",
  "network_device_group_location": "<location you which to add the network device keep in mind the tree representation should be represented by '#' sign EX: #HQ#EdgeSW>",
  "network_device_group_type": "<type you which to add the network device keep in mind the tree representation should be represented by '#' sign EX: #Cisco#EdgeSW>",
  "ISE_TACACS_username_check": "<TACACS username configured on ISE for verifying the configuration>",
  "ISE_TACACS_password_check": "<TACACS password for the configured username on ISE for verifying the configuration>",
  "exclude_switch_list":"<list of switches ips to be excluded from onboarding EX: ['1.1.1.1','1.1.1.2']>",
  "start_ip": "<switches list start ip>",
  "end_ip": "<switches list start ip>"
 }  
```

### Run the ise onboarding python file
```bash 
cd Network devices Tacacs configurations/2-Configuration Automation
python3 ISE-ONboarding.py  
```  

***
 
## Conclusion <a name="conclusion"></a>
<p align="justify">
Onboarding Cisco switches to Cisco ISE using a Python script requires careful preparation to ensure a smooth and successful onboarding process. This document has provided comprehensive guidelines for the prerequisite preparations required before running the Python script, including preparing the environment, configuring the Cisco switches, and configuring Cisco ISE.

To prepare the environment for the Python script, it is essential to install the necessary Python packages, configure network connectivity, and set up the required credentials. Configuring the Cisco switches involves enabling remote access via SSH, creating a local user account, and setting up necessary certificates. Configuring Cisco ISE involves enabling external RESTful services, creating a user with the appropriate group permissions, and performing a basic readiness test.

By following the instructions provided in this document, you can configure the necessary settings and credentials, ensuring a smooth onboarding experience. Additionally, the document includes troubleshooting tips for common issues that may arise during the onboarding process.

In conclusion, following the guidelines outlined in this document will help you successfully onboard your Cisco switches to Cisco ISE using a Python script. 
</p>

***  
 
<div align="center">
  <a href="https://www.linkedin.com/in/karim-shehata-74b15b178/"><img src="https://img.icons8.com/color/48/000000/linkedin.png"/></a>
  <a href="https://www.youtube.com/c/ArabHackSploit"><img src="https://img.icons8.com/color/48/000000/youtube-play.png"/></a>
</div>

***



