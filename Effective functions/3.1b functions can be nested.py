#region
def speak(text):
    def whisper(t):
        return t.lower() + "..."
    return whisper(text)

# print(speak("Hello world!"))
#endregion


#region Nested functions
"""Returnere en funktion baseret på volume

Returns:
    function -- yell / whisper
"""
def get_speak_func(volume):
    def whisper(text):
        return text.lower() + "..."
    def yell(text):
        return text.upper() + "!"
    if volume > 0.5:
        return yell
    else:
        return whisper

# # get_speak_func(0.3)
# # print(get_speak_func(0.3))
# # whisper_func = get_speak_func(0.3)
# # yell_func = get_speak_func(0.8)
# # print(whisper_func("Hello World"))
# # print(yell_func("Hello World"))
#endregion

#region
def speak_func(text, volume):
    def whisper(apples):
        return text.lower() + "..." + apples
    def yell():
        return text.upper() + "!"
    if volume > 0.5:
        return yell
    else:
        return whisper
# print(speak_func("hello world", 0.3)("helloooooooooo"))
# print(speak_func("hello world", 0.8)())
#endregion



#region
def make_adder(n):
    def add(x):
        return x + n
    return add

plus_3 = make_adder(3)
plus_5 = make_adder(5)
# print(plus_3(5)) # Output 8
# print(plus_5(5)) # Output 10
# print(make_adder(3)(5)) # Output 8
#endregion

#region Objects can behave like functions
"""Here's an exmaple of class defining a callable object:
Behind the scenes "calling" an object instance as a function attempts to execute the object's __call__ method.
"""
class Adder:
    def __init__(self, n):
        self.n = n
    def __call__(self, x):
        return self.n + x
plus_3 = Adder(3)
print(plus_3(4))
#endregion