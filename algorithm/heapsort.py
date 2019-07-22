"""
1. heap_adjust函数保证左右子树都是大顶堆的情况下，调整后的树为大顶堆。（根节点不断下沉，直到比左右孩子都大的时候停止）
2. 根据1，初始化树的时候要从下（length/2）往上1，保证每下一层都是大顶堆
3. 排序时，每次取出大顶堆根节点，放到末尾。自上而下。
"""

from collections import deque


def swap_param(L, i, j):
    L[i], L[j] = L[j], L[i]
    return L


def heap_adjust(L, start, end):
    temp = L[start]

    i = start
    j = 2 * i

    while j <= end:
        if (j < end) and (L[j] < L[j + 1]):
            j += 1
        if temp < L[j]:
            L[i] = L[j]
            i = j
            j = 2 * i
        else:
            break
    L[i] = temp


def heap_sort(L):
    L_length = len(L) - 1

    first_sort_count = L_length / 2
    for i in range(first_sort_count):
        heap_adjust(L, first_sort_count - i, L_length)

    for i in range(L_length - 1):
        L = swap_param(L, 1, L_length - i)
        heap_adjust(L, 1, L_length - i - 1)

    return [L[i] for i in range(1, len(L))]


def main():
    L = deque([50, 16, 30, 10, 60,  90,  2, 80, 70])
    L.appendleft(0)
    print(heap_sort(L))


if __name__ == '__main__':
    main()
