def do_twice(function, value):
    function(value)
    function(value)

def do_four(function, value):
    for x in range(0, 4):
        function(value)

def print_twice(string):
    print(string)
    print(string)

do_four(print_twice, 'warm')
