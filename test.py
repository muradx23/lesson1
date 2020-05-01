while True:
    c = input("What's your name? ")
    name = {
    'Murad': {"City": "Nizhniy Novgorod", "Temperature": "6 degree", "Wind":"moderate"},
    'Anya': {"City": "Piter", "Temperature": "7 degree", "Wind":"strong"}
    }
    if c in name:
        print("Information:")
        print()
        for i in name.get(c).items():
            print(": ".join(list(i)))
    else:
        print("It's a pity but there is not such name. You can enter another name.")
        continue
    print()
    r = input("Do you want to know information about another name? \nPlease write 'yes' or 'no' ")
    if r.casefold()=="yes":
        continue
    elif r.casefold()=="no":
        print("Thank you!")
        break
    else:
        print("Sorry but it's wrong! Only 'yes' or 'no': ")