DATA_PATH = 'data/prc_hpi_q_linear_2_0.csv'

PRICE_INDEX_MIN = 10
PRICE_INDEX_MAX = 500
MAX_YEAR = 2024

EXCLUDE_COUNTRY_CODES = ['EA', 'EA19', 'EA20', 'EU', 'EU27_2020', 'EU28']

COUNTRY_NAME_FIXES = {
    'Türkiye': 'Turkey',
    'Türkiye': 'Turkey',
    'Czechia': 'Czech Republic',
}

QUARTER_TO_MONTH = {'Q1': '01', 'Q2': '04', 'Q3': '07', 'Q4': '10'}

COLORBLIND_SAFE_PALETTE = [
    '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
    '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf'
]

APP_TITLE = "European Housing Price Index Dashboard"
HOST = '127.0.0.1'
PORT = 8050
DEBUG = True
