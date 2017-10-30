def find_last(s, key):
    if s.find(key)==-1:
        return -1
    pos = 0
    while(s.find(key,pos)!=-1):
        pos = s.find(key,pos)
    return pos
    




print find_last('aaaa', 'a')