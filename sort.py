import random

def binarySearch(n, k, A):
    l = 0
    r = n - 1
    while l <= r:
        m = int((l + r) / 2)
        if k == A[m]:
            return m
        elif k < A[m]:
            r = m - 1
        else:
            l = m + 1
    return -1


values = []

for i in range(1,1000):
    values.append(random.randint(1, 1000))

values.sort()
print(values)

num = input("Enter the number to search: ")

print("Your value is in position: " +str(binarySearch(len(values), int(num), values)))




