from dash import Input, Output, callback, State
from src.visualizations import bar_chart_viz
from src.data_processing import data_loader

def register_bar_chart_callback(df):
    @callback(
        [Output('bar-chart-sort', 'data'),
         Output('btn-expensive', 'outline'),
         Output('btn-affordable', 'outline')],
        [Input('btn-expensive', 'n_clicks'),
         Input('btn-affordable', 'n_clicks')],
        [State('bar-chart-sort', 'data')]
    )
    def update_sort_toggle(expensive_clicks, affordable_clicks, current_sort):
        from dash import ctx
        if not ctx.triggered_id:
            return 'expensive', False, True

        if ctx.triggered_id == 'btn-expensive':
            return 'expensive', False, True
        elif ctx.triggered_id == 'btn-affordable':
            return 'affordable', True, False

        return current_sort, False if current_sort == 'expensive' else True, True if current_sort == 'expensive' else False

    @callback(
        Output('price-bar-chart', 'figure'),
        [Input('year-slider', 'value'),
         Input('country-dropdown', 'value'),
         Input('bar-chart-sort', 'data')]
    )
    def update_bar_chart(year_range, selected_countries, sort_order):
        filtered_df = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

        if selected_countries and len(selected_countries) > 0:
            filtered_df = filtered_df[filtered_df['country_name'].isin(selected_countries)]

        filtered_df = data_loader.rebase_price_index(filtered_df, year_range[0])

        latest_data = filtered_df.sort_values('date').groupby('country_name').last().reset_index()

        global_min = latest_data['price_index'].min()
        global_max = latest_data['price_index'].max()

        latest_data = latest_data.sort_values('price_index', ascending=True)

        if not selected_countries or len(selected_countries) == 0:
            if sort_order == 'expensive':
                latest_data = latest_data.tail(15)
            else:
                latest_data = latest_data.head(15)
        elif len(latest_data) > 15:
            if sort_order == 'expensive':
                latest_data = latest_data.tail(15)
            else:
                latest_data = latest_data.head(15)

        return bar_chart_viz.create_bar_chart(latest_data, year_range[0], global_min, global_max)
