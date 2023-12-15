list74 = []
x = 0
while x != -1:
    x = int(input("Enter number to the sequence: "))
    list74.append(x)
summation = 0
count = 0
minimal = float('inf')
for i in list74:
    # checking if element from list is equal to -1
    if i == -1:
        break
    else:
        # updating count and summation
        count += 1
        summation += i
        # finding minimal element from the list as loop goes on
        if i < minimal:
            minimal = i
if count == 0:
    summation = -1
    minimal = -1
    average = -1
average = summation/count
print(f"Sum = {summation}")
print(f"Count = {count}")
print(f"Average = {average}")
print(f"Min = {minimal}")
# it looks like I learned how to use git today
