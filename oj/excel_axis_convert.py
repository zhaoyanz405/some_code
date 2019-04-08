def convert(num: int = 0):
    _map = {i: chr(ord('A') + i) for i in range(26)}
    if num == 0:
        return _map[num]

    ret_list = list()
    while True:
        if num == 0:
            break
        num, y = divmod(num, 26)
        ret_list.append(y)

    ret_list.reverse()
    temp_list = [r - 1 for r in ret_list[0:-1]]
    temp_list.append(ret_list[-1])
    return ''.join(map(lambda x: _map[x], temp_list))


for i in range(100):
    print(i, convert(i))
