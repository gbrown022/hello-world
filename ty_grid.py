def print_rail():
    print '+ - - - - + - - - - +'

def print_post():
    print '|         |         |'

def print_grid():
    for x in range(0, 2):
        print_rail()
        for y in range(0, 4):
            print_post()
    print_rail()

print_grid()
