# Etude 1: Rising Tide

Chart: *Minor Swing* (Reinhardt-Grapelli), A minor, the 16-bar A section as written in the iReal chart: Am6 Am6 Dm6 Dm6 / E7 E7 Am6 Am6 / Dm6 Dm6 Am6 Am6 / Bb7 E7 Am6 E7, here played with the chart's alternate chords in bars 9-13 (Dm7, G13b9, Cmaj7, Fmaj7) and the b9 colour on E7 in bar 6. See `SONGS/minor-swing.md`.

Standard tuning `E A D G B e`. Notes are named in written guitar pitch (the sounding pitch is an octave lower). 4/4, swung eighth notes: **quarter = 160** to learn it, work up to 180-200. Each bar has eight note slots of three columns each, so two-digit frets fit. A slot with no fret is a rest. Chord symbols sit above each bar with the bar number.

Written to the `guitar-etude` fingering rule: while a chord lasts, consecutive notes are at most 3 frets apart and on the same or an adjacent string; at a chord change the line moves at most 6 frets; each bar fits a four-fret window.

## The idea

Pure arpeggio sweeps. Each chord's tones are a ladder, and the bars walk up and down it. The two-bar chords (bars 1-2, 3-4, 7-8) are pairs: the first bar climbs six chord tones and steps back, the second falls past the root and returns. The single-bar chords alternate an arch (up, then back down) and a valley (down, then back up). The register rises through the form, from the nut end of the neck in bar 1 to the 7th-10th frets in bar 11, then settles back toward the nut by bar 16. Bars 6 and 10 use a five-tone ladder, so the b9 (F over E7b9, Ab over G13b9) is part of the sweep. The final bar runs down the E7 arpeggio and back to land on G#, which pulls to A at the top of the form.

## Tab

```
  Am6 1                    Am6 2                    Dm6 3                    Dm6 4
e|---------------0--------|------------------------|---------------1--------|------------------------|
B|------------1-----1-----|------------------------|------------3-----3-----|3-----------------3-----|
G|---------2-----------2--|2-----------------2-----|------2--4-----------4--|---4--2-----2--4-----2--|
D|---2--4-----------------|---4--2-----2--4-----2--|0--3--------------------|---------3--------------|
A|3-----------------------|---------3--------------|------------------------|------------------------|
E|------------------------|------------------------|------------------------|------------------------|

  E7 5                     E7b9 6                   Am6 7                    Am6 8
e|------------4-----------|4-----------------------|---------------5--------|5-----------------5-----|
B|------3--5-----5--3-----|---6--5--3-----3--5--6--|---------5--7-----7--5--|---7--5-----5--7-----5--|
G|---4-----------------4--|------------4-----------|------5-----------------|---------5--------------|
D|6-----------------------|------------------------|4--7--------------------|------------------------|
A|------------------------|------------------------|------------------------|------------------------|
E|------------------------|------------------------|------------------------|------------------------|

  Dm7 9                    G13b9 10                 Cmaj7 11                 Fmaj7 12
e|---------5--8--5--------|7-----------------------|---------7--8--7--------|8--5-----------------5--|
B|------6-----------6-----|---9--8--6-----6--8--9--|------8-----------8-----|------6--5-----5--6-----|
G|5--7-----------------7--|------------7-----------|---9-----------------9--|------------5-----------|
D|------------------------|------------------------|10----------------------|------------------------|
A|------------------------|------------------------|------------------------|------------------------|
E|------------------------|------------------------|------------------------|------------------------|

  Bb7 13                   E7 14                    Am6 15                   E7 16
e|---------4--6--4--------|4-----------------------|------------0--2--0-----|------------------------|
B|---3--6-----------6--3--|---5--3-----------3--5--|---------1-----------1--|3--0--------------------|
G|3-----------------------|---------4-----4--------|------2-----------------|------1-----------1-----|
D|------------------------|------------6-----------|2--4--------------------|---------2--0--2-----2--|
A|------------------------|------------------------|------------------------|------------------------|
E|------------------------|------------------------|------------------------|------------------------|
```

## Practice notes

- Start with bars 1-2, slowly, with strict alternate picking: one bar climbs, the next falls.
- Play bars 9-12 as two pairs. At each change the hand moves 4 frets at most; find the nearest chord tone of the new chord and arrive on it.
- Loop bar 16 into bar 1: the G# at the end is the leading tone into the A that the next chorus opens on.

Every pitch in the tab was checked against the chord in its bar by script (`.agents/skills/guitar-etude/scripts/check_etude.py`), and so was the fingering rule: inside a chord the biggest jump between notes is 3 frets, at a chord change it is 4 frets, and no bar needs more than a four-fret window. The etude has not been played on an instrument; fingerings are one way to play it, not the only way. The frets run from 0 to 10.
