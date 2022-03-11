class User:

    user = get_player_choice
    

    def get_player_choice():
        user_choice = int(input("Please enter" (1, 2, 3, 4, 5)))
        
        if choice == 1:
            user_choice = "Rock"
        elif choice == 2:
            user_choice = "Paper"
        elif choice == 3:
            user_choice = "Scissors"
        elif choice == 4:
            user_choice = "Lizard"
        elif choice  == 5:
            user_choice = "Spock"
        else:
            print("Select a valid option")

        print("Player chose" + user_choice)

        return user()
