print("Hello, this is the essence calculator created by Blubberinio, it's useless except if you don't know math!, use normal numbers no '3k' but '3000'")
type = int(input("\nWhat type of essence is it?\nType 1 for Undead,\n2 for Dragon,\n3 for Gold,\n4 for Diamond,\n5 for Wither,\n6 for Spider,\n7 for Ice"))

if type == 1:
    amount = int(input("How much undead essence is it?"))
    print("You'll have to pay", amount*1000, "coins")
if type == 2:
    amount = int(input("How much dragon essence is it?"))
    print("You'll have to pay", amount * 2500, "coins")
if type == 3:
    amount = int(input("How much gold essence is it?"))
    print("You'll have to pay", amount * 5000, "coins")
if type == 4:
    amount = int(input("How much diamond essence is it?"))
    print("You'll have to pay", amount * 4500, "coins")
if type == 5:
    amount = int(input("How much wither essence is it?"))
    print("You'll have to pay", amount * 6000, "coins")
if type == 6:
    amount = int(input("How much spider essence is it?"))
    print("You'll have to pay", amount * 5000, "coins")
if type == 7:
    amount = int(input("How much ice essence is it?"))
    print("You'll have to pay", amount * 27500, "coins")

