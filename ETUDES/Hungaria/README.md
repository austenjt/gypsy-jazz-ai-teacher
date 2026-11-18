# ETUDES: Hungaria

Three guitar etudes on *Hungaria* (Django Reinhardt), key of G. Each one is a full 32-bar chorus (A, B, A, C), written in tab with chord symbols, bar numbers and a degree line (R, 3, 5, ...) under each row. Chart: `SONGS/hungaria.md`.

| Etude | Idea | File |
| --- | --- | --- |
| 1. Six-Nine Sweeps | Arpeggio sweeps on the G6/9 sound, the Ab6/9 passing chord as a half-step slide of the same shape, pauses before the changes, double notes, and an enclosure into the final G | [etude-1-six-nine-sweeps.md](etude-1-six-nine-sweeps.md) |
| 2. Side Steps | Offbeat rests, chromatic approach notes and enclosures into chord tones, double notes | [etude-2-side-steps.md](etude-2-side-steps.md) |
| 3. One Shape, Many Chords | One set of four shapes moved through the changes; double notes, pauses and an enclosing tag at the end | [etude-3-one-shape-many-chords.md](etude-3-one-shape-many-chords.md) |

Every note was checked by script against the chord in its bar (approach notes and enclosures against the note they lead to), and against the `guitar-etude` fingering rule: while a chord lasts, consecutive notes are at most 3 frets apart on the same or an adjacent string; at a chord change the move is at most 6 frets (these etudes use 5 at most); each bar fits a four-fret window. The tabs sit in frets 0-10. They have not been played on an instrument.

Run the check yourself: `python3 .agents/skills/guitar-etude/scripts/check_etude.py "ETUDES/Hungaria/etude-1-six-nine-sweeps.md"`.
