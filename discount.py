subtotal = float(input('Please enter the subtotal: '))

from datetime import datetime


today = datetime.now()
today_number = today.weekday()

if subtotal >= 50 :
    if today_number == 1 or today_number == 2:
        discount = subtotal*0.1
        total=subtotal-discount
        tax = total*0.06
        total = total+tax
        print(f'Discount amount: {discount:.2f}')
        print(f'Sales tax amount: {tax:.2f}')
        print(f'Total: {total:.2f}') 
        
    else:
         tax = subtotal*0.06
         total = subtotal + tax
         print(f'Sales tax amount: {tax:.2f}')
         print(f'Total: {total:.2f}') 
else:
         tax = subtotal*0.06
         total = subtotal + tax
         print(f'Sales tax amount: {tax:.2f}')
         print(f'Total: {total:.2f}') 
         
         
