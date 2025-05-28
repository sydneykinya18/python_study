#if statement
a=20
b=40
if b>a:
    print('b is greater than a')
else:
    print('a is greater than b')
    #if else statement
    #2.write a program that prints 'pass' if marks are 50 or above , otherwise print 'fail'.
marks=80
if marks>=50:
    print('pass')
else:
    print('fail')
#write an if else statement that checks if the entered password is correct
#if yes print access granted otherwise print access denied
correct_password='kiki18'
enter_password=input('enter your password')
if enter_password==correct_password:
    print('access granted')
else:
    print('access denied')

#if elif else
marks=70
if marks>80:
    print('A')
elif marks>70 and marks<=80:
    print('B')
elif marks>60 and marks<=70:
    print('C')
elif marks>50 and marks<60:
    print('D')
else:
    print('fail')
