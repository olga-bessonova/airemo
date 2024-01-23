lowest, second_lowest = 10**9, 10**9
for i in range(N):
  if a[i] <= lowest:
    second_lowest = lowest
    lowest = a[i]
  elif a[i] < second_lowest:
    second_lowest = a[i]

return lowest * second_lowest
