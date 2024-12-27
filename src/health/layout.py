"""
GUI setup for placements of visuals.
"""
from dash import dcc, html
import dash_table

def create_layout(data):
    """
    Builds and returns the Dash layout (all the HTML/Dash components).
    This function requires the 'data' DataFrame to extract default filter values.
    """

    # Reusable card style
    card_style = {
        'padding': '10px',
        'margin': '10px',
        'borderRadius': '5px',
        'boxShadow': '2px 2px 2px lightgrey',
        'backgroundColor': 'white',
        'width': '20%',
    }

    layout = html.Div(
        style={'backgroundColor': '#f9f9f9', 'font-family': 'Arial'},
        children=[
            html.H1(
                children='Hospital Admissions Dashboard',
                style={'textAlign': 'center', 'color': '#333'}
            ),
            html.Div(
                children='An interactive dashboard to visualize hospital admissions data.',
                style={'textAlign': 'center', 'color': '#777'}
            ),

            # Filters Section
            html.Div([
                html.Div([
                    # Medical Conditions Dropdown
                    html.Div([
                        html.Label(
                            'Select Medical Conditions:',
                            style={'fontWeight': 'bold', 'marginBottom': '5px'}
                        ),
                        dcc.Dropdown(
                            id='condition-dropdown',
                            options=[
                                {'label': cond, 'value': cond}
                                for cond in sorted(data['Medical Condition'].unique())
                            ],
                            value=data['Medical Condition'].unique().tolist(),
                            multi=True
                        ),
                    ], style={
                        'width': '30%',
                        'padding': '10px',
                        'margin': '10px',
                        'backgroundColor': 'white',
                        'border': '1px solid lightgrey',
                        'borderRadius': '5px',
                        'boxShadow': '2px 2px 2px lightgrey'
                    }),

                    # Gender Checklist
                    html.Div([
                        html.Label(
                            'Select Gender:',
                            style={'fontWeight': 'bold', 'marginBottom': '5px', 'textAlign': 'center'}
                        ),
                        html.Div([
                            dcc.Checklist(
                                id='gender-checklist',
                                options=[
                                    {'label': gender, 'value': gender}
                                    for gender in data['Gender'].unique()
                                ],
                                value=data['Gender'].unique().tolist(),
                                labelStyle={
                                    'display': 'inline-block',
                                    'padding': '5px 10px',
                                    'margin': '0 auto',
                                    'cursor': 'pointer',
                                    'border': '1px solid #ccc',
                                    'borderRadius': '5px',
                                    'backgroundColor': '#fff',
                                    'textAlign': 'center'
                                }
                            ),
                        ], style={'textAlign': 'center'}),
                    ], style={
                        'width': '30%',
                        'padding': '10px',
                        'margin': '10px',
                        'backgroundColor': 'white',
                        'border': '1px solid lightgrey',
                        'borderRadius': '5px',
                        'boxShadow': '2px 2px 2px lightgrey'
                    }),

                    # Age Range Slider
                    html.Div([
                        html.Label(
                            'Select Age Range:',
                            style={'fontWeight': 'bold', 'marginBottom': '5px'}
                        ),
                        dcc.RangeSlider(
                            id='age-slider',
                            min=int(data['Age'].min()),
                            max=int(data['Age'].max()),
                            value=[int(data['Age'].min()), int(data['Age'].max())],
                            marks={
                                str(age): str(age)
                                for age in range(
                                    int(data['Age'].min()),
                                    int(data['Age'].max()) + 1,
                                    10
                                )
                            },
                            step=1
                        ),
                    ], style={
                        'width': '30%',
                        'padding': '10px',
                        'margin': '10px',
                        'backgroundColor': 'white',
                        'border': '1px solid lightgrey',
                        'borderRadius': '5px',
                        'boxShadow': '2px 2px 2px lightgrey'
                    }),

                    # Date Range Picker
                    html.Div([
                        html.Label(
                            'Select Date Range:',
                            style={'fontWeight': 'bold', 'marginBottom': '5px'}
                        ),
                        dcc.DatePickerRange(
                            id='date-picker',
                            start_date=data['Date of Admission'].min(),
                            end_date=data['Date of Admission'].max(),
                            display_format='YYYY-MM-DD'
                        ),
                    ], style={
                        'width': '30%',
                        'padding': '10px',
                        'margin': '10px',
                        'backgroundColor': 'white',
                        'border': '1px solid lightgrey',
                        'borderRadius': '5px',
                        'boxShadow': '2px 2px 2px lightgrey'
                    }),
                ], style={
                    'display': 'flex',
                    'flexWrap': 'wrap',
                    'justifyContent': 'space-between',
                    'alignItems': 'center',
                    'backgroundColor': '#f9f9f9',
                    'padding': '20px',
                    'borderRadius': '10px',
                    'boxShadow': '2px 2px 5px lightgrey'
                }),
            ]),

            # Tabs
            dcc.Tabs([
                dcc.Tab(label='Healthcare Overview', children=[
                    # Summary Cards
                    html.Div([
                        html.Div([
                            html.H3(id='total-patients', style={'textAlign': 'center', 'color': '#00509E'}),
                            html.P('Total Patients', style={'textAlign': 'center', 'color': '#00509E'})
                        ], style=card_style),

                        html.Div([
                            html.H3(id='average-age', style={'textAlign': 'center', 'color': '#C70039'}),
                            html.P('Average Age', style={'textAlign': 'center', 'color': '#C70039'})
                        ], style=card_style),

                        html.Div([
                            html.H3(id='total-billing', style={'textAlign': 'center', 'color': '#2ECC40'}),
                            html.P('Total Billing Amount', style={'textAlign': 'center', 'color': '#2ECC40'})
                        ], style=card_style),

                        html.Div([
                            html.H3(id='average-stay', style={'textAlign': 'center', 'color': '#FF851B'}),
                            html.P('Average Length of Stay (Days)', style={'textAlign': 'center', 'color': '#FF851B'})
                        ], style=card_style),
                    ], style={'display': 'flex', 'justify-content': 'space-around'}),

                    # Charts
                    html.Div([
                        html.Div([
                            dcc.Graph(id='admission-pie-chart', style={'width': '48%', 'display': 'inline-block'}),
                            dcc.Graph(id='admission-bar-chart', style={'width': '48%', 'display': 'inline-block'}),
                        ], style={'display': 'flex', 'justifyContent': 'space-between'}),

                        dcc.Graph(id='billing-graph'),
                        dcc.Graph(id='stay-line-chart'),
                    ]),

                    # Data Table
                    html.Div([
                        dash_table.DataTable(
                            id='data-table',
                            columns=[{"name": i, "id": i} for i in data.columns],
                            page_size=10,
                            style_table={'overflowX': 'auto'},
                            style_cell={'textAlign': 'left'},
                            sort_action="native",
                            filter_action="native"
                        )
                    ], style={'padding': '0 20'}),
                ]),

                dcc.Tab(label='Medical Details', children=[
                    # Medical Charts
                    html.Div([
                        html.Div([
                            dcc.Graph(id='blood-type-treemap', style={'width': '48%', 'display': 'inline-block'}),
                            dcc.Graph(id='blood-type-bar-chart', style={'width': '48%', 'display': 'inline-block'}),
                        ], style={'display': 'flex', 'justifyContent': 'space-between'}),

                        dcc.Graph(id='diagnosis-medication-heatmap'),

                        html.Div([
                            dcc.Graph(id='medication-bar-chart', style={'width': '48%', 'display': 'inline-block'}),
                            dcc.Graph(id='diagnosis-pie-chart', style={'width': '48%', 'display': 'inline-block'}),
                        ], style={'display': 'flex', 'justifyContent': 'space-between'}),
                    ]),
                ]),
            ]),
        ]
    )

    return layout
