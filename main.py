import json
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

subject_id = 1024

x = json.load((open('data/%d.0.json' % subject_id)))

# x[step_id] = (time, affectiva)

# example:
step_id = '0'
time_step = 0
time_stamp = x[step_id][time_step][0]
aff = x[step_id][time_step][1]
expression = aff['expressions']
emotions = aff['emotions']

'''
# emotions graphs for each step
for step_id in x.keys():
    if x[step_id] == {}:
        continue
    x_axis = [x[step_id][i][0] for i in range(len(x))]  #all time steps in step_id
    y_axis = [x[step_id][i][1]['emotions'][4] for i in range(len(x))]   #all surprise rank in each time step
    plt.plot(x_axis,y_axis)
    plt.title('step %s engagement level' % step_id)
    plt.xlabel('time stamp')
    plt.ylabel('valence')
    #plt.show()
'''

# median joy for each step
x_axis = []
y_axis = []

for step_id in x.keys():
    if x[step_id] == {}:
        continue
    x_axis.append(np.median([x[step_id][i][1]['emotions'][0] for i in range(len(x))]))   #all surprise rank in each time step

df = pd.read_excel('all_data_task_normalized.xlsx', index_col=0)

df['joy_median'] = np.where((df['subject_id'] == subject_id) & (df['step_id'] == 0), x_axis[0], None)
for i in range(1,len(x_axis)):
    df['joy_median'] = np.where((df['subject_id'] == subject_id) & (df['step_id'] == i), x_axis[i], df['joy_median'])

#print(df[df['subject_id'] == subject_id][['subject_id','step_id','joy_median']])


for i in range(len(x_axis)):
    y_axis.append(df[(df['subject_id'] == subject_id) & (df['step_id'] == i)]['sum_matrix_error'].values[0])

print(x_axis)
print(y_axis)

plt.scatter(x_axis,y_axis, s=5)
plt.title('median joy VS sum matrix error')
plt.xlabel('median joy')
plt.ylabel('sum matrix error')
plt.show()
