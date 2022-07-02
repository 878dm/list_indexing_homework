def main(list_num):
    """
    A list of numbers consisting of several elements is given. Return the largest between the first and last elements.
    Args:
        list_num (list): parameter
    Returns:
        int: return answer
    """
    l=list_num.pop(0)
    k=list_num.pop(-1)
    x=max(l,k)
    return x
