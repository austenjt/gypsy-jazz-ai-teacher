---
name: manouche-harmony
display-name: Manouche Harmony
description: Explain gypsy jazz harmony: 6/9 and m6 voicings, minor-swing changes, substitutions, passing chords and turnarounds.
---

# Manouche Harmony

Gypsy jazz harmony is a small vocabulary used well, not a large vocabulary used rarely. The core sounds are the **6/9 chord**, the **minor 6 chord**, the **dominant 9 or 13**, and the **diminished 7** sliding between them.

Use this skill to name what a chart is doing, choose voicings that voice-lead, and add color without obscuring the form.

## The four sounds

| Function | Default chord | Why |
| --- | --- | --- |
| Major tonic | 6 or 6/9 | Open, no leading tone, never sounds resolved-in-a-hurry |
| Minor tonic | m6 | Dark but stable; m7 sounds like a ii chord |
| Dominant | 7, 9, 13, 7b9 | 9 and 13 add color; b9 implies a diminished scale |
| Passing / tension | dim7, m7b5 | dim7 is a mobile passing chord; m7b5 is the minor ii |

Notice what is mostly absent: maj7 as a tonic color, m7 as a tonic minor, and dense extended voicings in the low register. This is a guitar idiom, and the voicings are shaped by the instrument.

## Reading a chart

1. **Find the key center**, including the relative minor.
2. **Write Roman numerals** under the bars. Do not skip this; substitution decisions are made in Roman numerals.
3. **Group the ii–V pairs.** Each one is a single event, not two chords.
4. **Mark the dominants that resolve** and those that do not. Non-resolving dominants are where substitutions live.
5. **Check the form** before adding anything: AABA, 12-bar, 16-bar, waltz, or rubato.

## Voicing rules

- Root on the 6th or 5th string, chord tones on the top four strings.
- Four notes maximum when comping at tempo; five when the chord is held.
- Move the top voice by step or half step, not by leap.
- When in doubt, drop the fifth. Nobody misses it.
- Fret strings are six characters, **low E → high e**, `x` = muted.

Worked examples:

```
x32233   C6/9    C E A D G
3x233x   Gm6     G E Bb D
x0455x   Am6     A F# C E
020100   E7      E B D G# B E
x3233x   C9      C E Bb D
x3424x   Cdim7   C F# A Eb
```

Full movable and open-position tables: `references/voicings.md`.

## Substitutions, in order of usefulness

1. **Tritone substitute.** Replace V7 with the dominant a tritone away. `G7 → Db7`, same guide tones, chromatic bass motion. Use it on the last V of a phrase, not on every V.
2. **Diminished passing chord.** A dim7 a half step above the target root, or a dim7 built on the b9 of the dominant, slides into the next chord. `C → C#dim7 → Dm7` and `G7 → G#dim7 → Am` both work.
3. **Minorization.** Turn a dominant into its relative minor 7 or m6 for part of the bar: `G7` becomes `Gm7` in the second half, resolving to C. Use sparingly; it softens the resolution.
4. **ii–V insertion.** Put a ii chord in front of any dominant: `G7 → Dm7 G7`. Works in major and minor (use m7b5 for minor ii).
5. **Backdoor.** `Cmaj7` approached by `Fm7 Bb7` instead of `Dm7 G7`. More modern than manouche, but it fits a ballad.
6. **Pedal and slash chords.** Hold the bass while the upper voices move. Useful for intros and vamps.

Sequence them: state the plain changes, then add one substitution per chorus. A chart full of substitutions stops being a form.

## Common progressions

Roman-numeral frameworks, plus what to play over them, are in `references/progressions.md`: minor swing, minor and major blues, rhythm changes, turnarounds, and endings.

Two things worth memorizing:

- **Minor swing form** (the backbone of the repertoire): `i – iv – i – V7`, with the bridge moving to `iv` and back. Most minor-key gypsy tunes are a variation on this.
- **Turnaround:** `I – VI7 – II7 – V7` in major, `i – VI7 – iiø7 – V7` in minor.

## Adding color without losing the tune

- On a tonic 6/9, move the top voice between the 6th and the 9th. That single move is a chorus of comping.
- On a dominant, alternate 9 and 13 on repeat passes so the soloist hears motion.
- On a dim7, do not hold it; it is a doorway, not a room.
- In a ballad, slower harmonic rhythm and wider voicings do more than extra extensions.

## Guardrails

- Never invent a tune's changes. If a chart is not certain, give the Roman numerals and say the exact bars need checking against the recording.
- Do not present a substitution as required. Present it as an option with a use case.
- Keep enharmonic spelling sane: b9 on a dominant, not #1; dim7 spelled from the leading tone when resolving up.
- If a student asks for "the Django chord" for something, ask which recording, then describe what is audible and flag what is not.
