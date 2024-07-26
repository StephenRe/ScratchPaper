

# Question 1
def assignFunctionToVariableExample():
    return 'FunctionToVariable'
    
ans1 = assignFunctionToVariableExample



# # Question 2
def sqrt(num):
   return num**0.5

def square(num):
   return num**2

def do_math(num,func):
    return func(num)

ans2a = do_math(16,sqrt)
ans2b = do_math(8,square)  ## << was ans, not ans2b


# # Question 3

def shout_hello():
    greeting = "hello world!"
    return greeting.upper()

def whisper_hello():
    shout = shout_hello()
    return shout.lower()

ans2a = whisper_hello()
print(ans2a)


# # Question 4

def shout_hello(name):
   greeting = "hello " + name + "!"
   return greeting.upper()

def whisper_hello(name):
    shout = shout_hello(name)
    return shout.lower()

ans4a = whisper_hello('General Grievous')
ans4b = whisper_hello('Count Dooku')

print(ans4a)
print(ans4b)


# # Question 5

def add_values(*args):
    result = 0
    for val in args:
        result = result + val
    return result

def my_add_values(func, *args):
    return f'Added decoration:{func(*args)}'

ans5a = my_add_values(add_values, 1,2,3,4,5,6,7,8,9,10)
ans5b = my_add_values(add_values, 40,60,70,100)

print(ans5a)
print(ans5b)


# Question 6

def calculate_percentage(num, *args):
    total = 0
    for num in args:
        total += num
    return num/total

def format_percentage(func, num, *args):
    return func(num, *args) * 100

ans6a = format_percentage(calculate_percentage, 100, 100,200,100)
ans6b = format_percentage(calculate_percentage, 60, 10,10,10,10,10,50)

print(ans6a)
print(ans6b)


# # Question 7

def add_values(*args,**kwargs):
    result = 0
    for v in args:
        result += v
    for k, v in kwargs.items():
        result += v
    return result


def my_deco(func):
    def wrapper(*args,**kwargs):
        return f'Added decoration - function defined inside function: {func(*args,**kwargs)}'
    return wrapper

add = my_deco(add_values)

ans7a = add(*(1,2,3,4,5,6,7,8,9,10),**{"arg1":1, "arg2":2, "arg3":3})
ans7b = add(*(40,60,70,100), **{"arg1":4, "arg2":10})

print(ans7a)
print(ans7b)


# # Question 8

def add_values(*args,**kwargs):
    result = 0
    for v in args:
        result += v
    for k, v in kwargs.items():
        result += v
    return result



def my_new_add(func):
    def wrapper(*args,**kwargs):
        if 'Federal' in kwargs:
            kwargs.pop('Federal')
        return func(*args,**kwargs)
    return wrapper

add = my_new_add(add_values)

args1 = (1000,35000,5000)
kwargs1 = {"Housing":5000, "Allowances":2000, "Federal":3500}
ans8a = add(*args1, **kwargs1)

args2 = (4000,6000,7000,1000)
kwargs2 = {"Housing":100}
ans8b = add(*args2, **kwargs2)

print(ans8b)


# Question 9

def verbose_sum(func):
    def inner(a,b):
        return str(a) + " + " + str(b) + " = " + str(func(a,b))
    return inner

@verbose_sum
def sum(a, b):
    return a + b
ans9a = sum(4,10)
ans9b = sum(200,500)

print(ans9b)


# # Question 10:
def my_add_values(func):
    def wrapper(*args,**kwargs):
        return f'Added decoration: {func(*args,**kwargs)}'
    return wrapper

@my_add_values
def add_values(*args,**kwargs):
    result = 0
    for v in args:
        result += v
    for k, v in kwargs.items():
        result += v
    return result

args1 = (1,2,3,4,5,6,7,8,9,10)
kwargs1 = {"arg1":1, "arg2":2, "arg3":3}
ans10a = add_values(*args1, **kwargs1)

args2 = (40,60,70,100)
kwargs2 = {"arg1":4, "arg2":10}
ans10b = add_values(*args2, **kwargs2)

print(ans10b)
