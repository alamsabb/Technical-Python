# days=int(input("Enter the number of days: "))
# year= days//365
# month=(days-(year*365))//30
# daysLeft=days%30

# print(f"{year} year {month} month {daysLeft} day")


# len 300feet 
# width 200 Feet

# area=300*200

# new_area=298*198
# # print(new_area)



def suraface(length,width):
    print(f"surface area without brick {length,width}")
    length=length-1
    width=width-1
    print(f"New Surface area {length*width}")
    
def border_area(oldsurface,innerArea):
    
len1,weidth=eval(input("Enter the lenth and weidth: "))
suraface(len1,weidth)