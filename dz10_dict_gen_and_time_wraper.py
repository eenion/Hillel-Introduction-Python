import time
from datetime import timedelta

def time_func_decorator(func_to_decor):
    def wrapper():
        start_time = time.monotonic_ns()
        func_to_decor()
        end_time = time.monotonic_ns()
        print('Finished in {} nanoseconds'.format(timedelta(seconds=end_time - start_time)))
    return wrapper

@time_func_decorator
def list_of_generated_dics(n = 5):
    my_dict_list = []
    my_dict = {}
    for n in range(n+1):
        my_dict[n] = n**2
        my_dict_list.append(dict(my_dict.items()))
    print(my_dict_list)

def main():
    list_of_generated_dics()
    
if __name__ == '__main__':
    main()
    