#This function will write the reagent list into a txt file.
def write_txt(reagents):
    filename = 'reagents.txt'
    with open(filename, 'w') as file_object:
        reagents = str(reagents)
        file_object.write(reagents)

#This function will read the reagent list from a txt file.
def read_txt():
    with open('reagents.txt') as file_object:
        contents = file_object.read()
        print(contents)
