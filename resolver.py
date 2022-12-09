"""
resolves card deck cards to their actual values
"""
def resolve(n):
    """
    resolves card deck cards to their actual values
    """
    if n == "A":
        return 1
    elif n in ["J", "Q", "K"]:
        return 10
    else:
        return n
