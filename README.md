\Application description

Pistus (short for "Piston Ski") is an event organised by WACS (Winter Association CentraleSupélec) during the winter holidays every year. It's an awesome week-long mountain trip involving many activities (including skiing, snowboarding, raclette binges, and parties, just to name a few).

When a student wants to register for the Pistus, the organizers write to a spreadsheet (i.e., an Excel file) the student personal data, as well as the registration date and the registration fee. Students have the option to pay their dues immediately or later; in any case, the student must pay within 5 days of the registration, otherwise the registration is considered as expired and it is removed. The organizers will send a reminder by email 2 days before the deadline. Once the student pays, the organizers write the payment date to the spreadsheet.

The organizers keep two spreadsheets. One contains the registration data, that include the student personal data (student number, first and last name, gender and email addresses), the registration and payment dates, the registration fee and the year of the event. The other Excel file contains information on the association membership.

\his organization presents a lot of issues:

If students participate to several Pistus editions in different years, their data is replicated for each registration. This might lead to inconsistencies. For instance, if a student changes her email address, the organizers should remove all the references to her old email address in the spreadsheets; these manual modifications are unlikely to be accurate.
The organizers must manually check whether a student meets the payment deadline.
The organizers must manually send email reminders to the students.
For this reason, we want to develop a software, called PistusResa, that the organizers can use to manage the registrations in an efficient way.

\The application consists of a graphical user interface (GUI) that allows an organizer to access all its functionalities. The backend consists of five modules, each dedicated to a specific functionality:

The Student module allows an organizer to manage the students personal data.
The Registration module allows an organizer to manage the registrations to the Pistus editions.
The Authentication module provides the functionalities to restrict the use of PistusResa to authorized users.
The Deadline module is a background process that manages the payment deadlines. Its two main functionalities are: sending an email reminder for unpaid registrations two days before the deadline and removing the expired registrations.
PistusResa uses a relational database to store all the data. Two additional modules are used to create the database and import the data into it.

The db module is used to create the database and its tables.
The ETL (Extract, Transform, Load) module is used to import into the database the data on the past Pistus editions that are kept in the two spreadsheets mentioned above.

--------------------------------------------------------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------------------------------------------------------

\Skeleton of the application : 
    \In folder config you'll find three files related to the configuration of the application.
        
        File config contains a list of key-value pairs describing the program settings:
        The name and the language of the application,
        The path to the database file,
        The reference reference to the messages bundle file (see below).
        Whether the authentication module of the application is enabled or not.
        Files messages_bundle_en and messages_bundle_fr contain all the text (labels, buttons, error messages) shown in the application GUI in English and French respectively. In the bundle, each message is identified by a key. In the program code, each message is referred to by using its key; the actual message is not hard-coded in the program. This way, if we want to change the language, we can simply load a different bundle, without changing the code.

    
    \The folder data contains all the data sources of the application. In particular, we find the two CSV files student_memberships.csv and student_registrations.csv that contain the data to import into the database. The database file itself will be created in this folder.

    \The root folder of the application contains the aforementioned folders and a bunch of Python files that implement the modules shown in the architecture.

        authentication.py, the Authentication module.
        db_playground.py, it contains the code you'll have to play with in order to learn how to implement the db module.
        db.py, the db module.
        etl.py, the ETL module.
        mdeadline_playground.py, examples for the Deadline module.
