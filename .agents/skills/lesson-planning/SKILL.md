---
name: lesson-planning
display-name: Lesson Planning
description: Suggest gypsy jazz guitar lessons and a practice routine, record the learner's feedback, and use it to adapt the plan to their weak spots.
---

# Lesson Planning

This skill turns the other skills in this project into a learning path. It decides *what to practise next*, *for how long*, and *how to change the plan when the learner reports back*. It does not teach technique itself: it points at the skill or file that does (tab, scales, arpeggios, songs, etudes).

The one idea that makes it work: **the plan is a hypothesis and the learner's feedback is the test.** Every plan is short, ends with a question to the learner, and the answer changes the next plan.

## Hard constraints

- **The AI cannot hear the learner play.** Everything about how they played comes from what they say, or from tab or notes they type. Never claim to have judged their tone, timing or technique. Ask, and believe the answer.
- **Short plans.** One session plan fits on a screen. A weekly plan lists a focus, not a script.
- **Stay in the material the project has.** Point at real files: a skill, a chart in `SONGS/` or `IREAL/`, an arpeggio position in `GENERATED/`, an etude in `ETUDES/`. Do not invent a chart, a resource or a teacher's name.
- **Pain stops practice.** If the learner reports pain, numbness or tingling, tell them to stop, rest, and see a professional if it continues. Do not push through it and do not diagnose.
- **Ask before writing files.** The learner's profile and log are saved in `STUDENT/` (see "Keeping records"). Say what you will write and where, and get a yes before creating or changing it.
- **Changes to this skill need a yes.** The AI may propose edits to `SKILL.md` after reviewing the log, but never edits it silently.

## What this skill reads

| Source | Use |
| --- | --- |
| `STUDENT/learner-profile.md` | Who the learner is, their goal, their level, their weak spots |
| `STUDENT/practice-log.md` | What they did and how it went, session by session |
| `.agents/skills/guitar-tablature` | How to write any exercise out as tab |
| `.agents/skills/music-theory-scales`, `music-theory-arpeggios` | Scale and arpeggio definitions, movable patterns, how to label a line |
| `.agents/skills/ireal-pro`, `SONGS/`, `IREAL/` | Songs and chord charts to practise on |
| `GENERATED/` | Ready-made arpeggio positions by key and chord (for example A and G minor 6th) |
| `ETUDES/` | Worked exercises on a real tune (Minor Swing) |

If `STUDENT/` does not exist, this is a new learner: start with the intake.

## Step 1: intake (new learner)

Ask a few questions, no more than five at a time. Record the answers.

1. **Goal.** What do you want to be able to do in three months? (Play Minor Swing, solo over a chord chart, accompany a singer, read tab faster...)
2. **Level.** How long have you played, and what can you play now? A real example beats a label: "I know open chords and a pentatonic scale."
3. **Time.** How many days a week and how many minutes a day, realistically?
4. **Gear and setup.** Acoustic or electric, a metronome or backing track, a way to record themselves.
5. **Hands and body.** Any pain, injury, or fatigue to plan around?
6. **Taste.** Which players or tunes do you love? (This decides what is worth practising.)

Then place the learner on the ladder below and write the profile from `templates/learner-profile.md`.

## The ladder

Where to start, in order. A learner can be on different rungs for different areas; track each.

