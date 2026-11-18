---
name: guitar-etude
display-name: Guitar Etude
description: Compose playable guitar etudes over chord changes, keeping consecutive notes close together on the neck (at most 3 chromatic degrees, or frets, apart within a chord; 5-6 only across a chord change) so the fingering stays easy and efficient, and shaped with gypsy jazz devices (enclosures, chromatics, voice leading, pauses, double stops).
---

# Guitar Etude

An etude is a short piece that drills one idea. This skill is about writing etudes that a student can actually play: the notes must fit the chord, and they must sit close enough together that the fingering is efficient and easy. A line that is correct on paper but needs constant jumps is a bad etude.

It builds on other skills: chord tones come from `music-theory-arpeggios`, scales and passing notes from `music-theory-scales`, and layout from `guitar-tablature`. The tune and its changes come from `SONGS/` (see the chart skill `ireal-pro`). Finished etudes live in `ETUDES/`.

## The proximity rule (do not forget this)

While writing an etude, **avoid notes that are too far apart on the same string**, and keep consecutive notes close, taking the chord into account as it changes through the bars.

| Situation | Maximum distance between consecutive notes |
| --- | --- |
| **While the chord stays the same** | **3 degrees** (semitones), on the same string or an adjacent string |
| **At a chord change** (the first note of the new chord) | A larger move is allowed: **5 or 6 degrees at most** |

How to measure:

- Degrees are **chromatic**: the 12 semitones in an octave, not steps of a scale. One degree is one fret. `A to C` is 3 degrees, `A to C#` is 4, `A to D` is 5.
- **On the same string,** the distance is the difference in fret numbers (`fret 3 to fret 6` is 3 degrees).
- **On an adjacent string,** compare the fret numbers the hand must reach, so the same 3-fret limit keeps the fingers in one small position. Check the two frets, not only the pitch.
- Across a chord change, aim for the **nearest chord tone of the new chord**, not the root by default. Use 5-6 degrees only when the line needs it; closer is better.
- A larger move that is a deliberate leap (octave displacement, a call-and-response gesture) must be **marked as a leap** in a footnote and kept to once or twice per etude.

If a phrase breaks the rule, rewrite it: change the string, change the octave, change the starting chord tone, or drop the note. Do not just note the exception.

## Hard constraints

- **Every note is justified by its bar's chord.** Chord tones on strong beats; passing and approach notes only on weak beats and resolving by a step. Check each note against the chord in its bar.
- **Fingering first.** Choose the position for the bar, then write the line inside it. One hand position per bar is the default; shifting mid-bar needs a reason.
- **Fret window.** At most a four-fret window within a bar. Five is a stretch. A move across a chord change may shift position.
- **Tab limits.** Six strings, frets 0-24, standard tuning unless stated (see `guitar-tablature`).
- **No rhythm ruler under the tab.** Do not add a `1 & 2 & 3 & 4 &` line. State the grid once above the block.

## Process

1. **Get the chart.** Take the changes bar by bar from `SONGS/` or the student's chart. If the chart is unknown, ask.
2. **Choose the idea.** One focus per etude: arpeggio sweeps, chromatic approach notes, a motif moved through the changes, pentatonic runs. Say what it is in one line.
3. **Set the grid.** State tempo, time signature and note value once (for example "swung eighths, quarter = 160").
4. **Plan the positions.** For each bar, pick the hand position and the target chord tone to arrive on. Check the change-over from bar to bar against the proximity rule.
5. **Write the line.** Fill each bar inside its position, keeping consecutive notes within the limits above.
6. **Check it.** Run the playability checks below. Fix before showing.
7. **Present it.** Name line, chord symbols with bar numbers above each bar, the tab, a degree line under every row of tab (see "Degree line" below), and a short note on the tricky spot.

## Degree line (always include it)

Under every row of tab, add a **degree line**: each note is labelled by its role in that bar's chord, in a column under its fret number. It helps the student see the pattern behind the shapes. The student likes it, so never leave it out.

- Labels: `R` root, `3` or `b3`, `5`, `6`, `7` or `b7`, `b9`, and so on, relative to the root of the bar's chord (not the key). Rests stay blank.
- `a` marks a chromatic approach or enclosure note that is not in the chord.
- A repeated note repeats its label.
- Keep the slot grid: three columns per slot, label at the first column of the slot, a space in place of each bar line.
- Say once, in the etude's intro, what the labels mean.

```
  Am6 1
e|------------------------|
B|---------------5--------|
G|------------5-----5-----|
D|---8--6--7-----------7--|
     a  a  R  b3 5  b3 R
```

