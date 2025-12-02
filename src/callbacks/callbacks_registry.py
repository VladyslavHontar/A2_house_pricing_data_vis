from src.callbacks import (
    metrics_callback,
    map_callback,
    bar_chart_callback,
    line_chart_callback,
    scatter_callback
)

def register_all_callbacks(df):
    metrics_callback.register_metrics_callback(df)
    map_callback.register_map_callback(df)
    bar_chart_callback.register_bar_chart_callback(df)
    line_chart_callback.register_line_chart_callback(df)
    scatter_callback.register_scatter_callback(df)
