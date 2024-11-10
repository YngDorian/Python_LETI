text = input('Enter text: ')
strings = text.split()
for string in range(len(strings)):    
    new_string = strings[string]
    if len(new_string) > 3:           new_string = new_string.lower()
    if len(new_string) % 2 != 0:      new_string = new_string[0].upper() + new_string[1:]
    strings[string] = new_string
print(strings)