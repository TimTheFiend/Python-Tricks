def old_style_string_formatting():
    print("Hello %s" % "billybob")

def old_style_with_tuple():
    print("Hello %s, you %s" % ("Billybob", "sex offender"))

def old_style_dictionary():
    print("Hello %(name)s, you %(jobdescription)s." % {"name": "billybob", "jobdescription": "sex offender"})

def new_style_string_formatting():
    print("Hello {}".format("billybob"))

def new_style_string_formatting_multiple():
    print("hey {name}, you {job}".format(name="Biblybob", job="catholic priest"))

def literal_string_interpolation_python_three_six_plus():
    name = "recently released from jail, Biblebob."
    print(f"Hello {name}")

def literal_string_maths():
    a, b = 5, 10
    print(f"five plus ten is {a + b} and not {2 * (a + b)}")

def literal_strings_as_arguments(name, question):
    print(f"Alright {name}, {question}")

def template_string(input_name):
    from string import Template
    t = Template("Hey $name")
    print(t.substitute(name=input_name))

def template_strings():
    from string import Template
    t = "Hey $name, $question"
    Template(t).substitute(name="Howdy", question="Yeehaw")


try:
    select_function = int(input("Vælg en funktion: "))
except ValueError:
    exit(0)
if select_function == 1:
    old_style_string_formatting()
elif select_function == 2:
    old_style_with_tuple()
elif select_function == 3:
    old_style_dictionary()
elif select_function == 4:
    new_style_string_formatting()
elif select_function == 5:
    new_style_string_formatting_multiple()
elif select_function == 6:
    literal_string_interpolation_python_three_six_plus()
elif select_function == 7:
    literal_string_maths()
elif select_function == 8:
    literal_strings_as_arguments("Biblebob", "Where are the bodies buried?")
elif select_function == 9:
    template_string("Joakim")
elif select_function == 10:
    template_strings()
elif select_function == 11:
    pass
elif select_function == 12:
    pass
elif select_function == 13:
    pass
else:
    print("guess i'll stop")