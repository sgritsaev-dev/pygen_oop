def limited_hash(left, right, hash_function=hash):
    def wrapper(obj):
        res = hash_function(obj)
        while res not in range(left, right+1):
            if res >= right+1:
                res = left+(res-(right+1))
            elif res < left:
                res = right-(left-(res+1))
        return res
    return wrapper


hash_function = limited_hash(10, 15)

print(hash_function(8))
print(hash_function(11))
print(hash_function(17))
