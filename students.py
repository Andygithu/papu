import csv
def main():
    #indexes of the two elements in the csv files.
    STUDENT_I_INDEX = 1
    ADDRESS_INDEX = 0
    #Read the contents of CSV file named destists.csv
    #into a dictionary named students.
    students_dic = read_dict('students.csv', ADDRESS_INDEX)
    I_number = input('Please enter an I-Number (xxxxxxxxx):')
    I_number = I_number.replace("-", "")
    if I_number in students_dic:
     value = students_dic[I_number]
     name = value[STUDENT_I_INDEX]
     print(name)
    else:
        print('No such student')

    

    
        
def read_dict(filename,key_column_index):
    #Create an empty dictionary
    dictionary = {}

    with open(filename,'rt') as csv_file:
        #Use the csv module to create to create a reader object that will read from
        # the opened csv file
        reader = csv.reader(csv_file)
        #the first line in not necessary so this statement will skip the first row.
        next(reader)

        #Read the rows one at a time
        #The reader object returns each row as a list.
        for row in reader:

            #from the current row, retrieve the data from the column that contains the key.
            key = row[key_column_index]

            #Store the data from the current row into the dictionary.
            dictionary[key] = row
    #Return the dictionary
    return dictionary


# Call main to start this program.
if __name__ == "__main__":
    main()
