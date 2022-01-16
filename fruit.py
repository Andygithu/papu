def main():
 try:
    # Create and print a list named fruit.
        fruit_list = ["pear", "banana", "apple", "mango"]
        print(f"original: {fruit_list}")
   #This is to reverse the order of the list above.
        fruit_list.reverse()
        print(f'reversed: {fruit_list}')
   #This is to append orange item inot the list above
        fruit_list.append('orange')
        print(f'append orange: {fruit_list}')
       #This is to find where apple is located in fruit_list and then replace it whit cherry.
        index_apple = fruit_list.index('apple')
        fruit_list.insert(index_apple,'cherry')
        print(f'insert cherry: {fruit_list}')
   #This is to remove 'banana' from the list.
        fruit_list.remove('banana')
        print(f'remove banana: {fruit_list}')
   #This is to remove the last item in the list.
        fruit_list.pop()
        print(f'pop orange: {fruit_list}')
    #This is to sort the items in the list.
        fruit_list.sort()
        print(f'sorted: {fruit_list}')
    #This is to remove all the items in the list.
        fruit_list.clear()
        print(f'cleared: {fruit_list}')

 except IndexError as index_err:
        print(type(index_err).__name__, index_err, sep=": ")
# Call main to start this program.
if __name__ == "__main__":
    main()