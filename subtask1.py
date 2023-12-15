n = int(input("Enter number n: "))
q = 1
while q**2 <= n:
    if (q+1)**2 > n:
        break
    else:
        q += 1
print(q)
# it looks like I learned how to use git today
