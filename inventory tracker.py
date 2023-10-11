#This function will create a dictionary to sort and track the inventory of reagents. Reagent are the keys and the inventory count is the value.
import ast
from email_noti import send_noti
from txt_func import write_txt
from txt_func import read_txt

#reagents ={'clv': '0', 'IMG':'0', 'EXA': '0', 'EXB': '0', 'RTN': '0','RIP': '0', 'SIP': '0', 'CSR': '0', 'RXP':'0',}


prmpt = ('To check inventory enter "1"'
        '\nTo add a new reagent to the list enter "2"'
        '\nTo add to reagent(s) to the inventory enter "3"'
        '\nTo take away from a reagent(s) from the inventory enter "4"')
print(prmpt)

prmpt_input = input('What would you like to do?')
for res in prmpt_input:
    if res == '1':
        try:
            with open('reagents.txt', 'r') as file:
                data_string = file.read()
        except FileNotFoundError:
            print('Error: The file "reagents.txt" was not found.')
            exit(1)

        # Convert the string to a dictionary
        try:
            reagents = ast.literal_eval(data_string)
        except (ValueError, SyntaxError):
            print('Error: Unable to convert the file content to a dictionary.')
        min_value = min(reagents.values())
        max_value = max(reagents.values())
        send_noti(min_value, max_value)
        print(reagents)
        break
    if res == '2':
        try:
            with open('reagents.txt', 'r') as file:
                data_string = file.read()
        except FileNotFoundError:
            print('Error: The file "reagents.txt" was not found.')
            exit(1)

        # Convert the string to a dictionary
        try:
            reagents = ast.literal_eval(data_string)
        except (ValueError, SyntaxError):
            print('Error: Unable to convert the file content to a dictionary.')
        add_key = input('What reagent would you like to add to the inventory list: ')
        reagents[add_key] = 0
        add_keyinv = input('How many would you like to add to the inventory: ')
        add_keyinv = int(add_keyinv)
        reagents[add_key] = int(reagents[add_key])
        reagents[add_key] = reagents[add_key] + add_keyinv
        write_txt()
        print(reagents)
        break
    if res == '3':
        try:
            with open('reagents.txt', 'r') as file:
                data_string = file.read()
        except FileNotFoundError:
            print('Error: The file "reagents.txt" was not found.')
            exit(1)

        # Convert the string to a dictionary
        try:
            reagents = ast.literal_eval(data_string)
        except (ValueError, SyntaxError):
            print('Error: Unable to convert the file content to a dictionary.')
        add_reag = input('What reagent inventory would you like to add to: ')
        add_keyinv = input('How many would you like to add to the inventory: ')
        add_keyinv = int(add_keyinv)
        slct_reag = int(reagents[add_reag])
        new_inv = slct_reag + add_keyinv
        reagents[add_reag] = new_inv
        write_txt(reagents)
        print(reagents)
        break
    if res == '4':
        try:
            with open('reagents.txt', 'r') as file:
                data_string = file.read()
        except FileNotFoundError:
            print('Error: The file "reagents.txt" was not found.')
            exit(1)

        # Convert the string to a dictionary
        try:
            reagents = ast.literal_eval(data_string)
        except (ValueError, SyntaxError):
            print('Error: Unable to convert the file content to a dictionary.')
        sub_reag = input('What reagent inventory would you like to take away from: ')
        sub_keyinv = input('How many would you like to take away from the inventory: ')
        sub_keyinv = int(sub_keyinv)
        slct_reag = int(reagents[sub_reag])
        new_inv = slct_reag - sub_keyinv
        reagents[sub_reag] = new_inv
        print(reagents)
        break
