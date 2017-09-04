nice = 0
mean = 0

def main():
    start()

def start():
    print "Welcome to Nice or Mean!!"
    name = raw_input("What is your name? : ")
    print "Hello, "+name+"!"
    print "In this game, you will be greeted by several different people. You can treat them nicely or you can be mean."
    print "At the end of the game your fate will be determined by how you acted."

    choice = raw_input("Do you want to play? y/n : ")

    if choice == "y":
        print "Yay, use 'm' for mean and 'n' for nice!"
        begin()

    if choice == "n":
        print "Okay, bye....."

def begin():
    global nice
    global mean

    if nice > 3:
        print "Nice job - you win! Everyone loves you because of your kindness!"
        choice = raw_input("Do you want to play again? y/n : ")

        if choice == "y":
            print "Okay lets go!"
            nice = 0
            mean = 0
            begin()

        if choice == "n":
            print "Say no more.... bye!"
            exit()

    if mean > 3:
        print "Too bad - game over! You are too unpleasant for friends."

        choice = raw_input("Do you want to play again? y/n : ").lower()

        if choice == "y":
            print "Okay lets go!"
            mean = 0
            nice = 0
            begin()

        if choice == "n":
            print "off you go!"
            exit()

        elif choice != "y"+"n":
            print "Please enter y or n"

            if choice == "y":
                begin()
            if choice == "n":
                print "See you later!"
                exit()

            if choice != "y"+"n":
                choice = raw_input("Do you want to play? y/n : ")

    pick = raw_input("Someone approaches you to talk. Will you be nice or mean? n/m : ")

    if pick == "n":
        print "They smile, wave and you both converse. Then they walk away."
        nice = nice+1
        print "You currently have " +str(nice) + " nice."
        begin()

    if pick == "m":
        print "They look sad and walk away."
        mean = mean+1
        print "You currently have " +str(mean) + " mean."
        begin()
                
        















start()
