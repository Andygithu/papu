import random
#Call to the append_random_numbers and then add a new numbe in the list randnums.
def main():
    randnums = [16.2, 75.1, 52.3]
    append_random_numbers(randnums)
    print(f'Randnums {randnums}')
    append_random_numbers(randnums,3)
    print(f'Randnums {randnums}')
    

    
#Compute the random number and the round that number according to the quantity times by default 1.
 
def append_random_numbers(numbers_list,quantity=1):
    
     
    for _ in range(quantity):
      float_number = random.uniform(1,50)
      pseudo_random_number = round(float_number,1)
      numbers_list.append(pseudo_random_number)
    
main()