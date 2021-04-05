import re
import pandas as pd
import numpy as np


# Imports file and drop 3 columns considered to be useless
shark_data = pd.DataFrame(pd.read_csv('data/attacks.csv'))
shark_data.drop(['Unnamed: 22','Unnamed: 23','Case Number.2'],axis=1,inplace=True)
shark_complete = shark_data.dropna(axis=0, thresh=20).copy(deep=True)


#Drops rows with all columns NaN and also those that have less than 15 columns of Data.
shark_data.dropna(axis=0, how='all',inplace=True)
shark_data.dropna(axis=0, thresh=15,inplace=True)


#Calls the function use_dates to change the date formate from dd-mm-yyyy to yyyy-mm-dd all numerical
shark_data['date_check'] = shark_data['Date'].apply(use_dates)


#Converts column to date type.
shark_data['date_check'] =  pd.to_datetime(shark_data['date_check'])


#Drops all rows considered "Not useful." by the use_dates function, sorts it and than assign to the original Date column.
shark_data.drop(shark_data.index[shark_data['date_check']== 'Not useful.'],inplace=True)
shark_data = shark_data.sort_values(by="date_check")
shark_data['Date'] = shark_data['date_check']
shark_data.drop(columns=['date_check'])



def use_dates(column_dates):
    '''This function will receive a date in the dd-mm-yyyy format, get rid
    of anything that isn't an actual date, change the date format to 
    yyyy-mm-dd all numerical and return it as the date changed or as a string
    'Not useful.' if the function deans it as such.'''

    from datetime import datetime
    regex_date = '\d+-\w{3,}-\d{4}'
    try:
        try:
            date_to_use = re.findall(regex_date,column_dates)[0]
        except IndexError:
            return 'Not useful.'
        if re.match(regex_date, column_dates):
            try:
                return datetime.strptime(date_to_use, "%d-%b-%Y").date()
            except ValueError:
                return datetime.strptime(date_to_use, "%d-%B-%Y").date()
        else:
            return 'Not useful.'
    except ValueError:
        return 'Not useful.'