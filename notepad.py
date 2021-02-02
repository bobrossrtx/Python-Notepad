import os

count = 1

def space():
        global title
        if " " in title:
            print('Your note\'s title can\'t contain whitespaces')
            title = input('Enter you list\'s name >>> ')
            space()

title = input('Enter you list\'s name >>> ')
space()
item = input(f'{count}. Enter your list item >>> ')
new_item = ''

def invalid_answer():
    global new_item

    if new_item.lower() != 'yes' and new_item.lower() != 'no':
        new_item = input('You need to enter either Yes or No')
        invalid_answer()

if os.path.exists('notes'):
    def note_name():
        global title
        with open(os.path.join("./notes", f'{title}.md'), "a") as f:
            f.writelines(f'# {title}\r\n')
    def write():
            global count, item, title
            with open(os.path.join("./notes", f'{title}.md'), "a") as f:
                f.writelines(f'- {item}\r')
                f.close
else:
    print('You need to create a notes directory') 

def list():
    def new():
        global new_item, item, count
        new_item = input('\nNew Item? Yes / No\r\n')
        invalid_answer()
        if new_item.lower() == 'yes':
            count += 1
            item = input(f'{count}. Enter your list item >>> ')
            write()
            new()
        elif new_item.lower() == 'no':
            file_path = os.path.abspath(f'{title}.md')
            print(f'Your note has been saved {file_path}')
            exit()

    new()

note_name()
write()
list()
