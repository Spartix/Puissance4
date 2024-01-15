from ctypes import List

def Gen() -> List[List[int]]:
    lst = list()
    for _ in range(6):
        lss = list()
        for _ in range(7):
            lss.append(0)
        lst.append(lss)
    return lst
