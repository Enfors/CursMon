#!/usr/bin/env python3

"""
Generate a simple input file.
"""

import random
import time

num = 0
val = 50
top = 100
bot = 0
direction = 0

while num < 200:
    steady = random.randint(2, 5)

    while steady > 0:
        val = val + direction * 5
        if val > top:
            val = top
        if val < bot:
            val = bot
        print(val)
        # time.sleep(1)
        steady = steady - 1

    direction = random.randint(-1, 1)
    num = num + 1
