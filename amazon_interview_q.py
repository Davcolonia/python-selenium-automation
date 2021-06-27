# create a function that will take a string as an input
def unique_letter(string: str):
    if not string:
        raise ValueError

    string = string.lower()
    for l in string.lower(): #O(n)
        if string.count(l) == 1: #O(n)
            return l
    return ""

# O(n) + O(n) = O(n^2)
print(unique_letter('llajhgjv'))

def unique_letter_optimal(string:str):
    if not string:
        raise ValueError
    string = string.lower()
    d = {}
    for l in string: #O(n)
        if l not in d:
            d[l] = 1
        else:
            d[l] += 1

        for k,v in d.items(): #O(n)
            if v == 1:
                return k
        return ""
