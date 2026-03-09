# AI-Assisted Prototyping Workflow

A repeatable workflow for using LLMs to accelerate your data prototyping.

## The Workflow

```
1. DEFINE  →  2. GENERATE  →  3. ITERATE  →  4. REFINE  →  5. SHIP
```

### 1. Define (5 min)

Tell your LLM what you're building. Be specific.

**Template:**
> I'm building a [type of app] that helps [who] do [what].
> The data has these columns: [list columns].
> The key features are: [list 2-3 features].
> I'm using [Streamlit / Loveable / both].

**Example:**
> I'm building a dashboard that helps analysts explore startup funding data.
> The data has columns: company_name, industry, funding_stage, amount_usd, date, city, country.
> The key features are: filter by industry and stage, show a funding timeline chart, display summary metrics.
> I'm using Streamlit with Plotly.

### 2. Generate (10 min)

Ask your LLM to generate the first version.

**For Streamlit:**
> Generate a complete Streamlit app with the features I described. Use pandas for data handling and plotly.express for charts. Include sidebar filters and a clean layout.

**For Loveable:**
> Write me a detailed prompt I can paste into Loveable to generate this app. Include layout, color scheme, and data structure details.

### 3. Iterate (20 min)

Fix issues and add features one at a time.

**Debugging pattern:**
> I'm getting this error: [paste error]
> Here's my code: [paste relevant section]
> How do I fix it?

**Feature addition pattern:**
> My app currently does [X]. I want to add [Y].
> Here's my current code: [paste code]
> Add this feature without breaking existing functionality.

### 4. Refine (10 min)

Polish the output.

> Review my app code and suggest improvements for:
> - Better chart formatting
> - More intuitive filter layout
> - Clearer labels and titles

### 5. Ship

Deploy and share.

> How do I deploy this Streamlit app to Streamlit Community Cloud?
> What files do I need and what's the step-by-step process?

## Tips for Working with LLMs

### Do
- **Paste your data schema** — column names, types, sample rows
- **Paste error messages in full** — including the traceback
- **Be specific about changes** — "change the bar chart to a line chart" not "make it better"
- **Iterate in small steps** — one feature or fix at a time
- **Share your current code** — so the LLM has full context

### Don't
- Ask for everything at once (the output will be generic)
- Assume the generated code works without testing
- Ignore errors and paste more prompts on top
- Forget to save working versions before making big changes

## Quick Reference: What to Ask Your LLM

| I need to... | Ask this... |
|--------------|-------------|
| Start a new app | "Generate a Streamlit app for [dataset] with [features]" |
| Add a filter | "Add a sidebar filter for [column] to my Streamlit app" |
| Add a chart | "Add a [chart type] showing [metric] by [category] using Plotly" |
| Fix an error | "Fix this error: [error]. Here's my code: [code]" |
| Improve layout | "Reorganize my app to use columns and tabs for better layout" |
| Add download | "Add a button to download the filtered data as CSV" |
| Deploy | "How do I deploy this to Streamlit Cloud?" |
| Style | "Change the color scheme to [theme] and improve spacing" |
