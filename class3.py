#numbers and operators
a=6
b=6
# d= a + b
# print(f"tha addition of a and b is {d}")
# f=a - b
# print(f"tha substraction of a and b is {f}")
# g=a * b
# print(f"tha multiplication of a and b is {g}")
# h=a % b
# print(f"tha modulus of a and b is {h}")
# k=a / b
# print(f"tha division of a and b is {k}")

# #comparison operator
# y=a == b
# print(f"a and b are equal ...{y}")
# l=a > b
# print(f"a is greater than b ...{l}")
# p=a < b
# print(f"a is less than b ...{p}")
# q= a >= b
# print(f"a is greater than or equal to b ...{q}")
# z= a <= b
# print(f"a is lesser than or equal to b ...{z}")
# u=a != b
# print(f"a is not to b ...{u}")

#logical operator
# v=a<5 or a<10
# print(v)
# y=6>7
# z=7 == 7
# print(not y)
# g=7
# g+=8
# print(g)
# g-=5
# print(g)

# #conditional statement
# #  if condition:
# #  code
# x=5
# if x>6 :
#     print("x is greater than 6")
# else:
#     print("na lie")
# deposit=int(input("enter deposit amount"))
# withdrawal=int(input("enter withdrawal amount"))
# if deposit >= withdrawal:
#     print("sufficient balance")
# else:
#     print("insufficient balance")
# balance= deposit - withdrawal
# print(f"your balance is{balance}")

# username=(input("enter username"))
# pass1=int(input("enter password"))
# pass2=int(input("enter password again"))

# if pass1 == pass2:
#     print("welcome")
# else:
#     print("reenter password")
user_biodata={
   
}
user_biodata["username"]=input("input username")
user_biodata["age"]=int(input("age"))
user_biodata["state"]=input("state")
user_biodata["gender"]=input("gender")
user_biodata["password"]=int(input("enter password"))
user_biodata["password2"]=int(input("enter same password"))
print(user_biodata)

if user_biodata["password"] == user_biodata["password2"]:
    print("your biodata has been collected successfully")
else:
    print("check password")

