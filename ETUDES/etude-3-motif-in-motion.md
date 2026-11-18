# Etude 3: Motif in Motion

Chart: *Minor Swing* (Reinhardt-Grapelli), A minor, the 16-bar A section as written in the iReal chart: Am6 Am6 Dm6 Dm6 / E7 E7 Am6 Am6 / Dm6 Dm6 Am6 Am6 / Bb7 E7 Am6 E7, here played with the chart's alternate chords in bars 9-13 (Dm7, G13b9, Cmaj7, Fmaj7) and the b9 colour on E7 in bar 6. See `SONGS/minor-swing.md`.

Standard tuning `E A D G B e`. Notes are named in written guitar pitch (the sounding pitch is an octave lower). 4/4, swung eighth notes: **quarter = 160** to learn it, work up to 180-200. Each bar has eight note slots of three columns each, so two-digit frets fit. A slot with no fret is a rest. Chord symbols sit above each bar with the bar number.

Written to the `guitar-etude` fingering rule: while a chord lasts, consecutive notes are at most 3 frets apart and on the same or an adjacent string; at a chord change the line moves at most 6 frets; each bar fits a four-fret window.

## The idea

One idea, moved through the changes. Each chord is treated as a ladder of its own tones (low to high, over two octaves), and the same shapes are played on every ladder, so the contour stays the same while the harmony changes under it. Four shapes are used: a rising zig-zag (bars 1, 3, 5, 9, 11), a falling zag (bars 2, 4, 6, 8, 10, 12, 15), a syncopated shape with rests (bars 7, 13, 16) and an arch (bar 14). The shapes are written as ladder steps, so on a four-note chord the step "two up" is always the next-but-one chord tone. E7b9 and G13b9 have five-tone ladders, so their b9 (F, Ab) is part of the shape. When the chord changes, you hear the same shape in a new colour.

## Tab

```
  Am6 1                    Am6 2                    Dm6 3                    Dm6 4
e|------------------------|------------------------|---------------------1--|1-----------------------|
B|---------------------5--|------------------------|---------------3--0-----|---0--3-----------------|
G|---------2-----5--2-----|5-----2-----------------|---2-----4--2-----------|---------2--4-----2-----|
D|---4--2-----4-----------|---4-----2--4-----2-----|0-----3-----------------|---------------3-----0--|
A|3-----------------------|---------------3-----0--|------------------------|------------------------|
E|------------------------|------------------------|------------------------|------------------------|

  E7 5                     E7b9 6                   Am6 7                    Am6 8
e|---------------0-----4--|4-----------------------|------------------------|------------------------|
B|---------3--0-----3-----|---5--6-----5-----------|---------------5--------|5-----------------------|
G|---4--1-----------------|---------7-----4--7-----|------5--2--------5-----|---2--5-----2-----------|
D|2-----------------------|---------------------6--|4-----------------------|---------4-----2--4-----|
A|------------------------|------------------------|------------------------|---------------------3--|
E|------------------------|------------------------|------------------------|------------------------|

  Dm7 9                    G13b9 10                 Cmaj7 11                 Fmaj7 12
e|------------------------|3-----1-----------------|------------------------|------------------------|
B|---------------------3--|---3-----0--3-----0-----|---------------------5--|5-----------------------|
G|---------2-----5--2-----|---------------1-----0--|---------4-----5--4-----|---2--5-----2-----------|
D|---3--0-----3-----------|------------------------|---5--2-----5-----------|---------3-----2--3-----|
A|3-----------------------|------------------------|3-----------------------|---------------------3--|
E|------------------------|------------------------|------------------------|------------------------|

  Bb7 13                   E7 14                    Am6 15                   E7 16
e|---------------4--------|------------------------|------------------------|------------------------|
B|------6--3--------6-----|---------9--------------|5-----------------------|---------------3--------|
G|3-----------------------|------9-----9-----------|---2--5-----2-----------|------4--1--------4-----|
D|------------------------|---9-----------9--6-----|---------4-----2--4-----|2-----------------------|
A|------------------------|7--------------------7--|---------------------3--|------------------------|
E|------------------------|------------------------|------------------------|------------------------|
```

## Practice notes

- Learn the zig-zag on Am6 (bar 1) until it is automatic, then play it on each chord of the form: it is the same finger pattern with different notes.
- The syncopated shape (bars 7, 13, 16) is where the swing lives: play it a little behind the beat.
- Write your own shape as eight numbers (0 is the lowest chord tone, 4 is the same tone an octave up) and run it through the ladders: Am6 = A C E F# A C E F#.

Every pitch in the tab was checked against the chord in its bar by script (`.agents/skills/guitar-etude/scripts/check_etude.py`), and so was the fingering rule: inside a chord the biggest jump between notes is 3 frets, at a chord change it is 3 frets, and no bar needs more than a four-fret window. The etude has not been played on an instrument; fingerings are one way to play it, not the only way. The frets run from 0 to 9.
