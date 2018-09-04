#일정 시간 간격으로 크롤링 및 기타 반복 작업 가능한 예제
import time
import threading

def thread_run():
    print('=====',time.ctime(),'=====')
    #######개발 하고자 하는 코드#######
    for i in range(1,10000):
        print('Thread running - ', i)
    #################################

    threading.Timer(2.5, thread_run).start() #2.5초마다 메모리가 프로세스에 상주하면서 반복실행
                                             #재귀함수

thread_run()
#threading.Timer(2, thread_run).start() : 메인에서 실행하면 1회 실행
