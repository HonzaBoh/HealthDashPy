"""
Originally called `CONSTANTS`, as the only constant in project is style (possibly OS path), named theme for now.
"""
def apply_chart_theme(fig):
    """
    Applies a consistent chart theme (layout, fonts, colors) to any Plotly figure.
    """
    fig.update_layout(
        title_font=dict(size=16, color='#333', family='Arial'),
        font=dict(size=12, color='#333', family='Arial'),
        plot_bgcolor='#f9f9f9',
        paper_bgcolor='#f9f9f9',
        legend=dict(title_font=dict(size=12), font=dict(size=10)),
        margin=dict(l=20, r=20, t=40, b=20)
    )
    return fig
