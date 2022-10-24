def DecToBin(num):
    List = []
    if isinstance(num, int):
        while num > 0:
            if num % 2 != 0:
                List.append('1')
            else:
                List.append('0')
            num = num // 2
        return ''.join(reversed(List))
    else:
        return 'Error'
def BinToDec(num):
    answer = 0
    if isinstance(num, int):
        num = ''.join(reversed(str(num)))
        for _ in range(len(num)):
            if num[_] == '1':
                answer += 2 ** _
            elif num[_] == '0':
                pass
        return answer
    else:
        return 'Error'