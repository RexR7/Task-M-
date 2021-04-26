I = input('Please enter a string ')
def most_frequent(string):
    A = dict()
    for key in string:
        if key not in A:
            A[key] = 1
        else:
            A[key] += 1
    return A
print (most_frequent(I))
