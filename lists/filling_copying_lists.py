N = int(input("What is the length of the list? "))

list_a = [0] * N
list_b = [0] * N


# filling a list
for i in range(N):
    list_a[i] = int(input("Enter a new element of the list: "))

print(list_a)

# copying a list
for i in range(N):
    list_b[i] = list_a[i]

print(list_b)

# reversing a list
for i in range(N-1, -1, -1):
    print(list_a[i])
