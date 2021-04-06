import re
import pandas as pd
import numpy as np

def use_dates(column_dates):
    '''This function will receive a date in the dd-mm-yyyy format, get rid
    of anything that isn't an actual date, change the date format to 
    yyyy-mm-dd all numerical and return it as the date changed or as a string
    'Not useful.' if the function deans it as such.'''

    from datetime import datetime
    regex_date = '\d+[- ]\w{3,}[- ]\d{4}'
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

def better_dates(date_all):
    from dateutil import parser
    from datetime import datetime
    try:
        date_use = parser.parse(date_all)
        string_date = str(date_use.year) + '-' + str(date_use.month) + '-' + str(date_use.day)
        
        return datetime.strptime(string_date, "%Y-%m-%d").date()
    except:
        return 'Not useful.'


def ranged_list(list_range,signal,amount):
    list_randok = []
    if signal == '-':
            for x in list_range:
                list_randok.append(str(x.year - amount) + '-' + str(x.month) + '-' + str(x.day))
            
            return list_randok
    
    else:
        for x in list_range:
            list_randok.append(str(x.year + amount) + '-' + str(x.month) + '-' + str(x.day))

        return list_randok

def fmt_date(date_to_format):
    from datetime import datetime
    return datetime.strptime(date_to_format, "%Y-%m-%d").date()
    


# Imports file and drop 3 columns considered to be useless
shark_data = pd.DataFrame(pd.read_csv('data/attacks.csv'))
acdc_ab = pd.DataFrame(pd.read_csv('data/acdc_albums.csv'))
shark_data.drop(['Unnamed: 22','Unnamed: 23','Case Number.2'],axis=1,inplace=True)


#Drops rows with all columns NaN and also those that have less than 15 columns of Data.
shark_data.dropna(axis=0, how='all',inplace=True)
shark_data.dropna(axis=0, thresh=15,inplace=True)


#Calls the function use_dates to change the date formate from dd-mm-yyyy to yyyy-mm-dd all numerical
shark_data['date_check'] = shark_data['Date'].apply(use_dates)


#Drops all the rows deemed not useful and converts column to date type.
shark_data.drop(shark_data.index[shark_data['date_check']== 'Not useful.'],inplace=True)
shark_data['date_check'] =  pd.to_datetime(shark_data['date_check'])


#Sorts the data by date and then assign to the original Date column.
shark_data = shark_data.sort_values(by="date_check")
shark_data['Date'] = shark_data['date_check']
shark_data.reset_index(inplace=True)
shark_data.drop(columns=['date_check','index','Case Number','Case Number.1','original order'],inplace=True)

acdc_ab['Release Date'] = acdc_ab['Release Date'].apply(lambda x: re.sub('Released: ', '', x)).apply(better_dates)
release_date_list = acdc_ab['Release Date'].tolist()
lista_menos = ranged_list(release_date_list,'-',1)
lista_mais = ranged_list(release_date_list,'+',1)
before_lst = []
after_lst = []

for i in range(len(release_date_list)-1):
    date_bef = fmt_date(lista_menos[i])
    date_aft = fmt_date(lista_mais[i])
    date_rls = release_date_list[i]
    before_lst.append(len(shark_data[(shark_data['Date'].dt.date >date_bef) & (shark_data['Date'].dt.date <date_rls)]))
    after_lst.append(len(shark_data[(shark_data['Date'].dt.date >date_rls) & (shark_data['Date'].dt.date <date_aft)]))