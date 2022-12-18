#Amstrong number
number=input("Enter a number : ")
number=str(number)
length =len(number)
sum = 0 
for i in number:
    sum += pow(int(i),length)
if int(number) == sum:
    print("Amstrong")
else:
    print("Not an Amstrong")
