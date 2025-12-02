import plotly.express as px
from config import settings

def create_line_chart(filtered_df, base_year):
    fig = px.line(
        filtered_df,
        x='date',
        y='price_index',
        color='country_name',
        labels={'date': 'Year', 'price_index': 'Price Index', 'country_name': 'Country'},
        title='Housing Price Index Trends',
        color_discrete_sequence=settings.COLORBLIND_SAFE_PALETTE
    )

    fig.update_layout(
        height=400,
        hovermode='x unified',
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.3,
            xanchor="center",
            x=0.5
        ),
        xaxis_title="Year",
        yaxis_title=f"Price Index ({base_year}=100)",
        margin=dict(l=50, r=20, t=40, b=40)
    )

    fig.update_traces(line=dict(width=3))

    fig.add_hline(y=100, line_dash="dash", line_color="gray",
                  annotation_text=f"Baseline ({base_year})", annotation_position="right")

    return fig
