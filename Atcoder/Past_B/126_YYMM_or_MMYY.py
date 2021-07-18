S = input()
up = int(S[0:2])
down = int(S[2:4])
if 1 <= up <= 12:
  if 1 <= down <= 12:
    print("AMBIGUOUS")
  else:
    print("MMYY")
else:
  if 1 <= down <= 12:
    print("YYMM")
  else:
    print("NA")