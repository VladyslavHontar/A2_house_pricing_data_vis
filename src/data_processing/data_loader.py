import pandas as pd
from config import settings

def load_and_clean_data():
    df = pd.read_csv(settings.DATA_PATH)

    df_clean = df[['geo', 'Geopolitical entity (reporting)', 'TIME_PERIOD', 'OBS_VALUE']].copy()
    df_clean.columns = ['country_code', 'country_name', 'time_period', 'price_index']

    df_clean = df_clean.dropna(subset=['price_index'])

    df_clean = df_clean[~df_clean['country_code'].isin(settings.EXCLUDE_COUNTRY_CODES)]

    df_clean['year'] = df_clean['time_period'].str[:4].astype(int)
    df_clean['quarter'] = df_clean['time_period'].str[-2:]

    df_clean['date'] = pd.to_datetime(
        df_clean['year'].astype(str) + '-' +
        df_clean['quarter'].map(settings.QUARTER_TO_MONTH) + '-01'
    )

    df_clean = df_clean[
        (df_clean['price_index'] >= settings.PRICE_INDEX_MIN) &
        (df_clean['price_index'] <= settings.PRICE_INDEX_MAX)
    ]
    df_clean = df_clean[df_clean['year'] <= settings.MAX_YEAR]
    df_clean = df_clean.sort_values(['country_name', 'date'])
    df_clean = df_clean.drop_duplicates(subset=['country_name', 'time_period'], keep='first')

    df_clean['country_name'] = df_clean['country_name'].replace(settings.COUNTRY_NAME_FIXES)

    return df_clean

def get_countries(df):
    return sorted(df['country_name'].unique())

def get_years(df):
    return sorted(df['year'].unique())

def rebase_price_index(df, base_year):
    df_rebased = df.copy()

    for country in df_rebased['country_name'].unique():
        country_data = df_rebased[df_rebased['country_name'] == country].copy()

        base_year_data = country_data[country_data['year'] == base_year]

        if len(base_year_data) == 0:
            earliest_data = country_data.sort_values('date').iloc[0]
            base_value = earliest_data['price_index']
        else:
            base_value = base_year_data.iloc[0]['price_index']

        if base_value > 0:
            df_rebased.loc[df_rebased['country_name'] == country, 'price_index'] = (
                df_rebased.loc[df_rebased['country_name'] == country, 'price_index'] / base_value * 100
            )

    return df_rebased
