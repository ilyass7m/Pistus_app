"""This modules defines some useful functions that are 
called in different points of the application.

"""

import csv 

def load_config():
    '''
    returns the application configuration in a dictionnary 
    '''
    config={}

    with open ('Pistus_app\config\config','r', encoding='utf-8') as csv_file:
        csv_reader= csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            config[row[0]]=row[1]

    return config


def load_messages_bundle(message_bundle):
    """Loads the messages bundle from the given file into a dictionary.

    The messages bundle contains all the text (labels, button labels..) 
    that is shown in the application GUI.
    In the bundle, each message is identified by a key.
    In the program code, each message is referred to by using its key; the message is not hard-coded in the program.
    This way, if we want to change the language, we can simply load a different bundle, without changing the code.

    Parameters
    ----------
    messages_bundle_file : string
        The path to the file containing the messages bundle.

    Returns
    -------
    dictionary
        Contains the key-value pairs that compose the bundle.
    """
    
    message_bundle={}
    with open(message_bundle, 'r', encoding='utf-8') as csv_file:
        csv_reader=csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            message_bundle[row[0]]=row[1]

    return message_bundle


