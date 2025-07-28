import mingus.core.chords as chords
import mingus.core.progressions as progressions
import ast
class Progression:

    interval_effects = {
    
    ('I', 'I'): "Same chord, no mood change",
    ('I', 'II'): "Resignation",
    ('I', 'III'): "Loneliness",
    ('I', 'IV'): "Exploration, warmth",
    ('I', 'V'): "Optimism, energy",
    ('I', 'VI'): "Pure negative",
    ('I', 'VII'): "Destabilization",
    
    ('II', 'I'): "Clouded peace",
    ('II', 'II'): "Same chord, no mood change",
    ('II', 'III'): "Heightened dramatic intensity",
    ('II', 'IV'): "Help, sweetness, magnificence",
    ('II', 'V'): "Happy clarification",
    ('II', 'VI'): "Closedness, shyness",
    ('II', 'VII'): "Uncertainty",

    ('III', 'I'): "Soft return",
    ('III', 'II'): "Faltering",
    ('III', 'III'): "Same chord, no mood change",
    ('III', 'IV'): "Overcoming, solace",
    ('III', 'V'): "Strength, happy surprise",
    ('III', 'VI'): "Sad resolution, acceptance",
    ('III', 'VII'): "Unknown, complexity",

    ('IV', 'I'): "Bright peace",
    ('IV', 'II'): "Darkening",
    ('IV', 'III'): "Loss, fragility",
    ('IV', 'IV'): "Same chord, no mood change",
    ('IV', 'V'): "Heightened joy",
    ('IV', 'VI'): "Hardship",
    ('IV', 'VII'): "Drama, tension, alarm",

    ('V', 'I'): "Bright resolution",
    ('V', 'II'): "Setback",
    ('V', 'III'): "Bad news, left hanging",
    ('V', 'IV'): "Calm",
    ('V', 'V'): "Same chord, no mood change",
    ('V', 'VI'): "Disappointment",
    ('V', 'VII'): "Thickening, added tension",
    
    ('VI', 'I'): "Pure positive",
    ('VI', 'II'): "Hope, opening up",
    ('VI', 'III'): "Gravitas, epicness",
    ('VI', 'IV'): "Redemption, support",
    ('VI', 'V'): "Positive transformation",
    ('VI', 'VI'): "Same chord, no mood change",
    ('VI', 'VII'): "Pain, confusion",
    
    ('VII', 'I'): "Bright resolution",
    ('VII', 'II'): "Negative surprise",
    ('VII', 'III'): "Despair, anger",
    ('VII', 'IV'): "Mystery, magic",
    ('VII', 'V'): "Release",
    ('VII', 'VI'): "Dark resolution",
    ('VII', 'VII'): "Same chord, no mood change"
}

    def __init__(self, key: str = None, chords: list=[]):
        self.key = key
        self.chords = chords
        self.moods = []
        if key is None:
            return
        print(f"\nKey set to {key}.")

    def add_chord(self, chord: str):
        try:
            chords.from_shorthand(chord)
        except Exception:
            print(f"Invalid chord name: {chord}")
            return False
        self.chords.append(chord)

        if len(self.chords) >= 2:
            prev = self.chords[-2]
            curr = self.chords[-1]
            prev_numeral = self.get_numeral(prev)
            curr_numeral = self.get_numeral(curr)
            if prev_numeral and curr_numeral:
                mood = self.interval_effects.get((prev_numeral, curr_numeral), "Unknown")
                self.moods.append((f"{prev_numeral}-{curr_numeral}", mood))
            else:
                self.moods.append(("Non-diatonic", "Unknown"))
        return True

    def get_current_chord_progression(self):
        return self.chords
    
    def get_natural_triads(self):
        if not self.key:
            return ""
        natural_triads = ""
        numeral_function = [chords.I, chords.II, chords.III, chords.IV, chords.V, chords.VI, chords.VII]
        
        natural_triads = f"\nI-VII natural triads in the key of {self.key} in format [Chord]:[Triad]:\n"
        for i in range(7):
            natural_triads += f"{chords.determine(numeral_function[i](self.key), True, True)}: {numeral_function[i](self.key)}\n"

        return natural_triads
    
    def suggest_chords(self):
        last_chord = self.chords[-1]
        numerals = ["I", "II", "III", "IV", "V", "VI", "VII"]
        numeral_function = [chords.I, chords.II, chords.III, chords.IV, chords.V, chords.VI, chords.VII]
        
        last_numeral = None
        for i in range(7):
            if chords.from_shorthand(last_chord) in chords.from_shorthand(chords.determine(numeral_function[i](self.key), True, True)):
                last_numeral = numerals[i]
                break
        if last_numeral is None:
            print("Caution: the added chord doesn't belong to the diatonic harmonic scale of the key.")
            return
        for i in range(7):
            current_numeral = numerals[i]
            if current_numeral == last_numeral:
                continue
            target_chord = chords.determine(numeral_function[i](self.key), True, True)
            feel = self.interval_effects.get((last_numeral, current_numeral), "Unknown")
            print(f"{last_numeral} -> {current_numeral} | {target_chord} | {feel}")
        
    def get_cadence(self):
        cadence = []
        for chord in self.chords:
            chord_triad = chords.from_shorthand(chord, True)
            cadence.append(chord_triad)
        return progressions.determine(cadence, self.key, True), progressions.determine(cadence, self.key)
    
    def get_numeral(self, chord):
        numerals = ["I", "II", "III", "IV", "V", "VI", "VII"]
        numeral_function = [chords.I, chords.II, chords.III, chords.IV, chords.V, chords.VI, chords.VII]
        for i in range(7):
            determined = chords.determine(numeral_function[i](self.key), True, True)
            if chords.from_shorthand(chord) in chords.from_shorthand(determined):
                return numerals[i]
        return

    def get_emotional_arc(self):
        output = "\nEmotional progression:\n"
        for step, mood in self.moods:
            output += f"{step}: {mood}\n"
        return output
    
    def save_progression(self, filepath="saved_progressions.txt"):
        # Format: [key, progression]
        entry = [self.key, self.chords]
        with open(filepath, "a") as file:
            file.write(str(entry) + "\n")
        print(f"Progression saved to '{filepath}'")

    def retrieve_progression(self, chord_progression):
        if not chord_progression or len(chord_progression) != 2:
            print("Invalid progression format. Expected [key, [chords]]")
            return
        self.key = chord_progression[0]
        for chord in chord_progression[1]:
            self.add_chord(chord)
        self.chords = chord_progression[1]
        print(f"Active Progression:\n{self.chords}\nKey: {self.key}")
    
    def select_progression(self, filepath = "saved_progressions.txt"):
        try:
            with open(filepath) as file:
                lines = file.readlines()
                progs = [ast.literal_eval(line.strip()) for line in lines]
        except FileNotFoundError:
            print(f"File '{filepath}' not found")
            return
        if not progs:
            print("No saved progressions found")
            return
        for i, progression in enumerate(progs):
            key, chords = progression
            print(f"{i + 1}. Key: {key}     Progression: {chords}")
            while True:
                choice = input("Select this progression? (y/n): ").strip().lower()
                if choice not in ["y", "n"]:
                    print("Invalid input. Please choose 'y' or 'n'.")
                    continue
                if choice == "y":
                    self.retrieve_progression(progression)
                    return
                break

    def general_report(self):
        numerical_cadence = self.get_cadence()[0]
        chord_descriptions = self.get_cadence()[1]
        
        print("-" * 25)
        print("General Report")
        print("-" * 25)
        print(f"Key: {self.key}")
        print(f"Progression: {self.chords}\n")
        print(f"Cadence: {numerical_cadence}\n")
        print(f"Chord functions: {chord_descriptions}")
        print(self.get_emotional_arc())

