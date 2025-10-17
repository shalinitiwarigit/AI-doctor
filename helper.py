import pandas as pd
def get_precautions(disease,df):
    row = df[df['Disease'].str.lower() == disease.lower()]

    if row.empty:
        return ['Consult nearest hospital']

    precautions = [
        row.iloc[0]['Precaution_1'],
        row.iloc[0]['Precaution_2'],
        row.iloc[0]['Precaution_3'],
        row.iloc[0]['Precaution_4']
    ]

    # Remove NaN values
    return [p for p in precautions if pd.notnull(p)]