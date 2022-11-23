import source.sorts_by_corner as sort
import source.functions as fun
import ui


def main():
    dots = fun.get_random_dots(10000)

    ui.gen_method_page(dots, sort.avl_sort_by_corner,'С помощью АВЛ-дерева')
    ui.gen_method_page(dots, sort.merge_3_sort_by_corner,'С помощью сортировки 3-слиянием')
    ui.gen_method_page(dots, sort.rb_sort_by_corner,'С помощью красно-черного дерева')


if __name__ == '__main__':
    main()