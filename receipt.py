import csv
from datetime import datetime
#I did create this list to append the quantity of each product.
items = []
prices = []
results = []
def main():
    try:
        #indexes of the two elements in the csv files.
    
        #Read the contents of CSV file named products.csv
        #into a dictionary named products.
        products = read_products('products.csv')
    
    
         #print the list of products
         # for key, value in products.items():
         #  print(f'{key} {value}')
    
         #Open a file named request.csv and store a reference to the opened file in variable named request_file.

    
        
        with open('request.csv','rt') as request_file:

             reader = csv.reader(request_file)
             next(reader)
             print()
             print('Inkom Emporium')
             print()
             for row in reader:
                #Retrieve the key to find it into the dictionary 
                key = row[0]
                #Retrieve the quantity from reader.
                quantity = row[1]
                if key in products:
                   #Retrieve the produ t name from the list.
                   product = products[key]
             
                print(f'{product[0]}: {quantity} @ {product[1]}')
                prices.append(product[1])
                 #This is to change from string to integer number the quantities inside the list and the to add the total items.
                items.append(int(quantity))
                total_items = sum(items)
        print()
        print(f'Number of items: {total_items}')
        #Get the current date and day number
        current_date_and_time = datetime.now()
        today = current_date_and_time.weekday()
        #In this part I'm doing the multiplication between the number of items and it's prices, then I´m getting the total. 
        for num1, num2 in zip(items, prices):
	          
	        results.append(num1 * num2)
        subtotal = sum(results)
        print(f'Subtotal: {subtotal:.2f}')
        #Compute the taxes.
        sales_tax_rate = 0.06 * subtotal
        print(f'Sales Tax: {sales_tax_rate:.2f}')
        
        #This is to make a discount if it's friday = 4.
        if today == 4:
            sales_tax_rate = 0.06 * subtotal
            total = subtotal +sales_tax_rate
            discount = total * 0.1
            total = total - discount
            print(f'Total: {total:.2f}')
           
            
        else:
            sales_tax_rate = 0.06 * subtotal
            total = subtotal +sales_tax_rate
            print(f'Total: {total:.2f}')
        
        
        #print total.
        
        print()
        #Print the current date and time.
        print('Thank you for shopping at the Inkom Emporium.')
       
        print(f"{current_date_and_time:%A %b  %d %X %p %Y}")
        
    except FileNotFoundError as not_found_err:
        print(not_found_err)
        print( 'The file you are trying to open does not exist')
    except PermissionError as perm_err:
        print(perm_err)
        print('You are not allowed to open this file')
    except KeyError as key_err:
        print(key_err)
        print("This key does not exist in product's dictionary")
def read_products(filename):

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
            dictionary[row[0]] = [row[1],float(row[2])]
    #Return the dictionary
    return dictionary


# Call main to start this program.
if __name__ == "__main__":
    main()