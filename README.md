# wsl_local_host
A python function that enables the use of Windows 'localhost' in a WSL environment

## The 'get_localhost_wsl()' function

When working within WSL (Windows Subsystem for Linux), applications that are running on Windows are generally not directly accessible via 'localhost'. This is because WSL (or WSL2) is running with a virtual network (vNIC) created by the Windows Virtual Machine Platform (a subset of Hyper-V). Inside WSL2, localhost is the address of the vNIC. The query is answered in a detailed manner within the following forum discussion: https://superuser.com/a/1679774

The answer within the forum also details that the actual windows address within WSL2 can be found by running the following command within WSL:
```
ip route
```
The "default via" address is the address to use for the Windows host. However, integrating this command directly within code and extracting the windows IP is a tedious task, especially when you consider that this IP will change every time your machine restarts.

The solution is contained within the 'get_localhost_wsl.py' file. It contains the function that can be used to extract the defacto 'localhost' value within WSL. An example of its use is also given within the 'example.py' file (please directly go to the main function at the end of the file for the example - the example of controlling the reachy robot is simply the specific case I tested the code with).

## Allowing communication between WSL and Windows

One important precursor (given within the example file's main function too) is to allow WSL to communicate with your windows applications in the first place. To do this, open a windows powershell as an administrator, and run the following command:
```
New-NetFirewallRule -DisplayName "WSL" -Direction Inbound  -InterfaceAlias "vEthernet (WSL)"  -Action Allow
```
After this, the 'get_localhost_wsl()' function should run as expected. To test whether communication between WSL and windows is actually enabled, you can run the following command within your WSL terminal:
```
ping "$(hostname).local"
```
Should this command run without any packet loss, the communication channel between WSL and windows is up and running. The function 'get_localhost_wsl()' should then hopefully run without issues.
