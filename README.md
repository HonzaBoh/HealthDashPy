# Hospital Admissions Dashboard

An interactive dashboard built with [Dash](https://dash.plotly.com/) and [Plotly](https://plotly.com/) to explore and visualize hospital admissions data. This dashboard allows you to filter patients by medical condition, gender, age range, and date range, and displays charts (pie, bar, treemap, heatmap, box plot) and summary statistics for quick insights.

Dataset is available as [Healthcare dataset](https://www.kaggle.com/datasets/prasad22/healthcare-dataset), it is an educational dataset for which I am thankful to build this simple tool for.
---

## Project Structure

```text
HealthDashPy (project root)
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
To install everything required, use
```text
pip install -e .
```
which will check and possibly install dependancies from requiremets.txt file.
Project has an entry point, using 
```text
dashboard
```
will initialize the application. You can open it in your web browser afterwards.

Alternatively, if you don't want to use the entry point, you can init the application, then you can run this as a project:

```text
python -m src.health.run
```
Don't forget to run all these commands in the project root, meaning the HealthDashPy (or other name for Project root).
