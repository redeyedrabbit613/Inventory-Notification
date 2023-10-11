#This function converts a string to a dictionary
import ast


# Define a string representing a dictionary
def str2dict():
    with open('reagents.txt') as file_object:
        contents = file_object.read()
        string_dict = contents

# Use ast.literal_eval to convert the string to a dictionary
    try:
        dictionary = ast.literal_eval(string_dict)
        if isinstance(dictionary, dict):
            print("Successfully converted string to dictionary:")
            print(dictionary)
        else:
            print("The string did not represent a valid dictionary.")
    except (ValueError, SyntaxError):
        print("Error: Unable to convert the string to a dictionary.")


