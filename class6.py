 def square(r):    return r ** 2
 print(square(7))

 def avg(list):
    return (sum(list)/len(list))
 print(avg([1,2,3,4,5,6,7,8]))

 def upper(letter):
    return letter.upper()
 print(upper("emeka"))

 def dupli(boy):
     return list(set(boy))
 print(dupli([1,1,2,2,3,3,4,5,6,6]))

def union(lista,listb):
    return list (set(lista) | set(listb))
print(union(["mango","orange"],["rice","beans"]))

def reverse(girl):
    return girl[::-1]
print(reverse([1,2,3,4,5]))

def quiz():
    q=input("Quiz question:How many bones are in the human body?")
    answer=int(input("your answer"))
    if answer == 207:
         print("correct")
     elif answer >= 200 and answer <=206:
          print("close. A little higher")
    elif answer >= 208 and answer <=212:
         print("close. A little lower")
    else:
         print("wrong")


quiz()
