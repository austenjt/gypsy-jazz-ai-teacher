#!/usr/bin/env python3
"""Check an etude's tab against the guitar-etude rules.

Usage: check_etude.py ETUDE.md [...]

Reads the tab block (six string lines, bars of 8 slots x 3 columns, chord label
line above each row, e.g. "  Am6 1   Am6 2") and checks:
  * every note is a chord tone of its bar, or an approach note one semitone from
    the chord tone that follows it
  * within a chord (same chord symbol on consecutive bars): consecutive notes are
    at most 3 frets apart and on the same or an adjacent string
  * at a chord change: the first note is at most 6 frets from the last note
  * each bar fits a window of at most 4 frets (open strings not counted)
Exit status 1 if any rule is broken.
"""
import re, sys

OPEN = [40, 45, 50, 55, 59, 64]  # E A D G B e, low to high
PC = {'C': 0, 'D': 2, 'E': 4, 'F': 5, 'G': 7, 'A': 9, 'B': 11}
CHORDS = {  # chord tones as pitch classes
    'Am6': 'A C E F#', 'Dm6': 'D F A B', 'Dm7': 'D F A C', 'E7': 'E G# B D',
    'E7b9': 'E G# B D F', 'G13b9': 'G B D F Ab', 'Cmaj7': 'C E G B',
    'Fmaj7': 'F A C E', 'Bb7': 'Bb D F Ab', 'Am7': 'A C E G', 'Am': 'A C E',
}
SLOT, SLOTS = 3, 8


def pcs(names):
    out = set()
    for n in names.split():
        v = PC[n[0]]
        for c in n[1:]:
            v += 1 if c == '#' else -1
        out.add(v % 12)
    return out


def parse(path):
    lines = open(path).read().splitlines()
    bars = []  # (label, number, [slots]) slots: None | (string, fret)
    i = 0
    while i < len(lines):
        if re.match(r'^\s+\S+ \d+', lines[i]) and i + 6 < len(lines) and lines[i + 1].startswith('e|'):
            labels = re.findall(r'(\S+) (\d+)', lines[i])
            rows = [lines[i + 1 + k] for k in range(6)]  # e B G D A E
            for b, (name, num) in enumerate(labels):
                slots = [None] * SLOTS
                for r, row in enumerate(rows):
                    string = 5 - r
                    cells = row[2:].split('|')[b]
                    for s in range(SLOTS):
                        txt = cells[s * SLOT:(s + 1) * SLOT].strip('-')
                        if txt:
                            if slots[s] is not None:
                                raise SystemExit(f'bar {num}: two notes in slot {s + 1}')
                            slots[s] = (string, int(txt))
                bars.append((name, int(num), slots))
            i += 7
        else:
            i += 1
    return bars


def main(path):
    bars = parse(path)
    bad, offs = [], []
    maxin = maxch = maxspan = 0
    prev = None
    prev_chord = None
    nnotes = 0
    for name, num, slots in bars:
        chord = pcs(CHORDS[name])
        notes = [(s, f) for s in slots if s for (s, f) in [s]]
        fretted = [f for _, f in notes if f > 0]
        span = max(fretted) - min(fretted) if fretted else 0
        maxspan = max(maxspan, span)
        if span > 3:
            bad.append(f'bar {num}: fret span {span} (window of {span + 1} frets)')
        seq = [x for x in slots if x]
        for k, (st, fr) in enumerate(seq):
            nnotes += 1
            p = OPEN[st] + fr
            if p % 12 not in chord:
                nxt = None
                if k + 1 < len(seq):
                    nxt = OPEN[seq[k + 1][0]] + seq[k + 1][1]
                elif num < len(bars):
                    s2 = next(x for x in bars[num][2] if x)
                    nxt = OPEN[s2[0]] + s2[1]
                N = ['C','C#','D','Eb','E','F','F#','G','Ab','A','Bb','B']
                nm = N[p % 12]
                if nxt is not None and abs(nxt - p) == 1 and nxt % 12 in chord:
                    offs.append(f'bar {num}: {nm} to {N[nxt % 12]}')
                else:
                    bad.append(f'bar {num}: {nm} (string {st}, fret {fr}) not in {name}')
            if prev is not None:
                df, ds = abs(fr - prev[1]), abs(st - prev[0])
                if k == 0 and prev_chord != name:
                    maxch = max(maxch, df)
                    if df > 6:
                        bad.append(f'bar {num}: change from {prev_chord} moves {df} frets')
                else:
                    maxin = max(maxin, df)
                    if df > 3 or ds > 1:
                        bad.append(f'bar {num}: {df} frets, {ds} strings apart within {name}')
            prev = (st, fr)
        prev_chord = name
    print(f'{path}: {len(bars)} bars, {nnotes} notes; max within-chord move {maxin} frets, '
          f'max move at a chord change {maxch}, max bar span {maxspan}')
    if offs:
        print('  approach notes: ' + ', '.join(offs))
    for b in bad:
        print('  FAIL ' + b)
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(max(main(p) for p in sys.argv[1:]))
