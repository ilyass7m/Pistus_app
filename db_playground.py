"""Playground to learn how to interact with a SQLite database.
"""

import sqlite3
import utils


def insert_student(stud, cursor):
    """Inserts a student into to the database.

    Parameters
    ----------
    stud : A dictionary
        Student personal data: stud["stud_number"], stud["first_name"], stud["last_name"] and stud["gender"].
    cursor : 
        The object used to query the database.

    Returns
    -------
    bool
        True if no error occurs, False otherwise.

    """

    try:

        # The student is described by four attributes: stud_number, first_name, last_name and gender.
        # The values of these attributes are available in the dictionary stud, one of the parameters of this function.
        
       
        insert_query = "INSERT INTO Student (stud_number, first_name, last_name, gender) VALUES (?, ?, ?, ?)"

        # A tuple with the values that will replace the ? in the insert_query.
        query_values = (stud["stud_number"], stud["first_name"],
                        stud["last_name"], stud["gender"])


        cursor.execute(
            insert_query,
            query_values
        )
    # We catch here a sqlite3.IntegrityError that is raised whenever an integrity constraint is violated in the database.
    # Here the only integrity constraint that might be violated is the primary key constraint on the table Student
    # when we add two student with the same student number.
    except sqlite3.IntegrityError as error:
        print("Student number already taken: {}".format(error))
        return False
    # Here we catch any other database error that can arise from this insert query.
    except sqlite3.Error as error:
        print("A database error occurred while inserting the student: {}".format(error))
        return False

    # Everything is OK
    return True


def add_email_address(stud_number, email_address, cursor):
    """Adds the email address of a given student.

    Parameters
    ----------
    stud_number : int
        The student number.
    email_address : string
        The student email address.
    cursor : 
        The object used to query the database.

    Returns
    -------
    bool
        True if no error occurs, False otherwise.

    """

    # We add the membership information on the student.
    try:

        cursor.execute(
            "INSERT INTO EmailAddress VALUES (?, ?)",
            (email_address, stud_number)
        )

        ################################################################################################
    except sqlite3.IntegrityError as error:
        print("An integrity error occurred while inserting the email address: {}".format(error))
        return False
    except sqlite3.Error as error:
        print(
            "A database error occurred while inserting the email address: {}".format(error))
        return False

    return True


def insert_clara():
    """Inserts a student into the database.

    Returns
    -------
    bool
        True if the student could be inserted, False otherwise.
    """

    # Personal data of the student Clara
    clara = {"stud_number": 12,
             "first_name": "Clara",
             "last_name": "Degas",
             "gender": "F"
             }

    print("Insert the student Clara")
    if insert_student(clara, cursor):
        print("Clara added successfully :)")
        return True
    else:
        print("Impossible to add Clara :(")
        return False


# The entry point of this module.
if __name__ == "__main__":

    # Loads the app config into the dictionary app_config.
    app_config = utils.load_config()

    # From the configuration, gets the path to the database file.
    db_file = app_config["db"]

    # Open a connection to the database.
    conn = sqlite3.connect(db_file)

    # Enables the foreign key contraints support in SQLite.
    conn.execute("PRAGMA foreign_keys = 1")

    # The cursor is used to execute queries to the database.
    cursor = conn.cursor()

    cursor.execute("BEGIN")
    if insert_clara():
        conn.commit()
    else:
        conn.rollback()

    # Closes the connection to the database
    cursor.close()
    conn.close()