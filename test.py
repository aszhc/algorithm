# encoding=utf8

sums = [3,1,5,8] 
new_sums = sorted(sums)
sum = 0
for i in range(0, len(new_sums),2):
    sum += new_sums[i]
print(sum)