## Style (gypsy jazz)

The rules above make an etude playable. This section makes it sound like the style. Use a few devices per phrase, not all of them in every bar, and name the device in the practice notes so the student knows what to listen for. Every device still has to obey the proximity rule and the chord check.

- **Swing feel.** Swung eighth notes, with the accent on the offbeats. Start phrases on the "&" of 1 (an eighth rest first) as often as on the beat. Land on chord tones on beats 1 and 3, and let the offbeats carry the decoration.
- **Arpeggios as the backbone.** Minor 6th over the minor tonic, the dim7 built on the 3rd over a dominant (see `music-theory-arpeggios`). Plain sweeps are the base; the devices below dress them.
- **Chromatics.** A chromatic approach is one semitone below or above a chord tone, played just before it on a weak beat. A short chromatic run of three or four notes should end on a chord tone on a strong beat. Approach notes are the only notes allowed outside the chord, and each must be followed by its target.
- **Enclosures.** Surround the target: one note a semitone (or scale step) above, one a semitone below, then the target, in either order. For target A that is `Bb G# A` or `G# Bb A`. Land the target on the beat, so the two enclosing notes fall on the weak beat just before it. All three notes still sit within 3 frets of each other.
- **Voice leading.** Join chords by the smallest move: the last note of one bar steps to the nearest chord tone of the next. The classic moves are the 7th of a dominant falling to the 3rd of the tonic (D of E7 down to C of Am6) and the leading tone rising to the root (G# to A). Plan the chord-change landing before writing the bar.
- **Pauses.** Rests are part of the line. Leave an eighth or quarter rest before a chord change, or after a long run, so the hand can move and the phrase can breathe. A bar that is full from beat 1 to the last eighth is a warning sign.
- **Double stops.** Two notes struck together on adjacent strings: thirds, sixths and octaves, used as accents on a strong beat or at the end of a phrase. Both notes must be tones of the chord. The pair counts as one position for the proximity rule, so measure the distance from the lower note. In tab the two frets are stacked in the same slot. The checker script does not read stacked notes yet, so say in the etude that double stops were checked by hand.
- **Double notes.** The same pitch played twice in a row, as a repeated eighth note, to give the line a rhythmic push. Repeats cost nothing under the distance rule (0 frets). Use them on the offbeat, not on every beat.
- **Slides and hammer-ons.** The usual ornaments: a slide into a chord tone (`/`), a hammer-on or pull-off on a weak beat (`h`, `p`), a fast grace note. Use the symbols from `guitar-tablature` and give the legend once.
- **Bends.** Rare in gypsy jazz and best kept small: a half-step bend into a chord tone, once or twice per etude. The note counts at its target pitch for every check.

Keep the style in proportion. A good etude has one clear idea (see "Process") and two or three of these devices that serve it.

## Playability checks

Before handing an etude to anyone:

- **Chord check.** Every note is in the chord of its bar, or is a labelled passing or approach note.
- **Distance check.** Walk each consecutive pair of notes. Within a chord: at most 3 degrees (frets) apart on the same or adjacent string. At a change: at most 5-6. List any exceptions and fix them.
- **Window check.** No bar needs more than a four-fret window.
- **Voice-leading.** The last note of one chord and the first note of the next are close, ideally a step or a half step.
- **Range and tuning.** Frets 0-24, standard tuning unless stated.
- **Run the script.** `python3 .agents/skills/guitar-etude/scripts/check_etude.py ETUDE.md` checks chord tones, the distance rule, chord-change moves and the bar window against a finished tab in the `ETUDES/` format (six lines, eight three-column slots per bar, chord label and bar number above each bar).
- **Say what was not tested.** Scripts check notes against chords; they do not play the guitar. State that the etude has not been played unless it has.

## Good habits

- Keep lines **singable**: motion by step and by third, with an occasional leap for contrast.
- Let the **contour** carry the idea. Move the same shape through the changes instead of inventing a new one per bar.
- Use **open strings** and **common-fingering** positions where they make a shift easier.
- Leave **space**. A rest gives the hand time to move at a chord change.
- Give each etude a **name** and a one-line purpose, and note a **practice tempo** (slow to start, a target tempo to work up to).

## Guardrails

- Do not trade the proximity rule for a prettier line. A playable line beats a clever one.
- Do not claim an etude is easy or efficient without running the checks above.
- Do not present one fingering as the only one. Say "one way to play it".
- If the chord chart, key, tempo or the student's level is unknown and it matters, ask before writing.
- Keep to six strings and 24 frets. If a requested note is outside the instrument, say so and offer the nearest playable option.
