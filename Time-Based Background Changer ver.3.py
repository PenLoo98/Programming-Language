#   1) 시간선택을 '분' 단위까지 유동적으로 하고 싶었지만
#       프로그램의 메모리 용량상 실시간으로 시간을 확인하는 일은 메모리를 너무 많이 먹기에
#       1시간 단위로 시간을 설정하고, 체크하도록 프로그래밍 했습니다.
#   2) 24시는 'time' 라이브러리로 확인시 0000이 나오기에 시간 비교에 하는데 어려움이 있었습니다.
#       그래서 시작시간과 끝시간 사이에 자정(0시)가 올 수 없게 설정하도록 프로그래밍 했습니다.
def select_time(start_time, end_time, address):
    while True:
        import time
        current_time = time.strftime('%X', time.localtime(time.time()))
        hour_minute_second = current_time.split(":")
        real_time = int(hour_minute_second[0] + hour_minute_second[1])

        if start_time <= real_time <= end_time:
            import ctypes
            ctypes.windll.user32.SystemParametersInfoW(20, 0, address, 0)
        time.sleep(60)


#  사진 디렉토리 띄어쓰기 주의!
select_time(1700, 1800, "C:/Users/sohnc/Desktop/잡/나를 위한 배경화면/1 생산활동 시간/12.jpg")
select_time(1800, 1900, "C:/Users/sohnc/Desktop/잡/나를 위한 배경화면/1 생산활동 시간/13.jpg")
select_time(1900, 2000, "C:/Users/sohnc/Desktop/잡/나를 위한 배경화면/1 생산활동 시간/14.jpg")
