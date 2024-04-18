import pandas as pd
import numpy as np
import random
import os
from datetime import datetime, timedelta

# Define the number of records you want to generate
num_records = 5000

# Generate Energy Consumption Data
energy_data = pd.DataFrame({
    'Timestamp': [datetime.now() - timedelta(minutes=random.randint(1, 10080)) for _ in range(num_records)],
    'Zone_ID': [f'Zone_{random.randint(1, 3)}' for _ in range(num_records)],
    'TGBT_ID': [f'TGBT_{random.randint(1, 3)}' for _ in range(num_records)],
    'Armoire_ID': [f'Armoire_{random.randint(1, 3)}' for _ in range(num_records)],
    'Machine_ID': [f'Machine_{random.randint(1, 10)}' for _ in range(num_records)],
    'Energy_Consumption_kWh': [random.uniform(10, 100) for _ in range(num_records)]
})

# Generate Machine Data
machine_data = pd.DataFrame({
    'Machine_ID': [f'Machine_{i}' for i in range(1, 11)],
    'Machine_Type': ['Type_A', 'Type_B', 'Type_C', 'Type_D', 'Type_E', 'Type_F', 'Type_G', 'Type_H', 'Type_I', 'Type_J'],
    'Operating_Hours': [random.uniform(10, 500) for _ in range(10)],
    'Production_Output': [random.uniform(100, 1000) for _ in range(10)],
    'Energy_Efficiency_Rating': [random.uniform(0.5, 1.0) for _ in range(10)],
})

# Generate Asset Information
asset_data = pd.DataFrame({
    'Asset_ID': ['TGBT_1', 'TGBT_2', 'TGBT_3', 'Armoire_1', 'Armoire_2', 'Armoire_3'],
    'Asset_Type': ['TGBT', 'TGBT', 'TGBT', 'Armoire', 'Armoire', 'Armoire'],
    'Capacity': [random.uniform(1000, 5000) for _ in range(6)],
    'Age': [random.randint(1, 10) for _ in range(6)],
    'Criticality': ['High', 'Medium', 'Low', 'Low', 'Medium', 'High']
})

# Generate Market Price Data
market_price_data = pd.DataFrame({
    'Timestamp': [datetime.now() - timedelta(hours=random.randint(1, 24)) for _ in range(num_records)],
    'Energy_Price': [random.uniform(0.05, 0.15) for _ in range(num_records)],
    'Raw_Material_Price': [random.uniform(50, 100) for _ in range(num_records)]
})

# Generate Production Data
production_data = pd.DataFrame({
    'Timestamp': [datetime.now() - timedelta(hours=random.randint(1, 24)) for _ in range(num_records)],
    'Production_Volume': [random.uniform(1000, 5000) for _ in range(num_records)]
})

# Generate Environmental Data
environmental_data = pd.DataFrame({
    'Timestamp': [datetime.now() - timedelta(hours=random.randint(1, 24)) for _ in range(num_records)],
    'Temperature': [random.uniform(10, 30) for _ in range(num_records)],
    'Humidity': [random.uniform(30, 70) for _ in range(num_records)]
})

# Generate Maintenance and Downtime Data
# Generate Maintenance and Downtime Data
maintenance_data = pd.DataFrame({
    'Timestamp': [datetime.now() - timedelta(days=random.randint(1, 30)) for _ in range(num_records)],
    'Machine_ID': [f'Machine_{random.randint(1, 10)}' for _ in range(num_records)],
    'Downtime_Reason': [random.choice(['Maintenance', 'Repair', 'Incident', 'Other']) for _ in range(num_records)]
})



# Generate Financial Data
financial_data = pd.DataFrame({
    'Timestamp': [datetime.now() - timedelta(days=random.randint(1, 30)) for _ in range(num_records)],
    'Operating_Costs': [random.uniform(1000, 10000) for _ in range(num_records)],
    'Revenue': [random.uniform(5000, 15000) for _ in range(num_records)]
})

# Generate External Factors Data
external_factors_data = pd.DataFrame({
    'Timestamp': [datetime.now() - timedelta(days=random.randint(1, 30)) for _ in range(num_records)],
    'Regulatory_Changes': [random.choice(['Yes', 'No']) for _ in range(num_records)],
    'Market_Trends': [random.choice(['Positive', 'Negative', 'Neutral']) for _ in range(num_records)],
    'Economic_Indicators': [random.choice(['Growth', 'Recession', 'Stable']) for _ in range(num_records)],
    'Geopolitical_Events': [random.choice(['Unstable', 'Stable']) for _ in range(num_records)]
})


# Define the directory where you want to save the CSV files
output_directory = './generated_data/'

# Create the directory if it doesn't exist

os.makedirs(output_directory, exist_ok=True)

# Save each DataFrame to a CSV file
energy_data.to_csv(os.path.join(output_directory, 'energy_data.csv'), index=False)
machine_data.to_csv(os.path.join(output_directory, 'machine_data.csv'), index=False)
asset_data.to_csv(os.path.join(output_directory, 'asset_data.csv'), index=False)
market_price_data.to_csv(os.path.join(output_directory, 'market_price_data.csv'), index=False)
production_data.to_csv(os.path.join(output_directory, 'production_data.csv'), index=False)
environmental_data.to_csv(os.path.join(output_directory, 'environmental_data.csv'), index=False)
maintenance_data.to_csv(os.path.join(output_directory, 'maintenance_data.csv'), index=False)
financial_data.to_csv(os.path.join(output_directory, 'financial_data.csv'), index=False)
external_factors_data.to_csv(os.path.join(output_directory, 'external_factors_data.csv'), index=False)
