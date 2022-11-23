import source.functions as fun

def grehem(arr,sort_func):
    min_index = 0
    shell = []

    for i in range(len(arr)):
        if(arr[i][1]<arr[min_index][1]):
            min_index = i

    shell.append(min_index)

    sorted_dots = sort_func(arr,min_index)

    shell.insert(0,sorted_dots[-1])

    index=0
    while index < len(sorted_dots):
        vec1=fun.get_vector(arr[shell[-2]], arr[shell[-1]])
        vec2=fun.get_vector(arr[shell[-1]], arr[sorted_dots[index]])
        if(fun.is_left_rotate(vec1,vec2)):
            shell.append(sorted_dots[index])
            index+=1
        else:
            shell.pop()
    res = []
    for i in shell:
        res.append(arr[i])
    return res


