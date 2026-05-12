from multiprocessing import pool
import random

def bitonic_sort(arr):
    def compare_and_awap(i, j, up):
        if (arr[i] > arr[j] == up):
            arr[i], arr[j] = arr[j], arr[i]
    
    def bitonic_merge(low, cnt, up):
        if cnt > 1:
            mid = cnt // 2

            for i in range(low, low + mid):
                compare_and_awap(i, i+mid, up)
            bitonic_merge(low, mid, up)
            bitonic_merge(low+mid, mid, up)


