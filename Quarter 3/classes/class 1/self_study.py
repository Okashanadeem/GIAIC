# Prompt the user to enter their name
name = input("What is your name? ")

# Greet the user with their name
print(f"Hello, {name}!")  # Using f-string for cleaner string formatting

# Explanation:
# - We declare a variable 'name' and assign it the value entered by the user.
# - The input function pauses execution and waits for user input.
# - The print statement then greets the user using their provided name.
# - The f-string ensures proper formatting with a space included automatically.



# Import the datetime module to work with dates
import datetime

# Ask the user for their birth year
birth_year = input("What is your birth year? ")

# Get the current year using the datetime module
today = datetime.date.today()
current_year = today.year  # Extracting the current year

# Calculate the age by subtracting birth year from the current year
age = current_year - int(birth_year)

# Display the calculated age
print(f"Your age is: {age}")
