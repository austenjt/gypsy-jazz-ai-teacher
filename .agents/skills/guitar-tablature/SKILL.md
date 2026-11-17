---
name: guitar-tablature
display-name: Guitar Tablature
description: Write and read fixed-width ASCII guitar tablature for six-string guitar: layout, timing, chords and techniques.
---

# Guitar Tablature

Tablature says *where* to put the fingers. It does not, by itself, say *when*. Most bad tab fails for one of two reasons: the timing is missing, or the layout cannot be read at a glance. This skill is about getting both right, in plain fixed-width text.

## Hard constraints

- **Six strings only.** Standard tuning `E A D G B e` unless a different tuning is stated at the top of the piece.
- **Frets 0–24.** `0` is an open string. Nothing above `24`.
- **ASCII only.** No smart quotes, no box-drawing characters, no emoji, no proportional fonts. Tab alignment is the whole ballgame.
- **No standard notation.** No staves, clefs, or note-heads. Rhythm is carried by layout, ruler lines, and stated grids.
- **Always inside a fenced code block** so spaces survive whatever renders it.
- **State tempo and time signature** before the first block.

## The block

Highest string on top, six labelled lines, bar lines aligned:

```
e|----------------|----------------|
B|----------------|----------------|
G|----------------|----------------|
D|--2---4---5---4-|--2-------------|
A|----------------|----------------|
E|----------------|----------------|
```

Defaults that keep it readable (adjust when the reader asks for something else):

- Label every string, even in standard tuning.
- One character per subdivision, chosen once and kept for the block.
- Bar lines on every bar, vertically aligned.
- Four bars per block, fewer when the rhythm is dense.
- Chord symbols on their own line above the block, never inside the fret columns.
- State tuning, capo, and tempo before the first block. If any of them is non-default, say so twice.

## Timing

Spacing alone is not rhythm. Pick one of these and say which:

**Ruler line** — works for any reader, needs no explanation:

```
e|----------------|----------------|
B|----------------|----------------|
G|----------------|----------------|
D|--2---4---5---4-|--2-------------|
A|----------------|----------------|
E|----------------|----------------|
   1 & 2 & 3 & 4 &   1 & 2 & 3 & 4 &
```

**Declared grid** — proportional spacing with an explicit resolution:

```
One character = one sixteenth note. Tempo: quarter = 120. 4/4.
```

If the rhythm is approximate, write "approximate rhythm" above the block. Never let a reader assume precision you do not have.

## Techniques

One legend per document, used consistently.

| Symbol | Meaning | Example |
| --- | --- | --- |
| `h` | hammer-on | `2h4` |
| `p` | pull-off | `4p2` |
| `/` | slide up | `5/7` |
| `\` | slide down | `7\5` |
| `b` | bend to pitch | `7b9` |
| `r` | release bend | `9r7` |
| `~` | vibrato | `7~~~` |
| `x` | muted or ghost note | `x` |
| `<7>` | natural harmonic at fret 7 | `<7>` |
| `T` | tapped note | `T12` |
| `PM` | palm mute | `PM----` |

Include the legend the first time a symbol appears. If a technique needs a paragraph, it needs a footnote, not more symbols.

## Chords

Two formats, for two different jobs.

**Fret string** — compact, for prose and reference tables. Six characters, low E to high e, `x` for a muted string:

```
x32233   =  C6/9   (C E A D G)
3x233x   =  Gm6    (G E Bb D)
```

**Grid** — for a reader who needs to see the shape:

```
C6/9          Gm6
e 3           e x
B 3           B 3
G 2           G 3
D 2           D 2
A 3           A x
E x           E 3
```

A column of numbers means "strike together." A row separated by dashes means "play in sequence." Never leave the reader guessing which one they are looking at.

## Positions, fingers, picking

- Mark position with `pos.` above the block: `pos. V`.
- Finger numbers (`1`–`4`, `T` for thumb) go on their own line or in a footnote, never inline with frets.
- Picking directions go under the block: `v` down, `^` up.
- If a passage only works in one position, say so. If it works anywhere, do not over-specify.

## Playability checks

Before handing tab to anyone, check it:

- **Range.** In standard tuning the instrument spans `E2` (open low E) to `E6` (24th fret, high e). Open strings: `E2 A2 D3 G3 B3 E4`.
- **Voices.** Six notes maximum in a chord, one per string. A six-note chord uses every string.
- **Fret window.** A chord or run that needs more than a four- or five-fret span in one position will not be playable as written; move it or say "shift."
- **Fret numbers.** Nothing above `24`, nothing negative. `0` is open, `x` is muted, and the two are not interchangeable.
- **Tuning.** If a note only makes sense in a non-standard tuning, the tuning must be stated before the block.
- **Muting.** Unplayed strings in a chord are `x`, not blank. Blank means "not written," which is not the same thing.

## Writing for a reader

Assume no shared context: the reader may be a beginner, a teacher, or another agent.

- Give the smallest useful unit: two bars, not a page.
- Say what the passage is and where it comes from: "A section riff, half speed."
- Show one fingering. Mention alternatives in a footnote instead of stacking options.
- Mark the tricky spot with a footnote marker, not a paragraph in the middle of the block.
- Pair the line with its chord symbols so the harmony is audible while learning it.
- Offer the same phrase in one other position when the point is fretboard knowledge.

## Reading tab back into music

When tab arrives as input:

- Check the tuning assumption first. A "wrong" transcription is often a capo or a dropped tuning.
- Convert a few notes to pitch names to confirm the tab matches the recording.
- Recover the timing: clap it against the recording until the rhythm is agreed. If the tab has no ruler or grid, say the rhythm is unknown.
- Name the device: arpeggio, scale run, chord shape, or something idiomatic.

## Guardrails

- Do not invent a fingering and present it as the only one. Say "one way to play it."
- Do not claim rhythmic precision you do not have. Label approximate rhythm as approximate.
- If tuning, capo, or key is unknown and it matters, ask before writing the block.
- Keep to six strings and 24 frets. If a requested note is outside the instrument, say so and offer the nearest playable option.
- When the reader asks for a different layout, adapt. Defaults here are defaults, not rules.
