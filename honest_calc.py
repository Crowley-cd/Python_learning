msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"
msg_9 = "You are"

memory = 0


def calc():
    global memory
    try:
        print(msg_0)
        x, oper, y = input().split(' ')
        if x == 'M' and y == 'M':
            x, y = memory, memory
        elif y == 'M':
            y = memory
        elif x == 'M':
            x = memory
        try:
            x, y = float(x), float(y)
        except TypeError('f:Calc try x,y float'):
            if not isinstance(x, float) or not isinstance(y, float):
                print(msg_1)
                return calc()

        check(x, y, oper)

        if oper == '+':
            result = x + y
        elif oper == '-':
            result = x - y
        elif oper == '*':
            result = x * y
        elif oper == '/' and y == 0:
            print(msg_3)
            return calc()
        elif oper == '/':
            result = x / y
        else:
            print(msg_2)
            return calc()

        print(result)
        save_result(result)

    except (TypeError, ValueError):
        print('Exception Type or Value Error. F:Calc()')
        calc()


def save_result(rslt):
    global memory
    print(msg_4)
    answer = input()
    if answer == 'y':
        return iod_save_to_memory(rslt)
    elif answer != 'n':
        return save_result(rslt)
    elif answer == 'n':
        continue_calc()


def iod_save_to_memory(result, msg_i=-99):
    global memory, msg_index

    if isinstance(result, float) and not is_one_digit(result):
        memory = result
    if is_one_digit(result):
        if msg_i == -99:
            msg_index = 10
        msg_n = {
            1: msg_1,
            2: msg_2,
            3: msg_3,
            4: msg_4,
            5: msg_5,
            6: msg_6,
            7: msg_7,
            8: msg_8,
            9: msg_9,
            10: msg_10,
            11: msg_11,
            12: msg_12,
        }
        iod_answer = input(f'{msg_n[msg_index]}\n')
        if iod_answer == 'y':
            if msg_index < 12:
                msg_index += 1
                return iod_save_to_memory(result, msg_index)
            else:
                memory = result
                return continue_calc()
        elif iod_answer == 'n':
            return continue_calc()
        else:
            return iod_save_to_memory(result)
    continue_calc()


def continue_calc():
    print(msg_5)
    answer = input()
    if answer == 'y':
        return calc()
    elif answer != 'n':
        return continue_calc()
    elif answer == 'n':
        exit(1)


def is_one_digit(value):
    if value.is_integer() and -10 < value < 10:
        return True
    else:
        return False


def check(x, y, oper):
    msg = ""
    if is_one_digit(x) and is_one_digit(y):
        msg = msg + msg_6
    if x == 1.0 or y == 1.0 and oper == '*':
        msg = msg + msg_7
    if (x == 0.0 or y == 0.0) and (oper == '*' or oper == '+' or oper == '-'):
        msg = msg + msg_8
    if msg != "":
        msg = msg_9 + msg
        print(msg)


calc()
