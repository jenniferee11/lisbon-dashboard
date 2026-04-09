# Capstone Project – Lisbon Road Accident Dashboard

Welcome to the final project of the **Geospatial Data Science for Urban Mobility** course. In this capstone challenge, you’ll apply everything you’ve learned—data exploration, geospatial visualization, clustering, and dashboards—to build a real-world analytical tool.

Your task is to extend the provided Streamlit template into a full dashboard that helps uncover accident patterns and supports mobility decision-making.

## 🎯 Objective

Using Lisbon’s 2023 road accident data, your goal is to create an interactive dashboard with filters, maps, and visual summaries that highlight accident patterns by hour, weekday, severity, or any other dimension you choose to explore.

This simulation mirrors how transport agencies and municipalities explore spatial datasets to identify risks and improve road safety.

## 📁 Folder Contents

- `template.py`: A working Streamlit dashboard starter with an accident map and basic filters.
- `data/Road_Accidents_Lisbon.csv`: The main dataset containing real accident data from Lisbon (2023).

## 🚀 Getting Started

1. Install the required libraries

```
pip install streamlit folium streamlit-folium geopandas shapely pandas
````

2. Run the app locally:

```
streamlit run template.py (or your_file.py)
```

You can modify this file or create your own variation in the same folder.

3. Explore the code: The template uses `Streamlit`, `Folium`, and `GeoPandas`. You can add charts, filters, layers, and analyses.

## ✅ What You Should Add

* Additional filters (e.g., severity, hour)
* Visual summaries (e.g., charts with Seaborn or Plotly)
* Insightful explanations or summaries
* Clean layout and labels to guide non-technical users
* Bonus: incorporate OSM data or clustering

## 📦 Submission

1. Deploy your final version using **Streamlit Cloud**
   👉 [Deployment guide](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app)

2. Submit the public app link and optionally a short written or video explanation.

---

> ⚠️ **Important Notice**
> This dataset contains real road accident records from Portugal in 2023, provided by **ANSR (National Road Safety Authority)**.
> It is intended **exclusively for educational use within this course**. Redistribution or use for any other purpose is strictly prohibited.

---

## 📚 References

* [Streamlit Documentation](https://docs.streamlit.io/)
* [Folium Documentation](https://python-visualization.github.io/folium/)
* [GeoPandas Documentation](https://geopandas.org/)
* [Shapely Documentation](https://shapely.readthedocs.io/en/stable/)
* *Geospatial Data Science Essentials* by Milan Janosov
* [Working with Geospatial Data in Python](https://www.datacamp.com/courses/working-with-geospatial-data-in-python) – DataCamp
