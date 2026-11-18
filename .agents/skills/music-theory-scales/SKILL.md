---
name: music-theory-scales
display-name: Music Theory: Scales
description: Define and identify scales (major, minor, harmonic minor, Neapolitan, major and minor blues, diminished half-whole) and label them as patterns in guitar tablature.
---

# Music Theory: Scales

This skill is the scale vocabulary behind the tab. When writing tablature (see `guitar-tablature`), use it to say *what* a run is: which scale, and which note is the root. When reading tab, use it to recognise the scale from the notes alone. Chord-tone patterns live in `music-theory-arpeggios`, which builds on this skill.

Everything is defined three ways so any can check the others: **interval formula** (relative to the root), **semitone set** (0-11 from the root), and **note names** (in the key of A).

## Hard constraints

- **Spell from the formula, not from memory.** Every pattern is its formula applied to a root. If a spelled-out scale disagrees with the formula, the formula wins.
- **Name the root and the pattern together.** "A harmonic minor", never just "harmonic minor". A pattern with no root is a shape, and should be called one.
- **Label which reading you chose** when a name is ambiguous (see "Ambiguous names" below). Do not silently pick one.
- **Tab limits still apply.** Six strings, frets 0-24, standard tuning unless stated. Every pattern here is movable; check it still fits at the new position.
- **Flats for minor-key spellings** (`Bb`, `Eb`), sharps where the formula asks for a raised degree (`G#` in A harmonic minor). Use `#` and `b` in ASCII, never the unicode symbols.

## Reference table

| Scale | Formula | Semitones | Notes in A |
| --- | --- | --- | --- |
| Major | 1 2 3 4 5 6 7 | 0 2 4 5 7 9 11 | A B C# D E F# G# |
| Minor (natural) | 1 2 b3 4 5 b6 b7 | 0 2 3 5 7 8 10 | A B C D E F G |
| Harmonic minor | 1 2 b3 4 5 b6 7 | 0 2 3 5 7 8 11 | A B C D E F G# |
| Neapolitan (minor) | 1 b2 b3 4 5 b6 7 | 0 1 3 5 7 8 11 | A Bb C D E F G# |
| Blues, minor | 1 b3 4 b5 5 b7 | 0 3 5 6 7 10 | A C D Eb E G |
| Blues, major | 1 2 b3 3 5 6 | 0 2 3 4 7 9 | A B C C# E F# |
| Diminished, half-whole | 1 b2 b3 3 b5 5 6 b7 | 0 1 3 4 6 7 9 10 | A Bb C C# Eb E F# G |

Major scale is the reference for everything else: "minor" means a flatted 3rd, "harmonic" means a raised 7th, "Neapolitan" means a flatted 2nd.

### Ambiguous names

These names are used for more than one thing. Defaults are in bold; say so if you use the other.

| Name | Default reading | Other reading |
| --- | --- | --- |
| Minor | **Natural minor scale** | Melodic or harmonic minor |
| Neapolitan | **Neapolitan minor** (1 b2 b3 4 5 b6 7) | Neapolitan major (1 b2 b3 4 5 6 7) |
| Blues | Always say **major** or **minor** | No default |

## Identifying a scale from tab

Given a passage of notes, name it like this:

1. **Convert to pitch classes.** Fret + open string: open strings are `E2 A2 D3 G3 B3 E4` (MIDI 40 45 50 55 59 64). Add the fret, take modulo 12, and name it (`C=0 C#=1 D=2 Eb=3 E=4 F=5 F#=6 G=7 Ab=8 A=9 Bb=10 B=11`).
2. **Remove duplicates** (octaves count once). The unique pitch classes are the set.
3. **Pick a root.** Try, in order: the first and last notes, the lowest note, the note the chord symbol names, the note that appears most often.
4. **Subtract the root, mod 12.** The result is the semitone set. Match it against the scale table above. For sets of three to five notes, see `music-theory-arpeggios`.
5. **If nothing matches,** try the next candidate root. A set can have several valid roots (see below).
6. **If it still does not match,** report the set as unclassified and give the intervals. Do not force a name.

### Fingerprints

The quickest tells, from the semitone set:

| Set size | Has | It is |
| --- | --- | --- |
| 6 | 0 3 5 6 7 10 | Blues, minor |
| 6 | 0 2 3 4 7 9 | Blues, major |
| 7 | 0 2 4 5 7 9 11 | Major scale |
| 7 | 0 2 3 5 7 8 10 | Natural minor scale |
| 7 | 0 2 3 5 7 8 11 | Harmonic minor scale |
| 7 | 0 1 3 5 7 8 11 | Neapolitan minor scale |
| 8 | 0 1 3 4 6 7 9 10 | Diminished half-whole scale |

### Same notes, different names

A pitch set can legitimately have more than one root. Say which one you chose and why.

