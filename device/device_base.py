from abc import ABC, abstractmethod

class Device(ABC):
    def __init__(self):
        device_info = self.get_device_info()
        self.device_name = device_info[0]
        self.device_memory = device_info[1]

    @abstractmethod
    def get_device_info(DEVICE_TYPE) -> list:  
        """    
        return [device_name, device_memory]
        """

        pass

    @abstractmethod
    def get_device_perf_info(self) -> list:
        """
        return [utilization, memory_usage, power_draw]
        """

        pass


