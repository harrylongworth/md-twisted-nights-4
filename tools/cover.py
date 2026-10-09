#!/usr/bin/env python3
"""Generate the placeholder cover for a Twisted Nights book.

Usage: python3 tools/cover.py <1|2|3> [out.jpg]
Shared by all three repos (keep copies identical); writes 1600x2400 JPEG.
"""
import math, random, sys
from PIL import Image, ImageDraw, ImageFilter, ImageFont

W, H = 1600, 2400
SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"

BOOKS = {
    1: dict(night="NIGHT ONE", sub="The Twisted Night", tag="They have always been watching.",
            sky=((8, 12, 12), (22, 30, 26)), title=(240, 232, 214), accent=(200, 60, 50)),
    2: dict(night="NIGHT TWO", sub="Shadows in the Dark", tag="There were never only seven.",
            sky=((8, 8, 18), (40, 28, 60)), title=(226, 214, 240), accent=(170, 110, 220)),
    3: dict(night="NIGHT THREE", sub="Night of Embers", tag="Grim's Night has always kept a secret.",
            sky=((10, 8, 8), (70, 26, 12)), title=(240, 130, 50), accent=(255, 196, 80)),
}


def gradient(top, bottom):
    img = Image.new("RGB", (W, H))
    d = ImageDraw.Draw(img)
    for y in range(H):
        t = y / (H - 1)
        d.line([(0, y), (W, y)], fill=tuple(int(a + (b - a) * t) for a, b in zip(top, bottom)))
    return img


def glow(img, xy, r, colour, blur):
    layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
    ImageDraw.Draw(layer).ellipse([xy[0] - r, xy[1] - r, xy[0] + r, xy[1] + r], fill=colour)
    img.alpha_composite(layer.filter(ImageFilter.GaussianBlur(blur)))


def eyes(img, x, y, gap, r, colour):
    for dx in (-gap, gap):
        glow(img, (x + dx, y), r * 3, colour + (150,), r * 2)
        ImageDraw.Draw(img).ellipse([x + dx - r, y - r, x + dx + r, y + r], fill=(255, 235, 230))


def moon(img, x, y, r, tint):
    glow(img, (x, y), int(r * 1.8), tint + (70,), 60)
    ImageDraw.Draw(img).ellipse([x - r, y - r, x + r, y + r], fill=(232, 226, 210))