- **Half-whole has three roots.** A, C, Eb and Gb half-whole all contain the same eight notes. The shape repeats every three frets.
- **Relative scales.** C major and A natural minor share all seven notes. The root decides.
- **Blues, major and minor.** A major blues (A B C C# E F#) and F# minor blues (F# A B C C# E) are the same six notes, as relative keys. The root decides which one it is, so name the root.

## Pattern library

Every block is a single movable shape, shown in A with the root on the 6th string at fret 5, ascending one octave from the root. The line under each block gives the scale degree. `R` is the root.

All shapes were checked: every fret is a note in the formula, and every formula note appears.

### Moving a pattern

- **Along the neck:** add or subtract the same number of frets from every note. Root on fret 7 means every fret is 2 higher than shown. Stay inside frets 0-24.
- **To the 5th string:** where the shape stays on the lower strings, play the same frets one string higher, root on the 5th string. A root at A-string fret 5 is D. For shapes that cross the G-to-B string pair, such as arpeggios, shift a fret; see `music-theory-arpeggios` for those.
- **To a new key:** find the root's fret on the 6th or 5th string, then place the shape there.

### Major scale (A)

```
e|---------------------------------|
B|---------------------------------|
G|---------------------------------|
D|--------------------------6---7--|
A|--------------5---7---9----------|
E|--5---7---9----------------------|
  R   2   3   4   5   6   7   R
```

### Natural minor scale (A)

```
e|---------------------------------|
B|---------------------------------|
G|---------------------------------|
D|--------------------------5---7--|
A|--------------5---7---8----------|
E|--5---7---8----------------------|
  R   2   b3  4   5   b6  b7  R
```

### Harmonic minor scale (A)

Natural minor with the 7th raised: `G` becomes `G#`.

```
e|---------------------------------|
B|---------------------------------|
G|---------------------------------|
D|--------------------------6---7--|
A|--------------5---7---8----------|
E|--5---7---8----------------------|
  R   2   b3  4   5   b6  7   R
```

### Neapolitan minor scale (A)

Harmonic minor with the 2nd lowered: `B` becomes `Bb`. The b2 next to the root and the augmented step between b6 and 7 are the sound.

```
e|---------------------------------|
B|---------------------------------|
G|---------------------------------|
D|--------------------------6---7--|
A|--------------5---7---8----------|
E|--5---6---8----------------------|
  R   b2  b3  4   5   b6  7   R
```

### Diminished half-whole scale (A)

Alternating half step, whole step: A Bb C C# Eb E F# G. Eight notes, symmetrical.

```
e|-------------------------------------|
B|-------------------------------------|
G|-------------------------------------|
D|------------------------------5---7--|
A|------------------6---7---9----------|
E|--5---6---8---9----------------------|
  R   b2  b3  3   b5  5   6   b7  R
```

## Labelling patterns in tab

When a passage is one of these patterns, say so. Use the same layout as `guitar-tablature`, and add two things:

1. **A name line above the block**, on its own line, never inside the fret columns: root, pattern name, formula.
2. **A degree line below the block**, under any picking line, aligned to the fret numbers: `R` for root, then `b3`, `5`, `b7`, and so on.

```
Am7 arpeggio, up and back (1 b3 5 b7). 4/4, eighth notes, one column group per note.
e|------------------------|
B|------------5-----------|
G|---------5-----5--------|
D|------5-----------5-----|
A|---7-----------------7--|
E|5-----------------------|
  R  5  b7 b3 5  b3 b7 5
```

Each note takes three columns so a two-character degree such as `b7` fits under its fret. The degree line starts at the same column as the first fret number.

Rules for labels:

- One name per pattern. If it is one pattern played twice, label it once.
- If a passage changes pattern mid-bar (arpeggio into a scale run), label each part.
- Label the root every time it appears, with `R`. That makes the pattern readable at a glance and makes it easy to transpose.
- If a passage is *almost* a pattern with one passing note, label the pattern and mark the extra note with `*` and a footnote: "* chromatic passing note, not part of Am7."
- If a note does not belong to the named pattern, the name is wrong or the note is a deliberate outside note. Say which.

## Reaching for a pattern (gypsy jazz context)

A rough map for choosing which scale fits a chord, used when composing a line over changes. For chord-tone lines see `music-theory-arpeggios`. These are suggestions, not rules.

| Chord | Scale to try | Why |
| --- | --- | --- |
| E7 or E7b9 | A harmonic minor (starts on E: E F G# A B C D), E half-whole | Harmonic minor from the 5th gives the b9 and b13 colours |
| Blues in A | A minor blues for the bluesy sound, A major blues for the sweeter sound, and the two together | Mixing them is common |
| Dm, Dm7 | D natural minor | Subdominant minor |
| Any dominant 7 | Half-whole scale on the root | Gives b9, #9, #11 and 13 over one chord |

The raised-7th and flat-2nd sounds (harmonic minor, Neapolitan) are the "gypsy" colours: both contain an augmented second (b6 to 7 in harmonic minor and Neapolitan minor), which is the interval most associated with the style.

## Playability checks

Before handing a pattern to anyone:

- **Fret window.** One position holds a four-fret window comfortably; five is a stretch. The shapes above are all four or fewer.
- **Range.** Shifted patterns must stay within frets 0-24 and above `E2`. Check the highest note too.
- **Every note is in the formula.** Convert the frets to pitch names and compare to the table. The check takes ten seconds and catches most mistakes.
- **Every formula note appears.** A scale with a missing degree is a different scale.
- **Octave reading.** A one-octave run starts on the root and ends on the root an octave up. If the shape ends on the 7th, it is not a full octave.

## Guardrails

- Do not name a pattern from its shape alone. Shapes repeat across scales; the interval set decides.
- Do not claim one root when the notes allow several. Say "also reads as C major" when A natural minor is the choice.
- Do not drift from the formula. If a source gives a different spelling for the same name, state which one you are using.
- Do not present a single fingering as the only one. These are movable defaults.
- Keep to six strings and 24 frets. If a pattern would need a fret outside the neck, say so and offer the nearest playable octave.
- If the key, tuning, or the reader's intended reading of an ambiguous name is unknown and it matters, ask before writing the block.
