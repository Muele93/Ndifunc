def bubble_sort(items):
    """The function returns a list which is sorted in a manner that places the greatr item on the left"""
    L = len(items)
    for x in range (0, L-1):
        for y in range (0, L-x-1):
            #When the item on the left side is greater than the one on the right, swap them
            if items[y]> items[y+1]:
                items[y],items[y+1]=items[y+1],items[y]

        return items

def merge_sort(items):
    """The function returns a sorted list"""

    L = len(items)
    if L<2:
        return items

    merged = []
    #The list is divided in the middle and adjacent items are then sorted
    middle = int(len(items)/2)

    Left_half = merge_sort(items[:middle])
    Right_half = merge_sort(items[middle:])
     #x is the index on Left_half and y is the index on Right_half
    x=y=0

    while x < len(Left_half) and y < len(Right_half):
        if Left_half[x] > Right_half[y]:
            merged.append(Right_half[y])
            y = y +1

        else:
            merged.append(Left_half[x])
            x = x+1

    merged = merged + Left_half[x:]
    merged = merged + Right_half[y:]

    return merged


def quick_sort(items):
    """The first element of the array is picked as the pivot. Elements less than the pivot go before it and those greater than it go after it"""
    below = []
    equal = []
    above = []

    if len(items) > 1:
        pivot = items[0]
        for i in items:
            if i < pivot:
                below.append(i)
            elif i == pivot:
                equal.append(i)
            elif i > pivot:
                above.append(i)
      #The function should return a list that is sorted in a way that elements less than 22 one before it and those greater go after it
        return quick_sort(below)+equal+quick_sort(above)
    #If the list only has one item, just return that item as it is
    else:
        return items
