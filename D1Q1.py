# Given an integer, perform the forllowing conditional actions:
# if n is odd, print Weird
# if n is even and in the inclusive range of 2 to 5, print Not Weird
# if n is even and in the inclusive range of 6 to 20, print Weird
# if n is even and greater that 20 perint Not Weird

n = int(input("Enter a number: "))

if n % 2 == 1:
    print("Weird")
else:
    if 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    else:
        print("Not Weird")