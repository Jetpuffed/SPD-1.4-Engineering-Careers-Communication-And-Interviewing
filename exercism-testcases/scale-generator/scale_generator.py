#!/usr/bin/env python3

chromatic_flat = ["A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab"]
chromatic_sharp = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
tonic = ["C", "G", "D", "A", "E", "B", "F#", "a", "e", "b", "f#", "c#", "g#", "d#"]


class Scale(object):
    def __init__(self, note):
        self.tonic = note.title()
        if note in tonic:
            self.notes = chromatic_sharp
        else:
            self.notes = chromatic_flat

    def chromatic(self):
        index = self.notes.index(self.tonic)
        return [self.notes[(index + i) % 12] for i in range(12)]

    def interval(self, intervals):
        index = self.notes.index(self.tonic)
        scale = [self.tonic]
        for step in intervals[:-1]:
            index = (index + {"m": 1, "M": 2, "A": 3}[step]) % 12
            scale.append(self.notes[index])
        return scale
