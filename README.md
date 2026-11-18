# gypsy-jazz-ai-teacher

A set of skills that lets an AI act as a **gypsy jazz guitar teacher**.

The skills give the AI the things a good teacher has: a clear way to write music down, a firm grip on the theory, a library of tunes and exercises to work from, and a way to plan lessons and adapt them to the student. You talk to the AI; it uses these skills to explain, show you tab, pick material, and plan what to practise next.

## Goals

1. **Teach gypsy jazz guitar.** The focus is the Django Reinhardt tradition: minor swing, the arpeggios and scales behind it, and the standard repertoire.
2. **Be accurate.** Tab, scales and chords are defined from formulas, and generated material is checked by script, so a fret number or a chord tone is not a guess.
3. **Be readable anywhere.** Everything is plain text: tab in fixed-width blocks, charts in markdown. It works in a terminal, an editor, or a chat window.
4. **Teach the student, not just the subject.** The lesson-planning skill asks for feedback after each session and uses it to adjust the plan and aim at the student's weak spots.
5. **Be honest about limits.** The AI cannot hear you play. It teaches from what you tell it and what you write down, and it says when it does not know.

## How a lesson works

```
Intake            goal, level, time, gear        (lesson-planning)
   |
Plan              one focus, short session        (lesson-planning)
   |
Material          tab, arpeggios, scales, a song  (the other skills and folders)
   |
Practise          you play
   |
Feedback          five quick questions            (lesson-planning)
   |
Adapt             tempo, difficulty, weak spots   (lesson-planning, saved in STUDENT/)
   |
Next plan   <-----+
```

You can also use the skills on their own: ask for a tab of a lick, the notes in a scale, the changes of a tune, or an exercise in a key you choose.

## The skills

| Skill | What it does |
| --- | --- |
| `lesson-planning` | Takes a short intake, builds a session or week plan, asks for feedback, and adapts the plan to the student's weak spots. Keeps a learner profile and a practice log in `STUDENT/` |
| `guitar-tablature` | Writes and reads six-line ASCII tab: layout, timing and ruler lines, technique symbols, chord shapes, fingering and picking notes, playability checks |
| `music-theory-scales` | Interval formulas and movable tab patterns for major, minor, harmonic minor, Neapolitan, major and minor blues, and diminished half-whole scales. How to name a scale from tab and label it |
| `music-theory-arpeggios` | Minor, minor 6th, minor 7th, 6/9 and diminished 7th arpeggios as movable tab patterns, with fingerprints for identifying them. Builds on the scales skill |
| `guitar-etude` | Composes playable etudes over chord changes. Keeps consecutive notes within 3 chromatic degrees (frets) on the same or adjacent string while a chord lasts (5-6 at most across a change), with playability checks and a gypsy jazz style guide (enclosures, chromatics, voice leading, pauses, double stops) |
| `ireal-pro` | Finds and decodes gypsy jazz chord charts from the iReal Pro forum "Gypsy Jazz" thread and saves them as readable charts. Includes a decoder script |

The skills work together. For example: a lesson plan picks a tune from `SONGS/`, an arpeggio from `GENERATED/`, writes the exercise out with `guitar-tablature`, and labels the notes with `music-theory-arpeggios`.

## What is in the folders

| Folder | Contents |
| --- | --- |
| `.agents/skills/` | The skills themselves (see above) |
| `SONGS/` | Hand-checked chord charts. Currently `minor-swing.md` |
| `IREAL/` | 376 decoded gypsy jazz charts from two iReal Pro playlists, one file per song: `rn-style-gj-charts/` (63) and `gypsy-jazz/` (313). The bar view in each file is a mechanical split, not hand-checked; the raw decoded chart is in every file |
| `GENERATED/` | Generated arpeggio tab by quality and root. `minor/A` (A minor 6th) and `minor/G` (G minor 6th): one-note-per-string positions and two-notes-per-string shapes, all up to fret 16 |
| `ETUDES/` | Three arpeggio etudes on Minor Swing, each a full 16-bar chorus in tab |
| `STUDENT/` | Created by `lesson-planning` on first use, with your permission: your profile and practice log. Not part of the repository's content; keep it private if you share the repo |

## Getting started

