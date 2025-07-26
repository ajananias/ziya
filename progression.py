import mingus.core.chords as chords
import mingus.core.keys as keys

class Progression:
    def __init__(self, key: str, chords: list=[]):
        self.key = key
        self.chords = chords
        print(f"Key manually set to {key}.")

        
    def add_chord(self, chord: str):
        try:
            chords.from_shorthand(chord)
        except Exception:
            return f"Invalid chord name: {chord}"
        self.chords.append(chord)
    
    def get_current_progression(self):
        return self.chords
    
    def get_suggestions(self):
        if not self.key:
            return ""
        suggestions = ""
        numeral_function = [chords.I, chords.II, chords.III, chords.IV, chords.V, chords.VI, chords.VII]
        if chords.from_shorthand(self.chords[-1]) == chords.I(self.key):
            suggestions = f"Now, you can use all degrees of the scale I-VII:\n"
            for i in range(7):
                suggestions += f"{chords.determine(numeral_function[i](self.key), True, True)}: {numeral_function[i](self.key)},\n"
        if chords.from_shorthand(self.chords[-1]) == chords.II(self.key):
            suggestions = f"Now, you can use the following chords:\n"

        return suggestions

