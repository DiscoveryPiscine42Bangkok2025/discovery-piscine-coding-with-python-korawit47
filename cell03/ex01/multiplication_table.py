i = int(input("Enter a number \n"))

print("\n".join(f"{j} x {i} = {int(i) * j}" for j in range(0, 10)) )