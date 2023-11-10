# Ask user for their name
# name = input =("What's your name? ")
name = input("Name? ").strip().title()

# remove whitespace from str and capitalize name
# name = name.strip().title()

# capitalize user's name
# name = name.title()

# split user name between name and last name
first, last = name.split(" ")

# Say hello to user
# print("hello, " + name)
# print("hello,", name)

# print("hello, ", end="")
# print(name)

# print('hello, "friend"')
# print("hello, \"friend\"")

# print(f"hello, {name}")
print(f"hello, {first}")
