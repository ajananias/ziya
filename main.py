from hashlib import new
from unicodedata import name
import mingus.core.chords as chords
import mingus.core.notes as notes
import mingus.core.keys as keys
import mingus.core.scales as scales
import mingus.core.progressions as progressions
from progression import Progression

def main():
    print("Welcome to the Music Theory Assistant")
    print("-" * 100)
           
    prog_builder_active = False
    prog_analyzer_active = False    
    # Selector for mode
    while True:
        message = "Choose Mode: \n1. Chord Progression Builder\n2. Chord Progression Analyzer\n3. Exit\n>>> "
        mode = input(message)
        if mode == "1":
            prog_builder_active = True
            print("-" * 100)
            print("Chord Progression Builder")
            print("You can now add chords to your progression.")
            break
        if mode == "2":
            prog_analyzer_active = True
            print("-" * 100)
            print("Chord Progression Analyzer")
            print("You can now analyze your saved progressions.")
            break
        if mode == "3":
            print("Exiting the program.")
            return
    
    # Progression Builder
    if prog_builder_active:
        
        while True:
            select_key = f"Select key: "
            print("First, select a key for your chord progression.")
            current_key = input(select_key)
            if notes.is_valid_note(current_key):
                prog = Progression(current_key)
                print("Enter chords (for example: C, Dm, Gmaj7). Type 'done' when finished.")
                break
            else:
                print("Invalid key. Please enter a valid musical key (e.g., C, D, E, etc.).")

        triads = prog.get_natural_triads()
        print("Suggested Chords based on the key:\n")
        print(triads)
        while True:
            print("Current progression: ", prog.get_current_chord_progression())
            enter_chord = f"Current key: {current_key}\nEnter chord name: "
            user_input = input(enter_chord)
            if user_input.lower() == 'done':
                break
            
            if prog.add_chord(user_input):
                print("\nChord added successfully.")
                print("\nSuggested chords based on previous chord:")
                prog.suggest_chords()

        if prog.chords:
            print("\nFinal Progression:")
            print("-" * 50)
            print("Chords:", prog.chords)
            print("Key:", prog.key)
            

    if prog_analyzer_active:
        print("Chord Progression Analyzer")

if __name__ == "__main__":
    main()