# Quick Start Guide

## European Housing Price Index Dashboard

Welcome! This guide will help you get the dashboard running in just a few minutes.

## Prerequisites

- Python 3.8 or higher (you have Python 3.13 ✓)
- All dependencies are already installed ✓

## Running the Dashboard

### Option 1: Using the Batch File (Windows)

1. Double-click `run_dashboard.bat`
2. Wait for the dashboard to start (about 5-10 seconds)
3. Open your web browser to: **http://127.0.0.1:8050**

### Option 2: Using Command Line

```bash
cd C:\Users\Administrator\PycharmProjects\A2_house_pricing_data_vis
python dashboard.py
```

Then open your browser to: **http://127.0.0.1:8050**

## What to Expect

When you run the dashboard, you'll see:

```
Dash is running on http://127.0.0.1:8050/

 * Serving Flask app 'dashboard'
 * Debug mode: on
```

This means it's working! Keep the terminal window open while using the dashboard.

## Dashboard Features

### 1. Interactive Map
- Shows housing price index across Europe
- Color-coded: Red = higher prices, Green = lower prices
- Hover over countries for exact values

### 2. Filters
- **Year Range Slider**: Select time period to analyze
- **Country Selector**: Choose countries for detailed comparison

### 3. Visualizations
- **Choropleth Map**: Geographic overview of Europe
- **Bar Chart**: Top 15 countries by price index
- **Time Series Chart**: Price trends over time for selected countries
- **Growth Scatter Plot**: Analyze price growth patterns

### 4. Key Metrics
- Number of countries analyzed
- Highest and lowest price growth
- Average price index

## Understanding the Data

- **Baseline (2010 = 100)**: All prices are compared to 2010
- **Index 150**: Prices are 50% higher than in 2010
- **Index 100**: Prices same as 2010
- **Index 80**: Prices 20% lower than 2010

## Navigation Tips

1. **Zoom the Map**: Use scroll wheel or zoom buttons
2. **Select Countries**: Click dropdown and choose multiple countries
3. **Adjust Time Range**: Drag the year slider handles
4. **View Details**: Hover over any chart element for exact values

## Stopping the Dashboard

Press `Ctrl + C` in the terminal window to stop the server.

## Troubleshooting

### Dashboard won't start?

Check if port 8050 is already in use:
```bash
netstat -ano | findstr :8050
```

If needed, change the port in `dashboard.py` line 443:
```python
app.run(debug=True, host='127.0.0.1', port=8051)  # Changed from 8050
```

### Browser shows "Can't reach this page"?

1. Make sure the dashboard is running (check terminal)
2. Try refreshing the page (F5)
3. Check the URL is exactly: http://127.0.0.1:8050

### Data not loading?

Make sure the CSV file exists:
```bash
dir data\prc_hpi_q_linear_2_0.csv
```

## Performance

- **Load Time**: Dashboard should load in under 3 seconds
- **Data Points**: 30,000+ rows of data analyzed
- **Countries**: 30+ European countries
- **Time Range**: 2010 to present (quarterly)

## Next Steps

1. **Explore the Data**: Try different country combinations
2. **Find Patterns**: Look for trends and anomalies
3. **Export Screenshots**: Use browser tools to save visualizations
4. **Share Insights**: Present findings using the dashboard

## Need Help?

- Check the full **README.md** for detailed documentation
- Review **data/README.md** for data specifications
- See the assignment PDFs in **docs/** folder

## Key Files

- `dashboard.py` - Main dashboard application
- `requirements.txt` - Python dependencies
- `data/prc_hpi_q_linear_2_0.csv` - Housing price data
- `README.md` - Complete documentation

## Team

**DataViz Duo**
- Sergei Litvinov (a00314281)
- Vladyslav Hontar (a00314279)

---

**Ready to start?** Just run `python dashboard.py` and open **http://127.0.0.1:8050** in your browser!
