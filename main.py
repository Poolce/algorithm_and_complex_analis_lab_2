import numpy as np
import matplotlib.pyplot as plt
import source.grehem as grm
from timeit import default_timer as timer
import source.sorts_by_corner as sort
import source.functions as fun
import source.red_black_tree.rb_tree as rb

# dots = fun.get_random_dots(500)

# a = grm.grehem(dots,sort.merge_3_sort_by_corner)


# x = []
# y= []

# for i in a:
#     x.append(i[0])
#     y.append(i[1])



# fgr = plt.figure()
# graph = fgr.add_subplot(111)
# graph.plot(x,y,'r-o')

# arr_x = np.transpose(dots)[0]
# arr_y = np.transpose(dots)[1]

# plt.plot(arr_x,arr_y,'b*')
# plt.ylabel('Time')
# plt.xlabel('Ellements')
# plt.show()


tree = rb.RBTree()
for x in range(1, 51):
    tree.insert(x)

tree.print_tree([1,2])
