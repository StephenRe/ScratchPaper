



def asumb(a,b):
    return a+b

def square(func):
    def wrapper(a,b):
        num = func(a,b)
        return num**2
    return wrapper


# @square
# def asumb(a,b):
#     return a+b

# print(asumb(3,4))

sums = square(asumb)
print(sums(3,4))




