---
name: music-theory-arpeggios
display-name: Music Theory: Arpeggios
description: Define and identify arpeggios (minor, minor 6th, minor 7th, 6/9, diminished 7th from the half-whole scale) and label them as patterns in guitar tablature.
---

# Music Theory: Arpeggios

This skill is the arpeggio vocabulary behind the tab: which chord tones a passage plays, and which note is the root. It builds on `music-theory-scales`; use that skill for the scale formulas (the half-whole scale in particular), for the method of converting frets to pitch classes, for moving patterns along the neck, and for the labelling convention (name line above the block, degree line below). Layout and timing come from `guitar-tablature`.

Each arpeggio is defined by **interval formula**, **semitone set** and **note names** (in the key of A).

## Hard constraints

- **Spell from the formula, not from memory.** Every pattern is its formula applied to a root. If a spelled-out arpeggio disagrees with the formula, the formula wins.
- **Name the root and the pattern together.** "Am7 arpeggio", never just "minor 7th arpeggio". A pattern with no root is a shape, and should be called one.
- **Label which reading you chose** when a name is ambiguous (see "Ambiguous names" below). Do not silently pick one.
- **Tab limits still apply.** Six strings, frets 0-24, standard tuning unless stated. Every shape here is movable; check it still fits at the new position.
- **Flats for minor-key spellings** (`Bb`, `Eb`), sharps where the formula asks for one (`C#` and `F#` in A6/9). Use `#` and `b` in ASCII, never the unicode symbols.

## Reference table

| Arpeggio | Formula | Semitones | Notes in A | Symbol |
| --- | --- | --- | --- | --- |
| Minor | 1 b3 5 | 0 3 7 | A C E | Am |
| Minor 6th | 1 b3 5 6 | 0 3 7 9 | A C E F# | Am6 |
| Minor 7th | 1 b3 5 b7 | 0 3 7 10 | A C E G | Am7 |
| 6/9 (major) | 1 3 5 6 9 | 0 4 7 9 14 (= 2) | A C# E F# B | A6/9 |
| Diminished 7th | 1 b3 b5 bb7 | 0 3 6 9 | A C Eb Gb | Adim7 |

The diminished 7th is drawn from the half-whole scale (1 b2 b3 3 b5 5 6 b7): take every other note starting on the root, 1 b3 b5 bb7.

### Ambiguous names

These names are used for more than one thing. Defaults are in bold; say so if you use the other.

| Name | Default reading | Other reading |
| --- | --- | --- |
| Minor | **Minor triad** (1 b3 5) | Any minor-family chord |
| Diminished half-whole arpeggio | **Dim7 arpeggio (1 b3 b5 bb7) drawn from the half-whole scale** | The dominant b9 chord tones (1 3 5 b7 b9) of the same scale |
| 6/9 | **Major 6/9** (1 3 5 6 9) | Minor 6/9 (1 b3 5 6 9) |

## Identifying an arpeggio from tab

Use the pitch-class method in `music-theory-scales` ("Identifying a scale from tab"), then match the set below. A set of three to five notes that is a subset of a scale is still named as an arpeggio when it is played as chord tones: one note per string, or a clear sweep up or down.

### Fingerprints

| Set size | Has | It is |
| --- | --- | --- |
| 3 | 0 3 7 | Minor triad arpeggio |
| 4 | 0 3 7 9 | Minor 6th arpeggio |
| 4 | 0 3 7 10 | Minor 7th arpeggio |
| 4 | 0 3 6 9 | Diminished 7th arpeggio |
| 5 | 0 4 7 9 2 | 6/9 arpeggio |

### Same notes, different names

