import string
import testbase
import os.path

UserFound = False
PassWordCheck = False
while True:
    if not os.path.exists('Data.txt'):
        f = open('Data.txt', 'x')
        f.close()
        with open('Data.txt', 'w') as data2:
            data2.write("User      | Hash                                                             | Save\n")
            data2.close
    with open('Data.txt', 'r') as d:
        if testbase.u[0] in d.read():
            UserFound = True
            d.close()
            d = open('Data.txt', 'r')
            if testbase.h[0] in d.read():
                PassWordCheck = True
                
    if UserFound == False:
        print('Welcome ', testbase.u[0])            
        with open('Data.txt', 'r') as data1:
            data_content = data1.readline()
            if data_content != '\0':
                data1.close
                with open('Data.txt', 'a') as data:
                    data.write(f'{testbase.u[0]}     | {testbase.h[0]}\n')
                    data.close
                break
    if UserFound == True and PassWordCheck == True:
        print("Welcome Again")
        break
    if UserFound == True and PassWordCheck == False:
        print('Wrong Password')
        break
    