"""
Piano = Multiple octaves
1 Octave = 7 White keys  + 5 Blck keys

White keys: C, D, E, F, G, A, B
Black Key: Flat(b), Sharp(#) {Realtive to white keys}

Understand waves: Mathematical aspect
y = A sin(wt - kx)
w = Angular frequency = 2.pi.f
k = Wave number = 2.pi./lamda

y = A sin (wt) 
y(f) = A sin(2.pi.f.t)

Equal Temperament System: note_freq = base_freq * 2 ** (n/12)
"""

import numpy as np #pip install numpy
from scipy.io.wavfile import write #pip install scipy

sample_rate = 44100 #Hz

def get_wave(freq, duration=0.5):
    amplitude = 4096
    t = np.linspace(0, duration, int(sample_rate * duration))
    wave = amplitude * np.sin(2 * np.pi * freq * t)

    return wave

def get_piano_notes():
    octave = [
        'A0', 'Bb0', 'B0', 'C1', 'Db1', 'D1', 'Eb1', 'E1', 'F1', 'Gb1', 'G1', 'Ab1',
        'A1', 'Bb1', 'B1', 'C2', 'Db2', 'D2', 'Eb2', 'E2', 'F2', 'Gb2', 'G2', 'Ab2',
        'A2', 'Bb2', 'B2', 'C3', 'Db3', 'D3', 'Eb3', 'E3', 'F3', 'Gb3', 'G3', 'Ab3',
        'A3', 'Bb3', 'B3', 'C4', 'Db4', 'D4', 'Eb4', 'E4', 'F4', 'Gb4', 'G4', 'Ab4',
        'A4', 'Bb4', 'B4', 'C5', 'Db5', 'D5', 'Eb5', 'E5', 'F5', 'Gb5', 'G5', 'Ab5',
        'A5', 'Bb5', 'B5', 'C6', 'Db6', 'D6', 'Eb6', 'E6', 'F6', 'Gb6', 'G6', 'Ab6',
        'A6', 'Bb6', 'B6', 'C7', 'Db7', 'D7', 'Eb7', 'E7', 'F7', 'Gb7', 'G7', 'Ab7',
        'A7', 'Bb7', 'B7', 'C8'
        ]
    base_freq = 27.50

    note_freqs = {octave[i]:base_freq*pow(2, (i/12)) for i in range(len(octave))}
    note_freqs[''] = 0.0

    return note_freqs

def get_song_data(music_notes):
    note_freqs = get_piano_notes()
    print(note_freqs)
    song = [get_wave(note_freqs[note]) for note in music_notes.split('-')]
    song = np.concatenate(song)

    return song.astype(np.int16)


def get_chord_data(chords):
    chords = chords.split('-')
    note_freqs = get_piano_notes()

    chord_data = []
    for chord in chords:
        data = sum([get_wave(note_freqs[note]) for note in list(chord)])
        chord_data.append(data)

    chord_data = np.concatenate(chord_data, axis = 0)

    return chord_data.astype(np.int16)

if __name__ == '__main__':
    music_notes = 'A0-Bb0-B0-C1-Db1-D1-Eb1-E1-F1-Gb1-G1-Ab1-A1-Bb1-B1-C2-Db2-D2-Eb2-E2-F2-Gb2-G2-Ab2-A2-Bb2-B2-C3-Db3-D3-Eb3-E3-F3-Gb3-G3-Ab3-A3-Bb3-B3-C4-Db4-D4-Eb4-E4-F4-Gb4-G4-Ab4-A4-Bb4-B4-C5-Db5-D5-Eb5-E5-F5-Gb5-G5-Ab5-A5-Bb5-B5-C6-Db6-D6-Eb6-E6-F6-Gb6-G6-Ab6-A6-Bb6-B6-C7-Db7-D7-Eb7-E7-F7-Gb7-G7-Ab7-A7-Bb7-B7-C8'
    data = get_song_data(music_notes)
    data = data * (16300/np.max(data))
    print(data)

    write('song.wav', sample_rate, data.astype(np.int16))

"""     chords = 'EgB-DfA-AcE-BDf-gAcE-fAc'
    data = get_chord_data(chords)
    data = data * (16300/np.max(data))
    data = np.resize(data, (len(data)*5,))
    
    write('chords.wav', sample_rate, data.astype(np.int16)) """