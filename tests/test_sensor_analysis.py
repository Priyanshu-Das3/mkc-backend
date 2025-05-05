import pytest
import pandas as pd
from app.sensor_analysis import analyze_sensor_data

def test_sensor_analysis_basic():
    """Test basic sensor data analysis"""
    test_data = [
        {'Timestamp': '2024-01-01 10:00', 'Temperature': 25.5, 'Humidity': 50, 'Gas': 120, 'PIR': 'Inactive', 'IR': 0},
        {'Timestamp': '2024-01-01 10:05', 'Temperature': 26.0, 'Humidity': 52, 'Gas': 130, 'PIR': 'Active', 'IR': 1},
        {'Timestamp': '2024-01-01 10:10', 'Temperature': 27.5, 'Humidity': 55, 'Gas': 140, 'PIR': 'Active', 'IR': 0}
    ]
    
    result = analyze_sensor_data(test_data)
    
    # Temperature stats
    assert round(result['temperature_stats']['avg'], 2) == 26.33
    assert result['temperature_stats']['max'] == 27.5
    
    # Alert counts
    assert result['alerts']['gas'] == 1  # Only 140 > 135
    assert result['alerts']['motion'] == 2  # Two 'Active' PIR entries

def test_missing_data_handling():
    """Test handling of missing values"""
    test_data = [
        {'Timestamp': None, 'Temperature': None, 'Humidity': None, 'Gas': None, 'PIR': None},
        {'Timestamp': '2024-01-01 10:05', 'Temperature': "invalid", 'Humidity': 'N/A', 'Gas': 'abc', 'PIR': 'Active'}
    ]
    
    result = analyze_sensor_data(test_data)
    
    # Should handle all missing/invalid values gracefully
    assert pd.isna(result['temperature_stats']['avg'])
    assert result['alerts']['motion'] == 1  # One 'Active' entry

def test_empty_dataset():
    """Test empty data input"""
    result = analyze_sensor_data([])
    assert pd.isna(result['temperature_stats']['avg'])
    assert result['alerts']['gas'] == 0
