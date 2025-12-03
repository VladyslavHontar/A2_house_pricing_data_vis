# European Housing Price Dashboard

**Team**: LH
**Members**: Sergei Litvinov (a00314281), Vladyslav Hontar (a00314279)

## What This Is

An interactive web dashboard showing housing prices across 30 European countries from 2010 to 2024. Helps students and young professionals compare housing costs when moving to a new country.

### Main Question

**Which European countries have the biggest housing price changes, and how do they compare?**

### What We Achieved

- ✅ 30 European countries
- ✅ Price trends from 2010 to 2024 (quarterly data)
- ✅ Loads in under 3 seconds
- ✅ Easy to use, no explanation needed
- ✅ Works for color-blind users
- ✅ Clear labels on everything

## Features

### 4 Interactive Charts

1. **Map**: See prices by country (red = high, green = low)
2. **Bar Chart**: Top 15 countries ranked
3. **Line Chart**: Price trends over time
4. **Scatter Plot**: Growth patterns

### Controls

- **Year Slider**: Pick time period (2010-2024)
- **Country Selector**: Choose countries to compare
- **Live Metrics**: Numbers update automatically

## Quick Start

### What You Need
- Python 3.8 or higher
- Web browser

### Install

1. Open terminal/command prompt
2. Go to project folder:
   ```bash
   cd A2_house_pricing_data_vis123
   ```
3. Create virtual environment (recommended):
   ```bash
   python -m venv venv
   ```
4. Activate it:
   ```bash
   # Windows:
   venv\Scripts\activate

   # Mac/Linux:
   source venv/bin/activate
   ```
5. Install packages:
   ```bash
   pip install -r requirements.txt
   ```

### Run

1. Start dashboard:
   ```bash
   python app.py
   ```
2. Open browser to: `http://127.0.0.1:8050`
3. Done! Dashboard loads in ~2 seconds

## How to Use

### Understanding the Numbers

- **Index = 100**: Same price as baseline year
- **Index > 100**: Prices went up
- **Index < 100**: Prices went down
- **Example**: 150 = 50% higher than baseline

### Interactive Features

**Map**
- Hover to see exact numbers
- Red = expensive, Green = cheap
- Zoom and pan to explore

**Bar Chart**
- Top 15 countries
- Easy comparison
- Updates with year slider

**Line Chart**
- Shows trends over time
- Click country names to show/hide
- Baseline at 100

**Scatter Plot**
- Bubble size = growth %
- Above line = growth
- Below line = decline (rare)

## Data Source

**Eurostat - House Price Index**
- Official EU statistics
- 30,307 records (25,000 after cleaning)
- 30 European countries
- 2010-Q1 to 2024-Q2
- Free for education/research

**Countries**: Austria, Belgium, Bulgaria, Cyprus, Czech Republic, Denmark, Estonia, Finland, France, Germany, Greece, Croatia, Hungary, Ireland, Iceland, Italy, Lithuania, Luxembourg, Latvia, Malta, Netherlands, Norway, Poland, Portugal, Romania, Sweden, Slovenia, Slovakia, Spain, Turkey, United Kingdom

## Project Files

```
A2_house_pricing_data_vis123/
├── data/
│   └── prc_hpi_q_linear_2_0.csv    # Eurostat data
├── src/                             # Source code
│   ├── callbacks/                   # Interactivity
│   ├── components/                  # UI layout
│   ├── data_processing/             # Data cleaning
│   └── visualizations/              # Charts
├── config/
│   └── settings.py                  # Settings
├── app.py                           # Main file
├── requirements.txt                 # Dependencies
└── README.md                        # This file
```

## Technology

- **Python 3.13**: Programming language
- **Dash 3.3**: Web framework
- **Plotly 6.5**: Interactive charts
- **Pandas 2.3**: Data processing

## Limitations

1. **Country averages only**: No city-specific data. Capital cities cost more than rural areas.
2. **Index, not real prices**: Shows % change, not actual euro/dollar prices.
3. **3-6 month delay**: Data is slightly old.
4. **Some gaps**: Smaller countries missing early data.
5. **No context**: Doesn't show income, jobs, interest rates.

**Use for general comparison only, not for buying decisions.**

## Accessibility

- **Color-blind safe**: RdYlGn palette (green to red)
- **Not just color**: Uses size, position, labels too
- **High contrast**: Easy to read
- **Simple language**: No jargon
- **Fast**: Loads in 2 seconds

## Future Ideas

**Data**
- Add city-level prices
- Include rental prices
- Show price-to-income ratios

**Features**
- Predict future trends
- Compare two countries side-by-side
- Export charts
- Mobile app

**Technical**
- Auto-update when new data comes
- More languages

## Ethics

**Privacy**: Only country averages, no personal info

**Bias**: EU countries have better data than non-EU

**Honest**: We clearly state all limitations

**Responsible**: Use for comparison only, get professional advice for big decisions

## Team

**Sergei Litvinov** - Data engineer, dashboard design, visualizations
**Vladyslav Hontar** - Data analysis, backend logic, documentation

## Citation

```
Litvinov, S., & Hontar, V. (2024).
European Housing Price Index Dashboard.
Data source: Eurostat.
```

## Contact

Questions? Contact:
- Sergei Litvinov (a00314281)
- Vladyslav Hontar (a00314279)

---

**Updated**: December 2024
**Version**: 1.0
