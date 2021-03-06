'''
################################################################################
#                               Write the Stuff                                #
################################################################################
'''

import os
import json
import copy

def writeDataToFile(filename,data,catagories,types,subtypes,comments,cur_data):
    new_data = copy.deepcopy(cur_data) # So that you don't overwrite stuff #paranoid

    ## Compare catgories and prepare new_data ##
    cur_cat = []
    for cat in cur_data['data'].keys():
        cur_cat.append(cat)

    if (len(catagories) - len(cur_cat)) == 0:
        print('No new catagories detected!')
    elif (len(catagories) - len(cur_cat)) == 1:
        print('1 new catagory detected!')
    else:
        print('%d new catagories detected!' % (len(catagories) - len(cur_cat)))

    for i,cat in enumerate(cur_cat): # Add the existing catagories
        try:
            new_data['data'][cat].append(float(data[i]))
        except ValueError: # This is the date
            print('Adding data for %s' % data[i])
            new_data['data'][cat].append(data[i])

    if len(catagories) > len(cur_cat): # Need to add a new catagory
        newcat = copy.copy(catagories)
        [newcat.remove(x) for x in cur_cat]
        newcatdata = [data[x] for x in range(0,len(data)) if catagories[x] not in cur_cat]
        for i,cat in enumerate(newcat):
            print('Adding a new catagory...')
            new_data['data'][cat] = [0.0] * (len(new_data['data']['Date']) - 1)
            new_data['data'][cat].append(float(newcatdata[i]))
            new_data['type'][cat] = types[-len(newcat)+i] # new cats will be at the end
            new_data['subtype'][cat] = subtypes[-len(newcat)+i]
            print('Data for %s added!' % cat)

    new_data['comment'] = comments

    with open(filename, "w") as write_file:
        json.dump(new_data, write_file)

    print('Data stored in %s.' % filename)
