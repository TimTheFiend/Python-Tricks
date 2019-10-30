"""Functions are objects

All data in a python program is represented by objects or releations between objects.
Things like strings, lists, modules, and functions are all objects

"""

def yell(text):
    print(text.upper() + "!")

bark = yell
bark("arf")

del yell
try:
    yell("hello")
except NameError:
    pass
bark("ciao")

"""Functions can be stored in data structures
"""
funcs = [bark, str.lower, str.capitalize,]
print(funcs)
for f in funcs:
    print(f, f("hello there"))
funcs[0]("shrek")

def greet(func):
    greeting = func("hi, I am a python program.")
    print(greeting)

greet(bark)

def whisper(text):
    return text.lower() + '...'

greet(whisper)
"""As you saw, map went through the entire list and applied the bark function to each element.
as a result we now have a new list object with modified greetings strings.
"""
list(map(bark, ["hello", "world", "I'm", "so", "Tired",]))