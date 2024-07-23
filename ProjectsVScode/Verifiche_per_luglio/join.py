# A list of strings
words = ["Hello", "world", "from", "ChatGPT"]

# Join the list into a single string with spaces
sentence = " ".join(words)

print(sentence)  # Output: Hello world from ChatGPT

# A list of strings
items = ["apple", "banana", "cherry"]

# Join the list with a comma and space
fruits = ", ".join(items)

print(fruits)  # Output: apple, banana, cherry

# An empty list
empty_list = []

# Join the empty list
result = "".join(empty_list)

print(result)  # Output: (an empty string)

# A list of integers
numbers = [1, 2, 3, 4, 5]

# Convert each integer to a string and join with a hyphen
number_str = "-".join(map(str, numbers))

print(number_str)  # Output: 1-2-3-4-5

# A tuple of strings
data = ("20240722")

# Join the tuple with slashes
date = "/".join(data)
str(date)
dati = date.split("/")
print(dati)  # Output: 2024/07/22
