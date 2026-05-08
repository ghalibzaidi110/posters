# CARPER FYP — Posters & Architecture Diagrams

All files in this folder are self-contained HTML — open in Chrome to view, then export to PNG with the included Python script.

---

## Posters (7 designs)

### Matched to your official FAST FYP poster (dark teal/navy theme)

| File | Preview · Style |
|---|---|
| [POSTER_4_OFFICIAL_FAITHFUL.html](POSTER_4_OFFICIAL_FAITHFUL.html) | Closest to your existing poster · 2-column header (logo + title + team / hero) · blue triangle accents · same section pill-headers · animated scan line |
| [POSTER_5_OFFICIAL_ENHANCED.html](POSTER_5_OFFICIAL_ENHANCED.html) | Enhanced layout · circuit-grid background · feature-icon row · dark cyan KPI dashboard · cost-model RMSE bar chart |
| [POSTER_6_OFFICIAL_PREMIUM.html](POSTER_6_OFFICIAL_PREMIUM.html) | Premium · gold FYP ribbon · larger hero with on-car bounding boxes · 6-class damage strip · 8-card Prisma data-model row · diamond-rotated pipeline nodes |

### Light theme variant

| File | Notes |
|---|---|
| [POSTER_7_OFFICIAL_LIGHT.html](POSTER_7_OFFICIAL_LIGHT.html) | White/soft-blue body with dark inspection card (mimics real app screenshot) · **rich illustrated pipeline icons** (camera with LIVE badge → video frames + FPS → neural-net + YOLO label → car with detection brackets → receipt + coin → stars + check → PDF report) · **live-detection flow** (no upload step) |

### Reference-style variants (different visual languages)

| File | Inspired by |
|---|---|
| [POSTER_1_INTELLEXA_STYLE.html](POSTER_1_INTELLEXA_STYLE.html) | INTELLEXA template — cream/beige body with dark chip headers, layered horizontal pipeline |
| [POSTER_2_IWAF_STYLE.html](POSTER_2_IWAF_STYLE.html) | iWAF template — orange/teal accents, detailed system architecture diagram, dashboard mock |
| [POSTER_3_TALENTMATCH_STYLE.html](POSTER_3_TALENTMATCH_STYLE.html) | TalentMatch AI template — purple gradient header, 3-layer architecture stack |

---

## Diagrams (standalone, embeddable)

### System Architecture

| File | Use case |
|---|---|
| [SYSTEM_ARCHITECTURE.html](SYSTEM_ARCHITECTURE.html) | Light theme · 1400×1000 · with title + footer · standalone slide |
| [SYSTEM_ARCHITECTURE_DARK.html](SYSTEM_ARCHITECTURE_DARK.html) | Dark theme · 1400×1000 · with title + footer · standalone slide |
| [SYSTEM_ARCHITECTURE_FOR_POSTER.html](SYSTEM_ARCHITECTURE_FOR_POSTER.html) | **Light** · 1200×720 · no title/footer, ready to embed in your FYP poster |
| [SYSTEM_ARCHITECTURE_FOR_POSTER.png](SYSTEM_ARCHITECTURE_FOR_POSTER.png) | The above, exported at **3600 × 2160 px** (3× retina) — drop into your poster |

All three diagrams contain the same components: **React + Next.js + Tailwind + ONNX-Web + React Query → NestJS + Prisma + TypeScript + JWT → splits into AI/ML (FastAPI · YOLOv8n · PyTorch · OpenCV · Sentence-BERT · Gradient Boosting) and Data (PostgreSQL · Cloudinary · Docker)**, with orange flow arrows and pill labels (REST API · WebSocket / JSON Response).

### Working Pipeline

| File | Use case |
|---|---|
| [WORKING_PIPELINE_FOR_POSTER.html](WORKING_PIPELINE_FOR_POSTER.html) | **Light** · 1400×360 · no title/footer, ready to embed in your FYP poster |
| [WORKING_PIPELINE_FOR_POSTER.png](WORKING_PIPELINE_FOR_POSTER.png) | The above, exported at **4200 × 1080 px** (3× retina) — drop into your poster |

