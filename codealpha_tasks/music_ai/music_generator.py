from music21 import note, stream
import random

# Sample notes (pretend these are learned patterns)
notes = ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5']

generated_notes = []

for i in range(40):
    generated_notes.append(random.choice(notes))

music = stream.Stream()

for n in generated_notes:
    music.append(note.Note(n))

music.write('midi', fp='generated_music.mid')

print("Music generated and saved as generated_music.mid")
