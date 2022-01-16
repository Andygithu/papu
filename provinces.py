def main():
    #Read the contents of a text file named provinces.txt.
    provinces = read_list('provinces.txt')

    #print out the list
    

    #remove the first item of the list
    provinces.pop(0)

    #remove the last item of the list
    provinces.pop()


    for i in range(len(provinces)):
        if provinces[i] == 'AB':
            provinces[i] = 'Alberta'
    #Count the number that Alberta appears in province list
    alberta = provinces.count('Alberta')


    print(f'Alberta occurs {alberta} times in the modified list.')
    print(provinces)  
def read_list(filename):


    provinces_list = []
    
    #Open the text file for reading.
    with open(filename, 'rt') as text_file:
        
        #Read the content of the file line by line.
        for line in text_file:
            #Clean line
            clean_line = line.strip()
            #Append the clean line into the list of provinces
            provinces_list.append(clean_line)
            

    return provinces_list



# Call main to start this program.
if __name__ == "__main__":
    main()