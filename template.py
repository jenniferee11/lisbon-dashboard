import streamlit as st
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import folium
from streamlit_folium import st_folium
import plotly.express as px

# Page configuration
st.set_page_config(page_title="Lisbon Road Accidents", layout="wide")

# Title and description
st.title("Lisbon Road Accidents – Interactive Dashboard")
st.markdown(
    "Explore and analyze road accident data from Lisbon."
)

# Educational use notice
st.markdown(
    """
> ⚠️ **Important Notice**  
> This dataset contains real road accident records from Portugal in 2023, provided by **ANSR (National Road Safety Authority)**.  
> It is intended **exclusively for educational use within this course**. Redistribution or use for any other purpose is strictly prohibited.
"""
)

# Load dataset
df = pd.read_csv("data/Road_Accidents_Lisbon.csv")
df["severity"] = "Minor"
df.loc[df["serious_injuries_30d"] > 0, "severity"] = "Serious"
df.loc[df["fatalities_30d"] > 0, "severity"] = "Fatal"

# Sidebar filter by weekday
st.sidebar.header("Filter Options")
weekday_options = df["weekday"].dropna().unique()
selected_weekdays = st.sidebar.multiselect("Filter by Weekday", weekday_options, default=weekday_options)
severity_options = ["Fatal", "Serious", "Minor"]
selected_severity = st.sidebar.multiselect("Filter by Severity", severity_options, default=severity_options)
hour_range = st.sidebar.slider("Filter by Hour", 0, 23, (0, 23))
# Filter dataset
df_filtered = df[df["weekday"].isin(selected_weekdays) & df["severity"].isin(selected_severity) & df["hour"].between(hour_range[0], hour_range[1])]
# Convert to GeoDataFrame
gdf = gpd.GeoDataFrame(
    df_filtered,
    geometry=[Point(xy) for xy in zip(df_filtered["longitude"], df_filtered["latitude"])],
    crs="EPSG:4326"
) 

# Center map on Lisbon
center = [gdf["latitude"].mean(), gdf["longitude"].mean()]
m = folium.Map(location=center, zoom_start=12, tiles="CartoDB Positron")

# Add accident markers
severity_colors = {"Fatal": "red", "Serious": "orange", "Minor": "blue"}

for _, row in gdf.iterrows():
    color = severity_colors.get(row["severity"], "gray")
    folium.CircleMarker(
        location=[row["latitude"], row["longitude"]],
        radius=5,
        color=color,
        fill=True,
        fill_opacity=0.6,
        popup=f"ID: {row['id']}<br>Weekday: {row['weekday']}<br>Severity: {row['severity']}<br>Fatalities: {row['fatalities_30d']}"
    ).add_to(m)

# Show map
st.subheader("Accident Map")
st_data = st_folium(m, width=800, height=600)

st.subheader("Accidents by Hour of Day")
hourly = df_filtered.groupby("hour").size().reset_index(name="count")
fig = px.bar(hourly, x="hour", y="count", labels={"hour": "Hour of Day", "count": "Accidents"})
st.plotly_chart(fig, use_container_width=True)

st.subheader("Accidents by Weekday")
weekday_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
weekly = df_filtered["weekday"].value_counts().reindex(weekday_order).reset_index()
weekly.columns = ["weekday", "count"]
fig2 = px.bar(weekly, x="weekday", y="count", labels={"weekday": "Day", "count": "Accidents"})
st.plotly_chart(fig2, use_container_width=True)

st.subheader("Accidents by Month")
month_order = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
monthly = df_filtered["month"].value_counts().reindex(month_order).reset_index()
monthly.columns = ["month", "count"]
fig3 = px.line(monthly, x="month", y="count", markers=True, labels={"month": "Month", "count": "Accidents"})
st.plotly_chart(fig3, use_container_width=True)





st.markdown("---")
st.subheader("About this Dashboard")
st.markdown("""
Starting from a basic Streamlit template with a simple map, I extended it into a fully interactive dashboard for exploring Lisbon's 2023 road accident data. The dashboard includes three sidebar filters — weekday, severity, and hour of day — allowing users to narrow down accidents by any combination of these dimensions. The map displays accidents as color-coded markers (red for fatal, orange for serious, blue for minor), and three charts show accident patterns by hour, weekday, and month.

**Key insights:** The most striking finding is that accidents are distributed across the entire city — there is no single safe area in Lisbon. Risk is everywhere. The hourly chart clearly shows a spike during the evening rush hour (16:00–19:00), suggesting that commuter traffic is the main driver of accidents. Interestingly, weekends show significantly fewer accidents than weekdays — which raises a broader question about car dependency: if fewer people drive on weekends, the data suggests the city could function with less car traffic overall.

**What I learned:** The biggest challenges were setting up the deployment pipeline and understanding how filters connect to the underlying data. Building this taught me how geospatial data can tell stories that raw numbers alone cannot.
""")
