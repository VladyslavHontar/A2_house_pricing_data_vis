from dash import Input, Output, callback
from src.visualizations import bar_chart_viz
from src.data_processing import data_loader

def register_bar_chart_callback(df):
    @callback(
        Output('price-bar-chart', 'figure'),
        [Input('year-slider', 'value'),
         Input('country-dropdown', 'value')]
    )
    def update_bar_chart(year_range, selected_countries):
        filtered_df = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

        if selected_countries and len(selected_countries) > 0:
            filtered_df = filtered_df[filtered_df['country_name'].isin(selected_countries)]

        filtered_df = data_loader.rebase_price_index(filtered_df, year_range[0])

        latest_data = filtered_df.sort_values('date').groupby('country_name').last().reset_index()
        latest_data = latest_data.sort_values('price_index', ascending=True)

        if not selected_countries or len(selected_countries) == 0:
            latest_data = latest_data.tail(15)
        elif len(latest_data) > 15:
            latest_data = latest_data.tail(15)

        return bar_chart_viz.create_bar_chart(latest_data, year_range[0])
