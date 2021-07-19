# # # Decorators

# import logging
# def logger_func(original_func):

#     logging.basicConfig(filename='{}.log'.format(original_func.__name__), level=logging.INFO)

#     def wrapper_func(*args, **kwargs):
#         logging.info('ran function with args: {} and kwargs: {}'.format(args, kwargs))
#         return original_func(*args, **kwargs)
    
#     return wrapper_func

# def display(name, age):
#     print('>name: {}, age: {}'.format(name, age))

# x = logger_func(display)
# x('nikos', 18)

def my_timer(original_func):
    import time

    def wrapper_func(*args, **kwargs):
        
        t1 = time.time()
        print('test')
        result = original_func(*args, **kwargs)
        t2 = time.time()
        print('time: {}'.format(t2-t1))
        return result

    return wrapper_func

def sum(x, y):
    return x + y

timed_x = my_timer(sum)
print(timed_x(1,2))

@my_timer
def sub(x, y):
    return x - y

print(sub(1,2))
























# # def outer_func(msg):

# #     message = msg

# #     def inner_func():
# #         print(message)
# #     return inner_func

# # hi_func = outer_func('hi')
# # hello_func = outer_func('hello')

# # hi_func()
# # hi_func()
# # hello_func()

# def decorator_function(original_function):
#     def wrapper_function(*args, **kwargs):
#         print('wrapper executed this before {}'.format(original_function.__name__))
#         return original_function(*args, **kwargs)
#     return wrapper_function

# def display():
#     print('display function ran')

# decorated_display = decorator_function(display)
# decorated_display()

# @decorator_function
# def display2():
#     print('display2 function ran')

# display2()

# def display_info(name, age):
#     print('display_info ran with arguments ({} {})'.format(name, age))

# display_info('nikos', '38')
# decorated_display_info = decorator_function(display_info)
# decorated_display_info('test', 69)

# @decorator_function
# def display_info2(name, age):
#     print('display_info2 function ran with arguments ({} {})'.format(name, age))

# display_info2('test2', 0)



























# # # Closures

# # # def outer_func(msg):
# # #     message = msg

# # #     def inner_func():
# # #         print(msg)

# # #     return inner_func

# # # hi_func = outer_func('Hi')
# # # hello_func = outer_func('Hello')

# # # hi_func()
# # # hello_func()

# # # def html_tag(tag):

# # #     def wrap_test(msg):
# # #         print('<{0}>{1}<{0}>'.format(tag, msg))
    
# # #     return wrap_test

# # # link = html_tag('a')
# # # link('www.google.com')

# # # para = html_tag('p')
# # # para('ipsum lorem')
# # # para('lorem ipsum')

# # import logging
# # logging.basicConfig(filename='example.log', level=logging.INFO)

# # def logger(func):
# #     def log_func(*args):
# #         logging.info('Running "{}" with arguments {}'.format(func.__name__, args))
# #         print(func(*args))
# #     return log_func

# # def sum(x, y):
# #     return x + y

# # lg = logger(sum)
# # lg(1,2)




















# # # First Class Functions

# # # def logger(msg):
# # #     def log_message():
# # #         print('Log: ', msg)
# # #     return log_message

# # # x = logger('test')
# # # x()

# # # def html_tag(tag):

# # #     def wrap_test(msg):
# # #         print('<{0}>{1}</{0}>'.format(tag, msg))

# # #     return wrap_test

# # # link = html_tag('a')
# # # print(link)
# # # link('www.google.com')