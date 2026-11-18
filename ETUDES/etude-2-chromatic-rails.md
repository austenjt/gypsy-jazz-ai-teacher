# Etude 2: Chromatic Rails

Chart: *Minor Swing* (Reinhardt-Grapelli), A minor, the 16-bar A section as written in the iReal chart: Am6 Am6 Dm6 Dm6 / E7 E7 Am6 Am6 / Dm6 Dm6 Am6 Am6 / Bb7 E7 Am6 E7, here played with the chart's alternate chords in bars 9-13 (Dm7, G13b9, Cmaj7, Fmaj7) and the b9 colour on E7 in bar 6. See `SONGS/minor-swing.md`.

Standard tuning `E A D G B e`. Notes are named in written guitar pitch (the sounding pitch is an octave lower). 4/4, swung eighth notes: **quarter = 160** to learn it, work up to 180-200. Each bar has eight note slots of three columns each, so two-digit frets fit. A slot with no fret is a rest. Chord symbols sit above each bar with the bar number.

Written to the `guitar-etude` fingering rule: while a chord lasts, consecutive notes are at most 3 frets apart and on the same or an adjacent string; at a chord change the line moves at most 6 frets; each bar fits a four-fret window.

## The idea

Rhythmic and chromatic. Eleven bars (1, 2, 3, 6, 7, 8, 9, 12, 13, 15, 16) open with an eighth-note rest, and several bars have rests inside them, which gives the line the bounce of Django-style playing. Approach notes (a semitone from a chord tone, played just before it) are the only notes outside the chords: G# to A in bar 1, Bb to B and Eb to D in bar 3, Bb to B in bar 4, G to G# in bar 5, B to C in bars 7 and 12, C# to D in bars 9, 10 and 14, F# to F in bar 9, Eb to E in bar 11, E to F in bar 13 and G to G# in bar 16. Bar 6 is a G#dim7 arpeggio (G# B D F) over E7b9, the classic dominant sound in this tune.

## Tab

```
  Am6 1                    Am6 2                    Dm6 3                    Dm6 4
e|------------0-----------|------------------------|------------------------|1-----------------------|
B|---------1-----1--------|---------------5--------|---------3--6--4--3--0--|---3--------------------|
G|---1--2-----------2-----|------------5-----5-----|---3--4-----------------|---------3--4--2-----4--|
D|---------------------4--|---4--7-----------------|------------------------|------------------------|
A|------------------------|------------------------|------------------------|------------------------|
E|------------------------|------------------------|------------------------|------------------------|

  E7 5                     E7b9 6                   Am6 7                    Am6 8
e|------------3--4--------|------------4-----------|------------------------|------------------------|
B|---3--5-----------5--3--|---------6-----6--------|---------5--7--5--------|------------5--7--5-----|
G|4-----------------------|---4--7-----------7--4--|---4--5-----------5-----|------5-----------------|
D|------------------------|------------------------|---------------------7--|---7--------------------|
A|------------------------|------------------------|------------------------|------------------------|
E|------------------------|------------------------|------------------------|------------------------|

  Dm7 9                    G13b9 10                 Cmaj7 11                 Fmaj7 12
e|------------5-----------|------------------------|------------------------|------------------------|
B|---------6-----7--6-----|8--6--------------------|------------4--5--------|---------5--6--6--5-----|
G|---6--7--------------7--|---------6--7--------7--|---4--5-----------5--4--|---4--5--------------5--|
D|------------------------|---------------9--------|5-----------------------|------------------------|
A|------------------------|------------------------|------------------------|------------------------|
E|------------------------|------------------------|------------------------|------------------------|

  Bb7 13                   E7 14                    Am6 15                   E7 16
e|---------4--6--4--------|4-----------------------|---------------0--------|------------------------|
B|---5--6-----------6--3--|---5-----2--3--------3--|------------1-----1-----|---------0--3--0--------|
G|------------------------|---------------4--------|------2-----------------|---0--1-----------1-----|
D|------------------------|------------------------|---4--------------------|---------------------2--|
A|------------------------|------------------------|------------------------|------------------------|
E|------------------------|------------------------|------------------------|------------------------|
```

## Practice notes

- The approach note should lean into the target: play it lightly and put the weight on the chord tone it leads to.
- Accent the beats with chord tones.
- Try bar 6 alone on every dim7 inversion (shift it three frets) to see how all four notes are equivalent.

Every pitch in the tab was checked against the chord in its bar by script (`.agents/skills/guitar-etude/scripts/check_etude.py`), and so was the fingering rule: inside a chord the biggest jump between notes is 3 frets, at a chord change it is 2 frets, and no bar needs more than a four-fret window. The etude has not been played on an instrument; fingerings are one way to play it, not the only way. Approach notes were checked as being one semitone from the chord tone that follows them. The frets run from 0 to 9.
