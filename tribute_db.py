"""
Description:
Handles all things database.
"""
# IMPORTS
#import [Module/Package]
import sqlite3
import logging
from sqlite3.dbapi2 import Error

#? Configures the logger to log messages of the "INFO" severity level or higher.
logging.basicConfig(level=logging.INFO)

class Tribute_Database():
    """
    Description:
    This class encapsulates the flow of database management into a single database object.
    """
    #? CONSTRUCTOR
    def __init__(self, filename: str=':memory:'):
        self.connect_to_database(filename)
        self.create_table()
    
    def connect_to_database(self, filename: str=':memory:'):
        """
        Connects to a database file with "sqlite.connect(filename)".

        Args:
            filename (STR): Name of the file to connect to, defaults to an in-memory database.
        """
        global db
        db = None
        try:
            db = sqlite3.connect(str(filename))
        except Error as e:
            logging.error(e)

    def create_table(self):
        #TODO: Construct an SQLite create statement as a formatted string, and pass it into "db.cursor().execute()"
        """
        Creates a table with the respective column names and data types declared.
        """
        cursor = db.cursor()
        sql_statement = '''CREATE TABLE IF NOT EXISTS tributes('User ID' INTEGER,
                    'Tribute Name' TEXT,
                    'Nicknames' TEXT,
                    'Age' INTEGER,
                    'District Number' INTEGER
                    )'''
        cursor.execute(sql_statement)
        db.commit()
        cursor.close()

    def insert_data(self, ID: str='Dummy User ID Number',
                    Name: str='Sample Tribute Name',
                    Nickname: str='Primary Nickname String',
                    Age: int=12,
                    District: int=1):
        """
        This method inserts tribute-related data into the database file.

        Args:
            ID (str, optional): [description]. Defaults to 'Dummy User ID Number'.
            Name (str, optional): [description]. Defaults to 'Sample Tribute Name'.
            Nickname (str, optional): [description]. Defaults to 'Primary Nickname String'.
            Age (int, optional): [description]. Defaults to 12.
            District (int, optional): [description]. Defaults to 1.
        """
        cursor = db.cursor()    # Creates Cursor
        #? This statement is defined above cursor.execute() to reflect that the tuple is being applied to the SQL statement.
        sql_statement = '''INSERT INTO tributes('User ID', 'Tribute Name', 'Nicknames', 'Age', 'District Number') VALUES (?, ?, ?, ?, ?)'''
        cursor.execute(sql_statement,
            (ID,
            Name,
            Nickname,
            Age,
            District))  # Selects Everything From The Tributes Table
        cursor.close()

    def view_data(self):
        """
        This method selects everything from t
        """
        cursor = db.cursor()    # Creates Cursor
        cursor.execute('''SELECT * FROM tributes''')    
        rows = cursor.fetchall()
        print(f"rows data type: {type(rows)}\n")
        for row in rows:
            print(row)
        cursor.close()
    
    

# MAIN METHOD
def main():
    """
    Description:
    This is the main function of the script, called when the module is ran directly.
    """
    sample_db = Tribute_Database()
    sample_db.insert_data()
    sample_db.view_data()

# DRIVER CODE
if __name__ == "__main__":
    main()
    input("Press Enter To Exit.") #? This is added to keep the script from exiting after the logic is ran.
    db.close()
else:
    print(f"{__name__} was successfully imported.", "\n".join(__doc__))
