#!/usr/bin/env python3
"""Read irealb:// links from a saved iReal Pro forum page (or URL) and decode chord charts.

Usage:
  ireal_decode.py list   <page.html | url>                 list every song found
  ireal_decode.py decode <page.html | url> "<title>"       print one song's decoded chart

Read-only. Does not log in, post, or download attachments.
"""
import html, re, sys, urllib.parse as up, urllib.request

PREFIX = "1r34LbKcu7"
# Two link formats appear in the forum:
#  irealb://     fields: 0 title, 1 composer, 2 (unused), 3 style, 4 key, 5 (unused),
#                6 chord data (obfuscated, starts with the PREFIX), 7 (unused), 8-9 numbers.
#                Songs are separated by "===". A link may hold many songs (a playlist).
#  irealbook://  older plain-text format, fields: 0 title, 1 composer, 2 style, 3 key,
#                4 time signature digits (e.g. 44), 5 chord chart in plain text.


def load(src):
    if re.match(r"https?://", src):
        req = urllib.request.Request(src, headers={"User-Agent": "Mozilla/5.0"})
        return urllib.request.urlopen(req, timeout=30).read().decode("utf-8", "ignore")
    return open(src, encoding="utf-8", errors="ignore").read()


def songs(page):
    seen, out = [], []
    for link in re.findall(r"(irealb(?:ook)?://[^\"'<> ]+)", page):
        if link in seen:
            continue
        seen.append(link)
        scheme = link.split("://", 1)[0]
        body = up.unquote(html.unescape(link)).split("://", 1)[1]
        for chunk in body.split("==="):
            f = chunk.split("=")
            if scheme == "irealbook" and len(f) >= 6:
                out.append({"title": f[0], "composer": f[1], "style": f[2],
                            "key": f[3], "data": f[5], "format": "irealbook"})
                continue
            data = [x for x in f if x.startswith(PREFIX)]
            if data and len(f) >= 7:
                out.append({"title": f[0], "composer": f[1], "style": f[3],
                            "key": f[4], "data": data[0], "format": "irealb"})
    return out


def _swap(block):
    a = list(block)
    for i in range(5):
        a[i], a[49 - i] = a[49 - i], a[i]
    for i in range(10, 24):
        a[i], a[49 - i] = a[49 - i], a[i]
    return "".join(a)


def decode(data):
    raw, out = data[len(PREFIX):], ""
    while len(raw) > 50:
        block, raw = raw[:50], raw[50:]
        out += _swap(block) if len(raw) >= 2 else block
    out += raw
    return out.replace("XyQ", " ").replace("Kcl", "| x").replace("LZ", " ")


def main(argv):
    if len(argv) < 3 or argv[1] not in ("list", "decode"):
        print(__doc__); return 2
    found = songs(load(argv[2]))
    if argv[1] == "list":
        for s in found:
            print(f'{s["title"]} | {s["composer"]} | {s["style"]} | {s["key"]} | {s["format"]}')
        print(f"{len(found)} songs", file=sys.stderr); return 0
    want = argv[3].lower() if len(argv) > 3 else ""
    hits = [s for s in found if s["title"].lower() == want] or [s for s in found if want in s["title"].lower()]
    if not hits:
        print("no match", file=sys.stderr); return 1
    for s in hits[:1]:
        print(f'Title: {s["title"]}\nComposer: {s["composer"]}\nStyle: {s["style"]}\nKey: {s["key"]}\n')
        print(decode(s["data"]) if s["format"] == "irealb" else s["data"])
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
