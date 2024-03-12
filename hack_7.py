"""
loop: while [] output => [5,4,3,2,1,0]
"""

result = []
def fn_hack_7():
    for i in reversed(range(6)):
            result.append(i)
    return result 