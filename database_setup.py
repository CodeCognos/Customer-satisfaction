from sqlalchemy import create_engine

# Replace 'your_database_url' with the actual URL of your database
# Example: 'postgresql://username:password@localhost:5432/database_name'
engine = create_engine(r'sqlite:///C:\Users\Mehta\AppData\Roaming\zenml\local_stores\default_zen_store/zenml.db')

# Execute the SQL command to drop the existing table
with engine.connect() as connection:
    connection.execute("DROP TABLE rolepermissionschema;")
