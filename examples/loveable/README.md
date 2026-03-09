# Loveable Step-by-Step Guide

A complete guide to building your prototype with Loveable during the workshop.

## What is Loveable?

Loveable is an AI-powered platform that generates full-stack web applications from natural language descriptions. You describe what you want — Loveable builds the frontend, connects data, and deploys it. No coding required.

## Quick Start

1. Go to [lovable.dev](https://lovable.dev/) and sign in with GitHub
2. Click **New Project**
3. Describe your app in the prompt box
4. Loveable generates a working app you can customize

## Step 1: Write Your Initial Prompt

The quality of your prompt determines the quality of your prototype. Be specific about:
- **What** the app does
- **Who** it's for
- **What data** it displays
- **What interactions** users should have

### Example Prompts by Brief

**Brief 1 — Startup Funding Explorer:**
> Build a dashboard for exploring startup funding data. It should have:
> - A sidebar with filters for industry, funding stage, and country
> - A summary row showing total companies, total funding, and average round size
> - A bar chart showing funding by industry
> - A timeline scatter plot showing funding rounds over time
> - A data table at the bottom with search and sort
> Use a clean, professional design with a blue/gray color scheme.

**Brief 2 — Coffee Survey:**
> Create an interactive survey results viewer for coffee preferences. Include:
> - Filter by age group and country in the sidebar
> - Pie chart showing favorite coffee types
> - Bar chart of brewing methods
> - A comparison section showing preferences by demographic
> - Summary cards showing total respondents and most popular choice
> Use a warm color scheme with coffee-related browns and creams.

**Brief 3 — City Bike-Share:**
> Build a bike-share analytics dashboard. It should show:
> - Key metrics: total trips, average duration, most popular station
> - A bar chart of trips by time of day
> - A chart comparing electric vs classic bike usage
> - A table of the most popular routes
> Use a modern, green-themed design.

## Step 2: Refine with Follow-Up Prompts

After Loveable generates the first version, iterate:

- "Move the filters to the left sidebar"
- "Make the chart colors consistent across all visualizations"
- "Add a download button for the filtered data"
- "Change the header to say 'Startup Funding Explorer'"
- "Make it responsive for mobile"

## Step 3: Connect Your Data

You can add data to Loveable in several ways:

### Option A: Paste CSV Data Directly
> "Replace the sample data with this CSV data: [paste your CSV]"

### Option B: Use Supabase (Built-in)
Loveable has built-in Supabase integration for persistent data:
1. Click the **Supabase** icon in the Loveable editor
2. Connect your Supabase project (or let Loveable create one)
3. Ask Loveable: "Store the data in Supabase and fetch it on load"

### Option C: Static JSON
> "Use this data as the app's dataset: [paste JSON array]"

## Step 4: Customize the Design

Prompt Loveable to adjust the look:

- "Use a dark theme with neon accents"
- "Make it look like a professional analytics dashboard"
- "Add a logo at the top — use a placeholder image for now"
- "Increase the font size and add more spacing"

## Step 5: Publish

1. Click **Share** in the top-right of the Loveable editor
2. Toggle the **Public** switch
3. Copy the shareable URL
4. (Optional) Connect a custom domain

## Tips for Better Results

| Do | Don't |
|----|-------|
| Describe layout and structure | Ask for vague "make it better" |
| Specify color schemes and themes | Assume Loveable knows your preferences |
| Iterate one change at a time | Ask for 10 changes in one prompt |
| Reference specific components | Use jargon without context |
| Paste real data early | Wait until the end to add data |

## Loveable + Streamlit: When to Use Which

| Scenario | Use Loveable | Use Streamlit |
|----------|-------------|---------------|
| Quick visual prototype | Yes | — |
| Data-heavy analytics | — | Yes |
| Custom Python logic | — | Yes |
| Beautiful UI with no code | Yes | — |
| Share with stakeholders | Yes | Yes |
| Complex data transformations | — | Yes |
| Rapid iteration on design | Yes | — |

**Workshop tip:** Start with Loveable to prototype the UI/UX, then switch to Streamlit if you need more data processing power. Or use both — Loveable for the frontend concept, Streamlit for the functional prototype.

## Reference

- [Loveable Documentation](https://docs.lovable.dev/)
- [Loveable YouTube Tutorials](https://www.youtube.com/@lovabledev)
