# children=4
# candies_with_chef=2
# each_packer=4
# remain_need_to_buy=children - candies_with_chef
# need_to_buy=remain_need_to_buy // each_packer
# if need_to_buy % 4 !=0 :
#     need_to_buy+=1
# print(need_to_buy)


x,y=eval(input("Enter the value of x and y: "))

x=x-y
y=y//2

print(x+y)