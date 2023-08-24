"""The ETL module.

Look at the instructions after the statement if __name__ == "__main__":

* First, we extract the data from the input CSV files into a collection of Pandas dataframes.
  Each dataframe corresponds to a table in the target relational database.
* Then, we transform the data in the dataframes.
* Finally, we load the data into the database.

"""

import pandas as pd
import sqlite3
import os
import db
import utils


from datetime import datetime

def get_right_date(input_date):
    '''
    converts the dates in the the data csv file in format  to the right format
    '''
    if pd.isnull(input_date):
        return None
    
    try:
        input_date=datetime.strptime(input_date,'Y%-m%-d%')
    except ValueError: 
        return None
    
    return datetime.strftime(input_date, 'd%/m%/Y%')



def extract():
    """Implementation of the extraction submodule.

    Returns
    -------
    dictionary
        The collection of dataframes containing the data of the input CSV files.
        You should have as many dataframes as tables in your relational database.
        Each dataframe corresponds to a table in the relational database.
        The dictionary contains a set of key-value pairs where
            * the value is a dataframe. 
            * the key is the name of the table corresponding to the dataframe  (e.g., "Student", "EmailAddress"...)

    """

    # This is the dictonary containing the collection of dataframes.
    # Each item of this dictionary is a key-value pair; the key is the name of a database table;
    # the value is a Pandas dataframe with the content of the table.
    dataframes = {}

    print("Extracting the data from the input CSV files...")

    ################## TODO: COMPLETE THE CODE OF THIS FUNCTION  #####################

    student_registrations = pd.read_csv(
        "./data/student_registrations.csv", delimiter=";")
    student_memberships = pd.read_csv(
        "./data/student_memberships.csv", delimiter=";")

    dataframes['Student'] = student_registrations[[
        'stud_number', 'first_name', 'last_name', 'gender']]
    dataframes['EmailAddress'] = student_registrations[[
        'stud_number', 'email']]
    dataframes['Association'] = student_memberships[['asso_name', 'asso_desc']]
    dataframes['Membership'] = student_memberships[[
        'stud_number', 'asso_name', 'stud_role']]
    dataframes['PistusEdition'] = student_registrations[[
        'year', 'registration_fee']]
    dataframes['Registration'] = student_registrations[[
        'stud_number', 'year', 'registration_date', 'payment_date']]

    ##################################################################################

    # Return the dataframe collection.
    return dataframes


def transform(dataframes):
    """Implementation of the transformation submodule.

    Parameters
    ----------
    dataframes : dictionary
        This is the dictionary returned by the function load()

    Returns 
    -------
    The input dictionary (after the transformations).
    """

    print("Transforming the data...")

    ################## TODO: COMPLETE THE CODE OF THIS FUNCTION  #####################

    # Remove duplicates
    dataframes['Student'] = dataframes['Student'].drop_duplicates()
    dataframes['EmailAddress'] = dataframes['EmailAddress'].drop_duplicates()
    dataframes['Association'] = dataframes['Association'].drop_duplicates()
    dataframes['PistusEdition'] = dataframes['PistusEdition'].drop_duplicates()

    # Make gender values uniform
    dataframes['Student'] = dataframes['Student'].replace(
        {'gender': {'garçon': 'M', 'H': 'M', 'fille': 'F', 'W': 'F'}})

    # Convert the dates to dd/mm/yyyy
    dataframes["Registration"]["registration_date"] = \
        dataframes["Registration"]["registration_date"].map(get_right_date)

    dataframes["Registration"]["payment_date"] = \
        dataframes["Registration"]["payment_date"].map(get_right_date)

    ##################################################################################

    # Returns the dataframe collection after the transformations.
    return dataframes


def load(dataframes):
    """Implementation of the load submodule.

    Parameters:
    ----------
    dataframes : dictionary
        The dictionary returned by the function extract()
    """
    # Loads the application configuration.
    app_config = utils.load_config()

    # Gets the path to the database file.
    database_file = app_config["db"]

    # You might bump into some errors while debugging your code which
    # This might result in a database that is partially filled with some data.
    # Each time you rerun the ETL module, you want the database to be in the same state as when
    # you first created.
    # The simpler solution here is to remove the database and recreate the tables back again.
#   if os.path.exists(database_file):
    # If the database file already exists, we remove it.
    # In order to test the existence of a file, and to remove it, we use functions that are
    # available in a Python module called "os".
#        os.remove(database_file)

    # We open a connection to the database.
    conn = sqlite3.connect(database_file)

    # We get the cursor to query the database.
    cursor = conn.cursor()

    # We create the tables in the database, by using the function create_database that you implemented in the module
    # db.
#    db.create_database(conn, cursor)

    print("Loading the data into the database...")

    ################## TODO: COMPLETE THE CODE OF THIS FUNCTION  #####################

    dataframes['Student'].to_sql(
        'Student', conn, if_exists="append", index=False)
    dataframes['EmailAddress'].to_sql(
        'EmailAddress', conn, if_exists="append", index=False)
    dataframes['Association'].to_sql(
        'Association', conn, if_exists="append", index=False)
    dataframes['Membership'].to_sql(
        'Membership', conn, if_exists="append", index=False)
    dataframes['PistusEdition'].to_sql(
        'PistusEdition', conn, if_exists="append", index=False)
    dataframes['Registration'].to_sql(
        'Registration', conn, if_exists="append", index=False)

    conn.commit()

    ##################################################################################

    print("Done!")

    # We close the connection to the database.
    cursor.close()
    conn.close()


# Entry point of the ETL module.
if __name__ == "__main__":

    ################## TODO: COMPLETE THE CODE OF THIS FUNCTION  #####################

    # REMOVE THIS BEFORE WRITING YOUR CODE.
    # pass is only added here to avoid the error mark that Visual Studio Code
    # uses to indicate some missing code.
    load(transform(extract()))

    ##################################################################################
