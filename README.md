# CARPER FYP Posters — 6 Design Variants

## Original-style completions (match your official FAST poster)
- `POSTER_4_OFFICIAL_FAITHFUL.html` — Faithful completion · same dark teal/navy theme, blue triangles, FAST-NU logo, hero car damage-detection viz, fills in System Architecture / Working Pipeline / Results
- `POSTER_5_OFFICIAL_ENHANCED.html` — Enhanced layout · adds circuit-grid background, top-band with hero+team+KPIs, feature icon row, animated scanning sweep
- `POSTER_6_OFFICIAL_PREMIUM.html` — Premium · larger hero with bounding boxes, FYP ribbon badge, damage-class strip, data-model row, diamond-shaped pipeline nodes

## Earlier reference-template variants
- `POSTER_1_INTELLEXA_STYLE.html` — Dark cream/beige, layered horizontal pipeline (INTELLEXA inspired)
- `POSTER_2_IWAF_STYLE.html` — Orange/teal with detailed system architecture diagram (iWAF inspired)
- `POSTER_3_TALENTMATCH_STYLE.html` — Purple gradient with 3-layer architecture stack (TalentMatch AI inspired)

## How to view & export

1. Open any `.html` file in **Chrome** (recommended) or Edge.
2. Each poster is sized at **1200 × 1800 px** (2:3 ratio, matches your original FAST poster).
3. To export as image / PDF at print resolution:
   - **Print to PDF**: Ctrl+P → Destination = "Save as PDF" → Paper = Custom → set 33.1 × 46.8 in (A0) → Margins = None → Background graphics = On.
   - **PNG export**: Right-click the poster → "Capture full page screenshot" (Chrome DevTools → Cmd/Ctrl+Shift+P → "Capture full size screenshot").
   - **High-res PNG**: open DevTools, set device toolbar to 4081 × 6122, then capture full-size screenshot. This matches your original poster pixel dimensions.

## Content covered (all 3 posters)
- Project: CARPER — The Car Problem Solver
- University: FAST-NUCES
- Team: Syed Wali Mohsin Naqvi (22K-4550, Lead), Syed Ghalib Hussain Zaidi (22K-4536), Syed Azhaan Ali (22K-4140)
- Supervisor: Mr. Shoaib Raza
- Detection: YOLOv8n on CarDD (4,000 images, 6 damage classes)
- Cost estimation: Gradient Boosting (vs LR / RF / Extra Trees)
- Recommendation: Sentence-BERT semantic part search
- Stack: Next.js 15 · NestJS 11 · PostgreSQL · Prisma · FastAPI · Cloudinary · ONNX-Web
- Results: mAP@0.5 = 0.732 · 4.4 ms inference · per-class scores
- System architecture diagram (3-tier with AI services)
- Working pipeline (capture → preprocess → detect → severity → estimate → recommend → report)

## Customization
- Colors: top of each `<style>` block (CSS variables)
- Dimensions: change `.poster { width / height }` in the CSS
- Content: edit the relevant section directly in the HTML
