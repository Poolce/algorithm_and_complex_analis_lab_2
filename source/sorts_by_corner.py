import numpy as np
import source.functions as fun
import source.avl_tree as avl
import source.merge_sort_four as mg
import source.red_black_tree.rb_tree as rb

def rb_sort_by_corner(arr,min_index):
    rb_tree = rb.RedBlackTree()
    for i in range(len(arr)):
        if(i==min_index):
            continue
        corner = fun.get_corner(fun.get_vector(arr[min_index],arr[i]))
        rb_tree.insert(corner,i)

    return rb_tree.sort_list_by_rb(rb_tree.root)

def avl_sort_by_corner(arr,min_index):
    rt = None
    avl_a = avl.avl_tree()
    for i in range(len(arr)):
        if(i==min_index):
            continue
        corner = fun.get_corner(fun.get_vector(arr[min_index],arr[i]))
        rt = avl_a.insert(corner,i,rt)

    return avl_a.sort_list_by_avl(rt)

def merge_3_sort_by_corner(arr,min_index):
    sort_arr = []
    for i in range(len(arr)):
        if(i==min_index):
            continue
        corner = fun.get_corner(fun.get_vector(arr[min_index],arr[i]))
        sort_arr.append([i,corner])
    sort_arr = mg.merge_sort_k(sort_arr,3)
    
    res = []
    for dot in sort_arr:
        res.append(dot[0])
    return res