7-step **live-detection** flow as illustrated icon chips on a light canvas: **CAMERA** (phone with LIVE + 28 FPS badges, car in viewfinder, dashed YOLO bracket) → **STREAM** (3 stacked video frames + green 28 FPS pill + motion lines) → **INFERENCE** (multi-layer neural network with red YOLOv8n label) → **DETECT** (blue car with yellow YOLO brackets, 96% confidence pill, pulsing red damage dot) → **ESTIMATE** (white receipt + cyan $ + gold coin) → **RECOMMEND** (3 gold stars + green check badge) → **REPORT** (PDF document with bar chart + red PDF stamp). Orange dashed connector line behind the icons.

---

## Conversion script: HTML → PNG

[html_to_png.py](html_to_png.py) — converts any of the HTML files (or any HTML, anywhere) into a high-resolution PNG using headless Chromium.

### One-time install

```bash
pip install playwright
playwright install chromium
```

### Usage

```bash
# Auto-detects .poster / .canvas wrapper size + selector, defaults to 2x scale
python html_to_png.py POSTER_4_OFFICIAL_FAITHFUL.html

# Print-quality 3x retina output
python html_to_png.py POSTER_7_OFFICIAL_LIGHT.html --scale 3

# Force a specific element capture
python html_to_png.py SYSTEM_ARCHITECTURE_FOR_POSTER.html --selector .canvas

# Custom viewport (overrides auto-detect)
python html_to_png.py diagram.html -W 1400 -H 900 --no-auto

# Transparent PNG (for overlaying)
python html_to_png.py diagram.html --transparent

# Convert every .html in a folder at once
python html_to_png.py . --batch --scale 3

# Custom output path
python html_to_png.py poster.html -o output.png
```

### Smart defaults

- **Auto-size** — peeks into the CSS for the first `.poster {... width:1200px; height:1900px ...}` block (or `.canvas`) and sets the viewport to match
- **Auto-selector** — if it finds `class="poster"` or `class="canvas"` in the markup, it captures only that element (no scrollbars, no extra background)
- **`--scale`** — 1 = normal, 2 = retina (default), 3 = print quality, 4 = giant prints
- **`--batch`** — convert every `.html` in a folder in one run
- **`--transparent`** — omit background for overlays

---

## Recommended workflow

1. **Pick a poster design** — open the HTML files in Chrome, decide which one fits.
2. **Edit content directly in HTML** — abstract text, results bars, team names, etc. (search-and-replace inside the relevant `.html` file).
3. **Export to PNG** with the script:
   ```bash
   python html_to_png.py POSTER_7_OFFICIAL_LIGHT.html --scale 3
   ```
4. **Embed the architecture diagram** — `SYSTEM_ARCHITECTURE_FOR_POSTER.png` is sized to drop straight into the System Architecture section of your FYP poster (paste in PowerPoint / Photoshop / Illustrator as an image).

### Output dimensions cheatsheet

| Source | Default scale | At `--scale 3` |
|---|---|---|
| 1200 × 1800 (poster portrait, e.g. POSTER_4–6) | 2400 × 3600 px | 3600 × 5400 px |
| 1200 × 1900 (POSTER_7 light) | 2400 × 3800 px | 3600 × 5700 px |
| 1200 × 720 (architecture embed) | 2400 × 1440 px | 3600 × 2160 px |
| 1400 × 1000 (architecture standalone) | 2800 × 2000 px | 4200 × 3000 px |

For A0 print (33.1 × 46.8 in @ 150 DPI = 4961 × 7016 px), use `--scale 3` or higher on the portrait posters.

---

## Project content baked into every poster

- **Title:** CARPER — The Car Problem Solver
- **University:** FAST-NUCES (FAST National University of Computer & Emerging Sciences)
- **Team:** Syed Wali Mohsin Naqvi (22K-4550, Lead) · Syed Ghalib Hussain Zaidi (22K-4536) · Syed Azhaan Ali (22K-4140)
- **Supervisor:** Mr. Shoaib Raza
- **Detection:** YOLOv8n on CarDD (4,000 images, 6 classes — Dent · Scratch · Crack · Glass Shatter · Tire Flat · Lamp Broken)
- **Cost estimation:** Gradient Boosting (vs Linear Regression / Random Forest / Extra Trees)
- **Marketplace:** Sentence-BERT semantic search + FAISS index
- **Stack:** Next.js 15 · NestJS 11 · PostgreSQL · Prisma 7 · FastAPI · Cloudinary · ONNX-Web · Docker
- **Results:** mAP@0.5 = 0.732 overall · 4.4 ms/image inference · per-class scores (Glass Shatter 0.979, Tire Flat 0.934, Lamp Broken 0.871, Dent 0.61, Scratch 0.55, Crack 0.43)
