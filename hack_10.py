"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def fn_hack_10():	
    old = "fooziman"
    old = old.replace("fooziman","F00Z1M@N")
    old2 = list(old) 
    return old2
