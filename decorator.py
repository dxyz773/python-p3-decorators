# CALL BACK FUNCTION/ FIRST CLASS FUNCTION

# def dance(music):
#     print(f"We dance to this {music}!")


# def listen(music):
#     print(f"We listen to this {music}")


# def active_fun(callbackfun):
#     return callbackfun("Prince")


# active_fun(listen)


# HIGHER ORDER FUNCTIONS ------------------------------------------

# def activate_fun():
#     def dance(music):
#         return f"We dance to {music}"

#     return dance


# print(activate_fun()("Prince"))

# DECTOARTOR


# 1. decorator
# def couple_calculator():
#     # 2. inner function
#     def report_price():
#         print("Initital price = $28.00")
# def hello():
#     print("Hello from the hello() function.")

#     def greet(name):
#         print(f"Greetings, {name} from the greet() function.")

#     return greet


# print(hello()("Guido"))
# def decorator(func):
#     def wrapper():
#         print("I am the output that lets you know the function is about to be called.")
#         func()
#         print("I am the output that lets you know the function has been called.")

#     return wrapper


# @decorator
# def get_called():
#     print("I am the function and I am being called.")


# get_called()
# sweep_floors(800)
def check_working_hours(func):
    def wrapper(time):
        if 1100 < time < 2100:
            func(time)
        else:
            print("I'm off duty!")

    return wrapper


@check_working_hours
def sweep_floors(time):
    print("Sweeping the floors...")


@check_working_hours
def wash_dishes(time):
    print("Washing the dishes...")


@check_working_hours
def chop_vegetables(time):
    print("Chopping the vegetables...")


chop_vegetables(1200)
