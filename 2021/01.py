with open("1.txt", "r") as f:
    data = f.readlines()

# map the data to a list of ints
data = list(map(int, data))

# use a sliding window of width 3
# and sum the values
# and store the result in a list

new_data = [sum(data[i:i+3]) for i in range(len(data)-2)]

assert len(new_data) == len(data)-2

# count number of times values have increased
count = 0
for i in range(1, len(new_data)):
    if new_data[i] > new_data[i-1]:
        count += 1

print(count)
