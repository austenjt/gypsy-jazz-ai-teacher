# gypsy-jazz-ai-teacher

Agent skills for writing, formatting, and reading guitar tablature, and for naming the scales and arpeggios inside it.

`guitar-tablature` covers the things tab usually gets wrong: missing rhythm, misaligned bars, inconsistent technique symbols, and chord shapes that are unreadable in prose. `music-theory-scales` and `music-theory-arpeggios` define the scales and arpeggios so a passage of tab can be identified and labelled as a pattern.

## The skill

| Skill | What it is for |
| --- | --- |
| `guitar-tablature` | Six-line tab layout, timing and ruler lines, technique notation, chord diagrams, fingering notes, and reading tab back into music |
| `music-theory-scales` | Interval formulas and movable tab patterns for major, minor, harmonic minor, Neapolitan, major and minor blues and diminished half-whole scales; how to identify a scale from tab and label it |
| `music-theory-arpeggios` | Minor, minor 6th, minor 7th, 6/9 and diminished 7th arpeggios as movable tab patterns, with identification fingerprints. Builds on `music-theory-scales` |

## Using it in Bionic

**As a project.** Open this folder as a project in Bionic. Project skills live in `.agents/skills/`, so the skill loads automatically for every session in that project. Type `@guitar-tablature`, `@music-theory-scales` or `@music-theory-arpeggios` to trigger a skill explicitly, or just ask and let the model pick it.

**Anywhere else.** Copy `.agents/skills/guitar-tablature/` `.agents/skills/music-theory-scales/` and `.agents/skills/music-theory-arpeggios/` into another project's `.agents/skills/` folder, or install it globally from Bionic's Settings → Skills.

## Repo layout

```
.agents/skills/
  guitar-tablature/
    SKILL.md          # front matter + instructions
  music-theory-scales/
    SKILL.md          # scale definitions, patterns, identification, tab labelling
  music-theory-arpeggios/
    SKILL.md          # arpeggio definitions and patterns; refers to the scales skill
```

## Conventions used by the skill

Tab blocks are six lines, high string on top, inside fenced code blocks so spacing survives:

```
e|----------------|
B|----------------|
G|----------------|
D|--2---4---5---4-|
A|----------------|
E|----------------|
   1 & 2 & 3 & 4 &
```

Chord shapes in prose are six-character fret strings, low E to high e, `x` for a muted string:

```
x32233   =  C6/9
```
