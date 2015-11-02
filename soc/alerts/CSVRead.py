import csv
import datetime
import happybase

class PollutantionData:
    name = ''
    Date = ''
    # AQS_SITE_ID = 0
    # POC_Daily_Max_8_hour_CO_Concentration = 0
#     UNITS = ''
    DAILY_AQI_VALUE = 0
#     DAILY_OBS_COUNT = 0
#     PERCENT_COMPLETE = 0
#     AQS_PARAMETER_CODE = 0
#     AQS_PARAMETER_DESC = ''
    STATE = ''
    COUNTY_CODE = 0
    COUNTY = ''
    SITE_LATITUDE = 0.0
    SITE_LONGITUDE = 0.0


    # Connect to hbase.
# connection = Connection('localhost',port=9000)
connection = happybase.Connection('localhost', port=9090)
print connection.tables()

#Create table if doesnt already exist.
# connection.create_table(
#     'pollution',
#     {'co': dict(max_versions=1)
#     }
# )
table_pollution = connection.table('pollution')
# table_pollution.put('1',{'co:name':'Srinija','co:date':'10/31/2015'})

# print table_pollution.row('1',['co:name'])

with open('resources/MD-2015.csv', 'rb') as csvfile:
    tempreader = csv.reader(csvfile, delimiter=',', quotechar='|')

    # First row is just the header. Use it to make Hbase column names.
    print tempreader.next()

    batch_data = table_pollution.batch()

    for row in tempreader:
        batch_data.put(row[0],{'co:DAILY_AQI_VALUE':row[5], 
            'co:STATE_CODE':row[12],
            'co:STATE':row[13],
            'co:COUNTY_CODE':row[14],'co:COUNTY':row[15],
            'co:SITE_LATITUDE':row[16], 'co:SITE_LONGITUDE':row[17]})

    batch_data.send()


# connection.disable_table('pollution');
# connection.delete_table('pollution')

connection.close()