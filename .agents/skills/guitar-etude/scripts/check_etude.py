#!/usr/bin/env python3
"""Check an etude's tab against the guitar-etude rules.

Usage: check_etude.py ETUDE.md [...]

Reads the tab block (six string lines, bars of 8 slots x 3 columns, chord label
line above each row, e.g. "  Am6 1   Am6 2") and checks:
  * every note is a chord tone of its bar, or an approach note (one semitone from
    the chord tone that follows) or an enclosure (two notes, one a semitone above
    and one below the chord tone that follows)
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
    'G69': 'G B D E A', 'Ab69': 'Ab C Eb F Bb', 'A7': 'A C# E G', 'D7': 'D F# A C',
    'G/B': 'G B D', 'Bbo7': 'Bb C# E G', 'A-7': 'A C E G', 'C-6': 'C Eb G A',
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
    N = ['C', 'C#', 'D', 'Eb', 'E', 'F', 'F#', 'G', 'Ab', 'A', 'Bb', 'B']
    bad, devices = [], []
    maxin = maxch = maxspan = 0
    flat = []  # (bar number, chord name, string, fret, pitch, first note of bar?)
    for name, num, slots in bars:
        fretted = [f for x in slots if x for f in [x[1]] if f > 0]
        span = max(fretted) - min(fretted) if fretted else 0
        maxspan = max(maxspan, span)
        if span > 3:
            bad.append(f'bar {num}: fret span {span} (window of {span + 1} frets)')
        first = True
        for x in slots:
            if x:
                flat.append((num, name, x[0], x[1], OPEN[x[0]] + x[1], first))
                first = False
    chords = {name: pcs(CHORDS[name]) for name, _, _ in bars}
    k = 0
    while k < len(flat):
        num, name, st, fr, p, _ = flat[k]
        if p % 12 not in chords[name]:
            run = [k]
            while run[-1] + 1 < len(flat) and flat[run[-1] + 1][4] % 12 not in chords[flat[run[-1] + 1][1]]:
                run.append(run[-1] + 1)
            tk = run[-1] + 1
            ok = False
            if tk < len(flat) and len(run) <= 2:
                tp = flat[tk][4]
                offs = [flat[r][4] - tp for r in run]
                if all(abs(o) == 1 for o in offs) and (len(run) == 1 or offs[0] != offs[1]):
                    ok = True
                    kind = 'approach' if len(run) == 1 else 'enclosure'
                    devices.append(f'bar {num}: {kind} ' + ' '.join(N[flat[r][4] % 12] for r in run) + f' to {N[tp % 12]}')
            if not ok:
                bad.append(f'bar {num}: {N[p % 12]} (string {st}, fret {fr}) not in {name} and not an approach or enclosure')
            k = run[-1] + 1
        else:
            k += 1
    for k in range(1, len(flat)):
        a, b = flat[k - 1], flat[k]
        df, ds = abs(a[3] - b[3]), abs(a[2] - b[2])
        if b[5] and a[1] != b[1]:
            maxch = max(maxch, df)
            if df > 6:
                bad.append(f'bar {b[0]}: change from {a[1]} moves {df} frets')
        else:
            maxin = max(maxin, df)
            if df > 3 or ds > 1:
                bad.append(f'bar {b[0]}: {df} frets, {ds} strings apart within {b[1]}')
    reps = sum(1 for k in range(1, len(flat)) if flat[k][4] == flat[k - 1][4])
    print(f'{path}: {len(bars)} bars, {len(flat)} notes; max within-chord move {maxin} frets, '
          f'max move at a chord change {maxch}, max bar span {maxspan}; repeated notes {reps}')
    if devices:
        print('  ' + ', '.join(devices))
    for b in bad:
        print('  FAIL ' + b)
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(max(main(p) for p in sys.argv[1:]))
