salary={1,1,2,3,4,5,6,78,9}
print(salary)
s=[21,32,43,54,65,76,7,8,9]
p=set(s)
print(p)
set1={1,2,3,4,5,6,78,9}
set1.add("dog")
print(set1)
set1.remove(78)
print(set1)
print(set1.pop)
print(len(set1))
set1.clear()
print(set1)
set1.__len__()
print(set1)
seta={"rice","beans","okazi","plantain","eba","banga"}
setb={"rice","beans","ewedu","plantain","amala","stew"}
setall=seta | setb
print(setall)
setcomon= seta & setb
print(setcomon)
# user_name=list(input("input random numbers"))
# non_duplicate=set(user_name)
# print(non_duplicate)
signup_user={"user1","user2","user3","user4","user5"}
login_user={"user2","user4","user1"}
active_user=signup_user & login_user
print(active_user)
joy_details={
    "username" :"joy",
    "password" : 8123586004,
    "email" : "chikaso111@gmail.com"
}
joy_name=joy_details["username"]
print(joy_name)
joy_email=joy_details["email"]
print(joy_email)
print(joy_details)
joy_details["id_number"]=80232
print(joy_details)
joy_details["password"]="moot"
print(joy_details)
del joy_details["email"]
print(joy_details)