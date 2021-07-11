from time import sleep

from threading import Timer

def SleepSort(value):
    SleepSort.results = []

    mx = value[0]
    def add(x):
        SleepSort.results.append(x)
    for i in value:
        if i>mx:
            mx = i
        Timer(i,add,[i]).start()
    sleep(mx+1)
    return SleepSort.results
if __name__ == '__main__':
    array = [4,6,1,8,3,9,5]
    data = SleepSort(array)
    print(data)