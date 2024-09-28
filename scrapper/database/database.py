import sqlite3
from sqlite3 import Error
from configparser import ConfigParser, ExtendedInterpolation

class Database:
    def __init__(self):
        self.read_config()
        self.database_path = self.config['Database']['path']
        self.schema_path = self.config['Schema']['path']

        self.connection = sqlite3.connect(self.database_path)
        self.cursor = self.connectionection.cursor()

        if self.connection is not None:
            self.create_tables_from_schema()
        else:
            print("Error! Cannot create the database connection.")

    def read_config(self):
        self.config = ConfigParser(interpolation=ExtendedInterpolation())
        self.config.read('config.ini')

    def read_schema(self):
        """ Create tables using the schema from a .sql file """
        try:
            with open(self.schema_path, 'r') as f:
                schema = f.read()
            with self.connection:
                self.connection.executescript(schema)
                print("Tables created successfully from the schema.")
        except Error as e:
            print(e)
        except FileNotFoundError:
            print(f"Schema file {self.schema_path} not found.")

    def insert(self, table, columns, values):
        """ Insert data into a table """
        columns_str = ', '.join(columns)
        placeholders = ', '.join('?' * len(values))
        query = f"INSERT INTO {table} ({columns_str}) VALUES ({placeholders})"
        try:
            with self.connection:
                self.connection.execute(query, values)
                print("Record inserted successfully.")
        except Error as e:
            print(e) 
            
# =============================================================================

# if __name__ == "__main__":
#     # Initialize the database and schema
#     db = Database("mydatabase.db", "schema.sql")
    
#     # Example usage
#     # Insert a record
#     db.insert("users", ["name", "age"], ["Alice", 30])

#     # Select all users
#     db.select("users")

#     # Update a record
#     db.update("users", {"name": "Bob"}, "name = 'Alice'")

#     # Delete a record
#     db.delete("users", "name = 'Bob'")

#     # Close the database connection
#     db.close()
