# guitar-tablature

An agent skill for writing, formatting, and reading guitar tablature.

It covers the things tab usually gets wrong: missing rhythm, misaligned bars, inconsistent technique symbols, and chord shapes that are unreadable in prose.

## The skill

| Skill | What it is for |
| --- | --- |
| `guitar-tablature` | Six-line tab layout, timing and ruler lines, technique notation, chord diagrams, fingering notes, and reading tab back into music |

## Using it in Bionic

**As a project.** Open this folder as a project in Bionic. Project skills live in `.agents/skills/`, so the skill loads automatically for every session in that project. Type `@guitar-tablature` to trigger it explicitly, or just ask for tab and let the model pick it.

**Anywhere else.** Copy `.agents/skills/guitar-tablature/` into another project's `.agents/skills/` folder, or install it globally from Bionic's Settings → Skills.

## Repo layout

```
.agents/skills/
  guitar-tablature/
    SKILL.md          # front matter + instructions
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
