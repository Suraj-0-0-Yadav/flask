def new_decorator(func):

    def wrap_func():
        print("Some code before func")

        func()

        print("Some code after func")
    
    return wrap_func

@new_decorator
def need_decorator():
    print("Please decorate me !!!")

need_decorator()