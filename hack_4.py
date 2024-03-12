"""
text: "fooziman" output => "foozimaN"
"""

def fn_hack_4():
    result = "FOOZIMAn"
    result = result.swapcase()
    return result