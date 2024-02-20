def check_primr(num):
    if num>2:
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                return False
   
        else:
            return True
def check_even(num):
    if num%2==0:
        return True
    else:
        return False

# x=int(input("Enter a number: "))
# if check_primr(x) and check_even(x):
#     print("True")
# else:
#     print("False")
    
# for i in range(1,10001):
#     if(check_primr(i)):
#         print(i,end=", ")
        
        
def getinput(weather):
    while True:
        data=input(f"enter yes or no {weather}: ").lower()
        if data=="yes" or data=="no":
            return data
    
    
        
weather1=getinput("Raning")
weather2=getinput("snowing")


if weather1.lower()=="yes" or weather2.lower()=="no":
    print("True")
else:
    print("False")