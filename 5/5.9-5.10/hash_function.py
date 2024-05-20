def hash_function_1(string):
    res = 0
    left_flag = 0
    right_flag = len(string)-1
    while left_flag < right_flag:
        res += ord(string[left_flag])*ord(string[right_flag])
        left_flag += 1
        right_flag -= 1
    if left_flag == right_flag:
        res += ord(string[left_flag])
    return res


def hash_function_2(string):
    res = 0
    for i in range(len(string)):
        if i % 2 == 0:
            res += ord(string[i])*(i+1)
        else:
            res -= ord(string[i])*(i+1)
    return res


def hash_function(obj):
    return (hash_function_1(str(obj)) * hash_function_2(str(obj)) % 123456791)


print(hash_function('python'))
