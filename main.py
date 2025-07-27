import mingus.core.chords as chords
import mingus.core.notes as notes
import mingus.core.keys as keys
import mingus.core.scales as scales
import mingus.core.progressions as progressions
from progression import Progression

def main():
    print("-" * 50)
    print("Welcome to the Music Theory Assistant")
    print("-" * 50)
           
    prog_builder_active = False
    prog_analyzer_active = False    
    # Selector for mode
    while True:
        message = "Choose Mode: \n1. Chord Progression Builder\n2. Chord Progression Analyzer [SOON]\n3. Exit\n>>> "
        mode = input(message)
        if mode not in ["1", "2", "3"]:
            print("Invalid option. Please choose 1, 2, or 3.")
            continue
        if mode == "1":
            prog_builder_active = True
            print("-" * 50)
            print("Chord Progression Builder")
            print("-" * 50)
            print("You can now add chords to your progression.")
            break
        if mode == "2":
            prog_analyzer_active = True
            print("-" * 50)
            print("Chord Progression Analyzer")
            print("-" * 50)
            print("You can now analyze your saved progressions.")
            break
        if mode == "3":
            print("Exiting the program.")
            return
    
    # Progression Builder
    if prog_builder_active:
        while True:
            select_key = f">>> Select key: "
            print("First, select a key for your chord progression.")
            current_key = input(select_key)
            if notes.is_valid_note(current_key):
                prog = Progression(current_key)
                print("\nEnter chords (for example: C, Dm, Gmaj7). Type 'done' when finished.\n")
                break
            else:
                print("Invalid key. Please enter a valid musical key (e.g., C, D, E, etc.).")

        triads = prog.get_natural_triads()
        print("Suggested chords based on the key:")
        print(f"{triads}")
        while True:
            print(f"\n>>> Current progression: {prog.get_current_chord_progression()}\nCurrent key: {current_key}")
            enter_chord = f"\nEnter chord name: "
            user_input = input(enter_chord)
            if user_input.lower() == 'done':
                print("Chord progression complete!\n")
                break
            if prog.add_chord(user_input):
                print("\nSuggested chords based on previous chord:")
                prog.suggest_chords()

        if prog.chords:
            print("-" * 25)
            print("Final Progression:")
            print("-" * 25)
            print("Progression (Chords):", prog.chords)
            print("Key:", prog.key)
            print(f"\nNumerical Progression: {prog.get_numerical_progression()[0]}")
            print(prog.get_emotional_arc())

        while True:
            save_message = "Do you want to save this progression? (y/n)\n>>> "
            save_input = input(save_message).strip().lower()
            if save_input not in ["y", "n"]:
                print("Invalid input. Please choose 'y' or 'n'.")
                continue
            if save_input == "y":
                prog.save_progression()
            else:
                print("Progression not saved")
            
            break



    # Progression Analyzer
    if prog_analyzer_active:
        print("Chord Progression Analyzer")

if __name__ == "__main__":
    main()