import math
def calc_num(n,c,d):
  div_c = n//c
  div_d = n//d
  div_cd = n//(c*d//math.gcd(c,d))
  return n-div_c-div_d+div_cd
a,b,c,d = map(int,input().split())
print(calc_num(b,c,d)-calc_num(a-1,c,d))