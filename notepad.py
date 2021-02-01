import os

count = 1

title = input('Enter you list\'s name >>> ')
# item = input(f'{count}. Enter your list item >>> ')

def invalid_answer():
    global new_item
    if new_item.lower() != 'yes' and new_item.lower() != 'no':
        new_item = input('You need to enter either Yes or No')
        invalid_answer()

def list():
    def new():
        global new_item, item, count
        new_item = input('\nNew Item? Yes / No\r\n')
        item = input(f'{count}. Enter your list item >>> ')
        invalid_answer()
        if new_item.lower() == 'yes':
            count += 1
            item = input(f'{count}. Enter your list item >>> ')
        elif new_item.lower() == 'no':
            print('no')

    new()

list()
