#This function will write the reagent list into a txt file.
def write_txt(reagents):
    filename = 'reagents.txt'
    try:
        with open(filename, 'w') as file_object:    
            reagents = str(reagents)
            file_object.write(reagents)
    except FileNotFoundError:
        print('Error: The file "reagents.txt" was not found.')
        exit(1)

#This function will read the reagent list from a txt file.
def read_txt():
    try:
        with open('reagents.txt', 'r') as file:
            contents = file.read()
    except FileNotFoundError:
        print('Error: The file "reagents.txt" was not found.')
        exit(1)