| Stage | Can do | Practise next | Where in this project |
| --- | --- | --- | --- |
| 1. Foundations | Fret cleanly, change between a few chords, read basic tab | Am, Dm, E7 shapes; A natural minor and A harmonic minor scale; reading a tab block with a ruler line | `guitar-tablature`, `music-theory-scales` |
| 2. Chord-tone playing | Play one arpeggio shape and name its notes | Am6, Am7, Dm6 and E7 arpeggios, one note per string, then up and back | `music-theory-arpeggios`, `GENERATED/minor/A` |
| 3. Arpeggios in time | Play arpeggios to a metronome | Two-notes-per-string shapes; link Am6, Dm6, E7 over the Minor Swing changes | `GENERATED/minor/A`, `ETUDES/etude-1-rising-tide.md` |
| 4. Phrasing | Play a line that starts and ends where it means to | Approach notes, rests, landing on 3rds and 7ths; dim7 over E7b9 | `ETUDES/etude-2-chromatic-rails.md` |
| 5. Motifs and variation | Take one idea and move it through the changes | Motif on the chord-tone ladder; change the rhythm, then the notes | `ETUDES/etude-3-motif-in-motion.md` |
| 6. Repertoire | Play a head and a chorus of a tune from a chart | Pick tunes from `SONGS/` and `IREAL/`; learn the changes first, then a line over them | `ireal-pro`, `SONGS/`, `IREAL/` |
| 7. Making it yours | Improvise a chorus over changes | Blues scales, Neapolitan, half-whole over dominants; transcribe a phrase from a recording | `music-theory-scales` |

The ladder is a default. If the learner's goal says otherwise (accompaniment first, for example), reorder it and say why.

## Step 2: build a plan

### A session (pick the length the learner gave you)

| Block | 15 min | 30 min | 60 min | What |
| --- | --- | --- | --- | --- |
| Warm-up | 2 | 4 | 6 | Slow, relaxed, something already known |
| Technique | 5 | 8 | 15 | One thing from the focus: a scale, an arpeggio shape, a picking pattern |
| Material | 6 | 12 | 24 | A passage from a chart, an etude or a song, in small pieces |
| Application | 2 | 4 | 10 | Use the technique in a context: play it over the changes, improvise two bars |
| Review | 0 | 2 | 5 | Play it once through, then answer the feedback questions |

Rules for a session plan:

- **One focus.** One technique, one passage. If two things are weak, pick the weaker one and park the other.
- **Slow first.** Start at a tempo the learner can play cleanly with no tension. A target tempo is a goal, not a start.
- **Small pieces.** Split anything long into one-or-two-bar chunks. Loop each chunk; then join.
- **Always a metronome or a backing track** when time is the focus.
- **Say what "done" looks like**: "four clean passes in a row at quarter = 100".

### A week

Give a focus per day, not a script. Example for a learner with 30 minutes, four days:

| Day | Focus | Material |
| --- | --- | --- |
| 1 | New shape | Am6 arpeggio in one position (`GENERATED/minor/A`) |
| 2 | Same shape, in time | Metronome, then play it over Am6 of Minor Swing |
| 3 | Link two chords | Am6 to Dm6, bars 1-4 of the chart |
| 4 | Review and play | Etude 1, bars 1-4; one pass of the whole chorus for fun |

Always leave one day lighter or free. Rest is part of the plan.

## Step 3: ask for feedback

At the end of every session, ask these five questions. Keep it quick; the learner can answer in a line each.

1. **Time:** how long did you actually practise?
2. **Result:** what could you play cleanly at the end, and at what tempo?
3. **Difficulty:** 1 (too easy) to 5 (too hard).
4. **Sticking point:** where exactly did it break down? (A bar, a shift, a string crossing, a speed?)
5. **Mood:** did it feel good, frustrating, boring, or stale?

Add one open question now and then: "What would you like more of next week?" Record every answer.

## Step 4: adapt the plan

The learner's answers change the next plan. Use these rules; say which rule you used.

| What you hear | Do this |
| --- | --- |
| Difficulty 1-2 and the target was met | Raise the tempo by about 5-10 BPM, or move to the next rung or the next bar |
| Difficulty 3, target met | Hold the tempo, add a variation (a new rhythm or a new position) |
| Difficulty 4-5, target not met | Go back a step: lower tempo, shorter chunk, simpler shape |
| Same sticking point twice | Isolate it: make the sticking point its own one-bar exercise, slow, for the next session |
| Same sticking point three times | Change the approach (different fingering, different string set, different exercise for the same skill); do not repeat what failed |
| "Boring" or "stale" twice | Swap the material for a tune they love; keep the same technique focus |
| "Frustrating" | Shorten the session, finish on something they can already do, and ask what would help |
| Missed sessions | Do not pile up work. Restart at the last point they felt good about |
| Pain | Stop. See the hard constraints |

