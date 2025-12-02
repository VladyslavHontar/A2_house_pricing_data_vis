from dash import Input, Output, callback
from src.visualizations import line_chart_viz
from src.data_processing import data_loader

def register_line_chart_callback(df):
    @callback(
        Output('price-time-series', 'figure'),
        [Input('country-dropdown', 'value'),
         Input('year-slider', 'value')]
    )
    def update_time_series(selected_countries, year_range):
        filtered_df = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

        filtered_df = data_loader.rebase_price_index(filtered_df, year_range[0])

        if not selected_countries or len(selected_countries) == 0:
            latest_data = filtered_df.sort_values('date').groupby('country_name').last()
            top_countries = latest_data.nlargest(10, 'price_index').index.tolist()
            filtered_df = filtered_df[filtered_df['country_name'].isin(top_countries)]
        else:
            filtered_df = filtered_df[filtered_df['country_name'].isin(selected_countries)]

        return line_chart_viz.create_line_chart(filtered_df, year_range[0])
