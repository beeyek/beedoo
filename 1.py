import pymysql
import pandas as pd

# Connect to the database
conn = pymysql.connect(host='localhost', user='root', password='hooshang', database='infringements')
cursor = conn.cursor()

# Read data from the Excel file
file_path = 'infringements.xlsx'  # Replace with the actual path to your Excel file
df = pd.read_excel(file_path, header=0)  # Set header=0 to use the first row as headers

# Create the 'reports' table
table_creation_query = '''
    CREATE TABLE IF NOT EXISTS reports (
        id INT AUTO_INCREMENT PRIMARY KEY,
        marketplace VARCHAR(255),
        infringing_listing_id VARCHAR(255),
        scope VARCHAR(255),
        type_of_infringement VARCHAR(255),
        complaint_reason VARCHAR(255),
        ip_owner VARCHAR(255),
        registration_number INT,
        additional_information TEXT
    )
'''
cursor.execute(table_creation_query)

# Insert data into the 'reports' table
insert_query = '''
    INSERT INTO reports (
        marketplace, 
        infringing_listing_id, 
        scope, 
        type_of_infringement, 
        complaint_reason, 
        ip_owner, 
        registration_number, 
        additional_information
    ) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
'''

for index, row in df.iterrows():
    cursor.execute(insert_query, (
        row['marketplace'], 
        row['infringing_listing_id'], 
        row['scope'], 
        row['type_of_infringement'], 
        row['complaint_reason'], 
        row['ip_owner'], 
        row['registration_number'], 
        row['additional_information']
    ))

# Commit the changes and close the connection
conn.commit()
conn.close()
