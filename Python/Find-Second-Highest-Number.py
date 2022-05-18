# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given n scores. 
# Store them in a list and find the score of the runner-up.

if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    
    # one way is to use the implemented sorting method
    # arr.sort()
    # the other way is to implement it yourself
    
    # implement my own sorting algorithm - insertion sort
    for i in range(1, n):
        temp = arr[i]
        j = i - 1
        
        while temp < arr[j] and 0 <= j:
            arr[j + 1] = arr[j]
            j = j - 1
        
        arr[j + 1] = temp
    
    highest = arr[0]
    for x in arr[1:]:
        if x > highest:
            second_highest = highest
            highest = x
    print(second_highest)
