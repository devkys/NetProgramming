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

# import sys
# try:
#     fp = open('sample.txt')
#     sl = fp.readline()
#     value = int(sl.strip())
# except OSError as err:
#     print("OS Error:", err)
# except ValueError:
#     print('No Convert int')
# except:
#     print('Unkown Error')

class CallBook:
    def __init__(self, name, number, email, address):
        self.name = name
        self.number = number
        self.email = email
        self.address = address
    for _ in range(5):
        print('1. 연락처 입력\n2. 연락처 출력\n3. 연락처 삭제\n4. 종료')
        menu = input('메뉴선택: ')
        menu = int(menu)
        if menu == 1:
            name = input('Name:')
            number = input('Phone:')
            email = input('Email:')
            address = input('Address:')
        elif menu == 2:
            print("Name:", name)
            print("Phone:", number)
            print("Email:", email)
            print("Address:", address)
        elif menu == 3:
            print('')
        else:
            break
aa = CallBook()