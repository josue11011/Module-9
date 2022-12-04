# Josue Cifuentes
# November 29, 2022
# Problem #2: : create a list called L that contains the numbers 0 to 10 then create a while loop to append
# current value then the while loop should stop once the counter variable is greater than 10.

def check_nums(list):
    i = 0
    New_list = []
    while i < 10:
        if list[i] > 10:
            break
        New_list.append(list[i])
        i = i + 1
    return New_list


L = [0,1, 2, 3, 4, 5, 6, 7, 8, 9,10]
list = L
print(check_nums(list))