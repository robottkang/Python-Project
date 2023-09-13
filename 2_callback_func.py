def call_10_times(func):
    for i in range(10):
        func(i)
        
def print_hello(number):
    print("안녕하세요", number)

call_10_times(print_hello)