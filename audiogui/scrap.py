from datetime import datetime
 
def timer(func):
    def wrapper(): 
        print(f'Start time: {datetime.now()}')
        func()
        print(f'End time: {datetime.now()}')
    return wrapper

def not_during_time(func, start, stop):
    hour = datetime.now().hour
    print(f'current hour {hour}')
    def wrapper(): 
        if  hour < start or hour > stop:
            func()
        else:
            print(f"try again after {stop} o'clock")
    return wrapper


# @timer
# def say_whee():
#     print('whee')