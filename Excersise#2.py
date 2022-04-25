from typing import Counter


numbers = [0,0,0,0]
numbers[0] = int(input(print("Write a number")))
numbers[1] = int(input(print("Write a number"))) 
numbers[2] = int(numbers[0] / numbers[1])

numbers[3] = numbers[0]/ numbers[1]  
numbers[3] = numbers[3] - numbers[2]
print("yours numbers " + str(numbers[0]) + " and " + str(numbers[1]) + " have a quotient " + str(numbers[2]) + "  and the rest is " + str(numbers[3]) )
#------------------Business---------------------------
money = int(input("how much money do you want to give"))
interest =int(input ("What is your interest %") )
years = int(input ("how many years "))
count = 0

if interest < 100 :
  interest = (interest + 100 )/100
else :
    interest = (interest /100)

while count != years :
 money = money * interest
 count = count+1
 print("Value in  " + str(count)+ "  year/s is: "+ str(money)) 
 #que es esto 