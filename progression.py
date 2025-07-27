import mingus.core.chords as chords
import mingus.core.progressions as progressions

class Progression:

    interval_effects = {
    
    ('I', 'II'): "Resignation",
    ('I', 'III'): "Loneliness",
    ('I', 'IV'): "Exploration, warmth",
    ('I', 'V'): "Optimism, energy",
    ('I', 'VI'): "Pure negative",
    ('I', 'VII'): "Destabilization",
    
    ('II', 'I'): "Clouded peace",
    ('II', 'III'): "Heightened dramatic intensity",
    ('II', 'IV'): "Help, sweetness, magnificence",
    ('II', 'V'): "Happy clarification",
    ('II', 'VI'): "Closedness, shyness",
    ('II', 'VII'): "Uncertainty",

    ('III', 'I'): "Soft return",
    ('III', 'II'): "Faltering",
    ('III', 'IV'): "Overcoming, solace",
    ('III', 'V'): "Strength, happy surprise",
    ('III', 'VI'): "Sad resolution, acceptance",
    ('III', 'VII'): "Unknown, complexity",

    ('IV', 'I'): "Bright peace",
    ('IV', 'II'): "Darkening",
    ('IV', 'III'): "Loss, fragility",
    ('IV', 'V'): "Heightened joy",
    ('IV', 'VI'): "Hardship",
    ('IV', 'VII'): "Drama, tension, alarm",

    ('V', 'I'): "Bright resolution",
    ('V', 'II'): "Setback",
    ('V', 'III'): "Bad news, left hanging",
    ('V', 'IV'): "Calm",
    ('V', 'VI'): "Disappointment",
    ('V', 'VII'): "Thickening, added tension",
    
    ('VI', 'I'): "Pure positive",
    ('VI', 'II'): "Hope, opening up",
    ('VI', 'III'): "Gravitas, epicness",
    ('VI', 'IV'): "Redemption, support",
    ('VI', 'V'): "Positive transformation",
    ('VI', 'VII'): "Pain, confusion",
    
    ('VII', 'I'): "Bright resolution",
    ('VII', 'II'): "Negative surprise",
    ('VII', 'III'): "Despair, anger",
    ('VII', 'IV'): "Mystery, magic",
    ('VII', 'V'): "Release",
    ('VII', 'VI'): "Dark resolution"
}

    def __init__(self, key: str, chords: list=[]):
        self.key = key
        self.chords = chords
        self.moods = []
        print(f"\nKey set to {key}.")

    def add_chord(self, chord: str):
        try:
            chords.from_shorthand(chord)
        except Exception:
            return f"Invalid chord name: {chord}"
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
        
        natural_triads = f"\nI-VII natural triads in the key of {self.key}:"
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
        
    def get_numerical_progression(self):
        numerical_progression = []
        for chord in self.chords:
            chord_triad = chords.from_shorthand(chord, True)
            numerical_progression.append(chord_triad)
        return progressions.determine(numerical_progression, self.key, True), progressions.determine(numerical_progression, self.key)
    
    def get_numeral(self, chord):
        numerals = ["I", "II", "III", "IV", "V", "VI", "VII"]
        numeral_function = [chords.I, chords.II, chords.III, chords.IV, chords.V, chords.VI, chords.VII]
        for i in range(7):
            determined = chords.determine(numeral_function[i](self.key), True, True)
            if chords.from_shorthand(chord) in chords.from_shorthand(determined):
                return numerals[i]  # ← already a string
        return None

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


