num=[-2,-4,1,2,4]

num_=[]

for i in num:

    num_.append(abs(i))

sorted_num=set(sorted(num_))

closest_num=[]

for i in sorted_num:

    closest_num.append(i)

print("closest num to 0 is",closest_num[0])














