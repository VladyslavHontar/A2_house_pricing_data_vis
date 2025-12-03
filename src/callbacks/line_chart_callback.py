from dash import Input, Output, State, callback, ctx
from src.visualizations import line_chart_viz
from src.data_processing import data_loader

def register_line_chart_callback(df):
    @callback(
        [Output('line-chart-sort-order', 'data'),
         Output('btn-most-growth', 'outline'),
         Output('btn-least-growth', 'outline')],
        [Input('btn-most-growth', 'n_clicks'),
         Input('btn-least-growth', 'n_clicks')],
        [State('line-chart-sort-order', 'data')]
    )
    def update_line_chart_sort_toggle(most_clicks, least_clicks, current_sort):
        if not ctx.triggered_id:
            return 'most_growth', False, True

        if ctx.triggered_id == 'btn-most-growth':
            return 'most_growth', False, True
        elif ctx.triggered_id == 'btn-least-growth':
            return 'least_growth', True, False

    @callback(
        Output('price-time-series', 'figure'),
        [Input('country-dropdown', 'value'),
         Input('year-slider', 'value'),
         Input('line-chart-country-limit', 'value'),
         Input('line-chart-sort-order', 'data')]
    )
    def update_time_series(selected_countries, year_range, country_limit, sort_order):
        filtered_df = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

        if len(filtered_df) == 0:
            return line_chart_viz.create_line_chart(filtered_df, year_range[0])

        filtered_df = data_loader.rebase_price_index(filtered_df, year_range[0])

        if not selected_countries or len(selected_countries) == 0:
            if len(filtered_df) > 0:
                # Calculate growth for each country
                country_data = filtered_df.sort_values('date').groupby('country_name').agg({
                    'price_index': ['first', 'last']
                })
                country_data.columns = ['start_price', 'end_price']
                country_data['growth_pct'] = ((country_data['end_price'] - country_data['start_price']) /
                                               country_data['start_price'] * 100)

                # Sort by growth rate
                if sort_order == 'most_growth':
                    country_data = country_data.sort_values('growth_pct', ascending=False)
                else:  # least_growth
                    country_data = country_data.sort_values('growth_pct', ascending=True)

                # Limit to top N countries
                top_countries = country_data.head(min(country_limit, len(country_data))).index.tolist()
                filtered_df = filtered_df[filtered_df['country_name'].isin(top_countries)]
        else:
            filtered_df = filtered_df[filtered_df['country_name'].isin(selected_countries)]

        return line_chart_viz.create_line_chart(filtered_df, year_range[0])
