def count_numbers(array, X):
    count = 0   

    # This stores the elements which have matched
    used_elements = []
    x = len(array)

    for i in range(x):
        for j in range(x):
            if array[i] + array[j] != X:
                continue
            if i == j :
                continue
            if i in used_elements or j in used_elements:
                continue

            # New match found, update count and add used 
            # elements to 
            count += 1
            used_elements.append(i)
            used_elements.append(j)

    return count


print(count_numbers([1, 1, 10, 32, 41], 42))
print(count_numbers([0, 15, 32, 2000, 15000], 15))
print(count_numbers([3, 4, 5, 6], 1))
