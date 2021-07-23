import statistics
n = int(input())
d = list(map(int,input().split()))
median_low = statistics.median_low(d)
median_high = statistics.median_high(d)
print(median_high-median_low)