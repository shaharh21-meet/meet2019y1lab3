name = input("What is your name?")
print("Hello there, "+ name.capitalize())

length = len(name)
length = str(length)
print("your name is " + length + " letters long")
print("first letter: " + name[0].capitalize())
print("last letter: " + name[-1].capitalize())

print("missing letters: " + name[1:-1])


