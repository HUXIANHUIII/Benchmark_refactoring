from enum import Enum
import subprocess

class DeviceType(Enum):
    NVIDIA = 'NVIDIA'
    AMD = 'AMD'
    SophgoTPU = 'SophgoTPU'
    UNKNOWN = 'Unknown'

def check_device_type():
    device_commands = {
        DeviceType.NVIDIA: ['nvidia-smi'],
        DeviceType.AMD: ['rocm-smi'],
        DeviceType.SophgoTPU: ['bm-smi', '--start_dev=0', '--last_dev=0', '--text_format']
    }

    for device_type, command in device_commands.items():
        try:
            subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
            return device_type
        except (subprocess.CalledProcessError, FileNotFoundError):
            continue

    return DeviceType.UNKNOWN
