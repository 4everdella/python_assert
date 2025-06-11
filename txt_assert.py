with open('txt_file.txt', 'w') as file:
    file.write('hello')


with open('txt_file.txt', 'r') as file:
    content = file.read()
assert 'hello' in content, AssertionError
print(True)
