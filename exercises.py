
# Exercise 1: List and Indexing
#
# Create a list named students containing at least three student names (strings).
# Assign the second student’s name to a variable named first_student.
# Assign the last student’s name to a variable named last_student.

def manage_students():
    # your code here
    students =['mohammed','Ali','Hussine']
    first_student=students[0]
    last_student = students[2]
    print(f'first student {first_student} last student {last_student}')



# Call the function and print the result
print('Exercise 1:', manage_students())


# Exercise 2: Loop and String Concatenation
#
# Create a tuple named foods containing the same number of foods (strings) as there are names in the students list.
# Create a variable named meal and assign an empty string to it.
# Use a for loop to iterate over the strings in foods and append each string to meal.

def combine_foods():
    # your code here
    foods=('fish','burger','kabab')
    meal=''
    for i in foods:
        meal= meal + i + ''
    return meal        


# Call the function and print the result
print('Exercise 2:', combine_foods())


# Exercise 3: Slicing Tuples
#
# Using the slice operator, assign a new tuple containing only the last two food strings in the foods to a variable named last_two_foods.

def slice_foods():
    # your code here
    foods=('fish','burger','kabab')
    last_two_foods= foods[1:]
    print(last_two_foods)

# Call the function and print the result
print('Exercise 3:', slice_foods())

# Exercise 4: Dictionaries and String Formatting
#
# Create a dictionary named home_town containing the keys of city, state, and population.
# Using the home_town dictionary, assign to a variable named home_town_message a string with this format: “I was born in <city>, <state> - population of <population>”

def hometown_info():
    # your code here
    home_town ={'city':'Amrica','state':'Los Angloes','population':'million'}
    
    home_town_message = f'I was born in {home_town["city"]},{home_town["state"]}- population of {home_town["population"]}'
    print(home_town_message)


# Call the function and print the result
print('Exercise 4:', hometown_info())


# Exercise 5: Iterating Over Dictionary Items
#
# Define an empty list named home_town_items.
# Use a for loop to iterate over the key: value pairs in the home_town dictionary and append a string with the following format to home_town_items: "<key> = <value>"

def list_home_town_items():
    # your code here
    home_town ={'city':'Amrica','state':'Los Angloes','population':'million'}
    home_town_items = []
    for i in home_town:
        home_town_items = f'{i} -> {home_town[i]}'
        print(home_town_items)


# Call the function and print the result
print('Exercise 5:', list_home_town_items())