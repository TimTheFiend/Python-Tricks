# 1
def greeting(name):
    return 'Hi %s!' % names[name]

names = {
    1: "Karl",
    2: "Magnus",
    3: "Helga"
}

print(greeting(2))  # Hi magnus
print(greeting(5))  # KeyError

# 2
def greeting(name):
    if name in names:
        return 'Hi %s!' % names[name]
    else:
        return "Hello there!"

names = {
    1: "Karl",
    2: "Magnus",
    3: "Helga"
}

print(greeting(2))  # Hi magnus
print(greeting(5))  # Hello there!

"""Better implementation!"""
def greeting(userid):
    try:
        return 'Hi %s!' % name_for_userid[userid]
    except KeyError:
        return 'Hi there'

name_for_userid = {
    1: "Karl",
    2: "Magnus",
    3: "Helga"
}
print(greeting(2))  # Hi magnus
print(greeting(5))  # Hello there!
