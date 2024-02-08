def binarySearch(start, end, ans, num):
    mid = (start + end) // 2
    if(num == ans):
        return num
    elif ans > num:
        return binarySearch(mid+1, end, ans, num)
    else:
        return binarySearch(start, mid+1, ans, num)
