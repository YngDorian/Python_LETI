text = input('Enter text: ')
strings = text.split()
for string in strings:
    new_string = string
    if len(string) > 3:
        new_string = new_string.lower()
    if len(string) % 2 != 0:
        new_string = new_string[0].upper() + new_string[1:]
    strings[0]=new_string
print(new_string)