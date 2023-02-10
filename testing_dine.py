# Initialize list of food options
food_options = ["pizza", "sushi", "burger", "tacos", "pasta", "salad"]

# Initialize dictionary of moods and corresponding food options
mood_options = {
    "hungry": ["pizza", "burger", "tacos"],
    "adventurous": ["sushi", "tacos"],
    "health-conscious": ["salad", "pasta"]
}

# Ask user what their mood is
mood = input("What is your mood? (hungry, adventurous, health-conscious) ")

# Eliminate food options not corresponding to user's mood
for food in food_options:
    if food not in mood_options[mood]:
        food_options.remove(food)

# Ask user if they want something hot or cold
temp = input("Do you want something hot or cold? ")

# Eliminate food options not corresponding to user's temperature preference
for food in food_options:
    if temp == "hot" and "cold" in food:
        food_options.remove(food)
    elif temp == "cold" and "hot" in food:
        food_options.remove(food)

# Ask user if they want something light or heavy
dish_type = input("Do you want something light or heavy? ")

# Eliminate food options not corresponding to user's dish preference
for food in food_options:
    if dish_type == "light" and "heavy" in food:
        food_options.remove(food)
    elif dish_type == "heavy" and "light" in food:
        food_options.remove(food)

# Suggest final food option
if len(food_options) == 1:
    print("Based on your preferences, we recommend: " + food_options[0])
else:
    print("Based on your preferences, we recommend: ")
    for food in food_options:
        print(food)
