#!/usr/bin/env python3

"""
Generate a simple input file.
"""

import csv
import datetime
import os
import random
import time

num = 0
val = 50
top = 100
bot = 0
direction = 0

file_name = "input.csv"

if not os.path.exists(file_name):
    new_file = True
else:
    new_file = False

with open(file_name, mode="a") as csv_file:
    field_names = ["datetime", "loop_load"]

    writer = csv.DictWriter(csv_file, fieldnames=field_names)
    if new_file:
        writer.writeheader()
    while num < 200:
        
        steady = random.randint(5, 9)
        
        while steady > 0:
            val = val + direction
            if val > top:
                val = top
            if val < bot:
                val = bot
            # time.sleep(0.2)
            steady = steady - 1
            num = num + 1
            writer.writerow({"datetime": datetime.datetime.now().isoformat(),
                             "loop_load": val})
            csv_file.flush()
            time.sleep(60)
            
        direction = random.randint(-8, 8)
