# Hospital Admissions Dashboard

An interactive dashboard built with [Dash](https://dash.plotly.com/) and [Plotly](https://plotly.com/) to explore and visualize hospital admissions data. This dashboard allows you to filter patients by medical condition, gender, age range, and date range, and displays charts (pie, bar, treemap, heatmap, box plot) and summary statistics for quick insights.

---

## Project Structure

```text
PROJECT_ROOT
├── pyproject.toml
├── README.md
├── requirements.txt
├── data
│   └── hospital_data.csv
└── src
    |── health
        ├── __init__.py (empty, used for pckg)
        ├── data.py
        ├── theme.py
        ├── layout.py
        ├── callbacks.py
        ├── app.py
        └── run.py
```
## Project Setup
To run the project, run command 'pip install -e .' and then simply call 'dashboard' command to run the application. Alternatively, you can setup the project directly, keep in mind all dependancies, call 'pip install -r requirements.txt' to install them.
All commands listed herein are supposed to be called in PROJECT_ROOT (named HeatlthDashPy, if you cloned this repo)
