# Etude 2: Chromatic Rails

Chart: *Minor Swing* (Reinhardt-Grapelli), A minor, the 16-bar A section as written in the iReal chart: Am6 Am6 Dm6 Dm6 / E7 E7 Am6 Am6 / Dm6 Dm6 Am6 Am6 / Bb7 E7 Am6 E7, here played with the chart's alternate chords in bars 9-13 (Dm7, G13b9, Cmaj7, Fmaj7) and the b9 colour on E7 in bar 6. See `SONGS/minor-swing.md`.

Standard tuning `E A D G B e`. Notes are named in written guitar pitch (the sounding pitch is an octave lower). 4/4, swung eighth notes: **quarter = 160** to learn it, work up to 180-200. Each bar has eight note slots of three columns each, so two-digit frets fit. A slot with no fret is a rest. Chord symbols sit above each bar with the bar number. The line under each row of tab labels every note by its role in that bar's chord: `R` root, `3` or `b3`, `5`, `6`, `7` or `b7`, `b9`, and `a` for a chromatic approach or enclosure note that is not in the chord. A repeated note repeats its label.

Written to the `guitar-etude` fingering rule: while a chord lasts, consecutive notes are at most 3 frets apart and on the same or an adjacent string; at a chord change the line moves at most 6 frets; each bar fits a four-fret window.

## The idea

Rhythmic and chromatic. Eleven bars (1, 2, 3, 6, 7, 8, 9, 12, 13, 15, 16) open with an eighth-note rest, and several bars have rests inside them or at the end, which gives the line the bounce of Django-style playing. Notes outside the chords are only **chromatic approach notes** (a semitone from the chord tone that follows) and **enclosures** (one note a semitone above the target, one below, then the target). Enclosures: Bb and Ab around A in bars 1 and 7, Eb and C# around D in bar 13, and A and G around the G# in bar 16. Approach notes: E to F in bars 3 and 4, Bb to A in bar 3, Eb to E in bar 5, Ab to A and C# to C in bar 9, C# to D in bar 10, F# to G in bar 11, B to C in bar 12 and Bb to B in bar 14. Bars 2, 8 and 15 repeat a note on the offbeat (a **double note**). Bar 6 is a G#dim7 arpeggio (G# B D F) over E7b9, the classic dominant sound in this tune. The last bar rests on the final eighth after the G#.

## Tab

```
  Am6 1                    Am6 2                    Dm6 3                    Dm6 4
e|------------------------|------------------------|---------5--7--6--5-----|7--5--------------------|
B|---------------5--------|---------------5--7--5--|---5--6--------------6--|---------5--6--------6--|
G|------------5-----5-----|------5--5--------------|------------------------|---------------7--------|
D|---8--6--7-----------7--|---7--------------------|------------------------|------------------------|
A|------------------------|------------------------|------------------------|------------------------|
E|------------------------|------------------------|------------------------|------------------------|
     a  a  R  b3 5  b3 R      R  b3 b3    5  6  5      a  b3 5  6  a  5  b3  6  5     a  b3 R     b3

  E7 5                     E7b9 6                   Am6 7                    Am6 8
e|------------------------|------------4-----------|---------------0--------|---------------0--2--0--|
B|------3-----4--5--3-----|---------6-----6--------|------------1-----1-----|------1--1--------------|
G|---4-----------------4--|---4--7-----------7--4--|---3--1--2-----------2--|---2--------------------|
D|6-----------------------|------------------------|------------------------|------------------------|
A|------------------------|------------------------|------------------------|------------------------|
E|------------------------|------------------------|------------------------|------------------------|
  3  5  b7    a  R  b7 5      5  b7 b9 3  b9 b7 5      a  a  R  b3 5  b3 R      R  b3 b3    5  6  5

  Dm7 9                    G13b9 10                 Cmaj7 11                 Fmaj7 12
e|------------------------|3--1--------------------|------------2--3--------|------------------------|
B|---------1--3--2--1-----|---------2--3--------3--|------5-----------5-----|---------5--6--6--5-----|
G|---1--2--------------2--|---------------4--------|4--5-----------------5--|---4--5--------------5--|
D|------------------------|------------------------|------------------------|------------------------|
A|------------------------|------------------------|------------------------|------------------------|
E|------------------------|------------------------|------------------------|------------------------|
     a  5  b7 R  a  b7 5   R  b7    a  5  3     5   7  R  3     a  5  3  R      a  5  7  R  R  7  5

  Bb7 13                   E7 14                    Am6 15                   E7 16
e|---------------4--------|------------------------|------------------0-----|------------------------|
B|---4--------6-----6-----|5--3--------------------|---------------1-----1--|---------0--------------|
G|------6--7-----------7--|---------3--4--------4--|------2--2--------------|------1-----2--0--1-----|
D|------------------------|---------------6--------|---4--------------------|---2--------------------|
A|------------------------|------------------------|------------------------|------------------------|
E|------------------------|------------------------|------------------------|------------------------|
     a  a  3  5  b7 5  3   R  b7    a  5  3     5      6  R  R     b3 5  b3     R  3  5  a  a  3
```

## Practice notes

- The approach and enclosing notes should lean into the target: play them lightly and put the weight on the chord tone they lead to.
- Accent the beats with chord tones.
- Play bars 1, 7 and 13 until the enclosure is automatic: two notes either side of the target, then the arpeggio.
- Try bar 6 alone on every dim7 inversion (shift it three frets) to see how all four notes are equivalent.

Every pitch in the tab was checked against the chord in its bar by script (`.agents/skills/guitar-etude/scripts/check_etude.py`), and so was the fingering rule: inside a chord the biggest jump between notes is 3 frets, at a chord change it is 2 frets, and no bar needs more than a four-fret window. The etude has not been played on an instrument; fingerings are one way to play it, not the only way. Approach notes and enclosures were checked as sitting one semitone from the chord tone that follows them. The frets run from 0 to 9.
