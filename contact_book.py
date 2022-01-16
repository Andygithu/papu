import csv
from types import CellType


def main():
     choice = None
     while choice != 0:
       print()
       print('Welcome to your contact book.To add a new contact press 1,')
       print('To show all the list contacts press 2')
       print('To delete a contact press 3,')
       print('To find an contact press 4')
       print('If you have finished press 0')
       print()
       choice = float(input("Enter a number: "))
       if choice == 1:
         #Add new contact
         new_contact = []
         print()
         print('Please add the following information to add a new contact')
         print()
        
         name = input('Enter the name: ')
         cel = input('Enter the number: ')
         email = input('Enter the email: ')
         if cel == '':
           cel = 'None'
           
           
           new_contact.append(name)
           new_contact.append(cel)
           new_contact.append(email)
           add_contact(new_contact)
         elif email == '':
           email = 'None'
           
           new_contact.append(name)
           new_contact.append(cel)
           new_contact.append(email)
           add_contact(new_contact)
         elif email == '' and cel == '':
           email = 'None'
           cel = 'None'
           new_contact.append(name)
           new_contact.append(cel)
           new_contact.append(email)
           add_contact(new_contact)
         else:
            name = name
            email = email
            cel = cel
            new_contact.append(name)
            new_contact.append(cel)
            new_contact.append(email)
            add_contact(new_contact)

       elif choice == 2:
         #Display list
         contact_dic = create_dictionary('contacts.csv')
         print()
         print('Contact List')
         print('Name    Phone          E-mail')
         print()
         contacts_list = display_contact_list(contact_dic)
         print()  
       elif choice == 3:
         #Delete a contact

        contact_choice = input('Enter the name contact you want to delete: ')
        #Create a dictionary
        contact_dic = create_dictionary('contacts.csv')
        #Remove the item selected in the dictionary
        contact_dic.pop(contact_choice)
        #This is to write the title in the new dictionary
        with open('contacts.csv','wt',newline='') as appendcon:
          append = csv.writer(appendcon)
          title = ['name','number','email']
          append.writerow(title)
        #This lines of code is to write the new dictionary in the csv_file.

        with open("contacts.csv", "at",newline ='') as csv_file:
          writer = csv.writer(csv_file)
          for key, value in contact_dic.items():
            
            writer.writerow([key,value[0],value[1]])
       elif choice == 4:
         #Find a contact
         contact_choice = input('Enter the name of the contact you want to find: ')
         #Create a dictionary
         contact_dic = create_dictionary('contacts.csv')
         if contact_choice in contact_dic:

          contact = contact_dic.get(contact_choice)
          print()
          print(f"Here is {contact_choice}'s information")
          print(f'cel: {contact[0]}')
          print(f'email: {contact[1]}')
         else:
           print()
           print("That contact doesn't exist")
         
       else:
         print()
          
def create_dictionary(filename):
  my_dic = {}
  with open(filename, "rt") as text_file:

        # Read the contents of the text
        # file one line at a time.
       reader = csv.reader(text_file)
    
       
       next(reader)
       for row in reader:
      #This is to create my dictionary by indication the keys and values corresponding.
         my_dic[row[0]] = [row[1],(row[2])]
  return my_dic
def add_contact(new_contact):
  with open('contacts.csv','at',newline='') as appendcon:
     append = csv.writer(appendcon)
     append.writerow(new_contact)

def display_contact_list(dictionary):
    for key, value in dictionary.items():
        print(f'{key:8}{value[0]:15}{value[1]}')
        # print(f'{key}{value[0]}{value[1]}')

    return dictionary

  
# Call main to start this program.
if __name__ == "__main__":
    main()