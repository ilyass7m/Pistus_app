import sqlite3
import utils


def create_database(conn,cursor):
        """Creates the PistusResa database

    Parameters
    ----------
    conn : 
        The object used to manage the database connection.
    cursor : 
        The object used to query the database.

    Returns
    -------
    bool
        True if the database could be created, False otherwise.

    """
        cursor.execute('BEGIN')

    # Create the tables.
        try:
            # We create the table Login.
            # To do so, we call the function cursor.execute() and we pass it the

            print("Creating the table Login....")
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Login(
                    username TEXT PRIMARY KEY,
                    password BINARY(256)
                )
            ''')

        
            print("Creating table Student...")
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Student(
                stud_number INTEGER PRIMARY KEY,
                first_name TEXT,
                last_name TEXT,
                gender TEXT
                ) 
            ''')

            print("Creating table EmailAddress...")
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS EmailAddress(
                    email TEXT  PRIMARY KEY,
                    stud_number INTEGER,
                    FOREIGN KEY(stud_number) REFERENCES Student(stud_number)
                ) 
            ''')

            print("Creating table Association...")
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Association(
                    asso_name TEXT PRIMARY KEY,
                    asso_desc TEXT
                ) 
            ''')

            print("Creating table Membership...")
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Membership(
                    stud_number INTEGER,
                    asso_name TEXT,
                    stud_role TEXT,
                    PRIMARY KEY(stud_number, asso_name),
                    FOREIGN KEY(stud_number) REFERENCES Student(stud_number),
                    FOREIGN KEY(asso_name) REFERENCES Association(asso_name)
                ) 
            ''')

            print("Creating table PistusEdition...")
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS PistusEdition(
                    year TEXT PRIMARY KEY,
                    registration_fee REAL
                ) 
            ''')

            print("Creating table Registration...")
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Registration(
                    stud_number INTEGER,
                    year TEXT,
                    registration_date TEXT,
                    payment_date TEXT,
                    PRIMARY KEY(stud_number, year),
                    FOREIGN KEY(stud_number) REFERENCES Student(stud_number),
                    FOREIGN KEY(year) REFERENCES PistusEdition(year)
                ) 
            ''')

        ###################################################################

        # Exception raised when something goes wrong while creating the tables.
        except sqlite3.Error as error:
            print("An error occurred while creating the tables: {}".format(error))
            # IMPORTANT : we rollback the transaction! No table is created in the database.
            conn.rollback()
            # Return False to indicate that something went wrong.
            return False

        # If we arrive here, that means that no error occurred.
        # IMPORTANT : we must COMMIT the transaction, so that all tables are actually created in the database.
        conn.commit()
        print("Database created successfully")
        # Returns True to indicate that everything went well!
        return True
      


if __name__ == "__main__":

    # Loads the app config into the dictionary app_config.
    app_config = utils.load_config()

    # From the configuration, gets the path to the database file.
    db_file = app_config["db"]

    # Open a connection to the database.
    conn = sqlite3.connect(db_file)

    # The cursor is used to execute queries to the database.
    cursor = conn.cursor()

    # Creates the database. THIS IS THE FUNCTION THAT YOU'LL NEED TO MODIFY
    create_database(conn, cursor)

    # Closes the connection to the database
    cursor.close()
    conn.close()