### Targeting weak spots

Keep a short **weakness list** in the profile, 1-3 items at a time, each with evidence from the log (what was said, when, how often). Tag each with a type so the plan can match it:

| Type | Typical signs | Practise |
| --- | --- | --- |
| Timing | Rushes, drags, loses the beat | Metronome on 2 and 4, play with a backing track, rests inside the bar |
| Clean fretting | Buzz, muted notes, wrong note | Slow single-bar loops, one string set at a time |
| Picking | Uneven attack, string-crossing errors | Alternate picking on one-note-per-string shapes, then two per string |
| Position shifts | Misses the target fret | Shift between two shapes on a repeated cycle |
| Fretboard knowledge | Cannot name notes or find the root | Name the notes as they play; find the root on the 6th and 5th string |
| Chord changes | Gaps between chords | Two-chord loops, then four |
| Ear | Cannot hear whether it fits | Play the target note first, then the line; sing the root |
| Theory | Cannot say why a note works | Label a line (R, 3, 5, 7) using the tab labelling convention |
| Speed | Clean slowly, falls apart fast | Short bursts at the next tempo, rest, repeat |
| Memory | Forgets the passage | Learn two bars at a time; play with eyes closed once |
| Phrasing | Notes right, line flat | Add rests, accents, an approach note, a clear landing note |

When a weakness has not come up for three sessions in a row, mark it **improving** and move on; check it once a month. Strengths go in the profile too, so the plan can build on them.

## Keeping records

Two files in `STUDENT/`, written from the templates in this skill:

- `STUDENT/learner-profile.md`: goal, level, time, setup, taste, strengths, weakness list, current focus. Update it when something changes.
- `STUDENT/practice-log.md`: one short entry per session: date, plan, answers to the five feedback questions, rule used, next step.

Rules:

- Ask before creating `STUDENT/` or writing to it, and say what you will write.
- Keep entries short. The log is read at the start of every session and must stay useful.
- Never write anything about the learner that they did not say. Facts come from the learner.
- The files are local. Do not copy them anywhere else.

## Start of a session

1. Read the profile and the last few log entries.
2. Say in one or two lines where things stand: "Last time you reached 90 BPM on bars 1-4 and the shift to the 7th fret was the snag."
3. Ask how the week went and whether the plan still fits.
4. Propose today's session from Step 2, adjusted by Step 4.

If there is no log yet, start with the intake.

## How this skill improves itself

The plan gets better by repetition; the skill gets better by review.

- **Every five sessions**, review the log and ask: which suggestions worked (target met, mood good), which failed twice, and which weakness types came up most.
- Record the result in the log as a "what worked" note: for example "arpeggios over a backing track worked better than a metronome alone".
- **If a pattern holds across several sessions or several learners' notes,** propose a change to this skill: a new row in a table, a different tempo step, a new ladder rung. Show the exact text, say what evidence supports it, and wait for a yes before editing `SKILL.md`.
- Never remove a safety rule (see hard constraints) because of feedback.
- Keep a one-line changelog at the bottom of this file when it is edited.

## Guardrails

- Do not claim to hear, see or measure the learner's playing.
- Do not promise results or timelines. Say what is likely, and what the learner can control.
- Do not give medical advice about pain or injury; stop and refer.
- Do not set a plan the learner has said they cannot do (time, gear, body). Ask again.
- Do not overload: one focus per session, three weaknesses at most, a lighter day every week.
- If the learner wants something this project does not cover (a style outside gypsy jazz, an instrument other than guitar), say so, and give a plain-language plan from what is here or suggest another resource.

## Changelog

- Initial version.
