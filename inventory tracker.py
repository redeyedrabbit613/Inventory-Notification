#This function will create a dictionary to sort and track the inventory of reagents. Reagent are the keys and the inventory count is the value.
from email_noti import send_noti
from txt_func import write_txt
from txt_func import read_txt

reagents ={'clv': '0', 'IMG':'0', 'EXA': '0', 'EXB': '0', 'RTN': '0','RIP': '0', 'SIP': '0', 'CSR': '0', 'RXP':'0',}


prmpt = ('To check inventory enter "1"'
        '\nTo add a new reagent to the list enter "2"'
        '\nTo add to reagent(s) to the inventory enter "3"'
        '\nTo take away from a reagent(s) from the inventory enter "4"')
print(prmpt)

prmpt_input = input('What would you like to do?')
for res in prmpt_input:
    if res == '1':
        send_noti()
        print(reagents)
    if res == '2':
        add_key = input('What reagent would you like to add to the inventory list: ')
        reagents[add_key] = 0
        add_keyinv = input('How many would you like to add to the inventory: ')
        add_keyinv = int(add_keyinv)
        reagents[add_key] = int(reagents[add_key])
        reagents[add_key] = reagents[add_key] + add_keyinv
        print(reagents)
        read_txt()
        #need to add try except statement.
    if res == '3':
        add_reag = input('What reagent inventory would you like to add to: ')
        add_keyinv = input('How many would you like to add to the inventory: ')
        add_keyinv = int(add_keyinv)
        slct_reag = int(reagents[add_reag])
        new_inv = slct_reag + add_keyinv
        reagents[add_reag] = new_inv
        print(reagents)
        #need to add try except statement.
    if res == '4':
        sub_reag = input('What reagent inventory would you like to take away from: ')
        sub_keyinv = input('How many would you like to take away from the inventory: ')
        sub_keyinv = int(sub_keyinv)
        slct_reag = int(reagents[sub_reag])
        new_inv = slct_reag - sub_keyinv
        reagents[sub_reag] = new_inv
        print(reagents)
        #need to add try except statement.
