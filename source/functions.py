import numpy as np
import random

def clear_data(arr,sorted_dots):
    i = 0
    while(i<len(sorted_dots)-1):
        if(arr[sorted_dots[i]][0]!=arr[sorted_dots[i+1]][0] or arr[sorted_dots[i]][1]!=arr[sorted_dots[i+1]][1]):
            i+=1
            continue
        else:
            arr.pop(sorted_dots[i])
            sorted_dots.pop(i)

def get_random_dots(size):
    dots = []    
    for i in range(size):
        res =[]
        res.append(random.random())
        res.append(random.random())
        dots.append(res)
    return dots


def get_vector(dot2,dot1):
    res = []
    res.append(dot1[0]-dot2[0])
    res.append(dot1[1]-dot2[1])
    return res

def get_corner(vec1):
    r = np.sqrt(np.square(vec1[0])+np.square(vec1[1]))

    res = np.arccos(vec1[0]/r)
    if(np.arcsin(vec1[1]/r)<0):
        res*=-1
    return res

def is_left_rotate(vec1,vec2):
    if(np.cross(vec1,vec2)>=0):
        return True
    return False