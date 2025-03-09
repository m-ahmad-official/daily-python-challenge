def start_game():
    print("🏰 Welcome to the Mysterious Forest Adventure! 🌲")
    print("You wake up in a dark forest. Two paths lie ahead of you...")

    choice1 = input("Do you go left (L) or right (R)? ").strip().lower()

    if choice1 == "l":
        print("\nYou walk down a narrow path and find a strange old man offering a potion.")
        choice2 = input("Do you drink it? (Y/N): ").strip().lower()

        if choice2 == "y":
            print("\n💀 Oh no! The potion was poisoned. You collapse and lose the game! ❌")
        else:
            print("\n✨ Wise choice! The old man smiles and gives you a map to a hidden treasure! 🏆 You win! 🎉")
    
    elif choice1 == "r":
        print("\nYou enter a cave and see a sleeping dragon. 🐉")
        choice2 = input("Do you sneak past it (S) or attack it (A)? ").strip().lower()

        if choice2 == "s":
            print("\n🤫 You carefully tiptoe past the dragon and find an exit! You escape safely. 🎉 You win!")
        else:
            print("\n🔥 The dragon wakes up and breathes fire! You are burned to ashes. ❌ Game Over!")
    
    else:
        print("\nInvalid choice! Please restart and choose L or R.")

# Start the adventure!
start_game()
