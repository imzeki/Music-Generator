py

from pyknon.music import Note, Rest, NoteSeq
from pyknon.genmidi import Midi
from IPython.display import Audio
import random
import os

os.chdir("C://Users//dos_2//Desktop//music//creations")
name = input("Name of song wanted to be generated? \n")
name += ".mid"

def get_random_note_seq(n:int, pitches:set, durations:set, rests=True):
    "Add a rest to the set of pitches if desired."
    if rests:
        pitches.add('r')

    n *= 5
    this_seq = ''
    for i in range(n):
        pitch = random.sample(pitches, 3)
        duration = random.sample(durations, 1)
        this_seq += pitch[0] + duration[0] + ' '

    return NoteSeq(this_seq)

durations = {
    "2",
    "4",
    "8",
    "16"
}
A_major = {
    'A',
    'B',
    'C#',
    'D',
    'E',
    'F#',
    'G#'
}
G_major = {
    'G',
    'A',
    'B',
    'C',
    'D',
    'E',
    'F#'
}
D_major = {
    'D',
    'E',
    'F#',
    'G',
    'A',
    'B',
    'C#'
}
C_major = {
    'C',
    'D',
    'E',
    'F',
    'G',
    'A',
    'B',
    'C'
}
E_major = {
    'E',
    'F#',
    'G#',
    'A',
    'B',
    'C#',
    'D#',
    'E'
},
F_major = {
    'F',
    'G',
    'A',
    'Bb',
    'C',
    'D',
    'E',
    'F'
}
B_major = {
    'B',
    'C#',
    'D#',
    'E',
    'F#',
    'G#',
    'A#',
    'B'
}
Db_major = {
    'Db',
    'Eb',
    'F',
    'Gb',
    'Ab',
    'Bb',
    'C',
    'Db'
}
All = {
    'A',
    'B',
    'C',
    'D',
    'E',
    'F',
    'G',
    'Ab',
    'Bb',
    'Db',
    'Eb',
    'Gb',
    'A#',
    'B#',
    'C#',
    'D#',
    'E#',
    'F#',
    'G#',
    'A',
    'B',
    'C',
    'D',
    'E',
    'F',
    'G',
    'Ab',
    'Bb',
    'Db',
    'Eb',
    'Gb',
    'A#',
    'B#',
    'C#',
    'D#',
    'E#',
    'F#',
    'G#'
}
if random.randint(1, 9) == 1:
    notes = get_random_note_seq(70, A_major, durations)
    print("A Major used")
    midi = Midi(1, tempo=139)
    midi.seq_notes(notes, track=0)
    midi.write(name)
elif random.randint(1, 9) == 2:
    notes = get_random_note_seq(70, G_major, durations)
    print("G Major used")
    midi = Midi(1, tempo=139)
    midi.seq_notes(notes, track=0)
    midi.write(name)
elif random.randint(1, 9) == 3:
    notes = get_random_note_seq(70, D_major, durations)
    print("D Major used")
    midi = Midi(1, tempo=139)
    midi.seq_notes(notes, track=0)
    midi.write(name)
elif random.randint(1, 9) == 4:
    notes = get_random_note_seq(70, E_major, durations)
    print("E Major used")
    midi = Midi(1, tempo=139)
    midi.seq_notes(notes, track=0)
    midi.write(name)
elif random.randint(1, 9) == 5:
    notes = get_random_note_seq(70, F_major, durations)
    print("F Major used")
    midi = Midi(1, tempo=139)
    midi.seq_notes(notes, track=0)
    midi.write(name)
elif random.randint(1, 9) == 6:
    notes = get_random_note_seq(70, All, durations)
    print("All used")
    midi = Midi(1, tempo=139)
    midi.seq_notes(notes, track=0)
    midi.write(name)
elif random.randint(1, 9) == 7:
    notes = get_random_note_seq(70, Db_major, durations)
    print("Db Major used")
    midi = Midi(1, tempo=139)
    midi.seq_notes(notes, track=0)
    midi.write(name)
elif random.randint(1, 9) == 8:
    notes = get_random_note_seq(70, B_major, durations)
    print("B Major used")
    midi = Midi(1, tempo=139)
    midi.seq_notes(notes, track=0)
    midi.write(name)
else:
    notes = get_random_note_seq(70, C_major, durations)
    print("C Major used")
    midi = Midi(1, tempo=139)
    midi.seq_notes(notes, track=0)
    midi.write(name)