arr1 = np.array([1,2,3,4,5])
arr2 = np.array([6,7,8,9,10])

def print_even_number(arrays):
    for array in arrays:
        for num in array :
            x = num % 2
            if x != 0:
                print('Even no. ',num)

print_even_number([arr1,arr2])
