class NotAValidAnswer(Exception):
    pass
#Maybe create another error for responses that are not numbers

def value_error(input_type, real_input = ''):
    if input_type == 'str' and real_input not in ['y', 'yes', 'n', 'no']:
        raise NotAValidAnswer("You should input yes (y) or no (n), it's not that difficult.")
    elif input_type == 'int':
        raise NotAValidAnswer("Do you know what an INTEGER is? And only positive numbers, please.")
    
    # value = 1
    # def some_inner_function():
    #     value += 1

    # some_value = "I don't know what you were expecting"
