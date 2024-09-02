from device_base import Device
import subprocess

class sophgoTPU(Device):
    def __init__(self):

        import sophon.sail as sail
        self.sail = sail

        super().__init__()


    def get_device_info(self) -> list:

        try:
            with open('/proc/bmsophon/card0/chipid', 'r') as file:
                device_name = 'Sophgo'+file.read().strip()
        except ImportError:
            raise ImportError("Not file: /proc/bmsophon/card0/chipid")
        
        device_memory = self.sail.get_dev_stat(0)[0]

        return [device_name, device_memory]

    def get_device_perf_info(self) -> list:

        result = subprocess.run(['cat', '/proc/bmsophon/card0/board_power'], stdout=subprocess.PIPE)
        output = result.stdout.decode('utf-8').strip()
        power_draw = float(output.split()[0])
        utilization = self.sail.get_tpu_util(self.dev_id)
        memory_usage = self.sail.get_dev_stat(self.dev_id)[1]

        return [utilization, memory_usage, power_draw]
