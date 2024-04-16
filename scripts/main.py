from droid.controllers.oculus_controller import VRPolicy
from droid.robot_env import RobotEnv
from droid.user_interface.data_collector import DataCollecter
from droid.user_interface.gui import RobotGUI
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-hz', '--control_hz', type=int, default=15)
args = parser.parse_args()

# Make the robot env
env = RobotEnv(control_hz=args.control_hz)
controller = VRPolicy()

# Make the data collector
data_collector = DataCollecter(env=env, controller=controller)

# Make the GUI
user_interface = RobotGUI(robot=data_collector)
