# Take three inputs from a user, separately. Print the largest of the numbers.
#     Hint: Determine what type of data is taken in as input.
first_number=int(input('enter first number:'))
second_number=int(input('enter second number:'))
third_number=int(input('enter third number:'))
if first_number>second_number and first_number>third_number:
    print(f'{first_number} is the largest')
elif second_number>first_number and second_number>third_number:
    print(f'{second_number} is the largest')
else:
    print(f'{third_number} is the largest')
# .Take as input from a user the temperature if the temperature is above 30°C display “The temperature is too high”,if the temperature is above 15 display “Normal temperature” otherwise display “Cold temperature”
temperature=float(input('enter temperature'))
if temperature>30:
    print('The temperature is too high')
elif temperature>15 and temperature<30:
    print('normal temperature')
else:
    print('cold temperature')
# 3.	Write a Python program that checks if a variable x is between 10 and 20 (inclusive)
# and if another variable y is greater than 100. If both conditions are true, print "Conditions met", otherwise print "Conditions not met"
x=input('enter a value:')
y=input('enter a number:')
if x>=10 and x<=20 and y>100:
    print('conditions met')
else:
    print('conditions not met')
# 4. Write a Python program that checks if a variable password is equal to the string "secret123". If it is, print "Access   granted", otherwise print "Access denied"
correct_password='kiki18'
enter_password=input('enter your password')
if enter_password==correct_password:
    print('access granted')
else:
    print('access denied')
# 5. Write a Python program that checks if a variable student_score is greater than 90. If true, check if the attendance is greater than 80. If both conditions are true, print "Excellent student", otherwise print "Good score, but attendance needs improvement"

