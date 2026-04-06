fig.write_html("desktop/mona-lisa-overdrive/dog-solitude/mlo-website/docs/vaporwave.html", include_plotlyjs="cdn", full_html=False)
"""
Vaporwave Drive - A looping 8/16-bit animation
For embedding in a static MkDocs site via pygame/pyodide or running standalone.

Run: python vaporwave_drive.py
"""

import pygame
import math
import random
import sys

# ── Constants ──────────────────────────────────────────────────────────────────
W, H      = 800, 600
FPS       = 30
HORIZON   = H // 2 - 30        # horizon line y-position
ROAD_VANISH = W // 2           # vanishing point x

# Vaporwave palette
BG_TOP    = (15,  5,  40)      # deep midnight purple
BG_BOT    = (40,  0,  60)      # dark magenta sky
GRID_COL  = (180, 0, 200)      # purple grid lines
GRID_GLOW = (255, 50, 220)     # hot-pink glow lines
ROAD_COL  = (25, 10,  50)      # road fill
STRIPE_C  = (255, 50, 200)     # road stripe pink
SUN_COL   = [(255,100,220),(255,60,180),(200,20,150),(140,0,110)]
TREE_COL  = [(0,220,120),(0,180,80),(0,140,60),(20,255,120)]  # neon greens
GATOR_C   = (0, 200, 80)
EYE_C     = (255, 50, 50)
DASH_BG   = (10,  0,  20)
DASH_BORD = (180, 0, 255)
LCD_BG    = (0,  30,  10)
LCD_TXT   = (0, 255, 100)
STAR_C    = (255, 200, 255)

pygame.init()
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("MONA LISA OVERDRIVE // VAPORWAVE DRIVE")
clock  = pygame.time.Clock()

# ── Fonts ──────────────────────────────────────────────────────────────────────
try:
    font_sm  = pygame.font.SysFont("Courier", 12, bold=True)
    font_med = pygame.font.SysFont("Courier", 16, bold=True)
    font_lg  = pygame.font.SysFont("Courier", 22, bold=True)
    font_xl  = pygame.font.SysFont("Courier", 28, bold=True)
except:
    font_sm  = pygame.font.Font(None, 14)
    font_med = pygame.font.Font(None, 18)
    font_lg  = pygame.font.Font(None, 24)
    font_xl  = pygame.font.Font(None, 30)

# ── Stars ──────────────────────────────────────────────────────────────────────
stars = [(random.randint(0, W), random.randint(0, HORIZON - 40),
          random.choice([1,1,1,2])) for _ in range(120)]

# ── Grid state ─────────────────────────────────────────────────────────────────
grid_offset  = 0.0   # drives the scrolling ground grid
speed        = 3.5   # scroll speed

# ── Road stripes ───────────────────────────────────────────────────────────────
# Each stripe: y-position in world space (0=horizon, 1=bottom of screen)
stripes = [i / 6 for i in range(7)]

