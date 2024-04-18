import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Define the number of records
num_records = 1000

# Generate dates for the dataset
start_date = datetime(2023, 1, 1)
dates = [start_date + timedelta(days=i) for i in range(num_records)]

# Generate random data for each variable
data = {
    'Date': dates,
    'Zone_ID': np.random.randint(1, 4, num_records),
    'TGBT_ID': np.random.randint(101, 104, num_records),
    'Armoire_ID': np.random.choice(['A1', 'A2', 'A3'], num_records),
    'Machine_ID': np.random.choice(['M1', 'M2', 'M3'], num_records),
    'Product_ID': np.random.choice(['P1', 'P2', 'P3'], num_records),
    'Demand': np.random.randint(50, 150, num_records),
    'Price': np.random.uniform(5, 20, num_records),
    'Production_Capacity': np.random.randint(300, 600, num_records),
    'Inventory_Level': np.random.randint(100, 250, num_records),
    'Order_Backlog': np.random.randint(20, 80, num_records),
    'Competitor_Price': np.random.uniform(5, 20, num_records),
    'Raw_Material_Cost': np.random.uniform(1, 5, num_records),
    'Labor_Cost': np.random.uniform(1, 5, num_records),
    'Energy_Cost': np.random.uniform(1, 5, num_records),
    'Machine_Utilization': np.random.uniform(0.7, 0.95, num_records),
    'Energy_Consumption': np.random.randint(4000, 5500, num_records),
    'Maintenance_History': np.random.choice(['No maintenance recorded', 'Routine maintenance', 'Replaced faulty component'], num_records),
    'Failure_Rate': np.random.uniform(0.01, 0.05, num_records),
    'Supply_Chain_Risks': np.random.choice(['Supplier A lead time increased', 'Supplier B bankruptcy risk', 'Transportation strike affecting delivery'], num_records),
    'Quality_Control': np.random.uniform(0.9, 0.98, num_records),
    'Financial_Risks': np.random.uniform(0.9, 0.98, num_records),
    'Compliance': np.random.choice(['Compliant with ISO 9001', 'Compliant with ISO 14001', 'Compliant with OHSAS 18001'], num_records)
}

# Create DataFrame
df = pd.DataFrame(data)

# Save DataFrame to CSV
df.to_csv('manufacturing_dataset.csv', index=False)
