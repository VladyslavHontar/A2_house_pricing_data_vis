import plotly.express as px

def create_bar_chart(latest_data, base_year):
    fig = px.bar(
        latest_data,
        y='country_name',
        x='price_index',
        orientation='h',
        color='price_index',
        color_continuous_scale='RdYlGn_r',
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