# ── Trees ──────────────────────────────────────────────────────────────────────
class Tree:
    """Pixel-art live-oak silhouette."""
    def __init__(self, side):
        self.side = side        # 'L' or 'R'
        self.z    = random.uniform(0.05, 1.0)   # depth (0=far, 1=near)
        self.reset()

    def reset(self):
        self.z = 0.05
        self.color = random.choice(TREE_COL)

    def world_x(self):
        offset = -260 if self.side == 'L' else 260
        # perspective: things near center at horizon, spread at bottom
        # at z=1 (nearest) offset is full; at z=0 it converges
        return ROAD_VANISH + int(offset * self.z)

    def world_y(self):
        # z=0 -> horizon; z=1 -> bottom
        return HORIZON + int((H - HORIZON) * self.z)

    def scale(self):
        return max(1, int(60 * self.z))

    def draw(self, surf):
        cx = self.world_x()
        by = self.world_y()
        s  = self.scale()
        c  = self.color
        trunk_w = max(2, s // 8)
        trunk_h = s // 3
        # trunk
        pygame.draw.rect(surf, (80, 40, 10),
                         (cx - trunk_w//2, by - trunk_h, trunk_w, trunk_h))
        # layered canopy blobs (8-bit style: rectangles)
        for layer, (dy, rw, rh) in enumerate([
            (trunk_h + s//2,     s,      s//2),
            (trunk_h + s,        s*3//4, s//3),
            (trunk_h + s*3//2,   s//2,   s//4),
        ]):
            shade = tuple(max(0, v - layer*30) for v in c)
            pygame.draw.rect(surf, shade,
                             (cx - rw//2, by - dy, rw, rh))
        # moss drape pixels
        for i in range(0, s, max(2, s//6)):
            px = cx - s//2 + i
            pygame.draw.line(surf, (0, 180, 60),
                             (px, by - trunk_h - s//4),
                             (px, by - trunk_h - s//4 + random.randint(s//6, s//3)), 1)

trees_L = [Tree('L') for _ in range(8)]
trees_R = [Tree('R') for _ in range(8)]

# ── Gators ────────────────────────────────────────────────────────────────────
class Gator:
    def __init__(self, side):
        self.side = side
        self.z    = random.uniform(0.1, 0.9)
        self.blink_t = 0

    def world_x(self):
        base = -320 if self.side == 'L' else 320
        return ROAD_VANISH + int(base * self.z)

    def world_y(self):
        return HORIZON + int((H - HORIZON - 20) * self.z)

    def scale(self):
        return max(1, int(28 * self.z))

    def draw(self, surf, tick):
        cx = self.world_x()
        cy = self.world_y()
        s  = self.scale()
        # body
        pygame.draw.ellipse(surf, GATOR_C,
                            (cx - s, cy - s//3, s*2, s//2))
        # snout
        sx = cx + s if self.side == 'R' else cx - s
        pygame.draw.rect(surf, (0, 160, 60),
                         (sx - s//2, cy - s//4, s//2, s//4))
        # eyes (blinking)
        ew = max(2, s//6)
        for ex in [cx - s//3, cx + s//3]:
            if (tick + self.blink_t) % 60 < 55:  # open
                pygame.draw.rect(surf, EYE_C, (ex, cy - s//2, ew, ew))
            else:
                pygame.draw.line(surf, EYE_C, (ex, cy - s//2 + ew//2),
                                 (ex + ew, cy - s//2 + ew//2), 1)

gators = [Gator('L') for _ in range(3)] + [Gator('R') for _ in range(3)]
for g in gators:
    g.blink_t = random.randint(0, 59)

# ── Sun / retrowave bands ─────────────────────────────────────────────────────
SUN_CX  = W // 2
SUN_CY  = HORIZON - 20
SUN_R   = 55

def draw_sky(surf):
    # gradient sky
    for y in range(HORIZON):
        t   = y / HORIZON
        r   = int(BG_TOP[0] + (BG_BOT[0] - BG_TOP[0]) * t)
        g   = int(BG_TOP[1] + (BG_BOT[1] - BG_TOP[1]) * t)
        b   = int(BG_TOP[2] + (BG_BOT[2] - BG_TOP[2]) * t)
        pygame.draw.line(surf, (r, g, b), (0, y), (W, y))

def draw_sun(surf, tick):
    # banded retro sun
    for i, col in enumerate(SUN_COL):
        r = SUN_R - i * (SUN_R // len(SUN_COL))
        pygame.draw.circle(surf, col, (SUN_CX, SUN_CY), r)
    # horizontal band cuts
    band_h = 5
    num_bands = SUN_R // (band_h * 2)
    for i in range(num_bands):
        by = SUN_CY - SUN_R + (i * band_h * 2) + band_h
        if abs(by - SUN_CY) < SUN_R:
            pygame.draw.rect(surf, BG_BOT,
                             (SUN_CX - SUN_R, by, SUN_R * 2, band_h))
    # glow ring
    pygame.draw.circle(surf, (255, 100, 200), (SUN_CX, SUN_CY), SUN_R + 4, 2)

def draw_stars(surf, tick):
    for (x, y, r) in stars:
        bright = 150 + int(100 * math.sin(tick * 0.05 + x))
        col = (bright, int(bright * 0.7), bright)
        pygame.draw.circle(surf, col, (x, y), r)

# ── Ground grid ───────────────────────────────────────────────────────────────
NUM_V_LINES = 20   # vertical grid lines
NUM_H_LINES = 12   # horizontal grid lines

def perspective_x(wx, z):
    """Map world x at depth z (0..1) to screen x."""
    return int(ROAD_VANISH + wx * z)

def perspective_y(z):
    """Map depth z (0..1) to screen y."""
    return int(HORIZON + (H - HORIZON) * z)

def draw_grid(surf, offset):
    # horizontal lines (spacing stretches near camera)
    for i in range(NUM_H_LINES + 1):
        raw_z = (i + offset % 1) / NUM_H_LINES
        z = raw_z ** 2                          # perspective squish
        if z < 0.002:
            continue
        y  = perspective_y(z)
        brightness = int(80 + 175 * z)
        col = (min(255, brightness), 0, min(255, brightness))
        pygame.draw.line(surf, col, (0, y), (W, y), 1 if z < 0.5 else 1)

    # vertical lines fanning from vanishing point
    spread = 900
    for i in range(NUM_V_LINES + 1):
        t  = i / NUM_V_LINES                   # 0..1
        wx = -spread + t * spread * 2
        x0 = ROAD_VANISH
        y0 = HORIZON
        x1 = perspective_x(wx, 1.0)
        y1 = H
        brightness = int(60 + 100 * abs(t - 0.5) * 2)
        col = (min(255, brightness + 80), 0, min(255, brightness + 120))
        pygame.draw.line(surf, col, (x0, y0), (x1, y1), 1)

# ── Road ──────────────────────────────────────────────────────────────────────
ROAD_L_WORLD = -140   # world half-width of road at z=1
ROAD_R_WORLD =  140

def draw_road(surf, offset):
    # road trapezoid
    pts = [
        (perspective_x(ROAD_L_WORLD, 0.001), HORIZON),
        (perspective_x(ROAD_R_WORLD, 0.001), HORIZON),
        (perspective_x(ROAD_R_WORLD, 1.0),   H),
        (perspective_x(ROAD_L_WORLD, 1.0),   H),
    ]
    pygame.draw.polygon(surf, ROAD_COL, pts)

    # center dashes
    for i, t in enumerate(stripes):
        z = ((t + offset) % 1.0) ** 2 + 0.01
        y = perspective_y(z)
        w = max(2, int(10 * z))
        h = max(3, int(20 * z))
        pygame.draw.rect(surf, STRIPE_C, (ROAD_VANISH - w//2, y - h//2, w, h))

    # road edge lines
    for side in [-1, 1]:
        wx = ROAD_L_WORLD if side == -1 else ROAD_R_WORLD
        glow = GRID_GLOW
        pygame.draw.line(surf, glow,
                         (perspective_x(wx, 0.001), HORIZON),
                         (perspective_x(wx, 1.0), H), 2)

# ── Dashboard ─────────────────────────────────────────────────────────────────
DASH_Y  = H - 130
DASH_H  = 130
RADIO_X = W // 2 - 110
RADIO_Y = DASH_Y + 20
RADIO_W = 220
RADIO_H = 50

def draw_dashboard(surf, tick):
    # dash panel
    pygame.draw.rect(surf, DASH_BG, (0, DASH_Y, W, DASH_H))
    pygame.draw.line(surf, DASH_BORD, (0, DASH_Y), (W, DASH_Y), 3)

    # steering wheel (simple circle + spoke)
    sw_cx, sw_cy, sw_r = W//2, DASH_Y + 90, 55
    pygame.draw.circle(surf, (50, 0, 80), (sw_cx, sw_cy), sw_r)
    pygame.draw.circle(surf, DASH_BORD, (sw_cx, sw_cy), sw_r, 3)
    for ang in [0, 120, 240]:
        rad = math.radians(ang)
        ex  = sw_cx + int((sw_r - 5) * math.cos(rad))
        ey  = sw_cy + int((sw_r - 5) * math.sin(rad))
        pygame.draw.line(surf, DASH_BORD, (sw_cx, sw_cy), (ex, ey), 3)
    pygame.draw.circle(surf, DASH_BORD, (sw_cx, sw_cy), 8)

    # left gauges (speed / rpm blocks)
    for gi, label in enumerate(["SPD", "RPM"]):
        gx = 60 + gi * 140
        gy = DASH_Y + 15
        pygame.draw.rect(surf, (20, 0, 40), (gx, gy, 100, 40))
        pygame.draw.rect(surf, DASH_BORD, (gx, gy, 100, 40), 2)
        val = 88 + int(10 * math.sin(tick * 0.07 + gi)) if gi == 0 else \
              3200 + int(400 * math.sin(tick * 0.11 + gi))
        txt = font_sm.render(f"{label}: {val}", True, LCD_TXT)
        surf.blit(txt, (gx + 6, gy + 13))

    # radio LCD screen
    pygame.draw.rect(surf, LCD_BG, (RADIO_X, RADIO_Y, RADIO_W, RADIO_H))
    pygame.draw.rect(surf, (0, 255, 100), (RADIO_X, RADIO_Y, RADIO_W, RADIO_H), 2)

    # scrolling "MONA LISA OVERDRIVE" text
    scroll_txt = "  ♪ MONA LISA OVERDRIVE ♪  "
    char_w     = 10
    total_w    = len(scroll_txt) * char_w
    offset_x   = -(tick * 2) % total_w
    radio_surf = pygame.Surface((RADIO_W - 8, RADIO_H - 10))
    radio_surf.fill(LCD_BG)
    for rep in range(3):
        label = font_med.render(scroll_txt, True, LCD_TXT)
        radio_surf.blit(label, (offset_x + rep * total_w, 6))
    surf.blit(radio_surf, (RADIO_X + 4, RADIO_Y + 5))

    # waveform bars on radio
    for bx in range(RADIO_X + 4, RADIO_X + RADIO_W - 4, 6):
        bh = int(6 + 6 * math.sin(tick * 0.3 + bx * 0.2))
        pygame.draw.rect(surf, (0, 200, 80),
                         (bx, RADIO_Y + RADIO_H - 12 - bh, 4, bh))

    # right: vaporwave label
    vtxt = font_lg.render("V A P O R W A V E", True, (255, 80, 220))
    surf.blit(vtxt, (W - 220, DASH_Y + 18))
    sub  = font_sm.render("// OVERDRIVE MODE //", True, (180, 0, 255))
    surf.blit(sub, (W - 190, DASH_Y + 48))

# ── Scanlines overlay ─────────────────────────────────────────────────────────
def draw_scanlines(surf):
    scan_surf = pygame.Surface((W, H), pygame.SRCALPHA)
    for y in range(0, H, 3):
        pygame.draw.line(scan_surf, (0, 0, 0, 55), (0, y), (W, y))
    surf.blit(scan_surf, (0, 0))

# ── CRT pixel shimmer ─────────────────────────────────────────────────────────
def draw_crt_border(surf, tick):
    # corner glow vignette-ish
    alpha = int(80 + 40 * math.sin(tick * 0.05))
    bord  = pygame.Surface((W, H), pygame.SRCALPHA)
    for i in range(12):
        col = (120, 0, 200, max(0, alpha - i * 7))
        pygame.draw.rect(bord, col, (i, i, W - i*2, H - i*2), 1)
    surf.blit(bord, (0, 0))

# ── Scroll objects ────────────────────────────────────────────────────────────
def update_scroll(objects, offset, speed):
    """Advance depth of objects and reset when they pass the camera."""
    for obj in objects:
        obj.z += speed * 0.012
        if obj.z >= 1.0:
            obj.z = 0.05
            obj.color = random.choice(TREE_COL) if hasattr(obj, 'color') else None

# ── Main loop ─────────────────────────────────────────────────────────────────
def main():
    tick = 0
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_ESCAPE, pygame.K_q):
                    running = False

        global grid_offset
        grid_offset += speed * 0.04

        # ── Draw layers ────────────────────────────────────────────────────
        draw_sky(screen)
        draw_stars(screen, tick)
        draw_sun(screen, tick)
        draw_grid(screen, grid_offset)
        draw_road(screen, grid_offset)

        # Sort all side objects by depth (far first)
        side_objects = sorted(trees_L + trees_R + gators,
                              key=lambda o: o.z)
        for obj in side_objects:
            if isinstance(obj, Tree):
                obj.draw(screen)
            else:
                obj.draw(screen, tick)

        draw_dashboard(screen, tick)
        draw_scanlines(screen)
        draw_crt_border(screen, tick)

        # ── Advance objects ────────────────────────────────────────────────
        update_scroll(trees_L, grid_offset, speed)
        update_scroll(trees_R, grid_offset, speed)
        for g in gators:
            g.z += speed * 0.010
            if g.z >= 1.0:
                g.z = 0.1

        # stripe scroll
        for i in range(len(stripes)):
            stripes[i] = (stripes[i] + speed * 0.005) % 1.0

        pygame.display.flip()
        clock.tick(FPS)
        tick += 1

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
