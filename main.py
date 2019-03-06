import json

subject_id = 1024

x = json.load((open('data/%d.0.json' % subject_id)))
# x[step_id] = (time, affectiva)

# example:
step_id = '0'
time_step = 10
time_stamp = x[step_id][time_step][0]
aff = x[step_id][time_step][1]
expression = aff['expressions']
emotions = aff['emotions']
print(time_stamp)
print(emotions)