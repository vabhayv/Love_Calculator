print("Welcome!!\nHere's Your Love Calculator")
name1 = input("Write Your Name Here: ") 
name2 = input("Write Your Lover Name Here: ") 
merg = name1+name2
l_mweg =merg.lower()
t=l_mweg.count("t")
r=l_mweg.count("r")
u=l_mweg.count("u")
e=l_mweg.count("e")
true = t+r+u+e
l=l_mweg.count("l")
o=l_mweg.count("o")
v=l_mweg.count("v")
e=l_mweg.count("e")
love = l+o+v+e
sum=int(str(true)+str(love))
if sum<10 or sum>90:
  print(f"Your score is {sum}.")
elif sum>40 and sum<50:
  print(f"Your score is {sum}.")
else:
  print(f"Your score is {sum}.")