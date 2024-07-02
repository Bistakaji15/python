'''
#program to calculate the electricity bill
amt=0
num=int(input("Enter number of electric unit"))
if nu<= 100:
    amt=0
    if nu>100 and nu<=200:   
       amt= (nu - 100 ) *5
    if nu> 200:
       amt=500 + (nu-200)*10
print("Amount to pay:",amt)
'''

fruits = ["apple " ,"banana","grapes"]
for index in range(len(fruits)):
    print(fruits[index])
else:
        print("inside Else Block")
