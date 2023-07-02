import string

def detect(character, _list, key):
    index = _list.index(character)
    new_index = index + key
    if new_index >= len(_list): # if list index out of range or key is big
        k = new_index // len(_list) # how many repetitions of the list need to skip
        result_index = new_index - k * len(_list)
        return  _list[result_index]
    else:
        return _list[new_index]

def encode(message, key):
    message_result = ""
    letters = list("abcdefghijklmnopqrstuvwxyz")
    numbers = list("0123456789")
    punctuation = list(string.punctuation)
    
    for i in message: # checks every character in the message
        if i.isupper():
            message_result += detect(i.lower(), letters, key).upper()
        elif i in letters:
            message_result += detect(i, letters, key)
        elif i in numbers:
            message_result += detect(i, numbers, key)
        elif i == " ":
            message_result += " "
        else:
            message_result += detect(i, punctuation, key)

    return message_result
