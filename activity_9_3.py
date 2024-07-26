

# 1
def mult(*args):
    result = 1
    for i in args:
        result *= i
    return result

ans1a = mult(2,6,6,8)
ans1b = mult(5,10.0,2,3)

# 2
def subtract_from_ten(*args):
    a = 10
    for x in args:
        a -= x
    return a

ans2a = subtract_from_ten(1,2,3)
ans2b = subtract_from_ten(5,10,1,2)


# 3
def subtract_from_highest(*args):
    h = max(args)
    result = h
    for x in args:
        if x != h:
            result-=x
    return result

ans3a = subtract_from_highest(1,2,3)
ans3b = subtract_from_highest(15,25,1,3)

# 4
def mult_keyword(**kwargs):
    result = 1
    for k,v in kwargs.items():
        result *= v
    return result

ans4a = mult_keyword(a =2, b = 3, c = 4)
ans4b = mult_keyword(a = 1, b = 5, c = 2, d = 3)

# 5
def concatenate(*args):
    result = ''
    for i in args:
        result += i
    return result

ans5a = concatenate("We", "Are", "Practicing", "Passing", "Unnamed", "Arguments!")
ans5b = concatenate("We", "Are", "Using", "The", "Unpacking", "Operator")

# 6
def list_keys(**kwargs):
    result = ''
    result = ', '.join(kwargs.keys())
    return result

ans6a = list_keys(a =2, b = 3, c = 4)
ans6b = list_keys(a = 1, b = 5, c = 2, d = 3)

# 7
def hello_user(**kwargs):
    result = ''
    return f'Hello {kwargs["First_Name"]}!'

ans7a = hello_user(First_Name="Elon", Last_Name="Musk", Email="Elon.Musk@yy.com")
ans7b = hello_user(First_Name="Jeff", Last_Name="Bezos", Email="Jeff.Bezos@zz.com")

# 8
def display_user_total_assets(first, last, **kwargs):
    result = ''
    s = sum(kwargs.values())
    result = result + first + ' ' + last + ': ' + str(s)
    return result

ans8a = display_user_total_assets("John", "Smith", Car=30000, House=450000, Savings=1000000)
ans8b = display_user_total_assets("Joe", "Clark", Car=15000, House=250000)

9
def display_user_total_assets2(*args, **kwargs):
    result = ' '
    s = sum(kwargs.values())
    for a in range(len(args)-1):
        result += args[a] + ' '
    result += args[-1] + ': ' + str(s)
    return result

ans9a = display_user_total_assets2("John", "S.", "Smith", "III", Car=30000, House=450000, Savings=1000000)
ans9b = display_user_total_assets2("Joe", "Clark", Car=15000, House=250000)

print(ans9a)
