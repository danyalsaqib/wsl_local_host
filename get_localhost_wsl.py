import subprocess

def get_localhost_wsl():
  result = subprocess.check_output("cat /etc/resolv.conf | grep nameserver | awk '{ print $2 }'", shell=True, text=True)
  result = result[:-1]
  print(result)

  return result
