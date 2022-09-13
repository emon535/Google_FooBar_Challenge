def solution(x, y):
    xval = (x+y-1)*(x+y-2)
    xval = xval/2 + x
    return str(int(xval))