Open the folder as a project in Bionic (see below), then try a prompt:

- "I'm a beginner and want to play Minor Swing. Plan my first week." (starts the intake)
- "Show me an A minor 6th arpeggio I can play at the 5th fret."
- "Write a two-bar lick over E7b9 in tab, with the degree line."
- "What chords are in Minor Swing?" (reads `SONGS/minor-swing.md`)
- "Give me an etude to practise approach notes." (points at `ETUDES/`)
- "I practised 20 minutes, got the shift at 80 BPM but it was hard." (feedback; the plan adapts)

## Using it in Bionic

**As a project.** Open this folder as a project in Bionic. Project skills live in `.agents/skills/`, so they load automatically for every session in that project. Type `@lesson-planning`, `@guitar-tablature`, `@music-theory-scales`, `@music-theory-arpeggios`, `@guitar-etude` or `@ireal-pro` to trigger a skill explicitly, or just ask and let the model pick it.

**Anywhere else.** Copy the skill folders you want from `.agents/skills/` into another project's `.agents/skills/` folder, or install them globally from Bionic's Settings → Skills. The skills refer to each other and to the content folders, so copy `lesson-planning` together with the folders it points at if you want the full set.

## Repo layout

```
.agents/skills/
  lesson-planning/
    SKILL.md          # intake, plans, feedback, adapting to weak spots
    templates/        # learner-profile.md, practice-log.md
  guitar-tablature/
    SKILL.md          # tab layout, timing, techniques, chords
  music-theory-scales/
    SKILL.md          # scale definitions, patterns, identification, tab labelling
  music-theory-arpeggios/
    SKILL.md          # arpeggio definitions and patterns; refers to the scales skill
  guitar-etude/
    SKILL.md          # writing playable etudes; proximity rule for fingering
  ireal-pro/
    SKILL.md          # reading iReal Pro forum charts, format, saving charts
    scripts/
      ireal_decode.py # list and decode charts from a saved page, link file or URL
    references/       # the two playlist links (63-song RN style GJ charts, 313-song Gypsy Jazz)
SONGS/                # hand-checked chord charts (minor-swing.md)
IREAL/                # 376 decoded charts in two packs
GENERATED/            # generated arpeggio tab (minor/A, minor/G)
ETUDES/               # three Minor Swing etudes
STUDENT/              # created on first use by lesson-planning
```

## Conventions

Tab blocks are six lines, high string on top, inside fenced code blocks so spacing survives:

```
e|----------------|
B|----------------|
G|----------------|
D|--2---4---5---4-|
A|----------------|
E|----------------|
```

No beat-counting ruler (`1 & 2 & 3 & 4 &`) under the tab; it is repetitive. Rhythm is stated once above the block (tempo, time signature, grid).

Chord shapes in prose are six-character fret strings, low E to high e, `x` for a muted string:

```
x32233   =  C6/9
```

Patterns are labelled with a name line above the tab and a degree line below (`R`, `b3`, `5`, `6`), so the notes can be read as chord tones at a glance.

## Limits

- **No ears.** The AI cannot hear or watch you play. Feedback comes from your own words. Record yourself and describe what you hear if you want a second opinion on a passage.
- **Not played.** Generated tab and the etudes are checked against the chord and scale definitions by script, but a script does not play the guitar. Fingerings are one way to play a line, not the only one.
- **Community charts.** The charts in `IREAL/` and `SONGS/` come from a public forum and were decoded automatically. Chord details can differ from other sources. They are for personal study; do not republish them.
- **Pain.** If playing hurts, stop. The AI is not a doctor and will not diagnose.
- **One style.** The skills are written for gypsy jazz on six-string guitar in standard tuning. Other styles and tunings are outside what this project covers.

## Extending

- **A new key or chord quality:** generate arpeggio tab the same way as `GENERATED/minor/A`, using the formulas in `music-theory-arpeggios`.
- **A new tune:** use `ireal-pro` to find and decode it, then save a chart in `SONGS/`.
- **A new skill:** add a folder under `.agents/skills/` with a `SKILL.md` that has front matter (`name`, `display-name`, `description`), then list it here.
- **Improving lesson-planning:** the skill reviews the practice log every five sessions and proposes changes to itself. It never edits itself without your agreement.
