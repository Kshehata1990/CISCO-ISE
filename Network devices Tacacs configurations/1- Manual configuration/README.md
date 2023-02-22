# [ISE Network devices TACACS administrations](https://app.tango.us/app/workflow/dbbbcba1-330c-412e-8a83-b0c194465712?utm_source=markdown&utm_medium=markdown&utm_campaign=workflow%20export%20links)

__Creation Date:__ February 22, 2023  
__Created By:__ Karim Shehata  


TACACS+ (Terminal Access Controller Access-Control System Plus) is a security protocol that is used to provide centralized authentication, authorization, and accounting services for network devices. TACACS+ allows network administrators to control access to their network devices by using a centralized server to manage user and device authentication and authorization.

Configuring TACACS+ on network devices is a two-step process that involves making the configuration on the TACACS+ server and making the configuration on the network device itself. This document provides step-by-step guides for configuring TACACS+ on a Cisco Identity Services Engine (ISE) server, as well as on a Cisco network device.

The configuration process on the Cisco ISE server includes creating user groups and identities, adding network resources, defining policy elements, creating TACACS+ command sets and profiles, and creating policy sets. The document also includes information on how to check the status of the TACACS+ process by using the reports and live logs features in the Cisco ISE interface.

The configuration process on the network device involves setting up the TACACS+ authentication method and defining the TACACS+ server information. This document includes instructions on how to configure the TACACS+ settings on a Cisco switch.

By following the instructions in this document, network administrators can configure TACACS+ on their network devices to improve security, manage access to devices, and maintain detailed logs of authentication, authorization, and accounting activities.



***
# [Cisco ISE Configuration](https://www.youtube.com/channel/UChYZfbY3bskumyaL7t0NQ4w)

### 1. Login to your CISCO ISE 


