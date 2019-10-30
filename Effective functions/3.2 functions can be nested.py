def speak(text):
    def whisper(t):
        return t.lower() + "..."
    return whisper(text)

# print(speak("Hello world!"))


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

def speak_func(text, volume):
    def whisper(apples):
        return text.lower() + "..." + apples
    def yell():
        return text.upper() + "!"
    if volume > 0.5:
        return yell
    else:
        return whisper
print(speak_func("hello world", 0.3)("helloooooooooo"))
print(speak_func("hello world", 0.8)())