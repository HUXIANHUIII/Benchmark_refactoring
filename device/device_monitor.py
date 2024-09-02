import time
from device_nvidia import NVIDIA
from device_amd import AMD
from device_sophgo import sophgoTPU

class DeviceMonitor:
    def __init__(self, opt, device_type):
        self.opt = opt
        self.device_type = device_type
        
        if self.device_type == 'NVIDIA':
            self.device = NVIDIA()

        elif self.device_type == 'AMD':
            self.device = AMD()

        elif self.device_type == 'SophgoTPU':
            self.device = sophgoTPU()


    def run_monitor(self, deviceUsage_list, start_event, stop_event):
        start_event.wait()
        print('=========Device monitor has started=========')

        while not stop_event.is_set():
            t_start = time.time()
            device_perf_info = self.device.get_device_perf_info()
            deviceUsage_list.append(device_perf_info)
            t_elapsed = time.time() - t_start
            
            time_to_sleep = max(0, self.opt.device_monitor_interval - t_elapsed)
            if time_to_sleep==0:
                print(f'{self.device_type}查询用时超过device循环监控间隔，建议降低--device_monitor_interval数值')
            time.sleep(time_to_sleep)





# 
