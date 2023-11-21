my_var = 0
def show_options():
    return f"""You can:
    HELP - get help
    PRINT - print var
    QUIT - quit
    ADD - add to var
    SUB - substract from var
    SET - set var
    ++ - increment
    -- - decrement
    """

def add(*args):
    global my_var
    numbers = list(map(int, *args))
    for number in numbers:
        print(f"{my_var} + {number} = {my_var+number}")
        my_var+=number

def sub(*args):
    global my_var
    numbers = list(map(int, *args))
    for number in numbers:
        print(f"{my_var} - {number} = {my_var-number}")
        my_var-=number

def inc(*args):
    global my_var
    my_var+=1

def dec(*args):
    global my_var
    my_var-=1

def setvar(val, *args):
    global my_var
    my_var = val


def react_to_command(command):
    match command:
        case ["help" | "h", *args]:
            print(show_options())
        case ["print", *args]:
            print(f"{my_var = }")
        case ["add", *numbers]:
            add(numbers)
        case ["sub", *numbers]:
            sub(numbers)
        case ["++" | "--" as operator,  *args]:
            inc(args) if operator == "++" else dec(*args)
        case ["set", _ as val, *args] if val.isdigit():
            setvar(int(val),*args)
        case [_ as anything, "yolo"]:
            print(anything)
        case _ :
            print("Idk")

print(show_options())
while True:
    user_ipt = input("What to do?\n")
    if user_ipt.lower()[0] == "q":
        break
    react_to_command(user_ipt.lower().split(" "))
    