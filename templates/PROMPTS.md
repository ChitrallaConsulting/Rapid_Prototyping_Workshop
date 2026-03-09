# Prompt Templates

Copy-paste these templates into your LLM. Replace the `[bracketed]` sections with your specifics.

---

## Starting a New Streamlit App

```
I want to build a Streamlit data app.

My dataset is a CSV with these columns:
[paste column names and types]

Here are the first 3 rows:
[paste sample rows]

Please generate a complete Streamlit app that:
1. Loads the CSV file from the path "[path to csv]"
2. Shows key metrics at the top (total rows, average of [column], etc.)
3. Has sidebar filters for [column1] and [column2]
4. Shows a [bar/line/scatter] chart of [metric] by [category]
5. Shows the filtered data table at the bottom

Use pandas and plotly.express. Keep the code clean and well-organized.
```

---

## Starting a Loveable Project

```
Build a web-based data dashboard with the following specifications:

PURPOSE: [what the dashboard is for]
AUDIENCE: [who will use it]

LAYOUT:
- Left sidebar with filters
- Top row with 3 summary metric cards
- Main area with 2 charts side by side
- Bottom section with a data table

FILTERS:
- Dropdown for [category column]
- Multi-select for [tags/labels column]
- Range slider for [numeric column]

CHARTS:
- Bar chart showing [metric] grouped by [category]
- [Line/Scatter/Pie] chart showing [other visualization]

DESIGN:
- Color scheme: [blue/green/dark/warm]
- Clean, modern, professional look
- Responsive layout

DATA: Use this sample data:
[paste 5-10 rows of your CSV or JSON]
```

---

## Adding a Feature

```
Here is my current Streamlit app code:

[paste your full app.py]

Please add the following feature:
[describe the feature]

Requirements:
- Don't remove any existing functionality
- Keep the same coding style
- Add the new feature in a logical place in the layout
```

---

## Debugging

```
I'm building a Streamlit app and getting this error:

ERROR:
[paste the full error message/traceback]

MY CODE:
[paste the relevant section of code]

MY DATA (first 3 rows):
[paste sample data]

Please fix the error and explain what went wrong.
```

---

## Generating a Chart

```
I have a pandas DataFrame `df` with these columns:
[list columns with types]

Generate a Plotly Express chart that shows:
- X axis: [column]
- Y axis: [column]
- Color by: [column]
- Chart type: [bar/line/scatter/pie/histogram]

Include:
- A descriptive title
- Clean axis labels
- A color scheme that uses [color preference]

Return the code as a Streamlit-compatible snippet using st.plotly_chart().
```

---

## Wireframe to Loveable Prompt

```
I have this wireframe sketch of a dashboard:

[describe each section of your wireframe]
- Top: [what's at the top]
- Left: [sidebar contents]
- Center: [main content area]
- Bottom: [footer/table area]

Convert this into a detailed Loveable prompt that will generate
a matching web app. Include specific instructions for:
- Layout and spacing
- Colors and typography
- Interactive elements
- Sample data structure
```

---

## Data Exploration

```
I have a CSV dataset. Here are the first 5 rows:

[paste first 5 rows]

And here are the column names and types:
[paste column info]

Please suggest:
1. Three interesting questions this data could answer
2. The best chart types for each question
3. Which columns to use as filters
4. A recommended layout for a dashboard
```

---

## Quick Polish

```
Here is my Streamlit app code:

[paste code]

Please improve it by:
1. Adding a proper page title and icon
2. Organizing the layout with columns and/or tabs
3. Adding better chart titles and axis labels
4. Making the sidebar filters more user-friendly
5. Adding a brief description under the title

Don't add new features — just polish what's there.
```
