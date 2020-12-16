A = 116
B = 299

judge = 0
K = 2**16-1

# part a)
# for i in range(40 * 10**6):
#     A = (A*16807)%2147483647
#     B = (B*48271)%2147483647
#     judge += (A & K) == (B & K)
#     if (i%10**6)==0:
#         print(i//10**6)

for i in range(5 * 10**6):
    A = (A*16807)%2147483647
    while A%4 != 0:
        A = (A*16807)%2147483647
    B = (B*48271)%2147483647
    while B%8 != 0:
        B = (B*48271)%2147483647
    judge += (A & K) == (B & K)
    if (i%10**6)==0:
        print(i//10**6)

print(judge)