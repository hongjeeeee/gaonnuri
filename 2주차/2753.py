ly = int(input())

if ly % 4 == 0 and ly % 100 != 0 or ly % 400 == 0:
  print(1)
else:
  print(0)