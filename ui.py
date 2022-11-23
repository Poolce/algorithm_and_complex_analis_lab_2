import matplotlib.pyplot as plt
import numpy as np
import source.grehem as grm
from timeit import default_timer as timer

def gen_method_page(arr,sort_method,str):

    start_timer = timer()
    a = grm.grehem(arr,sort_method)
    time = timer()-start_timer


    x = []
    y = []

    for i in a:
        x.append(i[0])
        y.append(i[1])

    fgr = plt.figure()
    graph = fgr.add_subplot(111)
    graph.plot(x,y,'r-o')

    arr_x = np.transpose(arr)[0]
    arr_y = np.transpose(arr)[1]

    plt.plot(arr_x,arr_y,'b*')
    plt.xlabel(str+f" time = {time}")
    plt.show()