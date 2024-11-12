# 1. Age Group Categorization
# Classify a person's age group: Child (< 13), Teenager (13-19), Adult (20-59), Senior (60+).

def Age_Group(age):
    if age<13:
        print("Child")
    elif 13<=age<=19:
        print("Teenager")
    elif 20<=age<=59:
        print("Adult")
    elif age>=60:
        print("Senior")

# 2. Movie Ticket Pricing
# Problem: Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.

def Movie_Ticket(age, day):
    if(age<18):
        price = 8
    else:
        price = 12
    if(day=="Wednesday"):
        price = price-2
    print(f"Price: {price}")

# 3. Grade Calculator
# Problem: Assign a letter grade based on a student's score: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60).

def Grade_Calculator(score):
    if (score>=90):
        grade = "A"
    elif (80<=score<=89):
        grade = "B"
    elif (70<=score<=79):
        grade = "C"
    elif (60<=score<=69):
        grade = "D"
    elif (score<60):
        grade = "F"
    print(f"Grade: {grade}")

# 4. Fruit Ripeness Checker
# Problem: Determine if a fruit is ripe, overripe, or unripe based on its color. (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)

def Ripeness_Checker(color):
    if (color=="Green"):  condition = "Unripe"
    elif(color=="Yellow"): condition = "Ripe"
    elif (color=="Brown"): condition = "Overripe"
    print(condition)

# 5. Weather Activity Suggestion
# Problem: Suggest an activity based on the weather (e.g., Sunny - Go for a walk, Rainy - Read a book, Snowy - Build a snowman).

def Activity_Suggestion(weather):
    if(weather=="Sunny"): print("Go for a walk")
    elif(weather=="Rainy"): print("Read a book")
    elif(weather=="Snowy"): print("Build a snowman")
    else: print("Input correct weather")

