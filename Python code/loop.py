# for i in range(5):
#     for j in range(2):
#         print(i,j)


# for i in range(20+1):
#     print(i)

# for a in (1,233,3):
#     print(a)

# for i in range(1,6):
#     print(i)



# import random

# jackpot = random.randint(1, 100)

# guess_number = int(input("Enter you guess number: "))

# counter = 1

# while guess_number != jackpot:

#     if guess_number < jackpot:
#         print("Wrong! Please guess higher")

#     else:
#         print("Wrong! Please guess lower")

#     guess_number = int(input("Enter you guess number: "))
#     counter += 1
# else:
#     print("Correct Guess")
#     print("Your attemtp is: ", counter)

    


# for i in range(1,6):
#     for j in range(i):
#         print("*", end=" ")
#     print("")

# for i in range(1,4):
#     for j in range(i):
#         print(j)


# for a in range(1,6):
#     for b in range(a):
#         print("Masum", end= "  ")

#     print()


# for a in range(1,6):
#     for b in range(1,a+1):
#         print(b, end=" ")

#     print()



# for a in range(20, 1, -1):
#     for b in range(a):
#         print("*", end=" ")
#     print()


# for a in range(1,6):
#     for b in range(1,9):
#         print("*", end=" ")

#     print()


row = 5

for i in range(1, row+1):
    print(" "*(row - i)+ " *"*i)