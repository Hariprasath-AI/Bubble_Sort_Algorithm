# Bubble Sort
# Time Complexity for this problem is based on the number of elements in the list
def Bubble_Sort(lst):
    # Assign 'True' for the variable swapped
    swapped = True

    # We really don't know about how many times we have to check the list.
    # We have to check until the list get sorted  
    while swapped:
        # Change swapped value to 'False'. While loop gets ended if 'If' condition inside the for loop doesn't satisfies.
        # It means that the List/Array is completely sorted  
        swapped = False
        
        # After Changing swapped value, we have to check pair of elements till the last element of the Array/List.
        for i in range(len(lst) - 1):
            # Check 1st element and 2nd element. If 1st element is greater than 2nd element, 1st and 2nd element will be swapped.
            # Checking continued until the 'if' condition fails. 
            if lst[i] > lst[i + 1]:
                swapped = True
                lst[i], lst[i + 1] = lst[i + 1], lst[i]

    # * infront of list variable is used to print the list elements without commas and square bracket            
    print(*lst)

if __name__ == "__main__":
    # Get a single line of integer input seperated by spaces/
    lst = list(map(int, input().split()))

    # Call the function 'Bubble_Sort' and pass the argument 'lst'
    Bubble_Sort(lst)