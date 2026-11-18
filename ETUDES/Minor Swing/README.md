# ETUDES

Three guitar arpeggio etudes on *Minor Swing* (Reinhardt-Grapelli). Each one is a full 16-bar chorus of the A section, written in tab with chord symbols, bar numbers and a degree line (R, b3, 5, ...) under each row, with the chart's alternate chords in bars 9-13 (Dm7, G13b9, Cmaj7, Fmaj7).

| Etude | Idea | File |
| --- | --- | --- |
| 1. Rising Tide | Arpeggio sweeps that climb and fall through each chord, with voice-leading from one chord to the next, pauses before the changes and an enclosure into the last G# | [etude-1-rising-tide.md](etude-1-rising-tide.md) |
| 2. Chromatic Rails | Offbeat rests, chromatic approach notes and enclosures into chord tones, double notes, and a G#dim7 arpeggio over E7b9 | [etude-2-chromatic-rails.md](etude-2-chromatic-rails.md) |
| 3. Motif in Motion | One set of four shapes moved through the changes, so the contour stays and the harmony changes; double notes, pauses and an enclosing tag at the end | [etude-3-motif-in-motion.md](etude-3-motif-in-motion.md) |

Every note was checked by script against the chord in its bar (approach notes against the note they lead to), and against the `guitar-etude` fingering rule: while a chord lasts, consecutive notes are at most 3 frets apart on the same or an adjacent string; at a chord change the move is at most 6 frets (these etudes use 3 at most); each bar fits a four-fret window. The tabs sit in frets 0-10. They have not been played on an instrument.

Run the check yourself: `python3 .agents/skills/guitar-etude/scripts/check_etude.py "ETUDES/Minor Swing/etude-1-rising-tide.md"`.

Chart source: `SONGS/minor-swing.md`. Arpeggio and scale definitions: `.agents/skills/music-theory-arpeggios` and `.agents/skills/music-theory-scales`.
