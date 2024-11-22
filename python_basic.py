# Python Basics Assignment

# 1. Print Statements
print("Question 1: Print Statements")
print("My name is Moeed.")
print("I love coding.")
print("I enjoy learning new technologies!")
print("\n")  # Blank line for better readability

# 2. Strings
print("Question 2: Strings")
greeting = "Hello, Python!"
print("Original string:", greeting)
print("Length of the string:", len(greeting))
print("String in uppercase:", greeting.upper())
print("String with replaced name:", greeting.replace("Python", "Moeed"))
print("\n")

# 3. f-Strings
print("Question 3: f-Strings")
name = input("Enter your name: ")
age = input("Enter your age: ")
print(f"Hello {name}! You are {age} years old.")
print("\n")

# 4. Operators
print("Question 4: Operators")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} / {num2} = {num1 / num2 if num2 != 0 else 'undefined (division by zero)'}")
print("\n")

# 5. Lists
print("Question 5: Lists")
fruits = ["apple", "banana", "cherry"]
print("Original list of fruits:", fruits)
fruits.append("orange")
print("List after adding a fruit:", fruits)
fruits.remove("banana")
print("List after removing a fruit:", fruits)
print("The second fruit in the list is:", fruits[1])
print("\n")

# 6. Tuples
print("Question 6: Tuples")
colors = ("red", "green", "blue")
print("Original tuple:", colors)
print("The first color in the tuple is:", colors[0])
print("The total number of colors in the tuple is:", len(colors))
print("\n")

# 7. For Loops
print("Question 7: For Loops")
for i in range(1, 6):
    print(f"This is loop iteration {i}")
print("\n")

# 8. Input Handling
print("Question 8: Input Handling")
user_input = input("Enter a sentence: ")
words = user_input.split()
print("You entered:", user_input)
print("The number of words in your sentence is:", len(words))
