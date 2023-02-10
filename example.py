from reachy_sdk import ReachySDK
from reachy_sdk.trajectory import goto
from reachy_sdk.trajectory import InterpolationMode
import time

import subprocess


def happy_antennas():
  for _ in range(7):
    reachy.head.l_antenna.goal_position = 30.0
    reachy.head.r_antenna.goal_position = -30.0
    
    time.sleep(0.2)
    
    reachy.head.l_antenna.goal_position = -30.0
    reachy.head.r_antenna.goal_position = 30.0
    
    time.sleep(0.2)
    
  reachy.head.l_antenna.goal_position = 0.0
  reachy.head.r_antenna.goal_position = 0.0

def hello_left_arm():
  left_arm_hello_position = {
    reachy.l_arm.l_shoulder_pitch: 0,
    reachy.l_arm.l_shoulder_roll: 50,
    reachy.l_arm.l_arm_yaw: 70,
    reachy.l_arm.l_elbow_pitch: -120,
    reachy.l_arm.l_forearm_yaw: 80,
    reachy.l_arm.l_wrist_pitch: 0,
    reachy.l_arm.l_wrist_roll: -40,
  }
  
  left_arm_base_position = {
    reachy.l_arm.l_shoulder_pitch: 0,
    reachy.l_arm.l_shoulder_roll: 0,
    reachy.l_arm.l_arm_yaw: 0,
    reachy.l_arm.l_elbow_pitch: 0,
    reachy.l_arm.l_forearm_yaw: 0,
    reachy.l_arm.l_wrist_pitch: 0,
    reachy.l_arm.l_wrist_roll: 0,
  }
  
  goto(
    goal_positions = left_arm_hello_position,
    duration = 1.0,
    interpolation_mode = InterpolationMode.MINIMUM_JERK
  )
  
  for _ in range(3):
    goto(
      goal_positions = {reachy.l_arm.l_wrist_roll: 20.0},
      duration = 0.5,
      interpolation_mode = InterpolationMode.LINEAR
    )
    goto(
      goal_positions = {reachy.l_arm.l_wrist_roll: -40.0},
      duration = 0.5,
      interpolation_mode = InterpolationMode.LINEAR
    )
    
  time.sleep(0.2)
  
  goto(
    goal_positions = left_arm_base_position,
    duration = 2.0,
    interpolation_mode = InterpolationMode.LINEAR
  )

def move_head():
  reachy.head.look_at(0.5, -0.3, -0.1, duration=1.0)
  time.sleep(0.3)
  reachy.head.look_at(0.5, 0.3, -0.1, duration=1.0)
  time.sleep(0.3)
  reachy.head.look_at(0.5, 0, -0.1, duration=1.0)
  time.sleep(0.3)

  head_tilted_position = {
    reachy.head.neck_roll: -20,
    reachy.head.neck_pitch: 0,
    reachy.head.neck_yaw:0,
  }

  goto(
    goal_positions = head_tilted_position,
    duration = 1.0,
    interpolation_mode = InterpolationMode.MINIMUM_JERK
  )

def say_hello():
  #move_head()
  happy_antennas()
  hello_left_arm()
  reachy.head.look_at(0.5, 0, 0, duration=0.5)

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

  say_hello()
