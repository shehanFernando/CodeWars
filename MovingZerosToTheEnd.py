#Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

def move_zeros(array):
    newAr =[]
    counter = []

    for i in array:
        if type(i) == type(False) or i != 0:
            newAr.append(i)

        else:
            counter.append(0)

    return newAr+counterWrite
