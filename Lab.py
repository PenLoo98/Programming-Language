global count
count = 0

while count == 0:  # 반복입력 피하기 (처음 입력시 0)
    try:  # 설정시간 입력 + 오류 보완
        start_time = int(input("시작 시간을 입력하시오 \n예)24시15분 → 0015\n:"))
        end_time = int(input("끝 시간을 입력하시오 \n예)18시50분 → 1850\n:"))

    except ValueError:  # 오류 - 글자나 공백을 입력할 경우
        print("글자 또는 공백은 입력할 수 없습니다")
        print('==================================================')
        continue

            #  입력 오류 보완
    if start_time // 10000 or end_time // 10000:  # 자릿수 4자리 초과
        print("잘못된 입력입니다")
        print('==================================================')
    else:
        count += 1  # 제대로 된 값이 입력되어 카운트 1


def time_select(s_hour_minute, e_hour_minute):
    import time  # 현재시간 파악
    T = time.strftime('%X', time.localtime(time.time()))
    hour_minute_second = T.split(":")
    hour_minute = int(hour_minute_second[0]+hour_minute_second[1])

        import ctypes
        ctypes.windll.user32.SystemParametersInfoW(20, 0, "C:/14.jpg", 0)


time_select(start_hour, start_minute, end_hour, end_minute)

    '''
        def Picture_save:
        
        def Change_Background:
            import ctypes
            ctypes.windll.user32.SystemParametersInfoW(20, 0,"C:/14.jpg" , 0)
    '''