# TODO: doesn't work with all negative ints

def find_max_crossing_subarray(arr, lo, mid, hi):
    sum = 0
    lsum = float('-inf')
    li = lo
    for i in range(mid, lo-1, -1):
        sum += arr[i]
        if sum >= lsum:
            lsum = sum
            li = i

    rsum = float('-inf')
    rj = hi
    sum = 0
    for i in range(mid+1, hi+1):
        sum += arr[i]
        if sum >= rsum:
            rsum = sum
            rj = i

    return (li, rj, lsum + rsum)


def find_max_subarray(arr, lo, hi):
    if lo == hi:
        return (lo, hi, arr[lo])
    mid = lo + (hi-lo) // 2
    (lsum, li, lj) = find_max_subarray(arr, lo, mid)
    (rsum, ri, rj) = find_max_subarray(arr, mid+1, hi)
    (csum, ci, cj) = find_max_crossing_subarray(arr, lo, mid, hi)

    if lsum >= rsum and lsum >= csum:
        return (lsum, li, lj)
    if rsum >= lsum and rsum >= csum:
        return (rsum, ri, rj)
    if csum >= rsum and lsum >= csum:
        return (csum, ci, cj)


e1 = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
e2 = [-3, -4, -22, -1, -33, -5, -24]
print(find_max_crossing_subarray(e1, 0, len(e1)//2, len(e1)-1))
print(find_max_crossing_subarray(e2, 0, len(e2)//2, len(e2)-1))
