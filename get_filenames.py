import os
import shutil

path = 'pyFiles'

for _ in os.listdir(path):
    if not _.endswith('.py'):
        continue
    # new_name = _.replace(' ', '_')
    # shutil.move(f"pyFiles/{_}", f"pyFiles/{new_name}")
    print(f"- [{_[:-3]}](pyFiles/{_})")

# print("This is a python script.")