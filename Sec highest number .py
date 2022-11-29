# Find second highest number from list without using any built-in function like min max count

def second_highest(list):
    list.sort()
    return list[-2]

list = [1,2,3,4,5,6]

print("Second highest number from list is: ", second_highest(list))
