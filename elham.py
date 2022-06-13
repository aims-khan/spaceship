
print("rock")
print("paper")
print("scissor")

p1 = input("p1 make your move: ")
p2 = input("p2 make your move: ")

if p1 == p2:
    print("its a tie")
elif p1 =="rock" and p2 == "paper":
    print("p1 wins")
elif p2 == "rock" and p1 =="paper":
    print("p2 wins")
elif p1 == "paper" and p2 =="scissor":
    print("p2 wins")
elif p2 =="paper" and p1 =="scissor":
    print("p1 wins")
elif p1 =="rock" and p2 =="scissor":
    print("p1 wins")
elif p2 =="rock" and p1 =="scissor":
    print("p2 wins")
else:
    print("Please Enter The Value")
