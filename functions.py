mySentence = 'loves the color'
color_list = ['pink','purple','blue','gray']
def color_function(name):
    lst = []
    for i in color_list:
        msg = "{0} {1} {2}".format(name,mySentence,i)
        lst.append(msg)
    return lst

def get_name():
    go = True
    while go:
        name = input('What is your name? ')
        if name == ' ':
            print("You need to provide your name")
        elif name == 'Sally':
            print("Sally, you may not use this software")
        else:
            go = False

    lst = color_function('Hailee')
    for i in lst:
        print(i)

get_name()

def my_function():
    print("Hailee is awesome")
my_function()
