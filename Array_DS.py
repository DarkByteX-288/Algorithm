#Array in python

arr=[1,2,3,4]
arr.append(18)
arr.insert(4,30)
arr.remove(2)
arr.append(15)
#deleting an element by index
del arr[1]
#searching array Linear search
if 15 in arr:
    print(arr.index(15))
else:
    print('15 is not found')


print(arr)

fruits=['apple','banana','pear']

for frut in fruits:
    print(frut)



Marks = [
    [20,30,40,50], #stu 1
    [40,50,60,70], #stu 2
    [70,80,90,100] 
]


print(Marks[1][2])


for row in Marks:
    print(row)


for row in Marks:
    for ele in row:
        print(ele, end=" : ")
