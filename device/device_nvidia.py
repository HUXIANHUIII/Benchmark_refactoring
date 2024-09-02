from device_base import Device

class AMD(Device):
    def __init__(self):

        import pynvml

        self.pynvml = pynvml
        self.pynvml.nvmlInit() 
        self.device = self.pynvml.nvmlDeviceGetHandleByIndex(0)  
        super().__init__()

    def __del__(self):

        self.pynvml.nvmlShutdown()

    def get_device_info(self) -> list:

        device_name = self.pynvml.nvmlDeviceGetName(self.device)
        device_memory = self.pynvml.nvmlDeviceGetMemoryInfo(self.device).total / 1024 / 1024  # MB

        return [device_name, device_memory]

    def get_device_perf_info(self) -> list:

        memory_usage = self.pynvml.nvmlDeviceGetMemoryInfo(self.device).used / 1024 / 1024  # MB
        utilization = self.pynvml.nvmlDeviceGetUtilizationRates(self.device).gpu
        power_draw = self.pynvml.nvmlDeviceGetPowerUsage(self.device) / 1000.0  # W

        return [utilization, memory_usage, power_draw]
