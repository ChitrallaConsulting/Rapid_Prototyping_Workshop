# Rapid Prototyping for Data Projects with AI, Loveable & Streamlit

A hands-on workshop where you'll build a working prototype of a data-driven app or dashboard in small groups — going from idea to implementation in a single session.

You'll leave with a **working prototype** and a **repeatable workflow** for AI-assisted rapid prototyping.

## What You'll Build

Using two complementary tools:
- **[Streamlit](https://streamlit.io/)** — Python-native framework for building interactive data apps and dashboards with minimal code
- **[Loveable](https://lovable.dev/)** — AI-powered no-code platform for rapid frontend prototyping and full-stack app generation

You'll pick one of three Strasbourg-themed project briefs and prototype it live.

## Workshop Timeline (2 Hours)

| Time | Phase | What Happens |
|------|-------|-------------|
| 0:00–0:15 | **Setup & Kickoff** | Intro, form groups, pick a brief |
| 0:15–0:30 | **Ideation** | Define your prototype scope using AI prompts |
| 0:30–1:15 | **Build Sprint** | Hands-on prototyping with Streamlit and/or Loveable |
| 1:15–1:40 | **Polish & Iterate** | Refine your prototype, add interactivity |
| 1:40–2:00 | **Show & Tell** | Groups demo their prototypes |

See [`guides/AGENDA.md`](guides/AGENDA.md) for the detailed facilitation guide.

## Repository Structure

```
.
├── datasets/                  # Example datasets (CSV files)
│   ├── alsace_wines.csv
│   ├── strasbourg_bikes.csv
│   └── christmas_markets.csv
├── examples/
│   ├── streamlit/             # Streamlit starter app + examples
│   │   ├── app.py            # Starter template
│   │   ├── requirements.txt
│   │   └── README.md         # Step-by-step Streamlit guide
│   └── loveable/              # Loveable prompts + workflow
│       └── README.md         # Step-by-step Loveable guide
├── guides/
│   └── AGENDA.md             # Workshop agenda & facilitation notes
├── resources/
│   └── AI_WORKFLOW.md        # AI-assisted prototyping workflow
├── templates/
│   └── PROMPTS.md            # Reusable prompt templates for LLMs
└── README.md                 # You are here
```

## Pre-Workshop Setup

Please complete these steps **before** the workshop so we can jump straight into building.

### Required

1. **Laptop with internet access**
2. **GitHub account** — [Sign up](https://github.com/signup)
3. **Access to any LLM** — No subscription needed. Free tiers work fine (output quality varies by model). Options:
   - [ChatGPT](https://chat.openai.com/) (free tier)
   - [Claude](https://claude.ai/) (free tier)
   - [Gemini](https://gemini.google.com/) (free tier)
4. **Loveable account** — [Sign up with GitHub](https://lovable.dev/) (free tier available)
5. **Streamlit account** — [Sign up with GitHub](https://streamlit.io/) (free tier available)

### For Streamlit (recommended)

If you want to run Streamlit locally:

```bash
# Clone this repo
git clone https://github.com/rchitralla/Rapid_Prototyping_Workshop.git
cd Rapid_Prototyping_Workshop

# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r examples/streamlit/requirements.txt

# Test that it works
streamlit run examples/streamlit/app.py
```

Alternatively, you can use **Streamlit Community Cloud** to run the app directly from GitHub — no local setup needed.

### Nice to Have (not required)

- **Wireframing tool** for quick sketches before building:
  - [Excalidraw](https://excalidraw.com/) (no registration needed)
  - Miro or Lucidchart (if you have accounts)

## Project Briefs

Choose one of these three Strasbourg-themed briefs.

### Brief 1: Alsace Wine Route Explorer
> **Dataset:** `datasets/alsace_wines.csv` (~500 wines)
>
> Build a wine discovery dashboard for the Alsace wine route. Filter by grape variety (Riesling, Gewurztraminer, Pinot Gris, etc.), village, producer, classification, and price range. Compare ratings across vintages and producers. Everyone in Strasbourg has an opinion about wine — now you can visualize it.

### Brief 2: Strasbourg Bike Share Analysis
> **Dataset:** `datasets/strasbourg_bikes.csv` (~1,400 records)
>
> Analyze usage patterns from Strasbourg's bike-sharing system (modeled on Velhop). Explore pickups and returns by station, neighborhood, time of day, weather, and day of week. Find peak commute hours, weather effects on ridership, and the busiest neighborhoods. Very local, very visual.

### Brief 3: Christmas Market Visitor Trends
> **Dataset:** `datasets/christmas_markets.csv` (~250 records)
>
> Prototype a tool that analyzes bike-share trip data — show popular routes, peak usage times, and trip duration distributions. Bonus: add a map view.

## Language

The workshop will be held in **English**. Small groups are free to collaborate in **French** among themselves.

## Resources

- [`guides/AGENDA.md`](guides/AGENDA.md) — Detailed workshop agenda
- [`resources/AI_WORKFLOW.md`](resources/AI_WORKFLOW.md) — AI-assisted prototyping workflow
- [`templates/PROMPTS.md`](templates/PROMPTS.md) — Reusable prompt templates
- [`examples/streamlit/README.md`](examples/streamlit/README.md) — Streamlit step-by-step guide
- [`examples/loveable/README.md`](examples/loveable/README.md) — Loveable step-by-step guide

## About

This workshop is created by **Regina Chitralla**, a freelance Data Analytics Consultant based in Strasbourg. Through [Chitralla Consulting](https://chitralla.com), she builds automated data pipelines, dashboards, and analytics solutions using Python, SQL, and BigQuery. Her background spans Nielsen, healthcare analytics, and VFX production. She writes about data and cybersecurity on [Medium](https://medium.com/@reginachitralla).
