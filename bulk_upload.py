import csv
from csv import reader
import pandas as pd 

import datetime
x = datetime.datetime.now()
date = x.strftime("%m") + x.strftime("%d") + x.strftime("%y")

#=================================================
#Read/Store data from sonsray + tksvinc emails
#=================================================
def read_csv(csv, lst):
    with open(csv) as file:
        csv_reader = reader(file)
        for row in csv_reader:
            lst.append(row)
            
sonsray_emails_csv = input('Input Sonsray CSV: ') #csv created from convert_email.py
tksvinc_emails_csv = input('Input Tksvinc CSV: ') #csv downloaded from google with original @tksvinc domain 

sonsray_email_list = [] 
tksvinc_email_list = [] 

read_csv(sonsray_emails_csv, sonsray_email_list)
read_csv(tksvinc_emails_csv, tksvinc_email_list)


#=================================================
#Zip email lists together to prep data for writing to CSV
#=================================================

zipped_emails = list(zip(sonsray_email_list, tksvinc_email_list))


#=================================================
#Create new list with format of: sonsray_email, tksvinc_email, password
#=================================================
bulk_upload_format = []

new_sonsray_email = zipped_emails[1][0][2]
tksvinc_email = zipped_emails[1][1][2]
email_password = zipped_emails[1][1][3]

for i in range(1, len(zipped_emails)):
    bulk_upload_format.extend([[zipped_emails[i][0][2], zipped_emails[i][1][2], zipped_emails[i][1][3]]])


#=================================================
#Write bulk_upload_format to csv 
#=================================================
df = pd.DataFrame(bulk_upload_format)
df.to_csv(f'bulk_upload_sonsray_{date}.csv', index=False)