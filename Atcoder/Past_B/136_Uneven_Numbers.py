n = int(input())
if n < 10:
  print(n)
elif n < 100:
  print(9)
elif n < 1000:
  print(9+n-100+1)
elif n < 10000:
  print(909)
elif n < 100000:
  print(909+n-10000+1)
else:
  print(90909)