- **Minor 6th and half-diminished.** Am6 (A C E F#) is the same four notes as F#m7b5 (F# A C E). Choose by the bass note and the chord symbol.
- **Minor 7th and major 6th.** Am7 (A C E G) is the same four notes as C6 (C E G A).
- **Diminished 7th has four roots.** Adim7, Cdim7, Ebdim7 and Gbdim7 are the same four notes. The shape repeats every three frets.

## Pattern library

Shapes are shown in A with the root on the 6th string at fret 5, one note per string. The line under each block gives the chord-tone degree. `R` is the root. Moving rules are in `music-theory-scales`.

All shapes were checked: every fret is a note in the formula, and every formula note appears.

### Minor arpeggio (Am)

One note per string, root on the 6th string. This is the Am barre shape played note by note.

```
e|----------------------5--|
B|------------------5------|
G|--------------5----------|
D|----------7--------------|
A|------7------------------|
E|--5----------------------|
  R   5   R   b3  5   R
```

### Minor 6th arpeggio (Am6)

```
e|----------------------5--|
B|------------------5------|
G|--------------5----------|
D|----------4--------------|
A|------7------------------|
E|--5----------------------|
  R   5   6   b3  5   R
```

### Minor 7th arpeggio (Am7)

```
e|----------------------5--|
B|------------------5------|
G|--------------5----------|
D|----------5--------------|
A|------7------------------|
E|--5----------------------|
  R   5   b7  b3  5   R
```

### 6/9 arpeggio (A6/9)

Spans a three-fret window with two notes on the D string. The 9th is `B`.

```
e|--------------------------5--|
B|----------------------2------|
G|------------------4----------|
D|----------2---4--------------|
A|------4----------------------|
E|--5--------------------------|
  R   3   5   6   9   3   R
```

### Diminished 7th arpeggio

The arpeggio drawn from the half-whole scale. Shown on the 5th string, root D (Ddim7: D F Ab B), because this shape is only two frets wide there.

```
e|------------------7--|
B|--------------6------|
G|----------7----------|
D|------6--------------|
A|--5------------------|
E|---------------------|
  R   b5  R   b3  bb7
```

Move it up or down **three frets** and it is the same four notes with a different root (`F dim7`, `Ab dim7`, `B dim7`). Move it **one fret** and it is a new chord.

### Arpeggios rooted on the 5th string (D)

For when the lowest note is on the A string.

```
Dm                           Dm6
e|------------------5--|     e|------------------5--|
B|--------------6------|     B|--------------6------|
G|----------7----------|     G|----------4----------|
D|------7--------------|     D|------7--------------|
A|--5------------------|     A|--5------------------|
E|---------------------|     E|---------------------|
  R   5   R   b3  5           R   5   6   b3  5

Dm7                          D6/9
e|------------------5--|     e|----------------------2--|
B|--------------6------|     B|------------------5------|
G|----------5----------|     G|----------2---4----------|
D|------7--------------|     D|------4------------------|
A|--5------------------|     A|--5----------------------|
E|---------------------|     E|-------------------------|
  R   5   b7  b3  5           R   3   5   6   9   3
```

## Arpeggios and scales together

An arpeggio is a scale with most of its notes left out, so a line often moves between the two. Label each part (see "Labelling patterns in tab" in `music-theory-scales`), and label any scale note that is not a chord tone as a passing note.

## Reaching for an arpeggio (gypsy jazz context)

A rough map for choosing which arpeggio fits a chord, used when composing a line over changes. These are suggestions, not rules.

| Chord | Arpeggio to try | Why |
| --- | --- | --- |
| Am, Am6 | Am6 arpeggio | Am6 is the tonic sound in minor-key swing |
| Am7 | Am7 arpeggio | Straight minor 7th sound |
| E7 or E7b9 | G#dim7 arpeggio (scales: see `music-theory-scales`) | A dim7 arpeggio built on the 3rd of a dominant b9 chord gives its upper structure |
| A6/9 or A6 | A6/9 arpeggio | Major tonic with a closed sound |

## Playability checks

Before handing a pattern to anyone:

- **Fret window.** One position holds a four-fret window comfortably; five is a stretch. The shapes above are all four or fewer.
- **Range.** Shifted patterns must stay within frets 0-24 and above `E2`. Check the highest note too.
- **Every note is in the formula.** Convert the frets to pitch names and compare to the table. The check takes ten seconds and catches most mistakes.
- **Every formula note appears.** An arpeggio with a missing chord tone is a different chord.
- **One note per string** is the default for arpeggios; where a shape doubles a string, say so.

## Guardrails

- Do not name an arpeggio from its shape alone. Shapes repeat across chords; the interval set decides.
- Do not claim one root when the notes allow several. Say "also reads as F#m7b5" when it does.
- Do not drift from the formula. If a source gives a different spelling for the same name, state which one you are using.
- Do not present a single fingering as the only one. These are movable defaults.
- Keep to six strings and 24 frets. If a pattern would need a fret outside the neck, say so and offer the nearest playable octave.
- If the key, tuning, or the reader's intended reading of an ambiguous name is unknown and it matters, ask before writing the block.
