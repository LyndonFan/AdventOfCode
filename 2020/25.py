cardpk = 9093927
doorpk = 11001876

cardls = 0
cards = 1
while cards != cardpk:
    cards = (cards * 7) % 20201227
    cardls += 1

doorls = 0
doors = 1
while doors != doorpk:
    doors = (doors * 7) % 20201227
    doorls += 1

res = 1
for _ in range(doorls):
    res = (res*cardpk) % 20201227
print(res)
