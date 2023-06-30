# a function that takes a list and target parameter
# multiple variables : middle , start, end, steps 
# recurrsion or while loop
# increase the steps each time a split is done
# conditions to track target position
def binary_search(list, element):
    middle = 0
    start = 0
    end = len(list)
  

    while start<=end:
        middle = (start+end)//2
        if element == list[middle]:
            return middle
        elif element>list[middle]:
            start = middle+1
        else:
            end = middle-1
    return -1

list = [1,22,56,76,87,100]
target = 56
print(binary_search(list,target)  )  
        
