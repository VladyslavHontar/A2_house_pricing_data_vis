import plotly.express as px

def create_map(latest_data, base_year):
    fig = px.choropleth(
        latest_data,
        locations='country_name',
        locationmode='country names',
        color='price_index',
        hover_name='country_name',
        hover_data={'country_name': False, 'price_index': ':.1f', 'time_period': True},
        color_continuous_scale='RdYlGn_r',
        labels={'price_index': 'Price Index', 'time_period': 'Quarter'},
    )

    fig.update_layout(
        geo=dict(
            showframe=True,
            showcoastlines=True,
            showcountries=True,
            projection_type='natural earth',
            bgcolor='rgba(230, 245, 255, 0.5)',
            lakecolor='rgb(200, 220, 240)',
            landcolor='rgb(250, 250, 250)',
            oceancolor='rgb(220, 235, 250)',
            countrycolor='rgb(200, 200, 200)',
            coastlinecolor='rgb(150, 150, 150)',
            coastlinewidth=0.8,
            center=dict(lat=50, lon=20),
            projection_scale=1.8,
        ),
        autosize=True,
        margin=dict(l=0, r=0, t=10, b=0, pad=0),
        coloraxis_colorbar=dict(
            title=dict(text=f"Price Index<br>({base_year}=100)", font=dict(size=11)),
            thickness=18,
            len=0.65,
            x=1.0,
            xpad=5
        ),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )

    fig.update_traces(
        marker_line_color='white',
        marker_line_width=1.2
    )

    return fig
