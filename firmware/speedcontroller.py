import odrive
import time

from odrive.enums import *

odrv = odrive.find_any()
axis = odrv.axis0

axis.controller.config.control_mode = ControlMode.VELOCITY_CONTROL
axis.controller.config.input_mode = InputMode.PASSTHROUGH
axis.requested_state = AxisState.CLOSED_LOOP_CONTROL

axis.controller.config.vel_limit = 30.0

time.sleep(0.5)

def set_rpm(axis, rpm):
    turns_per_sec = rpm / 60.0
    axis.controller.input_vel = turns_per_sec

def get_actual_rpm(axis):
    turns_per_sec = axis.pos_vel_mapper.vel
    return turns_per_sec * 60.0

set_rpm(axis, 500)

try:
    while True:
        print(f"Target: {axis.controller.input_vel * 60:.1f} RPM | "
            f"Actual: {get_actual_rpm(axis):.1f} RPM")
        time.sleep(0.1)

finally:
    print("Stopping motor...")
    axis.controller.input_vel = 0.0
    time.sleep(0.5)
    axis.requested_state = AxisState.IDLE
    print("Motor Stopped")
