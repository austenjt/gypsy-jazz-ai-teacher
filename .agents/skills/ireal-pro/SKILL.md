---
name: ireal-pro
display-name: iReal Pro
description: Find and read gypsy jazz chord charts from the iReal Pro forum "Gypsy Jazz" thread (irealb:// and irealbook:// links), decode them to plain chords, and save them as readable files in SONGS/.
---

# iReal Pro

This skill reads chord charts shared in one place: the **Gypsy Jazz** thread on the iReal Pro forums. It turns the links people post there into plain chord charts that can sit next to the tab and theory skills.

Thread: https://forums.irealpro.com/threads/gypsy-jazz.215/ (about 24 pages; later pages are at `.../gypsy-jazz.215/page-2`, `.../page-3`, and so on).

## Scope

- **Stay in that thread.** Gypsy jazz charts from `forums.irealpro.com/threads/gypsy-jazz.215/` only. Do not crawl the rest of the forum, other threads, or other sites unless the reader gives a URL.
- **Read-only.** Fetch public pages, read links, decode text. Do not log in, post, reply, vote, or follow attachment downloads.
- **Personal study.** Charts are community contributions. Save them for the reader's own practice and teaching notes. Do not republish them or bundle them as a collection for distribution.
- **Be polite.** One page at a time, no tight loops. If a page will not load, report it and stop; do not retry in a loop.

## What the thread contains

The thread has no file attachments. Charts are posted as links in two formats:

| Format | Looks like | What it holds |
| --- | --- | --- |
| `irealb://` | `irealb://Title=Composer==Style=Key==1r34LbKcu7...` | One or many songs (a playlist) in the current format. The chord string is scrambled. |
| `irealbook://` | `irealbook://Title=Composer=Style=Key=44={*A...` | One song in the older format. The chord string is plain text. |

Links are percent-encoded (`%41%27...`). Decode the percent-encoding first, then split.

Page 1 alone holds one `irealb://` playlist of 313 songs and 65 single-song `irealbook://` links.

### Fields

`irealb://`, fields separated by `=`, songs separated by `===`:

| Index | Meaning |
| --- | --- |
| 0 | Title |
| 1 | Composer |
| 2 | (unused) |
| 3 | Style, such as `Up Tempo Swing`, `Gypsy Swing`, `Gypsy Bossa`, `Waltz` |
| 4 | Key, such as `A-` (A minor), `C`, `Eb` |
| 5 | (unused) |
| 6 | Chord data, starts with `1r34LbKcu7` |
| 7-9 | (unused) and numbers |

`irealbook://`: title, composer, style, key, time-signature digits (`44` is 4/4), then the chord chart in plain text.

## Known playlist: "RN style GJ charts" (63 songs)

The user supplied an `irealb://` playlist link named **RN style GJ charts** that holds **63 gypsy jazz songs**. All 63 can be downloaded (decoded and saved to `SONGS/`) from that one link. The decoder script reads it the same way as any other `irealb://` link: save the link or the page that contains it, then run `list` and `decode`.

The link is stored in `references/rn-style-gj-charts-63.irealb.txt` (about 30,000 characters). It was written out from the user's pasted message, then checked by decoding: it parses as exactly 63 songs and every chart decodes to plain chord text. The page it came from was not recorded; it was not on page 1 of the forum thread.

```
python3 scripts/ireal_decode.py list references/rn-style-gj-charts-63.irealb.txt
python3 scripts/ireal_decode.py decode references/rn-style-gj-charts-63.irealb.txt "Nuages"
```

Songs in the playlist, in link order (counted from the pasted link: 63):

After You've Gone, All Of Me, Anouman, Avalon, Babik, Belleville, Blue Drag, Blues Clair, Blues For Ike, Bolero Blue, Bossa Dorado, Caravan, Clair de Lune, Confessin' That I Love You, Coquette, Danse Norwegienne, Daphne, Django's Castle, I Can't Give You Anything But Love, I Love You, I'll See You In My Dreams, I've Found A New Baby, It Don't Mean A Thing, J'attendrai, Limehouse Blues, Lulu Swing, Luna Tango, Ma Premiere Guitare, Melodie Au Crepuscule, Micro, Minor Blues, Minor Swing, Moppin' The Bride, Night And Day, Noto Swing, Nuages, Nuits St. Germain Des Pres, Number One, Oriental Shuffle, Out Of Nowhere, Place De Broukere, Rose Room, Sheik Of Araby (The), Shine, Some Of These Days, Stompin' At Decca, Summertime, Sweet Chorus, Sweet Georgia Brown, Sweet Sue Just You, Swing 39, Swing 42, Swing 48, Swing de Paris, Swing Guitars, Swingtime In Springtime, Tea For Two, Tears, Them There Eyes, Topsy, Troublant Bolero, Undecided, What Is This Thing Called Love.

Titles carry a trailing marker such as ` - rn` or ` - rn 1` in the link (for example `Minor Swing - rn 1`). Drop that marker from the file name and the heading, but keep the full original title in the source line.

The playlist also contains Minor Swing. It was not compared with the chart already saved in `SONGS/minor-swing.md` (which came from the 313-song playlist on page 1).

## Known playlist: "Gypsy Jazz" (313 songs)

The user supplied a second `irealb://` playlist link, named **Gypsy Jazz**, that holds **313 gypsy jazz songs**. All 313 can be downloaded (decoded and saved to `SONGS/`) from that one link. It starts with A'Sprengisandi 1, Alembert's 1, All Love, Alors? Voila! 2 and Angelo's Waltz, and ends with You Made Me Love You 2.

This looks like the same playlist that is already on page 1 of the forum thread (that link has 313 songs, the same first and last titles, and the playlist name "Gypsy Jazz"). It was not compared song by song, so treat it as the same list rather than 313 extra songs on top of it. The decoder can read it from the stored file, or straight from the thread:

```
python3 scripts/ireal_decode.py list references/gypsy-jazz-313.irealb.txt
python3 scripts/ireal_decode.py list https://forums.irealpro.com/threads/gypsy-jazz.215/
```

The link is stored in `references/gypsy-jazz-313.irealb.txt` (about 247,000 characters). It is a byte-for-byte copy of the link on page 1 of the thread, not of the user's pasted message, so it is exactly what the forum serves. It parses as 313 songs.

Songs in it that also appear in "RN style GJ charts" have different title markers (for example `Minor Swing - rn 1` there and `Minor Swing` here).

## Reading a chart

### Bundled decoder

`scripts/ireal_decode.py` reads a saved page or a URL and does the decoding:

```
python3 scripts/ireal_decode.py list   <page.html | url>
python3 scripts/ireal_decode.py decode <page.html | url> "<title>"
```

`list` prints title, composer, style, key and format for every song on the page. `decode` prints one song (a title match, exact first, then partial). Use it instead of decoding by hand.

To read a page, `curl -sL -A "Mozilla/5.0" <url> -o page.html` works; the thread needs no login.

### How the scrambled format decodes

Only for the `irealb://` format; the script does this for you.

1. Drop the `1r34LbKcu7` prefix.
2. Cut the rest into 50-character blocks (leave the last short piece, and any block with fewer than 2 characters after it, as it is).
3. In each 50-character block, swap characters `i` and `49-i` for `i` in 0-4, and again for `i` in 10-23.
4. Join the blocks, then replace `XyQ` with a space, `Kcl` with `| x`, and `LZ` with a space.

### Chart symbols

This is the set seen in the gypsy jazz thread. If you meet a symbol not on the list, say so; do not guess.

| Symbol | Meaning |
| --- | --- |
| `\|` | Bar line |
| `{` `}` | Repeat start, repeat end |
| `[` `]` | Section brackets |
| `*A`, `*B`, `*i` | Section label (A, B, intro) |
| `T44` | Time signature 4/4 (`T34` is 3/4) |
| `N1`, `N2` | First ending, second ending |
| `Q` | Coda symbol |
| `Z` | Final bar |
| `n` | No chord (N.C.) |
| `x` | Repeat the previous bar |
| `<text>` | A comment, such as `<Bass break>` or `<Fine>` |
| `( )` | An alternate chord for that bar or beat, such as `D-6(D-7)` |
| `,` | Separates chords within a bar |

### Chord names

iReal writes chords its own way. Convert to plain notation when saving, and keep the original beside it.

| iReal | Plain |
| --- | --- |
| `A-` | Am |
| `A-6` | Am6 |
| `D-7` | Dm7 |
| `C^7` | Cmaj7 |
| `Bb-7b5` | Bbm7b5 |
| `Eo`, `Eo7` | Edim, Edim7 |
| `G13b9` | G13b9 |
| `E7` | E7 |

## Saving a song

Songs go in `SONGS/`, one file each, named from the title in lowercase with hyphens: `SONGS/minor-swing.md`. The format is the one in `SONGS/minor-swing.md`:

1. Title, then a table: composer, style, key, time, source (thread URL and page), format read.
2. A legend line: how `x`, `N.C.` and `[alt]` are shown.
3. One section per part of the chart (Intro, A, B, coda), as 4-bar rows in a fenced block, chords in plain notation, with breaks and endings noted.
4. The original iReal chord string under each section.
5. A form summary.
6. The raw decoded chart at the bottom, so the reading can be checked.

Before saving, check:

- **Bar count.** Count the bars after expanding `x`. A standard section is 8, 12, 16 or 32 bars. If a count looks wrong, say so rather than force it.
- **Key.** The first and last chords usually agree with the key field.
- **Repeats and endings.** Mark where `{`/`}` and `N1`/`N2` fall. Do not invent jumps the chart does not state; write "chart does not say where to jump" when it does not.

## Using a chart with the other skills

- **Tab (`guitar-tablature`)**: write a chord chart or a line over the changes with chord symbols above the block.
- **Arpeggios (`music-theory-arpeggios`)** and **scales (`music-theory-scales`)**: pick patterns per bar from the chord. For example, Am6 gets the Am6 arpeggio; E7 gets the half-whole scale or a dim7 arpeggio built from its third.
- Pull one chord at a time; do not generate a tab for the whole chorus unless asked.

## Guardrails

- Only the Gypsy Jazz thread. If asked for something outside it, ask for the URL and confirm.
- Never log in or act on a page; never fetch attachments or run files from the forum.
- Always ask before saving to `SONGS/`, and say which song and where. Saving one chart a reader named is fine; bulk-saving a playlist, including the 63-song "RN style GJ charts" list, is not without being asked.
- Keep charts to personal use. Do not paste a full chart into other published material.
- Say when the chart is ambiguous (unknown symbol, odd bar count, no jump marked). A flagged gap is better than a confident wrong chart.
- Keep the source: title, thread, page, format. A chart without its source cannot be rechecked.
