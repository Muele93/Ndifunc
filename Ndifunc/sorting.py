def bubble_sort(items):
    """When the item on the left side is greater than the one on the right, swap them"""
    array_copy = items.copy() #initialising array_copy which is a copy of item array
    for i in range(len(array_copy)):
        for j in range(len(array_copy)-1-i):
            if array_copy[j] > array_copy[j+1]:
                array_copy[j], array_copy[j+1] = array_copy[j+1], array_copy[j]
    return array_copy

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
