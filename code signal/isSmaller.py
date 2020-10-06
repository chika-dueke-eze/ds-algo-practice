def removeOneDigit(s, t):
    issmaller = 0
    s_lst = []
    s_index = 0
    s_count = 0
    for s_val in s:
        if s_val.isnumeric():
            s_count += 1
            s_lst.append(s_index)
        s_index+=1
        
    t_lst = []
    t_index = 0
    t_count = 0
    for t_val in t:
        if t_val.isnumeric():
            t_count += 1
            t_lst.append(t_index)
        t_index+=1
            
    for i in range(s_count):
        vals = s[s_lst[i]]
        s_iter = s.replace(vals, "")
        
        if s_iter < t:
            issmaller += 1
       
        
    for i in range(t_count):
        valt = t[t_lst[i]]
        t_iter = t.replace(valt, "")
        if s < t_iter:
            issmaller += 1
        
            
    return issmaller
