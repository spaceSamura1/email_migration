"""
Creates a new csv containing the users with the target email domain for the email migration.

Needs to receive a csv downloaded from the source G-Suite domain.

The newly created csv will be uploaded to the target G-Suite account to bulk create new users - these are the targets for the migration.

The newly created csv will also be used in ``bulk_upload.py`` so it can pull the new email into its own csv which will be used to initiate the migration. 
"""


import csv
from csv import reader
import pandas as pd
from operator import setitem

import datetime
x = datetime.datetime.now()
date = x.strftime("%m") + x.strftime("%d") + x.strftime("%y")

#=================================================
#Read and store data from csv
#=================================================
csv = input('List of emails to convert: ')
target_users = []

with open(csv) as file:
    csv_reader = reader(file)
    for row in csv_reader:
        target_users.append(row)

#=================================================
#create a list to contain new emails
#take first initial + last name and prepend to @sonsray.com to create new email address
#append new email to sonsray_emails list
#=================================================
sonsray_emails = []
domain = '@sonsray.com'

for i in range(1, len(target_users)):
    first_initial = target_users[i][0][0].lower()
    last_name = target_users[i][1].lower()
    new_email = first_initial + last_name + domain
    sonsray_emails.append(new_email)


#=================================================
#Replace tksvinc email in target_users with new sonsray email
#=================================================
for i in range(1, len(target_users)):
    target_users[i][2] = sonsray_emails[i-1]


#=================================================
#Write target_users list to csv
#=================================================
location = input('Enter Location: ')
df = pd.DataFrame(target_users)
df.to_csv(f"new_sonsray_profiles_{location}_{date}.csv",index=False)
