#Write a Python program that checks if a variable student_score is greater than 90. 
# If true, check if the attendance is greater than 80. 
# If both conditions are true, print "Excellent student", otherwise print "Good score, but attendance needs improvement"
student_score=int(input('enter score:'))
attendance=int(input('enter attendance:'))
if student_score>90:
    if attendance>80:
        print('excellent student')
    else:
        print('good score but attendance needs improvement')
else:
    print('score less than 90')
# Write a program that:e
# = > Takes the user's credit score and annual income as input.
credit_score=int(input('enter credit score:'))
anual_income=int(input('enter anual income:'))
# # # =>If the credit score is above 700, check if the income is above 50,000:
# # # =>If both conditions are met, print "Loan approved."
# # # =>If only the credit score is high, print "Income requirement not met."
# # # =>If the credit score is below 700, print "Credit score too low."
if credit_score>700 :
    if anual_income>50000:
        print('loan approved')
    else:
        print('income requirement not met')
else:
    print('credit score is too low')

# #     #task slide 56
# # #     Write a program that:
# # # Takes a transaction amount and account type ("Standard" or "Premium") as input.
transaction_amount=int(input('enter amount:'))
account_type=str(input('enter account type standard or premium:'))
# # # If the account type is "Standard":
# # # Check if the amount is above 500:
# # # If it is, print "Transaction exceeds the limit for Standard accounts."
# # # if account_type
# # # If not, print "Transaction approved.">
# # # If the account type is "Premium":
# # # Check if the amount is above 1,000:
# # # If it is, print "Transaction exceeds the limit for Premium accounts."
# # # If not, print "Transaction approved."
if account_type=='standard':
    if transaction_amount>500:
        print('transaction exceeeds the limit for stansard account')          
    else:
        print('transaction approved')
elif account_type=='premium':
    if transaction_amount>1000:
        print('transaction exceeds the limit for premium accounts')
    else:
        print('transaction approved')
else:
    print('wrong account')

#         #SLIDE 57
# # 1.Assume start_date = '2024-01-01' and end_date = '2024-12-31'. Write a conditional statement that checks:
# # If start_date comes before end_date, print "Valid period",
# # If start_date is after end_date, print "Invalid period".
# # If both dates are the same, print "One-day period".
start_date = '2024-01-01'
end_date = '2024-12-31'
if start_date<end_date:
    print('valid period')
elif start_date>end_date :
    print('invalid period')
else:
    print('one day period')
# # # 2.Given two strings str1 and str2, write a conditional statement that checks:
str1=800
str2=800
# # # If str1 is longer than str2, print "str1 is longer".
# # # If str2 is longer than str1, print "str2 is longer".
# # # If both have equal length, print "Both are of equal length".
if str1>str2:
    print('str1 is longer')
elif str2>str1:
    print('str2 is longer')
else:
    print('both are of equal length')
# #     #SLIDE 58

# # # 1.Given a list valid_ids = [101, 102, 103] and a variable user_id = 105, write a conditional statement that:
# # # Prints "Access Granted" if user_id is in valid_ids.
# # # Prints "Access Denied" if user_id is not in valid_ids.
valid_ids = [101, 102, 103]
user_id = 105
if user_id in valid_ids:#==valid_ids[0]and user_id==valid_ids[1]and user_id==valid_ids[2]:
    print('access granted')
else:
    print('access denied')
# # 4.Given a variable value that could be of any type, write a conditional statement that:
# # Prints "String Detected" if value is a string.
# # Prints "Integer Detected" if value is an integer.
# # Prints "Unknown Type" for any other type.
s=300
print(type(s))
if type(s)==str:
    print('string detected')
elif type(s)==float:
    print('float detected')
elif type(s)==int:
    print('integer detected')
else:
    print('unknown type')
# 5.Given x = 7 and y = 14, write nested conditional statements that print:
x = 7
y = 9
# "x and y are both even" if both x and y are even numbers.
# "Only y is even" if only y is even.
# "Neither x nor y are even" if both are odd.
if x%2==0:
    if y%2==0:
        print('x and y are both even')
    else:
        print('only x is even')
else:
    if y%2==0:
        print('only y is even')
    else:
        print('both are odd')



    
