"""
list: [1,3,5,7,9] output => [3,5,7]
"""

result = [1,3,5,7,9]
delItems = {1,9}
def fn_hack_8():
    resList = [i for i in result if i not in delItems]
    return resList