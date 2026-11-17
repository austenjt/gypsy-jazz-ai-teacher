# Gypsy Jazz AI Teacher

Agent skills that turn a general-purpose LLM into a gypsy jazz (*manouche*) teacher: rhythm guitar, harmony, soloing, repertoire, and transcription.

The skills are plain Markdown, with no scripts, network calls, or dependencies. They are written for [Bionic](https://lmstudio.ai) in LM Studio, and the format is portable to other agent frameworks that read `SKILL.md` files.

## The skills

| Skill | What it is for |
| --- | --- |
| `gypsy-jazz-coach` | Lesson planning, level checks, practice routines, diagnosing what is holding a player back |
| `la-pompe` | Rhythm guitar: the pump, right-hand mechanics, voicings, tempo, playing behind a soloist |
| `manouche-harmony` | 6/9 and m6 vocabulary, minor-swing changes, substitutions, passing chords, turnarounds |
| `gypsy-jazz-improvisation` | Rest-stroke picking, arpeggios, vocabulary, target tones, building a solo over changes |
| `gypsy-jazz-repertoire` | Tune selection by level, forms and roadmaps, intros and endings, jam-session readiness |
| `transcribe-by-ear` | Transcribing solos and turning them into exercises, tab, and vocabulary |

They are designed to be used together. The coach skill decides *what* to work on, and the others supply the *how*.

## Using it in Bionic

**As a project.** Open this folder as a project in Bionic. Project skills live in `.agents/skills/`, so all six load automatically for every session in that project. Type `@` to pick one explicitly, or just ask a question and let the model pick.

**Globally, or in another project.** Copy any folder from `.agents/skills/` into your own project's `.agents/skills/` folder. To make a skill available everywhere, install it from Bionic's Settings → Skills, pointing at the skill folder. Each folder is self-contained: `SKILL.md` plus its own `references/`.

## How the skills behave

- **Concrete over abstract.** Answers come with fret strings, bar numbers, and tempo targets, not adjectives.
- **One correction at a time.** A student cannot fix five things at once, so the skills are written to prioritize.
- **Honest about uncertainty.** Chord shapes and keys are treated as facts to be verified. If something is not certain, the skill says so rather than inventing it.
- **Practice-room shaped.** Every suggestion converts into something playable in 10 minutes with a metronome.

## Notation

Chord shapes are written as six-character fret strings, **low E to high e**, with `x` for a muted or unused string:

```
x32233   =  C6/9     (C E A D G)
3x233x   =  Gm6      (G E Bb D)
```

Movable shapes use `n` for the root fret:

```
n x n-1 n+1 n n+2   =  6/9 chord rooted on the low E string
```

## Repo layout

```
.agents/skills/
  <skill-name>/
    SKILL.md          # front matter + instructions
    references/       # optional detail the model reads on demand
scripts/validate_skills.py
```

## Adding a skill

1. Create `.agents/skills/<skill-name>/SKILL.md`.
2. Add front matter with `name`, `display-name`, and `description`.
3. Keep `name` **identical to the folder name** (kebab-case, 1-63 chars, no leading, trailing, or doubled hyphens).
4. Keep `description` short — roughly 150 characters. It is injected into the system prompt and is how the agent decides whether to read the skill.
5. Put anything long (tables, curricula, tune lists) in `references/` and point to it from `SKILL.md`.

Validate the whole repo with:

```bash
python3 scripts/validate_skills.py
```

## License

No license has been chosen yet. Add one before publishing if you want others to reuse the content.
