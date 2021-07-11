
def merge_sort(array):
    if len(array) > 1:
        m = len(array) // 2
        l = array[:m]
        r = array[m:]

        merge_sort(l)
        merge_sort(r)

        i = j = k = 0
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                array[k] = l[i]
                i += 1
            else:
                array[k] = r[j]
                j += 1
            k += 1
        while i < len(l):
            array[k] = l[i]
            i += 1
            k += 1
        while j < len(r):
            array[k] = r[j]
            j += 1
            k += 1
        return array


if __name__ == '__main__':
    print(merge_sort([1, 4, 2, 3, 5, 3, 5, 2]))
