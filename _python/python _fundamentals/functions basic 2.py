#1
def countDown(a):
    for i in range(a, -1, -1):
        print(i)
countDown(5)

#2
def print_and_return(a,b):
    print(a)
    return(b)
print(print_and_return(4,7))

#3
def firstPlusLength(a):
    print(a[0]+len(a))

firstPlusLength([2,3,4,5,6,1])

#4
def greater_than_second(list):
    new_list = []
    counter = 0
    if len(list) <= 2:
        return False
    else:
        for i in range(len(list)):
            if list[i] > list[1]:
                new_list.append(list[i])
                counter = counter + 1
        print(counter)
        return new_list

print(greater_than_second([1,2]))
print(greater_than_second([1,6,3,4,7]))

#5
def length_value(a,b):
    result = []
    for i in range(b):
        result.append(a)
    return result

print(length_value(2,6))


        
