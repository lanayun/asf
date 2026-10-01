input("XOR all - pairs cncel,two odd-occurring one remains.enter")
print("[1,4,5,5] XOR of all",1^4^3^3," binary:",bin(1^4^3^3)[2:])
print("  split bit 1-> group A (bit 0 ON):1 group B (bit 0 OFF):4")

n = int(input("Enter a number(6,9):"))
guess = input("is bit 0 of "+str(n)+" ON?(yes/no):")
input("check the bit.enter")
if n&1:
    print("  ",n,"  binary:",bin(n)[2:]," bit 0 ON - group A your guess ", guess)
else:
    print("  ",n,"  binary:",bin(n)[2:]," bit 0 OFF- group B your guess ", guess)