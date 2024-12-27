"""
File handling preprocessing, made file for possible scalability if more data would require aggregation
"""
import os
import pandas as pd

def load_data(csv_path=None):
    """
    Loads the hospital_data.csv from the data folder, applies preprocessing,
    and returns two DataFrames: data and monthly_data.
    """
    if csv_path is None:
        # Use an OS-agnostic way to reference the CSV
        current_dir = os.path.dirname(os.path.abspath(__file__))
        default_csv_path = os.path.join(current_dir, '..', '..', 'data', 'hospital_data.csv')
        csv_path = default_csv_path

    # Load the data
    data = pd.read_csv(csv_path)

    # Data preprocessing
    data['Date of Admission'] = pd.to_datetime(data['Date of Admission'])
    data['Discharge Date'] = pd.to_datetime(data['Discharge Date'])
    data['Billing Amount'] = pd.to_numeric(data['Billing Amount'], errors='coerce')
    data['Age'] = pd.to_numeric(data['Age'], errors='coerce')
    data['Length of Stay'] = (data['Discharge Date'] - data['Date of Admission']).dt.days

    # Aggregate data
    monthly_data = data.groupby([
        pd.Grouper(key='Date of Admission', freq='M'),
        'Medical Condition'
    ]).size().reset_index(name='Count')

    return data, monthly_data

data, monthly_data = load_data()
