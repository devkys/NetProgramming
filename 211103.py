# b = 0
# try:
#     a = 1/b
# except ZeroDivisionError:
#     print('0으로 나눌 수 없습니다.')
# else:
#     print(a)


# try:
#     a = int(input('Type a Number:'))
# except Exception as e:
#     print('Ocuur Erorr', e)
# else:
#     print(a)

import sys
try:
    fp = open('sample.txt')
    sl = fp.readline()
    value = int(sl.strip())
except OSError as err:
    print("OS Error:", err)
except ValueError:
    print('No Convert int')
except:
    print('Unkown Error')