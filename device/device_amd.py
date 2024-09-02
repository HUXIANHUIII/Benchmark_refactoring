from device_base import Device
import sys

class AMD(Device):
    def __init__(self):

        sys.path.append("/opt/rocm/libexec/self.rocm_smi/")
        try:
            import rocm_smi 
        except ImportError:
            raise ImportError("Could not import /opt/rocm/libexec/rocm_smi/rocm_smi.py")

        rocm_smi.initializeRsmi()
        self.rocm_smi = rocm_smi
        self.devices = rocm_smi.listdevices()

        super().__init__()

    def get_device_info(self) -> list:
        (memory_usage, memTotal) = self.rocm_smi.getMemInfo(self.devices[0], "vram")
        device_memory = float(memTotal) / 1024 / 1024  # MB
        device_name = 'Sophgo'+ self.rocm_smi.getDeviceName(self.devices[0])

        return [device_name, device_memory]

    def get_device_perf_info(self) -> list:
        utilization = float(self.rocm_smi.getGpuUse(self.devices[0]))
        (memory_usage, memTotal) = self.rocm_smi.getMemInfo(self.devices[0], "vram")
        memory_usage = float(memory_usage) / 1024 / 1024  # MB
        power_draw = float(self.rocm_smi.getPower(self.devices[0])['power'])

        return [utilization, memory_usage, power_draw]
