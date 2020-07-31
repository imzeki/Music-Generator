from pyknon.music import Note, Rest, NoteSeq
from pyknon.genmidi import Midi
import random
import os
from typing import Any

def jumble(word:Any):
    """
    Jumbles a word to a random order, but with the same words, chances of it being the same are really low and chances of it shifting into a another word with meaning depends on the word given, spaces can end up being in a different
    location in the str, if you give a different type of variable, it will be returned randomized in a string format
    >>> jumble("Python")
    yphtno
    """
    import random
    Jumble = ""
    word = str(word)
    word = word.lower()
    while word:
        position = random.randrange(len(word))
        Jumble += word[position]
        word = word[:position] + word[(position + 1):]
    return Jumble


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

#Add more chords if you want to

while True:
    yes_or_no = input("Would you like to give the name or let the compter generate it?(Answer with yes or no, not case sensative) \n")
    yes_or_no = yes_or_no.lower()
    if yes_or_no == "yes":
        name = input("Name of song generated? \n")
        name += ".mid"
    else:
        prevWord = "The quick brown fox jumps over the lazy dog"
        word = "The quick brown fox jumps over the lazy dog".split()
        for i in range(random.randint(1, 10)):
            prevWord = random.choice(word)
            prevWord = jumble(prevWord)
            name = prevWord
            name += ".mid"
    os.chdir("C://Users//dos_2//Desktop//music//creations") #Replace this with the dircetory leading to creations starting from C://(OS)
    try:
        Notes = int(input("Notes(Affects duration of song, the more the longer) \n"))
    except:
        print("Only numbers!")
        Notes = 70

    def get_random_note_seq(n:int, pitches:set, durations:set, rests=True):
        "Add a rest to the set of pitches if desired."
        if rests:
            if random.randint(1, 10) is 1:
                pitches.add('r')

        n *= random.randint(1, 2)
        this_seq = ''
        for i in range(n):
            pitch = random.sample(pitches, 3)
            duration = random.sample(durations, 3)
            try:
                this_seq += pitch[0] + duration[0] + ' ' + pitch[1] + duration[1] + pitch[2] + duration[2] + pitch[0] + duration[0] + ' ' + pitch[1] + duration[1] + pitch[2] + duration[2] + pitch[0] + duration[0] + ' ' + pitch[1] + duration[1] + pitch[2] + duration[2] + ' '
            except:
                try:
                    this_seq += pitch[0] + duration[0] + ' ' + pitch[1] + duration[1] + ' '
                except:
                    this_seq += pitch[0] + duration[0] + ' '
        return NoteSeq(this_seq)

    if random.randint(1, 9) == 1:
        notes = get_random_note_seq(70, A_major, durations)
        print("A Major used")
        midi = Midi(1, tempo=random.randint(100, 240), instrument=[random.randint(1,117), random.randint(1,117), random.randint(1,117), random.randint(1,117)])
        midi.seq_notes(notes, track=0)
        midi.write(name)
    elif random.randint(1, 9) == 2:
        notes = get_random_note_seq(70, G_major, durations)
        print("G Major used")
        midi = Midi(1, tempo=random.randint(100, 240), instrument=[random.randint(1,117), random.randint(1,117), random.randint(1,117), random.randint(1,117)])
        midi.seq_notes(notes, track=0)
        midi.write(name)
    elif random.randint(1, 9) == 3:
        notes = get_random_note_seq(70, D_major, durations)
        print("D Major used")
        midi = Midi(1, tempo=random.randint(100, 240), instrument=[random.randint(1,117), random.randint(1,117), random.randint(1,117), random.randint(1,117)])
        midi.seq_notes(notes, track=0)
        midi.write(name)
    elif random.randint(1, 9) == 4:
        notes = get_random_note_seq(70, E_major, durations)
        print("E Major used")
        midi = Midi(1, tempo=random.randint(100, 240), instrument=[random.randint(1,117), random.randint(1,117), random.randint(1,117), random.randint(1,117)])
        midi.seq_notes(notes, track=0)
        midi.write(name)
    elif random.randint(1, 9) == 5:
        notes = get_random_note_seq(70, F_major, durations)
        print("F Major used")
        midi = Midi(1, tempo=random.randint(100, 240), instrument=[random.randint(1,117), random.randint(1,117), random.randint(1,117), random.randint(1,117)])
        midi.seq_notes(notes, track=0)
        midi.write(name)
    elif random.randint(1, 9) == 6:
        notes = get_random_note_seq(70, All, durations)
        print("All used")
        midi = Midi(1, tempo=random.randint(100, 240), instrument=[random.randint(1,117), random.randint(1,117), random.randint(1,117), random.randint(1,117)])
        midi.seq_notes(notes, track=0)
        midi.write(name)
    elif random.randint(1, 9) == 7:
        notes = get_random_note_seq(70, Db_major, durations)
        print("Db Major used")
        midi = Midi(1, tempo=random.randint(100, 240), instrument=[random.randint(1,117), random.randint(1,117), random.randint(1,117), random.randint(1,117)])
        midi.seq_notes(notes, track=0)
        midi.write(name)
    elif random.randint(1, 9) == 8:
        notes = get_random_note_seq(70, B_major, durations)
        print("B Major used")
        midi = Midi(1, tempo=random.randint(100, 240), instrument=[random.randint(1,117), random.randint(1,117), random.randint(1,117), random.randint(1,117)])
        midi.seq_notes(notes, track=0)
        midi.write(name)
    else:
        notes = get_random_note_seq(70, C_major, durations)
        print("C Major used")
        midi = Midi(1, tempo=random.randint(100, 240), instrument=[random.randint(1,117), random.randint(1,117), random.randint(1,117), random.randint(1,117)])
        midi.seq_notes(notes, track=0)
        midi.write(name)
    ask = input("Would you like to exit?(Answer with yes or no, not case-sensative) \n")
    if ask.lower() == "yes":
        exit(0)
    else:
        continue
