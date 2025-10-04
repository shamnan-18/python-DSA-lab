num=[]
for i in range (5):
    num.append (int(input("Enter the Number's")))
print("first:",num[0])
print("last:",num[-1])
print("All the elemnts:")
for n in num:
        print(n)
num.reverse()
print("reversed list:",num)