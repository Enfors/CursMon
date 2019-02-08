#!/usr/bin/env python3

"""
Generate a simple input file.
"""

import random
import sys
import time

num = 0
val = 50
top = 100
bot = 0
direction = 0

while num < 70:
    steady = random.randint(5, 9)

    while steady > 0:
        val = val + direction * 5
        if val > top:
            val = top
        if val < bot:
            val = bot
        print(val)
        sys.stdout.flush()
        # time.sleep(0.2)
        steady = steady - 1
        num = num + 1

    direction = random.randint(-1, 1)
