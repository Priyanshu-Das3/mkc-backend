import pandas as pd

def analyze_sensor_data(sensor_data):
    """Process data from Google Sheets"""
    df = pd.DataFrame(sensor_data)

    # Clean data
    df = df.dropna(subset=['Timestamp'])
    numeric_cols = ['Temperature', 'Humidity', 'Gas']
    df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors='coerce')

    # Calculate metrics
    metrics = {
        'temperature_stats': {
            'avg': df['Temperature'].mean(),
            'max': df['Temperature'].max()
        },
        'alerts': {
            'gas': sum(df['Gas'] > 135),
            'motion': sum(df['PIR'] == 'Active')
        }
    }
    return metrics
