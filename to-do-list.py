# to do list in Python
# 3 lists: To do, In progress, & Completed
def checkInt(entry):
    try:
        int(entry)
        return True
    except ValueError:
        return False
    
def printLists(lists_list):
    for n in  range(0,len(lists_list)):
        print(lists_list[n][0])
        for item in lists_list[n][1]:
            print(item)
        print(' ')
    
def printOptions(x):
    for n in x:
        print(str(x.index(n)) + ' ' + n[0])

def updateLists(lists_list):
    print('Move item from?')
    #lists_list = [('-To Do-', todo_list), ('-In Progress-', inprog_list), ('-Completed-', compl_list)]
    printOptions(lists_list)
    print('enter any other character to cancel')
    response1 = input('> ')
    if not checkInt(response1):
          print('Entry was not number => move item cancelled.')
          print('Returned to create item mode.')
    elif int(response1) >= len(lists_list):
         print('Number entered not in valid range => move item cancelled')
    else:
         print('You are moving an item from {}. Move to?'.format(lists_list[int(response1)][0]))
         printOptions(lists_list)
         response2 = input('> ')
         print('Moving item from {} to {}. Choose item to move: '.format(lists_list[int(response1)][0], lists_list[int(response2)][0]))
         for item in lists_list[int(response1)][1]:
             print(str(lists_list[int(response1)][1].index(item)) + ' ' + item)
         print('enter digit: ')
         response3 = input('> ')
         if not checkInt(response3):
             print('Entry was not number => move item cancelled.')
             print('Returned to create item mode.')
         elif int(response1) >= len(lists_list):
             print('Number entered not in valid range => move item cancelled')
         else:
             # get item to copy
             working_str = lists_list[int(response1)][1][int(response3)]
             # copy item to new list
             lists_list[int(response2)][1].append(working_str)
             # remove item from original list
             lists_list[int(response1)][1].pop(int(response3))
             # if > 5 completed items, delete oldest
             if len(compl_list) == 5:
                 compl_list.pop(0)
             print('Item moved.')
             print(' ')
             printLists(lists_list)
             print('Returned to create mode.')
# make lists to hold on to items
todo_list = []
inprog_list = []
compl_list = []
lists_list = [('To Do', todo_list), ('In Progress', inprog_list), ('Recently Completed', compl_list)]

# print out instructions on how to use the app
helpInfo_str = 'Enter "SHOW" to display lists, "UPDATE" to move an item to another list, "HELP" to show this line and "DONE" when finished'
print('Add an item to TO DO list:')
print(helpInfo_str)

while True:
    # ask for new items
    new_item = input('> ')
    
    if new_item == 'DONE':
        break
    elif new_item == 'SHOW':
        printLists(lists_list)

    elif new_item == 'HELP':
        print(helpInfo_str)
    elif new_item == 'UPDATE':
        updateLists(lists_list)
    
    #add new item to list
    else:
        todo_list.append(new_item)
        print('Added {}. To Do list now has {} items.'.format(new_item, len(todo_list)))
        
#print out the lists
printLists()
