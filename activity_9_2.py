


# Question 1
class House:
    pass
ans1a = type(House)
ans1b = House.__module__

print(ans1a)
print(ans1b)


# Question 2
class House:
    square_footage = 1450
    number_of_bedrooms = 3
    garage = True
    
ans2a = House.square_footage

print(ans2a)


# Question 3
ans3a = setattr(House, 'square_footage', 1600)
ans3b = setattr(House, 'number_of_bedrooms', 2)


# Question 4
setattr(House, 'private_listing', False)
ans4 = House.private_listing

print(ans4)


# Question 5
class House:
    def __init__(self, square_footage, number_of_bedrooms, garage, private_listing):
        self.square_footage = square_footage
        self.number_of_bedrooms = number_of_bedrooms
        self.garage = garage
        self.private_listing = private_listing
        
ans5 = House(930, 1, False, True)

ans5.square_footage


# Question 6
class House:
    def __init__(self, square_footage, number_of_bedrooms, garage, private_listing):
        self.square_footage = square_footage
        self.number_of_bedrooms = number_of_bedrooms
        self.garage = garage
        self.private_listing = private_listing
    def property_taxes(self):
        self.total_tax = self.square_footage * 1.67
        return self.total_tax

ans5 = House(930, 1, False, True)
ans6 = ans5.property_taxes()
ans6


# Question 7
class House:
    def __init__(self, square_footage, number_of_bedrooms, garage, private_listing):
        self.square_footage = square_footage
        self.number_of_bedrooms = number_of_bedrooms
        self.garage = garage
        self.private_listing = private_listing
    def property_taxes(self):
        self.total_tax = self.square_footage * 1.67
        return self.total_tax
    def non_bedrooms_area(self):
        self.non_bedrooms_total_area = (self.square_footage - self.number_of_bedrooms)*142
        return self.non_bedrooms_total_area

ans5 = House(930, 1, False, True)        
ans7 = ans5.non_bedrooms_area()

ans7