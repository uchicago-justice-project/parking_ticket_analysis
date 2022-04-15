
import csv
import sqlite3
import pandas as pd

CONNECTION = sqlite3.connect("city_tickets.sqlite3")

def read_sheet():
    """
    pulls data and inserts into sql table

    Returns: (pandas dataframe) parking ticket data with selected columns
    """
    parking_tickets = pd.read_csv("parking_tickets.csv", usecols= ["ticket_number", "issue_date", "violation_location"])
    # insert_sql(parking_tickets, 'parking')
    return parking_tickets


def insert_sql(df,table_name):
    '''
    insert latest data into sql table

    Inputs:
        incidents (df): dataframe of new data
        name (str): name of table to insert into
        path (str): file path to sql file

    '''
    df.to_sql(table_name, CONNECTION, if_exists='append')


def df_query():
    '''
    skeleton code to query sqlite3 database
    '''
    connection = CONNECTION
    parking = connection.cursor()

    parking_query = '''
        SELECT
        FROM parking
        '''

    parking_query = (parking_tickets.execute(parking_query).fetchall())


# Findings
# DtypeWarning: Columns (6,9,19,21) have mixed types
# Specify dtype option on import or set low_memory=False.

# fields in raw dataset
# # ticket_number,issue_date,violation_location,license_plate_number,license_plate_state,license_plate_type,
# zipcode,violation_code,violation_description,unit,unit_description,vehicle_make,fine_level1_amount,fine_
# level2_amount,current_amount_due,total_payments,ticket_queue,ticket_queue_date,notice_level,hearing_disposition,notice_number,officer,address