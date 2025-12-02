# European Housing Price Index Dashboard

**Team**: DataViz Duo
**Members**: Sergei Litvinov (a00314281), Vladyslav Hontar (a00314279)

## Project Overview

An interactive web dashboard for exploring and comparing housing price indices across European countries. This tool helps young professionals, students, and researchers understand housing affordability trends across Europe from 2010 onwards.

### Problem Statement

Young professionals and students looking to relocate within Europe need a simple way to compare housing costs across different cities and countries. Currently, they have to check multiple websites and manually compare prices, which is time-consuming and confusing with different currencies and data formats.

### Main Question

**Which European countries have experienced the most significant housing price changes, and how do current prices compare across Europe?**

### Success Metrics

- ✅ Compare 30+ European countries and regions
- ✅ Show price trends from 2010 to present (quarterly data)
- ✅ Dashboard loads within 3 seconds
- ✅ Interactive and easy to understand without explanation
- ✅ Color-blind safe visualizations
- ✅ Accessible design with proper labels and descriptions

## Features

### Interactive Visualizations

1. **Choropleth Map**: Geographic view of Europe showing housing price index by country
2. **Bar Chart**: Top 15 countries by housing price index for easy comparison
3. **Time Series Line Chart**: Track price trends over time for selected countries
4. **Growth Scatter Plot**: Analyze price growth patterns comparing start and end periods

### Interactive Controls

- **Year Range Slider**: Filter data by time period
- **Country Selector**: Choose specific countries for detailed time series analysis
- **Dynamic Metrics**: Real-time updates of key statistics

### Key Metrics Dashboard

- Total countries analyzed
- Highest price growth country
- Lowest price growth country
- Average price index across selected period

## Data Source

**Eurostat - House Price Index (2010=100)**
- **Source**: Official EU housing statistics
- **License**: Open license for educational and research use
- **Size**: 30,307 rows (quarterly data from 2010-2024)
- **Coverage**: 30+ European countries
- **Frequency**: Quarterly updates
- **Baseline**: 2010 = 100 (all prices are indexed relative to 2010 values)

### Data Dictionary

| Column | Description |
|--------|-------------|
| `country_code` | ISO 3166-1 alpha-2 country code (e.g., DE, FR, IT) |
| `country_name` | Full country name |
| `time_period` | Year and quarter (e.g., 2023-Q1) |
| `price_index` | Housing price index value (2010=100) |
| `year` | Extracted year from time period |
| `quarter` | Extracted quarter (Q1, Q2, Q3, Q4) |
| `date` | Parsed datetime for time series analysis |

### Countries Included

Austria (AT), Belgium (BE), Bulgaria (BG), Switzerland (CH), Cyprus (CY), Czech Republic (CZ), Germany (DE), Denmark (DK), Estonia (EE), Spain (ES), Finland (FI), France (FR), Croatia (HR), Hungary (HU), Ireland (IE), Iceland (IS), Italy (IT), Lithuania (LT), Luxembourg (LU), Latvia (LV), Malta (MT), Netherlands (NL), Norway (NO), Poland (PL), Portugal (PT), Romania (RO), Sweden (SE), Slovenia (SI), Slovakia (SK), Turkey (TR), United Kingdom (UK)

## Project Structure

```
A2_house_pricing_data_vis/
│
├── data/
│   └── prc_hpi_q_linear_2_0.csv      # Raw Eurostat housing price data
│
├── docs/
│   ├── Assignment 2 — Team Data Analytics Visualization Project.pdf
│   └── A2_DataVizDuo_HousingPrice_proposal.pdf
│
├── dashboard.py                        # Main dashboard application
├── requirements.txt                    # Python dependencies
├── README.md                          # This file
└── main.py                            # Entry point (if needed)
```

## Environment Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone or download this repository**

2. **Navigate to the project directory**
   ```bash
   cd A2_house_pricing_data_vis
   ```

3. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv

   # On Windows:
   venv\Scripts\activate

   # On macOS/Linux:
   source venv/bin/activate
   ```

4. **Install required packages**
   ```bash
   pip install -r requirements.txt
   ```

## How to Run

### Quick Start

1. **Ensure you are in the project directory with the virtual environment activated**

2. **Run the dashboard**
   ```bash
   python dashboard.py
   ```

3. **Open your web browser and navigate to**
   ```
   http://127.0.0.1:8050
   ```

4. **The dashboard should load within 3 seconds**

### Expected Output

When you run the dashboard, you should see:
```
Dash is running on http://127.0.0.1:8050/

 * Serving Flask app 'dashboard'
 * Debug mode: on