def cypress(d, x, base, h, w, colour, rng):
    d.polygon([(x - w, base), (x - w // 3, base - h), (x + w // 3, base - h), (x + w, base)], fill=colour)
    d.ellipse([x - w * 3, base - h - w * 2, x + w * 3, base - h + w * 2], fill=colour)
    for _ in range(6):  # hanging moss
        mx = x + rng.randint(-w * 3, w * 3)
        my = base - h + rng.randint(-w, w)
        d.line([(mx, my), (mx + rng.randint(-8, 8), my + rng.randint(60, 180))], fill=colour, width=4)


def scene_one(img, rng):
    moon(img, 1240, 1060, 110, (220, 220, 200))
    d = ImageDraw.Draw(img)
    for i in range(14):  # back row of cypress, bayou ground
        cypress(d, 60 + i * 115 + rng.randint(-20, 20), 1900, rng.randint(500, 750), 34, (14, 20, 18), rng)
    d.rectangle([0, 1880, W, H], fill=(10, 14, 13))
    for x, y in [(300, 1530), (760, 1580), (1330, 1560)]:
        eyes(img, x, y, 16, 6, (220, 40, 30))
    # Twisted Wolf: body facing away, head turned straight at the reader
    d = ImageDraw.Draw(img)
    d.ellipse([520, 1700, 1000, 1900], fill=(4, 6, 6))
    d.polygon([(860, 1720), (900, 1560), (1000, 1560), (1020, 1720)], fill=(4, 6, 6))
    d.polygon([(890, 1580), (905, 1490), (935, 1575)], fill=(4, 6, 6))
    d.polygon([(965, 1575), (995, 1490), (1010, 1580)], fill=(4, 6, 6))
    eyes(img, 950, 1620, 22, 9, (230, 40, 30))


def scene_two(img, rng):
    moon(img, 330, 1040, 100, (150, 100, 200))
    d = ImageDraw.Draw(img)
    for i in range(16):
        cypress(d, 40 + i * 105 + rng.randint(-20, 20), 1950, rng.randint(480, 760), 30, (16, 10, 26), rng)
    d.rectangle([0, 1930, W, H], fill=(22, 16, 34))
    # long shadow with rabbit ears falling across the ground
    sh = Image.new("RGBA", img.size, (0, 0, 0, 0))
    sd = ImageDraw.Draw(sh)
    sd.polygon([(470, 1960), (1350, 2250), (1420, 2190), (560, 1940)], fill=(4, 2, 10, 200))
    sd.polygon([(1360, 2215), (1520, 2240), (1500, 2265)], fill=(4, 2, 10, 200))
    sd.polygon([(1385, 2180), (1550, 2160), (1540, 2190)], fill=(4, 2, 10, 200))
    img.alpha_composite(sh.filter(ImageFilter.GaussianBlur(4)))
    # the raccoon that isn't one
    d = ImageDraw.Draw(img)
    d.ellipse([420, 1840, 600, 1970], fill=(6, 4, 12))
    d.ellipse([500, 1780, 610, 1880], fill=(6, 4, 12))
    d.polygon([(510, 1800), (520, 1760), (545, 1795)], fill=(6, 4, 12))
    d.polygon([(570, 1795), (595, 1760), (602, 1805)], fill=(6, 4, 12))
    for i in range(5):  # ringed tail
        d.ellipse([340 - i * 22, 1900 + i * 6, 420 - i * 22, 1945 + i * 6],
                  fill=(6, 4, 12) if i % 2 else (30, 22, 44))
    eyes(img, 555, 1828, 18, 7, (180, 110, 255))


def scene_three(img, rng):
    d = ImageDraw.Draw(img)
    d.ellipse([300, 1880, 1300, 2160], fill=(28, 14, 10))  # the dig mound
    glow(img, (800, 1930), 360, (255, 110, 30, 110), 120)
    # sickle: Grim Foxy's sickle-hand, rising out of the dig on a metal forearm
    d = ImageDraw.Draw(img)
    d.line([(740, 1960), (830, 1500)], fill=(40, 30, 26), width=48)

    def bez(p0, c, p1, n=40):
        return [((1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * c[0] + t * t * p1[0],
                 (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * c[1] + t * t * p1[1])
                for t in (i / n for i in range(n + 1))]
    outer = bez((850, 1520), (1260, 1180), (690, 1080))
    inner = bez((690, 1080), (1120, 1230), (800, 1500))
    d.polygon(outer + inner, fill=(70, 60, 58))
    d.line(inner, fill=(170, 90, 40), width=6)  # rust/ember edge
    for _ in range(260):  # rising embers
        x, y = rng.randint(0, W), rng.randint(900, 2300)
        r = rng.choice([2, 2, 3, 4, 5])
        c = rng.choice([(255, 170, 60), (255, 120, 40), (255, 210, 120)])
        glow(img, (x, y), r * 2, c + (220,), r)


def text_c(d, y, s, font, fill, shadow=True):
    w = d.textlength(s, font=font)
    if shadow:
        d.text(((W - w) / 2 + 4, y + 4), s, font=font, fill=(0, 0, 0))
    d.text(((W - w) / 2, y), s, font=font, fill=fill)


def main():
    n = int(sys.argv[1])
    out = sys.argv[2] if len(sys.argv) > 2 else "cover.jpg"
    b = BOOKS[n]
    rng = random.Random(n)
    img = gradient(*b["sky"]).convert("RGBA")
    {1: scene_one, 2: scene_two, 3: scene_three}[n](img, rng)
    d = ImageDraw.Draw(img)
    text_c(d, 150, "TWISTED", ImageFont.truetype(SERIF_B, 200), b["title"])
    text_c(d, 360, "NIGHTS", ImageFont.truetype(SERIF_B, 200), b["title"])
    d.line([(420, 600), (1180, 600)], fill=b["accent"], width=5)
    text_c(d, 630, b["night"], ImageFont.truetype(SERIF_B, 80), b["accent"])
    text_c(d, 740, b["sub"], ImageFont.truetype(SERIF, 84), b["title"])
    text_c(d, 2120, b["tag"], ImageFont.truetype(SERIF, 46), (220, 214, 200))
    text_c(d, 2200, "T.L. SHADOWMARSH", ImageFont.truetype(SERIF_B, 64), b["title"])
    text_c(d, 2300, "DRAFT EDITION — NOT FOR SALE", ImageFont.truetype(SERIF, 30), (150, 146, 140), False)
    img.convert("RGB").save(out, "JPEG", quality=92)


if __name__ == "__main__":
    main()