### 2. Navigate to Work Center >> Device Administration >>> User Identity Groups
![Step 2 screenshot](https://images.tango.us/workflows/dbbbcba1-330c-412e-8a83-b0c194465712/steps/a39b7182-a2b4-465a-a3b8-1274e03c6376/261e7ed5-9dae-477b-8969-ae2ce1d18f17.png?crop=focalpoint&fit=crop&fp-x=0.5000&fp-y=0.5000&w=1200&blend-align=bottom&blend-mode=normal&blend-x=800&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmsucG5n)


### 3. Add User Identity Groups
To ensure effective access control and management of user accounts, it is recommended to create user identity groups in your system. Depending on your organization's requirements, you may want to create multiple user identity groups. For example, you might want to create one user identity group for network administrators and another for systems administrators.

Once you have created the user identity groups, you can use them in policies to control access to specific resources and ensure that only authorized individuals are able to perform certain actions.
![Step 3 screenshot](https://images.tango.us/workflows/dbbbcba1-330c-412e-8a83-b0c194465712/steps/03736fcd-2eb6-4f39-9f91-483b8c6de907/3d24850b-d828-4630-950d-d5bc74221936.png?crop=focalpoint&fit=crop&fp-x=0.5000&fp-y=0.5000&w=1200&blend-align=bottom&blend-mode=normal&blend-x=800&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmsucG5n)


### 4. Navigate to Identities and Click Add 
In addition to creating user identity groups for network and system administrators, you may also want to create separate user accounts for network access and for the administrators themselves.

By creating separate user accounts for network access and for the administrators, you can ensure that each user has access only to the resources and permissions that they need to perform their tasks. This can help improve security and reduce the risk of unauthorized access
![Step 4 screenshot](https://images.tango.us/workflows/dbbbcba1-330c-412e-8a83-b0c194465712/steps/5fa13cb1-8a47-4c73-8230-db59a4fd4d29/f3c5778d-24ad-468e-b09c-463137d50c1f.png?crop=focalpoint&fit=crop&fp-x=0.5000&fp-y=0.5000&w=1200&blend-align=bottom&blend-mode=normal&blend-x=800&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmsucG5n)


### 5. Assign user group
Remember to assign the appropriate user identity group to each user account so that they are subject to the same access policies and controls as others in their role.
![Step 5 screenshot](https://images.tango.us/workflows/dbbbcba1-330c-412e-8a83-b0c194465712/steps/fd81d406-4e39-4dbe-b8f9-d61ff644650d/ffb51a65-0add-492b-8dae-4a077565374c.png?crop=focalpoint&fit=crop&fp-x=0.3992&fp-y=0.7374&fp-z=2.0000&w=1200&blend-align=bottom&blend-mode=normal&blend-x=800&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmsucG5n)


### 6. Navigate to Network Resources >> Network Device Groups
After creating user accounts and user identity groups, you can start adding network resources to your system. To make it easier to manage and segregate your network devices, it is recommended to create network device groups.

In this example, we will assume that you want to add edge switches to your system and create two different device groups based on their location: HQ and Branch.

By creating device groups based on location or other relevant criteria, you can improve the organization and management of your network resources. This can help reduce the risk of errors or misconfigurations and make it easier for administrators to perform their tasks.
![Step 6 screenshot](https://images.tango.us/workflows/dbbbcba1-330c-412e-8a83-b0c194465712/steps/a686eb6a-b562-4ece-9ae7-43401c7efd13/e1d81d66-a9bc-4be0-a247-a0a00925b482.png?crop=focalpoint&fit=crop&fp-x=0.5000&fp-y=0.5000&w=1200&blend-align=bottom&blend-mode=normal&blend-x=800&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmsucG5n)


### 7. Navigate to Network Resources >> Network Devices
Once you have created the device groups, you can start adding network devices to each group
![Step 7 screenshot](https://images.tango.us/workflows/dbbbcba1-330c-412e-8a83-b0c194465712/steps/fc3eee8b-09b5-4dcb-8bd2-ab461eff9d6f/83e40b5f-cf86-4c5c-b70d-08f2e2ee9eea.png?crop=focalpoint&fit=crop&fp-x=0.5000&fp-y=0.5000&w=1200&blend-align=bottom&blend-mode=normal&blend-x=800&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmsucG5n)


### 8. Check to enable TACACS Authentication Settings
It is important to ensure that the TACACS+ key that you enter on the network device is the same key that you configured on your TACACS+ server. This will ensure that the device is successfully authenticated and authorized by the server.
![Step 8 screenshot](https://images.tango.us/workflows/dbbbcba1-330c-412e-8a83-b0c194465712/steps/6633440d-d653-4e12-a658-460036949a4a/b9e28a69-6b74-4d8f-a1bc-5c801c140504.png?crop=focalpoint&fit=crop&fp-x=0.5394&fp-y=0.7500&fp-z=2.0000&w=1200&blend-align=bottom&blend-mode=normal&blend-x=800&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmsucG5n)


### 9. Navigate to Policy Elements >> Library conditions
After completing the configuration of user identities and network resources, you can start creating policy elements and conditions to be used in your authentication and authorization policies.

Policy elements and conditions are used to define the attributes and characteristics of users and network resources, such as their roles, locations, device types, and other relevant criteria. These attributes can then be used in your policies to determine which users or devices are granted access to which resources.
![Step 9 screenshot](https://images.tango.us/workflows/dbbbcba1-330c-412e-8a83-b0c194465712/steps/d8932562-85e7-437e-b5b5-b656d687492a/ae32aa4c-28b5-444e-9426-fb3587e1733b.png?crop=focalpoint&fit=crop&fp-x=0.2452&fp-y=0.4042&fp-z=2.0395&w=1200&blend-align=bottom&blend-mode=normal&blend-x=800&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmsucG5n)


### 10. Here is an example of Device type
![Step 10 screenshot](https://images.tango.us/workflows/dbbbcba1-330c-412e-8a83-b0c194465712/steps/8920c2b7-2548-4b9b-92f3-01c2b231f164/5c7a1a7d-47a2-40bf-8159-655d2efc2251.png?crop=focalpoint&fit=crop&fp-x=0.5503&fp-y=0.4985&fp-z=2.0000&w=1200&blend-align=bottom&blend-mode=normal&blend-x=800&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmsucG5n)


### 11. Here is an example of User Identity
![Step 11 screenshot](https://images.tango.us/workflows/dbbbcba1-330c-412e-8a83-b0c194465712/steps/fdef793c-74c2-4b6f-a5a7-6bbb3737041c/33f27e4d-bbe1-4b75-8de0-5cf338807dec.png?crop=focalpoint&fit=crop&fp-x=0.3178&fp-y=0.6548&fp-z=3.0000&w=1200&blend-align=bottom&blend-mode=normal&blend-x=800&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmsucG5n)


### 12. Navigate to Policy Elements >> TACACS+ command sets
Once you have created the policy element conditions, you can start creating TACACS+ command sets. TACACS+ command sets contain a set of commands that can be performed on a network device, and they are used to define the level of access that a user is granted.

By creating TACACS+ command sets, you can define the level of access that a user is granted on a network device. For example, you might create a full privilege command set for network administrators and a show commands only command set for network operators. This can help ensure that users have the appropriate level of access to perform their tasks, while also reducing the risk of unauthorized access or misconfigurations.
![Step 12 screenshot](https://images.tango.us/workflows/dbbbcba1-330c-412e-8a83-b0c194465712/steps/12176de1-6183-4ef7-86f6-874283e221a3/043c5e92-a265-4519-9e0f-45e89668dd2a.png?crop=focalpoint&fit=crop&fp-x=0.5000&fp-y=0.5000&w=1200&blend-align=bottom&blend-mode=normal&blend-x=800&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmsucG5n)


### 13. Here is an example of a full privilege TACACS+ command set
![Step 13 screenshot](https://images.tango.us/workflows/dbbbcba1-330c-412e-8a83-b0c194465712/steps/b25ddaa2-b9cf-4b55-8c35-25f3beff7cca/59083dcb-8102-4abb-900d-3ba9d3ccf778.png?crop=focalpoint&fit=crop&fp-x=0.5000&fp-y=0.5000&w=1200&blend-align=bottom&blend-mode=normal&blend-x=800&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmsucG5n)


### 14. Here is an example of a Show privilege TACACS+ command set
![Step 14 screenshot](https://images.tango.us/workflows/dbbbcba1-330c-412e-8a83-b0c194465712/steps/55176bf4-a73b-4160-99cf-c38550aa0b94/cc3f4725-377a-4897-b87e-750143f078b5.png?crop=focalpoint&fit=crop&fp-x=0.5000&fp-y=0.5000&w=1200&blend-align=bottom&blend-mode=normal&blend-x=800&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmsucG5n)


### 15. Navigate to Policy Elements >> TACACS Profiles
After creating policy elements conditions and TACACS+ command sets, the next step is to create TACACS+ profiles . By default, you can use default shell profile. However, it is recommended that you create new profiles for your different user groups, rather than modifying the default shell profile. This will help you to keep track of which profile is associated with which user group, and make it easier to manage and update your TACACS+ policies in the future.
![Step 15 screenshot](https://images.tango.us/workflows/dbbbcba1-330c-412e-8a83-b0c194465712/steps/af95b209-e386-4377-ae7c-08a87c07f2a0/e5a1caa2-11d9-4bd1-88d1-1f1db1d1faf3.png?crop=focalpoint&fit=crop&fp-x=0.5000&fp-y=0.5000&w=1200&blend-align=bottom&blend-mode=normal&blend-x=800&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmsucG5n)


### 16. Here is an example of a Full privilege TACACS Profile
![Step 16 screenshot](https://images.tango.us/workflows/dbbbcba1-330c-412e-8a83-b0c194465712/steps/181f671f-e570-43b1-8c05-22eef93bf163/82206c61-8067-44f2-a363-77c31762e5ae.png?crop=focalpoint&fit=crop&fp-x=0.5000&fp-y=0.5000&w=1200&blend-align=bottom&blend-mode=normal&blend-x=800&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmsucG5n)


### 17. Here is an example of a SHOW privilege TACACS Profile
![Step 17 screenshot](https://images.tango.us/workflows/dbbbcba1-330c-412e-8a83-b0c194465712/steps/b3f00cee-5a8b-43f0-9a89-16bf2292d980/e93389a3-eaea-4212-b4db-020bd9c395ee.png?crop=focalpoint&fit=crop&fp-x=0.5000&fp-y=0.5000&w=1200&blend-align=bottom&blend-mode=normal&blend-x=800&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmsucG5n)


### 18. Navigate to Device Admin policy Sets and create new policy
After creating the policy elements, command sets, and TACACS+ profiles, the next step is to create policy sets that combine all of these attributes and conditions into a comprehensive policy. Policy sets are used to define the specific conditions and attributes that should be used for a particular group of users or devices. For example, you might create a policy set that applies to all network administrators, which includes a specific TACACS+ command set, authentication policies, and authorization policies. By creating policy sets, you can define the specific conditions and attributes that should be used for a particular group of users or devices.
![Step 18 screenshot](https://images.tango.us/workflows/dbbbcba1-330c-412e-8a83-b0c194465712/steps/9a1ab8d9-39fa-481e-ad10-fd02381d576a/2c7cbf8b-8c51-4325-b99c-e2411d0b3972.png?crop=focalpoint&fit=crop&fp-x=0.5000&fp-y=0.5000&w=1200&blend-align=bottom&blend-mode=normal&blend-x=800&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmsucG5n)


### 19. Click on  Authentication Policy (2)
![Step 19 screenshot](https://images.tango.us/workflows/dbbbcba1-330c-412e-8a83-b0c194465712/steps/7635bb89-694e-4164-a8cb-dc504ff1d907/86ce6711-a003-4a0a-896e-72ce8ff2295c.png?crop=focalpoint&fit=crop&fp-x=0.5000&fp-y=0.5000&w=1200&blend-align=bottom&blend-mode=normal&blend-x=800&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmsucG5n)


### 20. Here is an example of an Authentication policy
![Step 20 screenshot](https://images.tango.us/workflows/dbbbcba1-330c-412e-8a83-b0c194465712/steps/ac42d02d-b98a-4d87-828e-6cb815f27c89/63ce9c51-1d47-42a0-bd52-56ff2b809505.png?crop=focalpoint&fit=crop&fp-x=0.5000&fp-y=0.5000&w=1200&blend-align=bottom&blend-mode=normal&blend-x=800&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmsucG5n)


### 21. Here is an examples of an Authorization policy
![Step 21 screenshot](https://images.tango.us/workflows/dbbbcba1-330c-412e-8a83-b0c194465712/steps/4a4af820-80d9-4b26-8e27-539b447060e4/2caddc03-c86b-46f8-b1ea-2b216b322f66.png?crop=focalpoint&fit=crop&fp-x=0.5000&fp-y=0.5000&w=1200&blend-align=bottom&blend-mode=normal&blend-x=800&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmsucG5n)

***
# [Cisco Switch Configuration](https://www.youtube.com/channel/UChYZfbY3bskumyaL7t0NQ4w)
 
# Before starting switch configuration, please take the following precautions
1.  Ensure that the configuration is being done by a local user with level 15 privileges.  
2.  Write the memory to save the current configuration.
3.  Export a configuration backup.   
4.  Execute the command "reload in 10" as a precaution if the configuration fails.  
5.  Confirm that the ISE configuration is complete and accurate.
    
Additionally, it is recommended that switch configuration be performed after office hours to minimize disruption to normal operations. Failure to take these precautions can result in data loss, system downtime, or other unforeseen issues. Please proceed with caution and consult with a qualified expert if needed


### 23. Define TACACS Servers, secret key and group for new command sets
```
tacacs server ise 
address ipv4 <ISE_IP> 
key <tacas_key> 
exit 
! 
aaa group server tacacs+ ISE-TACACS 
server name ise 
ip tacacs source-interface <interface_name> 
exit 
!
```

### 24. Define TACACS Servers, secret key and group for old command sets
```
tacacs-server host <ISE_IP>
tacacs-server key <tacas_key>
aaa group server tacacs+ ISE-TACACS
server <ISE_IP>
ip tacacs source-interface <interface_name>
exit
!
```

### 25. Define AAA servers list for remote login
```
aaa authentication enable default enable
aaa authorization config-commands
aaa authentication login VTY-LOGIN local group ISE-TACACS
aaa authorization exec VTY-LOGIN local group ISE-TACACS
aaa authorization commands 0 VTY-LOGIN local group ISE-TACACS if-authenticated
aaa authorization commands 1 VTY-LOGIN local group ISE-TACACS if-authenticated
aaa authorization commands 15 VTY-LOGIN local group ISE-TACACS if-authenticated
aaa accounting exec VTY-LOGIN start-stop group ISE-TACACS
aaa accounting commands 0 VTY-LOGIN start-stop group ISE-TACACS
aaa accounting commands 1 VTY-LOGIN start-stop group ISE-TACACS
aaa accounting commands 15 VTY-LOGIN start-stop group ISE-TACACS
!
```

### 26. Define AAA servers list for console login
```
aaa authentication login con-login local group ISE-TACACS
aaa authorization exec con-login local
aaa authorization commands 0 con-login group ISE-TACACS local if-authenticated
aaa authorization commands 1 con-login group ISE-TACACS local if-authenticated
aaa authorization commands 15 con-login group ISE-TACACS local if-authenticated
!
```

### 27. Apply AAA configuration on console login
```
line con 0
accounting commands 0 VTY-LOGIN
accounting commands 15 VTY-LOGIN
accounting exec VTY-LOGIN
logging synchronous
login authentication con-login
authorization commands 15 con-login
authorization exec con-login
exit
!
```

### 28. Apply AAA configuration on VTY lines
```
line vty 0 4
authorization commands 15 VTY-LOGIN
authorization exec VTY-LOGIN
accounting commands 0 VTY-LOGIN
accounting commands 15 VTY-LOGIN
accounting exec VTY-LOGIN
logging synchronous
transport input ssh
login authentication VTY-LOGIN
exit
!
line vty 5 15
authorization commands 15 VTY-LOGIN
authorization exec VTY-LOGIN
accounting commands 0 VTY-LOGIN
accounting commands 15 VTY-LOGIN
accounting exec VTY-LOGIN
logging synchronous
transport input ssh
login authentication VTY-LOGIN
exit
!
```

### 29. Test Configuration with ISE username and password
```
test aaa group ISE-TACACS <ise_username> <ise_password> legacy
```

### 30. if Attempting authentication test to server-group ISE-TACACS using tacacs+ was successfully authenticated 
```
reload cancel
write memory
```

### 31. To verify the configuration Navigate to Reports >> Device Administration Reports
Once you have finished the configuration on your TACACS+ server using Cisco ISE, you can use the Reports section and live logs to verify that the configuration is working correctly.

In the Reports section, you can view reports on authentication and authorization activities, as well as reports on TACACS+ device administration activity. You can use these reports to identify any issues or errors that may be occurring in the TACACS+ process.

To view live logs, you can navigate to the Operations tab in the Cisco ISE interface and then click on the TACACS+ option. From there, you can select the option to view live logs. The live logs provide real-time information on TACACS+ authentication and authorization activity, including successful and failed login attempts.

By regularly reviewing the reports and live logs, you can ensure that your TACACS+ server is working correctly and identify any issues or errors as soon as they occur. This can help you quickly resolve any problems and maintain the security and integrity of your network.
![Step 31 screenshot](https://images.tango.us/workflows/dbbbcba1-330c-412e-8a83-b0c194465712/steps/feab3cab-97f8-40b9-be7e-fc2aba719f97/6d4812bb-4e56-43c9-a6f4-52498265cd1b.png?crop=focalpoint&fit=crop&fp-x=0.5000&fp-y=0.5000&w=1200&blend-align=bottom&blend-mode=normal&blend-x=800&blend64=aHR0cHM6Ly9pbWFnZXMudGFuZ28udXMvc3RhdGljL21hZGUtd2l0aC10YW5nby13YXRlcm1hcmsucG5n)


***