```

## How to Use the Dashboard

### Navigation Guide

1. **Year Range Slider**
   - Located at the top of the dashboard
   - Drag handles to select date range
   - All charts update automatically

2. **Country Selector**
   - Multi-select dropdown
   - Choose countries for time series comparison
   - Default: Germany, France, Italy, Spain, United Kingdom

3. **Choropleth Map**
   - Hover over countries to see exact values
   - Color intensity indicates price level
   - Red = higher prices, Green = lower prices

4. **Bar Chart**
   - Shows top 15 countries by price index
   - Horizontal bars for easy reading
   - Updated based on selected year range

5. **Time Series Chart**
   - Displays trends for selected countries
   - Hover for exact values
   - Baseline at 100 (2010 reference)
   - Click legend items to show/hide countries

6. **Growth Scatter Plot**
   - X-axis: Starting price index
   - Y-axis: Ending price index
   - Bubble size: Growth percentage
   - Diagonal line: No growth reference

### Interpretation Guide

- **Price Index = 100**: Housing prices same as 2010
- **Price Index > 100**: Prices increased since 2010
- **Price Index < 100**: Prices decreased since 2010
- **Example**: Index of 150 means prices are 50% higher than 2010

## Accessibility Features

### Color-Blind Safe Design

- **ColorBrewer palettes**: RdYlGn, Viridis
- **High contrast**: All text meets WCAG AA standards
- **Pattern differentiation**: Size, shape, and position used alongside color

### Usability Features

- **Clear labels**: All axes labeled with units
- **Tooltips**: Hover information for all data points
- **Responsive design**: Works on different screen sizes
- **Fast loading**: Optimized for < 3 second load time

### Visual Design Principles

- Sans-serif fonts for readability
- Consistent color scheme throughout
- White space for visual clarity
- Minimal cognitive load

## Technical Implementation

### Technologies Used

- **Python 3.8+**: Core programming language
- **Dash 2.14**: Web framework for building the dashboard
- **Plotly 5.18**: Interactive visualization library
- **Pandas 2.1**: Data manipulation and analysis
- **Dash Bootstrap Components**: UI styling and layout

### Data Processing Pipeline

1. **Load**: Read CSV data from Eurostat
2. **Clean**: Remove missing values and aggregate regions
3. **Transform**: Parse dates, extract year/quarter
4. **Filter**: Apply user-selected date ranges
5. **Aggregate**: Calculate metrics and growth rates
6. **Visualize**: Render interactive charts

### Performance Optimizations

- In-memory data loading (one-time read)
- Efficient pandas operations
- Minimal callback chains
- Optimized plot rendering

## Reproducibility

### Deterministic Execution

- Data is read from static CSV file
- No random seeds required (no stochastic processes)
- Same input always produces same output

### Data Provenance

- **Source**: Eurostat (European Commission)
- **Download Date**: November 2024
- **License**: Open for educational/research use
- **URL**: https://ec.europa.eu/eurostat

### Manual Steps

No manual steps required. The entire pipeline is automated.

## Limitations & Future Work

### Current Limitations

1. **Data Granularity**: Country-level only (no city/neighborhood data)
2. **Update Frequency**: Quarterly (3-6 month lag)
3. **Historical Depth**: Limited to 2010 onwards
4. **Missing Data**: Some smaller countries have incomplete records
5. **Index Only**: Shows relative change, not absolute prices

### Future Enhancements

- Add city-level data from additional sources
- Include affordability metrics (price-to-income ratio)
- Predictive modeling for future price trends
- Comparison with rental price indices
- Integration with income and employment data
- Mobile app version
- Export functionality for reports

## Ethics & Bias Considerations

### Data Quality

- **Official Source**: Eurostat provides verified, standardized data
- **Sampling**: Census-level data from national statistical offices
- **Missing Data**: Documented and not imputed

### Potential Biases

- **Geographic**: Better coverage for EU members vs. non-EU countries
- **Temporal**: More recent data is more complete
- **Representativeness**: Averages may not reflect local variations

### Responsible Use

- Data should be used for comparative analysis only
- Not suitable for individual purchasing decisions
- Users should consult local real estate professionals
- Privacy: No personal or identifiable information included

## Team Contributions

### Sergei Litvinov (Data Engineer)
- Downloaded and prepared Eurostat dataset
- Built data cleaning and transformation pipeline
- Designed dashboard frontend layout and styling
- Implemented choropleth map and bar chart visualizations
- Testing and performance optimization

### Vladyslav Hontar (Analyst/Modeler)
- Conducted exploratory data analysis
- Calculated growth metrics and statistical summaries
- Implemented dashboard backend logic and callbacks
- Created time series and scatter plot visualizations
- Git repository setup and management
- Documentation (README, code comments)

### Shared Responsibilities
- Dashboard interactivity and filters
- Color scheme and accessibility features
- Testing and bug fixes
- Presentation preparation

## License & Citation

### Data License
The Eurostat data is available under the European Commission's open data policy for educational and research purposes.

### Code License
This project is created for academic purposes as part of Assignment 2.

### Citation
If you use this work, please cite:
```
Litvinov, S., & Hontar, V. (2024). European Housing Price Index Dashboard.
Assignment 2 - Team Data Analytics Visualization Project.
```

## Support & Contact

For questions or issues:
- **Team**: DataViz Duo
- **Members**: Sergei Litvinov (a00314281), Vladyslav Hontar (a00314279)
- **Course**: Data Analytics & Visualization

## Acknowledgments

- **Eurostat**: For providing open, high-quality housing data
- **Plotly/Dash**: For excellent visualization tools
- **Course Instructors**: For guidance and feedback

---

**Last Updated**: December 2024
**Version**: 1.0
**Status**: Production Ready
