
A = [21,3,4,5,8,5,2]
#def rearrange(A: list[int]):
for i in range(len(A)):
    print(f"{i} - {A[i:i+2]}")
    print(bool(i % 2))
    A[i:i+2] = sorted(A[i:i+2], reverse=bool(i % 2))

rearrange([2,3,4,5,8,5,2])
