from dash import Input, Output, callback
from src.data_processing import data_loader

def register_metrics_callback(df):
    @callback(
        [Output('metric-countries', 'children'),
         Output('metric-highest', 'children'),
         Output('metric-lowest', 'children'),
         Output('metric-avg', 'children')],
        [Input('year-slider', 'value'),
         Input('country-dropdown', 'value')]
    )
    def update_metrics(year_range, selected_countries):
        filtered_df = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

        if selected_countries and len(selected_countries) > 0:
            filtered_df = filtered_df[filtered_df['country_name'].isin(selected_countries)]

        filtered_df = data_loader.rebase_price_index(filtered_df, year_range[0])

        latest_data = filtered_df.sort_values('date').groupby('country_name').last()

        num_countries = len(latest_data)

        if len(latest_data) > 0:
            highest_country = latest_data['price_index'].idxmax()
            highest_value = latest_data['price_index'].max()

            lowest_country = latest_data['price_index'].idxmin()
            lowest_value = latest_data['price_index'].min()

            avg_value = latest_data['price_index'].mean()

            return (
                str(num_countries),
                f"{highest_country}: {highest_value:.1f}",
                f"{lowest_country}: {lowest_value:.1f}",
                f"{avg_value:.1f}"
            )

        return "0", "N/A", "N/A", "N/A"
