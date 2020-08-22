from pyknon.music import Note, Rest, NoteSeq
from pyknon.genmidi import Midi
import random
import os
from typing import Any

def jumble(word:Any):
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
    "4"
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
Sharps = {
    'A#',
    'B#',
    'C#',
    'D#',
    'E#',
    'F#',
    'G#'
}

Beautiful = {
    'C',
    'F',
    'G'
}

Beautiful2 = {
    'E',
    'A',
    'B'
}

Ab_Major = {
    'Ab',
    'C',
    'Eb'
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
    path = input('Where is the path to store the music files(e.g \'C:\\\')? \n')
    os.chdir(path)
    try:
        Notes = int(input("Notes(Affects duration of song, the more the longer, 100 is reccomended) \n"))
    except:
        print("Only numbers!")
        Notes = 70

    def get_random_note_seq(notes:int, pitches:set, durations:set, rests=False):
        if rests:
            if random.randint(1, 20) is 1:
                pitches.add('r')

        notes *= random.randint(1, 2)
        this_seq = ''
        for i in range(notes):
            try:
                pitch = random.sample(pitches, 3)
            except:
                pitch = random.sample(pitches, 2)
            duration = random.sample(durations, 1)
            try:
                this_seq += pitch[0] + duration[0] + ' ' + pitch[1] + duration[1] + pitch[2] + duration[2] + pitch[0] + duration[0] + ' ' + pitch[1] + duration[1] + pitch[2] + duration[2] + pitch[0] + duration[0] + ' ' + pitch[1] + duration[1] + pitch[2] + duration[2] + ' '
            except:
                try:
                    this_seq += pitch[0] + duration[0] + ' ' + pitch[1] + duration[1] + ' '
                except:
                    this_seq += pitch[0] + duration[0] + ' '
        return NoteSeq(this_seq)

    if random.randint(1, 13) == 1:
        notes = get_random_note_seq(Notes, A_major, durations)
        print("A Major used")
        midi = Midi(4, tempo=random.randint(50, 300), instrument=[random.randint(1,300), random.randint(1,300), random.randint(1,300), random.randint(1,300)])
        midi.seq_notes(notes, track=0)
        midi.write(name)
        print("Name is:", name)
    elif random.randint(1, 13) == 2:
        notes = get_random_note_seq(Notes, G_major, durations)
        print("G Major used")
        midi = Midi(4, tempo=random.randint(50, 300), instrument=[random.randint(1,300), random.randint(1,300), random.randint(1,300), random.randint(1,300)])
        midi.seq_notes(notes, track=0)
        midi.write(name)
        print("Name is:", name)
    elif random.randint(1, 13) == 3:
        notes = get_random_note_seq(Notes, D_major, durations)
        print("D Major used")
        midi = Midi(4, tempo=random.randint(50, 300), instrument=[random.randint(1,300), random.randint(1,300), random.randint(1,300), random.randint(1,300)])
        midi.seq_notes(notes, track=0)
        midi.write(name)
        print("Name is:", name)
    elif random.randint(1, 13) == 4:
        notes = get_random_note_seq(Notes, E_major, durations)
        print("E Major used")
        midi = Midi(4, tempo=random.randint(50, 300), instrument=[random.randint(1,300), random.randint(1,300), random.randint(1,300), random.randint(1,300)])
        midi.seq_notes(notes, track=0)
        midi.write(name)
        print("Name is:", name)
    elif random.randint(1, 13) == 5:
        notes = get_random_note_seq(Notes, F_major, durations)
        print("F Major used")
        midi = Midi(4, tempo=random.randint(50, 300), instrument=[random.randint(1,300), random.randint(1,300), random.randint(1,300), random.randint(1,300)])
        midi.seq_notes(notes, track=0)
        midi.write(name)
        print("Name is:", name)
    elif random.randint(1, 13) == 6:
        notes = get_random_note_seq(Notes, All, durations)
        print("All used")
        midi = Midi(4, tempo=random.randint(50, 300), instrument=[random.randint(1,300), random.randint(1,300), random.randint(1,300), random.randint(1,300)])
        midi.seq_notes(notes, track=0)
        midi.write(name)
        print("Name is:", name)
    elif random.randint(1, 13) == 7:
        notes = get_random_note_seq(Notes, Db_major, durations)
        print("Db Major used")
        midi = Midi(4, tempo=random.randint(50, 300), instrument=[random.randint(1,300), random.randint(1,300), random.randint(1,300), random.randint(1,300)])
        midi.seq_notes(notes, track=0)
        midi.write(name)
        print("Name is:", name)
    elif random.randint(1, 13) == 8:
        notes = get_random_note_seq(Notes, B_major, durations)
        print("B Major used")
        midi = Midi(4, tempo=random.randint(50, 300), instrument=[random.randint(1,300), random.randint(1,300), random.randint(1,300), random.randint(1,300)])
        midi.seq_notes(notes, track=0)
        midi.write(name)
        print("Name is:", name)
    elif random.randint(1, 13) == 9:
        notes = get_random_note_seq(Notes, C_major, durations)
        print("C Major used")
        midi = Midi(4, tempo=random.randint(50, 300), instrument=[random.randint(1,300), random.randint(1,300), random.randint(1,300), random.randint(1,300)])
        midi.seq_notes(notes, track=0)
        midi.write(name)
        print("Name is:", name)
    elif random.randint(1, 13) == 10:
        notes = get_random_note_seq(Notes, Sharps, durations)
        print("Sharps are used")
        midi = Midi(4, tempo=random.randint(50, 300), instrument=[random.randint(1,300), random.randint(1,300), random.randint(1,300), random.randint(1,300)])
        midi.seq_notes(notes)
        midi.write(name)
        print("Name is:", name)
    elif random.randint(1, 13) == 11:
        notes = get_random_note_seq(Notes, Beautiful, durations)
        print("Beautiful 1 is used")
        midi = Midi(4, tempo=random.randint(50, 300), instrument=[random.randint(1,300), random.randint(1,300), random.randint(1,300), random.randint(1,300)])
        midi.seq_notes(notes)
        midi.write(name)
        print("Name is:", name)
    elif random.randint(1, 13) == 12:
        notes = get_random_note_seq(Notes, Beautiful2, durations)
        print("Beautiful 2 is used")
        midi = Midi(4, tempo=random.randint(50, 300), instrument=[random.randint(1,300), random.randint(1,300), random.randint(1,300), random.randint(1,300)])
        midi.seq_notes(notes)
        midi.write(name)
        print("Name is:", name)
    else:
        notes = get_random_note_seq(Notes, Ab_Major, durations)
        print("Ab Major is used")
        midi = Midi(4, tempo=random.randint(50, 300), instrument=[random.randint(1,300), random.randint(1,300), random.randint(1,300), random.randint(1,300)])
        midi.seq_notes(notes)
        midi.write(name)
    os.startfile(name)
    ask = input("Would you like to exit?(Answer with yes or no, not case-sensative) \n")
    if ask.lower() == "yes":
        exit(0)
    else:
        continue
