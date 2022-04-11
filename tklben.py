from playsound import playsound # Used to play the sounds in Python
from random import choice # Random answer by Ben

REPLIES_BEN = ("Yes.mp3", "No.mp3", "Laugh.mp3", "Ugh.mp3")

def BEN_REPLY():
    FILE_OPEN = f"ben_sounds/{choice(REPLIES_BEN)}" # Choose a random Ben sound
    playsound(FILE_OPEN) # Play the sound
    

def main():
    print("\n\n==================== Talking Ben in Python ====================\n\n")

    while True:
        USER_INPUT = input("Your message: ") # User Message
        if USER_INPUT.lower().strip() == "quit": break # If user types "quit" then quit
        BEN_REPLY() # Random sound from Ben
        
        
if __name__ == "__main__":
    main()
    