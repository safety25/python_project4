print("Welcome to my game!")

name = input("What is your name? ")
age = int(input("What is your age? "))

print(f"Hello {name} you are {age} years old.")


health = 10



if age >= 18:
    print("You are old enough to play! Yeyy!")

    want__to_play = input("Do you want to play? Yes/No ").upper()
    if want__to_play == "YES":
        print("Let's play!")
        print(f"You are starting with {health} health")
        weapon = "blade","shoutgun"
        
        pick_weapon = input ("Pick a weapon. Blade or shoutgun. ").lower()
        first_question = input("Left or Right? ").lower()
        
        
        if first_question == "left":
            ans = input("Nice, you followed the path reach a lake... Do you swim across or around? ").lower()
            if ans == "around":
                print("You went around and reach the other side of the lake.")
                
            
            elif ans == "across" and pick_weapon == "shoutgun":
                print("You managed to get across, but get bit by a snake and lost 5 health")
                health = health -5
            
            elif ans=="across" and pick_weapon=="blade":
                print("You got attacked by snake and you chop off his head and you manage to get across safely.")

            ans = input("You notice a house and a river. Which do you go?(river/house) ").lower()

            if ans == "house" and pick_weapon=="blade":
                print("You go to the house and are greated by the owner... \
                    He does not like you and attacked. You loose 5 health")
                health = health - 5
                if health <=0:
                    print("You have 0 life left and you lost...")
                elif health != 0:
                    print("You survived... You win!")
            
            elif ans == "house" and pick_weapon=="shoutgun":
                print("You go to the house and are greated by the owner... He attacked you but you shooted him.")
                
                if health <=0:
                    print("You have 0 life left and you lost...")    
                elif health != 0:
                    print("You survived... You win!")
                    

            else:
                print("You fell in the river and lost!")
                

            
        
        else:
            print("You fell down and lost")

    
    else:
        print("See you...")




else:
    print(f"Sorry {name} you are not old enough to play :(")

