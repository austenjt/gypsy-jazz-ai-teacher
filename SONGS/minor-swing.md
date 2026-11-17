# Minor Swing

| | |
| --- | --- |
| Composer | Reinhardt-Grapelli (Django Reinhardt, Stephane Grappelli) |
| Style | Up Tempo Swing |
| Key | A minor |
| Time | 4/4 |
| Source | iReal Pro Forums, thread "Gypsy Jazz" (https://forums.irealpro.com/threads/gypsy-jazz.215/), page 1, in the 313-song playlist link |
| Format read | `irealb://` link, decoded to plain chords (see "Raw decoded chart" below) |

Chord names are given as iReal writes them, then in plain notation. `-` is minor, `^7` is major 7th, `x` in the chart means "repeat the previous bar", `N.C.` is no chord. Alternate chords (iReal parentheses) are shown as `[alt]`: a substitute for that bar, not an extra chord.

## Intro (8 bars, between repeat signs)

```
| Am              | Dm6             | Am6             | Dm6             |
| Am6             | Dm6             | E7 (bass brk)   | N.C.            |
```

iReal: `A- | D-6 | A-6 | D-6 | A-6 | D-6 | E7 | n`

## A section (16 bars, repeated for solos)

```
| Am6             | Am6             | Dm6             | Dm6             |
| E7              | E7              | Am6             | Am6             |
| Dm6 [Dm7]       | Dm6 [G13b9]     | Am6 [Cmaj7]     | Am6 [Fmaj7]     |
| Bb7 [Bbm7b5]    | E7              | Am6             | E7 (coda mark)  |
```

iReal: `A-6 | x | D-6 | x | E7 | x | A-6 | x | D-6(D-7) | x (G13b9) | A-6(C^7) | x (F^7) | Bb7(Bb-7b5) | E7 | A-6 | E7 Q`

Bars 10 and 12 are `x` (repeat of the bar before) with an alternate chord, so bars 9-10 read as Dm7 | G13b9 and bars 11-12 as Cmaj7 | Fmaj7 when the alternates are played.

## Coda section

```
| Am6             | Am6             | Dm6 (bass brk)  | Dm6             |
| E7              | E7              | 1. Am6 (gtr brk) | 1. N.C.         |
| 2. E7           | 2. Am6 (end)    |                 |                 |
```

iReal: `Q A-6 | x | D-6 <Bass break> | x | E7 | x | N1 A-6 <Guitar break> | n | N2 E7 | A-6 Z`

First time through, bars 7-8 are Am6 then N.C. (guitar break) and repeat from the top of the coda section. Second time, play the 2nd ending: E7, then Am6 to finish.

## Form summary

1. Intro, 8 bars.
2. A section, 16 bars, repeated as many times as needed (head, then solos).
3. Coda section, with a first and second ending.

The chart does not say where the jump to the coda happens. It marks the coda symbol (`Q`) at the end of bar 16 of the A section and leaves it to the players.

## Raw decoded chart

Decoded from the `irealb://` data (the 50-character block un-scramble, then `XyQ` to a space, `Kcl` to `| x`, `LZ` to a space):

```
{*iT44A- |D-6 |A-6 |D-6 |A-6 |D-6 |<Bass break>E7 |n }{*AA-6, | x  D-6 | x  E7 | x  A-6 | x  D-6(D-7) | (G13b9)x  A-6(C^7) | (F^7)x  Bb7(Bb-7b5) |E7 |A-6 |E7  Q }{QA-6 | x  D-6 <Bass break>   x  E7 | x  N1A-6 <Guitar break>   n  }    N2E7 |  A-6, Z
```

Metadata fields from the link: title `Minor Swing`, composer `Reinhardt-Grapelli`, style `Up Tempo Swing`, key `A-`.
