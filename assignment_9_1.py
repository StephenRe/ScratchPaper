




# Question 1
# class Student:
#     pass
# ans1a = type(Student)
# ans1b = Student.__module__

# print(ans1a)
# print(ans1b)



# # Question 2
# class Student:
#     student_name = 'John Smith'
#     grade = 86
    
# ans2a = Student.student_name

# # print(ans2a)


# # Question 3
# ans3a = setattr(Student, 'student_name', 'Angela Brooks')
# ans3b = setattr(Student, 'grade', 87)



# # Question 4
# class Student:
#     def __init__(self, student_name, student_id, grade, email):
#         self.student_name = student_name
#         self.student_id = student_id
#         self.grade = grade
#         self.email = email
        
# ans4 = Student('Francis Green', 475895, 56, 'francisgreen@mit.edu')

# print(ans4.student_name)




# Question 5

# class Student:
#     def __init__(self, student_name, student_id, grade, email):
#         self.student_name = student_name
#         self.student_id = student_id
#         self.grade = grade
#         self.email = email
#     def curved_average(self):
#         self.updated_grade = self.grade * 1.2
#         return self.updated_grade
# ans4 = Student('Francis Green', 475895, 56, 'francisgreen@mit.edu')    
# ans5 = ans4.curved_average()   
# print(ans5)



# # Question 6
# def my_sum(*args):
#     result = 0
#     for i in args:
#         result += i
#     return result

# ans1a = my_sum(1,3,5,6,10)
# ans1b = my_sum(10,4,6,2)

# print(ans6a)
# print(ans6b)


# Question 7
# def my_average(*args):
#     sums = sum(args)
#     counts = len(args)
#     return sums/counts

# ans7a = my_average(78,82,91,66)
# ans7b = my_average(56,89,76,100)

# print(ans7a)
# print(ans7b)


# Question 8

# def print_last_info(**kwargs):
#     parse = []
#     klen = len(kwargs)-1
#     for k, v in kwargs.items():
#         parse.append((k,v))
#     return f'{parse[klen][0]} is {parse[klen][1]}'
# person1 = {'Name':'Rosie', 'Age':33, 'Profession':'Data Scientist'}
# person2 = {'Name':'Kyle', 'Age':28, 'Profession':'Data Engineer', 'Phone_Number': 4659874982}

# ans8a = print_last_info(**person1)
# ans8b = print_last_info(**person2)

# print(ans8a)
# print(ans8b)


# Question 9
# movie = {'Title':'Inception', 'Director':'Nolan', 'Year':2010}

# def print_movie(**kwargs):
#     for k,v in kwargs.items():
#         return f'{k}: {v}'

# ans9a = print_movie(**movie)
# ans9b = print_movie(**movie, Music = "Zimmer")


# Question 10
# def plus_one(num):
#     def add_one(num):
#         return num + 1
#     return add_one(num)

# ans10 = plus_one(7)
# print(ans10)


# Question 11

def uppercase_decorator(func):
    def wrapper():
        a = func()
        return a.upper()
    return wrapper

@uppercase_decorator
def say_hello():
    return 'hello there!'

say_hello()



# Question 12

# def decorator_with_arguments(func):
#     def wrapper_accepting_arguments(arg1, arg2):
#         print(f'My arguments are: {arg1}, {arg2}')
#     return wrapper_accepting_arguments

# def cities(a, b):
#     print(f'Cities I love are: {a}, {b}')

# a = 'Paris'
# b = 'New York'

# runs = decorator_with_arguments(cities)
# ans12 = runs(a, b)
 


# Question 13

# def decorator_passing_arbitrary_arguments(func):
#     def wrapper_accepting_arbitrary_arguments(*args):
#         arglist =  tuple(i for i in args)
#         print(f'The positional arguments are {arglist}')
#     return wrapper_accepting_arbitrary_arguments

# def function_with_arguments(a, b, c):
#     return (a, b, c)

# runs = decorator_passing_arbitrary_arguments(function_with_arguments)

# ans13 = runs(1, 2, 3)

# ans13













