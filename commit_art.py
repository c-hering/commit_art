#!/usr/bin/env python
import datetime
import time
import os

template = [
    [0,0,0,1,1,0,0],
    [0,0,0,0,0,1,0],
    [1,1,1,1,0,0,1],
    [0,0,0,0,0,0,1],
    [1,1,1,1,0,0,1],
    [0,0,0,0,0,1,0],
    [0,0,0,1,1,0,0]
]

# set this to the SUNDAY of which you want to start the commits
START_DATE = 14
LAST_DATE = 14
CURRENT_DATE = 14

for week in template:
    for day in week:
        if(template[week][day] == 1):
            with open('progress.txt', 'a') as file:
                file.write('Making a commit on day ' + str(CURRENT_DATE))
            os.system('git add *')
            os.system('git commit -m \' just making some pixel art :) \' ')
            os.system('git push origin master')
        CURRENT_DATE = datetime.datetime.now()
        while LAST_DATE == CURRENT_DATE:
            # wait 12 hours until checking again
            time.sleep(43200)
            CURRENT_DATE = datetime.datetime.now()
