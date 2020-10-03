def makeArrayConsecutive2(statues):
    statues.sort()                                  #sort the  array in ascending order 
    min_val = statues[0]                            #take smallest value in array
    max_val = statues[-1]                           #take largest value in array
    len_arr = len(statues)                          #return length of array
    no_of_ideal_vals = (max_val - min_val) + 1      #get the no of values that should be present from min val to max value          
    vals2Complete = no_of_ideal_vals - len_arr      # subract no of vals in array from no of vals supposed to be present 
    return vals2Complete
