# 1. converted a float to an integer with an inbuilt function in python
#temp=56.8926 to 57
temp=56.8926
temp=round(56.8926)
print(temp)
# 2 .convert the float below to give the results
#temp = 56.8926 to 56.89 
temp=56.8926
temp=round(temp,2)
print(temp)
#Convert the float below to give the results as follows
#temp = 56.8926 to 56.893 
temp=56.8926
temp=round(temp,2)
print(temp)
#Convert the float below to give the results as follows
#temp=56.8926 to 8.926 
temp=56.8926
temp=str(temp)
temp=temp[3:7]
temp=temp[0]+"."+temp[1:4]
temp=float(temp)
print(temp)

