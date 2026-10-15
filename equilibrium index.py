def eq_mid(n):
    arr = [1] * n + [0] + [1] * n

    for i in range(len(arr)):
        left = sum(arr[:i])
        right = sum(arr[i+1:])

        if left == right:
            return i
    return -1

n = int(input("Enter n:"))
print("Array:", [1] * n + [0] + [1] * n)

answer = eq_mid(n)
print("Equilibrium point:", answer)