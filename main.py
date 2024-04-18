import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Define the number of records
num_records = 1000

# Generate dates for the dataset
start_date = datetime(2023, 1, 1)
dates = [start_date + timedelta(days=i) for i in range(num_records)]

# Define constants for easier tweaking
MIN_CAPACITY = 300
MAX_CAPACITY = 600
MIN_PRICE = 5
MAX_PRICE = 20
MIN_DEMAND = 50
MAX_DEMAND = 150
MIN_INVENTORY = 100
MAX_INVENTORY = 250
MIN_BACKLOG = 20
MAX_BACKLOG = 80
MIN_UTILIZATION = 0.7
MAX_UTILIZATION = 0.95
MIN_CONSUMPTION = 4000
MAX_CONSUMPTION = 5500
MIN_FAILURE_RATE = 0.01
MAX_FAILURE_RATE = 0.05
MIN_QUALITY = 0.9
MAX_QUALITY = 0.98
MIN_RISKS = 0.9
MAX_RISKS = 0.98

# Generate random data for each variable
data = {
    'Date': dates,
    'Zone_ID': np.random.randint(1, 4, num_records),
    'TGBT_ID': np.random.randint(101, 104, num_records),
    'Armoire_ID': np.random.choice(['A1', 'A2', 'A3'], num_records),
    'Machine_ID': np.random.choice(['M1', 'M2', 'M3'], num_records),
    'Product_ID': np.random.choice(['P1', 'P2', 'P3'], num_records),
    'Demand': np.random.randint(MIN_DEMAND, MAX_DEMAND, num_records),
    'Price': np.random.uniform(MIN_PRICE, MAX_PRICE, num_records),
    'Production_Capacity': np.random.randint(MIN_CAPACITY, MAX_CAPACITY, num_records),
    'Inventory_Level': np.random.randint(MIN_INVENTORY, MAX_INVENTORY, num_records),
    'Order_Backlog': np.random.randint(MIN_BACKLOG, MAX_BACKLOG, num_records),
    'Competitor_Price': np.random.uniform(MIN_PRICE, MAX_PRICE, num_records),
    'Raw_Material_Cost': np.random.uniform(1, 5, num_records),  # Assuming raw material cost between $1 and $5
    'Labor_Cost': np.random.uniform(1, 5, num_records),  # Assuming labor cost between $1 and $5
    'Energy_Cost': np.random.uniform(1, 5, num_records),  # Assuming energy cost between $1 and $5
    'Machine_Utilization': np.random.uniform(MIN_UTILIZATION, MAX_UTILIZATION, num_records),
    'Energy_Consumption': np.random.randint(MIN_CONSUMPTION, MAX_CONSUMPTION, num_records),
    'Maintenance_History': np.random.choice(['No maintenance recorded', 'Routine maintenance', 'Replaced faulty component'], num_records),
    'Failure_Rate': np.random.uniform(MIN_FAILURE_RATE, MAX_FAILURE_RATE, num_records),
    'Supply_Chain_Risks': np.random.choice(['Supplier A lead time increased', 'Supplier B bankruptcy risk', 'Transportation strike affecting delivery'], num_records),
    'Quality_Control': np.random.uniform(MIN_QUALITY, MAX_QUALITY, num_records),
    'Financial_Risks': np.random.uniform(MIN_RISKS, MAX_RISKS, num_records),
    'Compliance': np.random.choice(['Compliant with ISO 9001', 'Compliant with ISO 14001', 'Compliant with OHSAS 18001'], num_records)
}

# Create DataFrame
df = pd.DataFrame(data)

# Save DataFrame to CSV
df.to_csv('manufacturing_dataset.csv', index=False)
