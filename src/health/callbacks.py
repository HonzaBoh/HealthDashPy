"""
Mostly functional code here for `data` interactivity.
"""
import pandas as pd
import plotly.express as px
from dash import Input, Output

# Relative imports from the same package
from .data import data, monthly_data
from .theme import apply_chart_theme

def register_callbacks(app):
    """
    Defines and registers all Dash callbacks with the provided `app`.
    """

    @app.callback(
        [
            Output('total-patients', 'children'),
            Output('average-age', 'children'),
            Output('total-billing', 'children'),
            Output('average-stay', 'children'),
            Output('billing-graph', 'figure'),
            Output('admission-pie-chart', 'figure'),
            Output('admission-bar-chart', 'figure'),
            Output('stay-line-chart', 'figure'),
            Output('medication-bar-chart', 'figure'),
            Output('diagnosis-pie-chart', 'figure'),
            Output('blood-type-treemap', 'figure'),
            Output('blood-type-bar-chart', 'figure'),
            Output('diagnosis-medication-heatmap', 'figure'),
            Output('data-table', 'data')
        ],
        [
            Input('condition-dropdown', 'value'),
            Input('age-slider', 'value'),
            Input('gender-checklist', 'value'),
            Input('date-picker', 'start_date'),
            Input('date-picker', 'end_date')
        ]
    )
    def update_dashboard(selected_conditions, selected_age, selected_genders, start_date, end_date):
        # 1. Filter the data
        filtered_data = data[
            (data['Medical Condition'].isin(selected_conditions)) &
            (data['Age'] >= selected_age[0]) & (data['Age'] <= selected_age[1]) &
            (data['Gender'].isin(selected_genders)) &
            (data['Date of Admission'] >= start_date) &
            (data['Date of Admission'] <= end_date)
        ]

        # 2. Summary Cards
        total_patients = len(filtered_data)
        average_age = round(filtered_data['Age'].mean(), 1) if total_patients > 0 else 0
        total_billing = f"${filtered_data['Billing Amount'].sum():,.2f}"
        average_stay = round(filtered_data['Length of Stay'].mean(), 1) if total_patients > 0 else 0

        # 3. Billing Line Chart
        filtered_monthly_data = monthly_data[
            (monthly_data['Medical Condition'].isin(selected_conditions)) &
            (monthly_data['Date of Admission'] >= start_date) &
            (monthly_data['Date of Admission'] <= end_date)
        ]
        billing_fig = px.line(
            filtered_monthly_data,
            x='Date of Admission',
            y='Count',
            color='Medical Condition',
            title='Billing Amount Over Time (Monthly Aggregation)',
            labels={'Count': 'Number of Admissions', 'Date of Admission': 'Admission Date'}
        )
        billing_fig = apply_chart_theme(billing_fig)

        # 4. Admission Type Pie Chart
        pie_fig = px.pie(
            filtered_data,
            names='Admission Type',
            title='Admission Types Distribution',
            hole=0.4
        )
        pie_fig.update_traces(textposition='outside', textinfo='percent+label')
        pie_fig = apply_chart_theme(pie_fig)

        # 5. Admission Type Bar Chart
        bar_data = filtered_data.groupby('Admission Type')['Billing Amount'].sum().reset_index()
        bar_fig = px.bar(
            bar_data,
            x='Admission Type',
            y='Billing Amount',
            color='Admission Type',
            title='Total Billing Amount by Admission Type',
            labels={
                'Billing Amount': 'Total Billing Amount ($)',
                'Admission Type': 'Admission Type'
            }
        )
        bar_fig.update_layout(showlegend=False)
        bar_fig = apply_chart_theme(bar_fig)

        # 6. Medication Bar Chart
        med_counts = filtered_data['Medication'].value_counts().reset_index()
        med_counts.columns = ['Medication', 'Count']
        med_fig = px.bar(
            med_counts,
            x='Medication',
            y='Count',
            title='Medication Counts',
            labels={'Medication': 'Medication', 'Count': 'Number of Prescriptions'},
            color='Medication',
            color_discrete_sequence=px.colors.qualitative.Pastel
        )
        med_fig = apply_chart_theme(med_fig)

        # 7. Diagnosis Pie Chart
        diag_fig = px.pie(
            filtered_data,
            names='Medical Condition',
            title='Diagnosis Distribution',
            hole=0.4
        )
        diag_fig.update_traces(textposition='outside', textinfo='percent+label')
        diag_fig = apply_chart_theme(diag_fig)

        # 8. Blood Type Treemap
        blood_treemap_data = filtered_data.groupby('Blood Type').size().reset_index(name='Count')
        blood_treemap_fig = px.treemap(
            blood_treemap_data,
            path=['Blood Type'],
            values='Count',
            title='Blood Type Distribution',
            color='Blood Type',
            color_discrete_sequence=px.colors.qualitative.Pastel
        )
        blood_treemap_fig = apply_chart_theme(blood_treemap_fig)

        # 9. Blood Type Stacked Bar Chart
        blood_type_grouped = filtered_data.groupby(['Blood Type', 'Admission Type']).size().reset_index(name='Count')
        blood_bar_chart_fig = px.bar(
            blood_type_grouped,
            x='Blood Type',
            y='Count',
            color='Admission Type',
            title='Number of Admissions by Blood Type and Admission Type',
            labels={'Count': 'Number of Admissions', 'Blood Type': 'Blood Type', 'Admission Type': 'Admission Type'},
            barmode='stack'
        )
        blood_bar_chart_fig = apply_chart_theme(blood_bar_chart_fig)

        # 10. Length of Stay Box Plot
        stay_fig = px.box(
            filtered_data,
            x='Medical Condition',
            y='Length of Stay',
            color='Medical Condition',
            title='Distribution of Length of Stay by Medical Condition',
            labels={'Length of Stay': 'Length of Stay (Days)', 'Medical Condition': 'Medical Condition'}
        )
        stay_fig.update_layout(
            xaxis_title='Medical Condition',
            yaxis_title='Length of Stay (Days)',
            showlegend=False
        )
        stay_fig = apply_chart_theme(stay_fig)

        # 11. Data Table
        table_data = filtered_data.to_dict('records')

        # 12. Diagnosis vs Medication Heatmap
        diag_med_pivot = filtered_data.pivot_table(
            index='Medical Condition',
            columns='Medication',
            values='Name',
            aggfunc='count',
            fill_value=0
        )
        heatmap_fig = px.imshow(
            diag_med_pivot,
            labels=dict(x="Medication", y="Medical Condition", color="Number of Patients"),
            title='Diagnosis vs Medication Heatmap'
        )
        heatmap_fig = apply_chart_theme(heatmap_fig)

        return (
            total_patients,
            average_age,
            total_billing,
            average_stay,
            billing_fig,
            pie_fig,
            bar_fig,
            stay_fig,
            med_fig,
            diag_fig,
            blood_treemap_fig,
            blood_bar_chart_fig,
            heatmap_fig,
            table_data
        )
