def toggle_case(string):
    toggled_string = ""
    for char in string:
        if char.isupper():
            toggled_string += char.lower()
        elif char.islower():
            toggled_string += char.upper()
        else:
            toggled_string += char
    return toggled_string
if __name__ == "__main__":
    input_str = input("Enter the string: ")
    result = toggle_case(input_str)
    print("Toggled string:", result)
