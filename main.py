from hashlib import new
from unicodedata import name
import mingus.core.chords as chords
import mingus.core.notes as notes
import mingus.core.keys as keys
import mingus.core.scales as scales
import mingus.core.progressions as progressions
from progression import Progression

def main():
    current_key = None
    print("Welcome to the Music Theory Assistant")
    print("First, select a key for your chord progression.")
    select_key = f"Select key: "
    print("-" * 100)
    while True:
        current_key = input(select_key)
        if notes.is_valid_note(current_key):
            prog = Progression(current_key)
            print("Enter chords (for example: C, Dm, Gmaj7). Type 'done' when finished.")
            break
        else:
            print("Invalid key. Please enter a valid musical key (e.g., C, D, E, etc.).")
        
            

    while True:
        print("Current progression: ", prog.get_current_progression())
        enter_chord = f"Enter chord (Current key: {current_key}): "
        user_input = input(enter_chord)
        if user_input.lower() == 'done':
            break
        if prog.add_chord(user_input):
            print(prog.add_chord(user_input))
        suggestion = prog.get_suggestions()
        print(suggestion)


    if prog.chords:
        print("\nFinal Progression:")
        print("Chords:", prog.chords)
        print("Key:", prog.key)

if __name__ == "__main__":
    main()