from reachy_sdk import ReachySDK
import subprocess



def get_localhost_wsl():
  result = subprocess.check_output("cat /etc/resolv.conf | grep nameserver | awk '{ print $2 }'", shell=True, text=True)
  result = result[:-1]
  print(result)

  return result


if __name__ == "__main__":
  # First, run Windows Powershell as an administrator, and run the following command: 
  ### New-NetFirewallRule -DisplayName "WSL" -Direction Inbound  -InterfaceAlias "vEthernet (WSL)"  -Action Allow
  
  # The following command is how the line is supposed to be run without WSL. However, for WSL, the 'get_localhost_wsl()' is used to get the defacto 'localhost'
  # reachy = ReachySDK(host='localhost') # replace with correct IP if the simulation is not on your computer
   
  ip_address = get_localhost_wsl()
  reachy = ReachySDK(host=ip_address) # Find IP in WSL by running 'ip route' command in the terminal, and looking for the 'default via' value
