#Prints a maximum set of activities that can be done by a 
#single person, one at a time
#n --> Total number of activities 
#s[]--> An array that contains start time of all activities 
#f[] --> An array that contains finish time of all activities 

def print_max_activities(s, f):
    n = len(f)

    # the first activity is always selected
    i = 0
    print(i, end=' ')

    # for the rest
    for j in range(n):
        if s[j] >= f[i]:
            print(j, end=' ')
            i = j
