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

        if (int(hour_minute_second[1]) == 0) or (int(hour_minute_second[1]) == 30):  # 정각
            if start_time <= real_time <= end_time:
                import ctypes
                ctypes.windll.user32.SystemParametersInfoW(20, 0, address, 0)


select_time(1700, 1800, "C:/Users/sohnc/Desktop/잡/나를 위한 배경화면/1 생산활동 시간/ 12.jpg")
select_time(1800, 1900, "C:/Users/sohnc/Desktop/잡/나를 위한 배경화면/1 생산활동 시간/ 13.jpg")
select_time(1900, 2000, "C:/Users/sohnc/Desktop/잡/나를 위한 배경화면/1 생산활동 시간/ 14.jpg")
# 1) 클래스를 이용해서 제대로 된 인스턴스를 만들 수 있는가? >> 클래스가 꼭 필요해보이진 않는다
# 2) 23시~1시 사이에 시간 문제를 해결 했는가? >> 시작 시간과 끝 시간 사이에 자정(0시)시간이 올 수 없도록 설정
# 3) 모르는 내용, 해결하고 싶은 문제를 제대로 파악했는가?
# 4) 시간체크 주기를 얼마나 할지 정했는가 >> 1시간
