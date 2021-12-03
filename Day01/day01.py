## AoC Day 1

with open('input') as f:
    df = [int(l.strip('\n')) for l in f.readlines()]

## first half
count = 0
for i in range(1,len(df)):
    if df[i] > df[i-1]:
        count += 1

print(count)

## second half

count = 0
for i in range(3,len(df)):
    if len(df[(i-3):i]) > 2:
        if sum(df[(i-3):i]) > sum(df[(i-4):(i-1)]):
            count += 1
print(count)