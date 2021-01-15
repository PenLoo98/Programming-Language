global start_time, end_time


class back_changer:
    def __init__(self):
        self.start_time = start_time
        self.end_time = end_time

    def choose_time(self, s_time, e_time, address):
        start_time = s_time
        end_time = e_time

        import time  # 현재시간 파악
        current_time = time.strftime('%X', time.localtime(time.time()))
        hour_minute_second = current_time.split(":")
        real_time = int(hour_minute_second[0] + hour_minute_second[1])

        if start_time <= real_time <= end_time:
            import ctypes
            ctypes.windll.user32.SystemParametersInfoW(20, 0, address, 0)
        elif real_time <= end_time:
            import ctypes
            ctypes.windll.user32.SystemParametersInfoW(20, 0, address, 0)
        elif start_time <= real_time:
            import ctypes
            ctypes.windll.user32.SystemParametersInfoW(20, 0, address, 0)
        else:
            pass
