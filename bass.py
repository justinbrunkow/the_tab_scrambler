#!/usr/bin/env python3

from random import randint, choice

letters = ('C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab', 'A', 'A#/Bb', 'B')

tuning  = ('G', 'D', 'A', 'E')
frets   = 20

fretboard = {string: [letters[(letters.index(string) + i) % 12] for i in range(frets)] for string in tuning}

major = (True, False, True, False, True, True, False, True, False, True, False, True)
key   = randint(0, 11)
scale = [letters[(interval + key) % 12] for interval in range(len(major)) if major[interval]]
print(f'\n  key = {letters[key]}\n')

from shutil import get_terminal_size
width = get_terminal_size().columns
beats = int((width - 8) / 7)

class note:
    def __init__(self, string, fret):
        self.string = string
        self.fret   = fret
        self.letter = fretboard[string][fret]

position = randint(0, frets - 4)
pattern  = {}
for string in tuning:
    pattern[string] = []
    for fret in range(position, position + 4):
        if fretboard[string][fret] in scale:
            pattern[string].append(note(string, fret))

melody = [choice(pattern[choice(tuning)]) for beat in range(beats)]

line = ''
for beat in melody:
    if len(str(beat.letter)) == 1:
        line += '   ' + str(beat.letter) + '   '
    else:
        line += ' ' + str(beat.letter) + ' '
print(f'note   ={line}')

line = ''
for beat in melody:
    line += '   ' + str(beat.fret - position + 1) + '   '
print(f'finger = {line}')

print('')
for string in pattern:
    line = ''
    for beat in melody:
        if beat.string == string:
            if len(str(beat.fret)) == 1:
                line += '—— ' + str(beat.fret) + ' ——'
            else:
                line += '— ' + str(beat.fret) + ' ——'
        else:
            line += '———————'
    print(f'     {string} | {line}')
print('')

# TESTING TESTING TESTING