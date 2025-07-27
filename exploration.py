import mingus.core.notes as notes
print(notes.int_to_note(0),
notes.int_to_note(1),
notes.int_to_note(2),
notes.int_to_note(3),
notes.int_to_note(4),
notes.int_to_note(5),
notes.int_to_note(6),
notes.int_to_note(7),
notes.int_to_note(8),
notes.int_to_note(9),
notes.int_to_note(10),
notes.int_to_note(11)
)

import mingus.core.chords as chords
print(chords.dominant_flat_ninth("D"))
print("Notes from I-VII of C:", chords.I("C"), chords.II("C"), chords.III("C"), chords.IV("C"), chords.V("C"), chords.VI("C"), chords.VII("C"))

cmaj7=chords.from_shorthand("Cmaj7")
print("Cmaj7 notes:", cmaj7)
print("CHORD NAMING ", chords.determine_triad(['A', 'C', 'E'], True))
print(chords.determine(['A', 'C', 'E'], True))
print(chords.determine(chords.IV('C'), True))


import mingus.core.scales as scales

diatonic_scale_c = scales.Diatonic("C", (3,7))
harmonic_minor_scale = scales.HarmonicMinor("A")
scale_notes = scales.get_notes(key="C")
whole_note_scale = scales.Chromatic("C")
print("Diatonic:", diatonic_scale_c)
print("Harmonic Minor:", harmonic_minor_scale)
print("Scale Notes:", scale_notes)
print("Whole Note Scale:", whole_note_scale)

import mingus.core.progressions as progressions
print("Position of chords:", progressions.determine([["C", "F", "G"], ["G", "C", "D"]], "C", True))
print("Function of chords:", progressions.determine([["C", "F", "G"], ["G", "C", "D"]], "C"))
print("Position of chords:", progressions.determine([['C', 'E', 'G'], ['G', 'B', 'D']], 'C', True))
import mingus.core.keys as keys
print("Notes of C:", keys.get_notes("C"))
print("Notes of C major scale:", keys.get_notes("A"))
import mingus.core.intervals as intervals