import pandas as pd
import plotly.graph_objects as go

def create_scatter(filtered_df, year_range):
    growth_data = []
    for country in filtered_df['country_name'].unique():
        country_df = filtered_df[filtered_df['country_name'] == country].sort_values('date')
        if len(country_df) > 1:
            start_price = country_df.iloc[0]['price_index']
            end_price = country_df.iloc[-1]['price_index']

            if start_price > 0 and end_price > 0:
                growth_pct = ((end_price - start_price) / start_price) * 100

                growth_data.append({
                    'country_name': country,
                    'start_price': start_price,
                    'end_price': end_price,
                    'growth_pct': growth_pct,
                    'abs_growth': max(abs(growth_pct), 1)
                })

    growth_df = pd.DataFrame(growth_data)

    if len(growth_df) == 0:
        return go.Figure().update_layout(
            title='No data available for selected range',
            height=400
        )

    fig = go.Figure()

    max_abs_growth = max(growth_df['abs_growth'])
    normalized_sizes = (growth_df['abs_growth'] / max_abs_growth * 35) + 5

    max_abs_pct = max(abs(growth_df['growth_pct'].min()), abs(growth_df['growth_pct'].max()))

    fig.add_trace(go.Scatter(
        x=growth_df['start_price'],
        y=growth_df['end_price'],
        mode='markers',
        marker=dict(
            size=normalized_sizes,
            sizemode='diameter',
            color=growth_df['growth_pct'],
            colorscale='RdYlGn_r',
            cmid=0,
            cmin=-max_abs_pct,
            cmax=max_abs_pct,
            colorbar=dict(
                title=dict(text='Growth %', font=dict(size=12)),
                thickness=15,
                len=0.7,
                tickformat='+.0f'
            ),
            line=dict(width=1, color='white'),
            opacity=0.8
        ),
        text=growth_df['country_name'],
        customdata=growth_df['growth_pct'],
        hovertemplate='<b>%{text}</b><br>' +
                      f'Start ({year_range[0]}): %{{x:.1f}}<br>' +
                      f'End ({year_range[1]}): %{{y:.1f}}<br>' +
                      'Growth: %{customdata:+.1f}%<br>' +
                      '<extra></extra>',
        showlegend=False
    ))

    min_val = min(growth_df['start_price'].min(), growth_df['end_price'].min())
    max_val = max(growth_df['start_price'].max(), growth_df['end_price'].max())
    fig.add_trace(
        go.Scatter(
            x=[min_val, max_val],
            y=[min_val, max_val],
            mode='lines',
            line=dict(dash='dash', color='gray', width=1),
            showlegend=False,
            hoverinfo='skip'
        )
    )

    fig.update_layout(
        xaxis_title=f'Price Index in {year_range[0]} (2010=100)',
        yaxis_title=f'Price Index in {year_range[1]} (2010=100)',
        height=400,
        margin=dict(l=50, r=20, t=20, b=40),
        hovermode='closest',
        plot_bgcolor='rgba(250,250,250,0.5)',
        font=dict(size=11)
    )

    fig.add_annotation(
        x=max_val * 0.7,
        y=max_val * 0.7,
        text="No change line",
        showarrow=True,
        arrowhead=2,
        arrowsize=1,
        arrowwidth=1,
        arrowcolor="gray",
        ax=-40,
        ay=-40,
        font=dict(size=10, color="gray")
    )

    return fig
