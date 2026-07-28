import pandas as pd
from sqlalchemy import create_engine

# Read cleaned CSV
df = pd.read_csv("customer_shopping_behavior_clean.csv")

# Connect to MySQL database
engine = create_engine(
    "mysql+pymysql://root:8273207364@localhost:3306/customer_behavior"
)

# Upload DataFrame as a table
df.to_sql(
    "customers",
    con=engine,
    if_exists="replace",
    index=False
)

print("CSV imported successfully!")