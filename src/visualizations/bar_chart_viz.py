import plotly.express as px
import plotly.graph_objects as go

def create_bar_chart(latest_data, base_year, global_min=None, global_max=None):
    if len(latest_data) == 0:
        fig = go.Figure()
        fig.update_layout(
            title='No data available for selected filters',
            height=500,
            annotations=[{
                'text': 'Please adjust your filters to see data',
                'xref': 'paper',
                'yref': 'paper',
                'x': 0.5,
                'y': 0.5,
                'showarrow': False,
                'font': {'size': 16}
            }]
        )
        return fig

    fig = px.bar(
        latest_data,
        y='country_name',
        x='price_index',
        orientation='h',
        color='price_index',
        color_continuous_scale='RdYlGn_r',
        range_color=[global_min, global_max] if global_min and global_max else None,
        labels={'country_name': 'Country', 'price_index': 'Price Index'},
        title='Top 15 Countries by Price Index'
    )

    fig.update_layout(
        height=500,
        showlegend=False,
        yaxis={'categoryorder': 'total ascending'},
        xaxis_title=f"Price Index ({base_year}=100)",
        yaxis_title="",
        margin=dict(l=10, r=10, t=40, b=40)
    )

    return fig
