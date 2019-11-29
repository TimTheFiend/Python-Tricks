import os

path = 'pyFiles'

for _ in os.listdir(path):
    if not _.endswith('.py'):
        continue
    print(f"- [{_[:-3]}](pyFiles/{_})")

print("This is a python script.")