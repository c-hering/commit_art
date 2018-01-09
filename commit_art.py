#!/usr/bin/env python
import datetime
# import sleep from time
import os

template = [
    [0,0,0,1,1,0,0],
    [0,0,1,0,0,0,0],
    [0,1,0,0,1,1,1],
    [0,1,0,0,0,0,0],
    [0,1,0,0,1,1,1],
    [0,0,1,0,0,0,0],
    [0,0,0,1,1,0,0]
]

# set this to the SUNDAY of which you want to start the commits
START_DATE = 14
LAST_DATE = 14
CURRENT_DATE = 14
os.system('git commit -m " just making some pixel art :) " ')
# for week in template:
#     for day in week:
#         if(template[week][day] == 1):
#             os.system('git commit -m \' just making some pixel art :) \' ')
#         CURRENT_DATE = datetime.datetime.now()
#         while LAST_DATE == CURRENT_DATE:
#             # wait 12 hours until checking again
#             sleep(43200)
#             CURRENT_DATE = datetime.datetime.now()
