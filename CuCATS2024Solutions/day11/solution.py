import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from utilities import *
data = loadinput(os.path.join(os.path.dirname(__file__),"input.txt"))

course_length,num_reindeer = getints(data[0])

def speed(length,normal_speed,turbo_speed,cooldown,turbo_duration):
    pos = 0
    current_cooldown = 0
    current_turbo_time = 0
    time = 0
    while pos < length:
        time += 1
        prev = pos
        if turbo_speed<normal_speed:
            pos+=normal_speed
            continue
        if current_cooldown == 0: # activate turbo
            current_turbo_time = turbo_duration
            current_cooldown = cooldown
        if current_cooldown > 0 and current_turbo_time == 0: # turbo unavailable
            current_cooldown -= 1

        if current_turbo_time > 0: # turbo active
            pos += turbo_speed
            current_turbo_time -= 1
        else:
            pos += normal_speed
    return time - ((pos-length)/(pos-prev))
def speed2(length,normal_speed,turbo_speed,cooldown,turbo_duration):
    pos = 0
    current_cooldown = turbo_duration
    time = 0
    turbo = True
    while pos < length:
        time += 1
        prev = pos
        if turbo_speed<normal_speed:
            pos+=normal_speed
            continue
        if turbo:
            pos += turbo_speed
        else:
            pos += normal_speed
        current_cooldown -= 1
        if current_cooldown == 0:
            turbo = not turbo
            if turbo:
                current_cooldown = turbo_duration
            else:
                current_cooldown = cooldown
    return time - ((pos-length)/(pos-prev))

times = []
for line in data[1:]:
    nums = getints(line)
    times.append((line.split()[0],speed(course_length,nums[0],nums[1],nums[2],nums[3])))
times = sorted(times, key=lambda x: x[1])
print(times[:5])
times = []
for line in data[1:]:
    nums = getints(line)
    times.append((line.split()[0],speed2(course_length,nums[0],nums[1],nums[2],nums[3])))
times = sorted(times, key=lambda x: x[1])
print(times[:5])