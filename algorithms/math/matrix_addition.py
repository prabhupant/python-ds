def addition(a, b):
    if len(a)==len(b):
        y=[]
        m=0
        while m<len(a):
            c=a[m]+b[m]
            m=m+1
            y.append(c)
    return y


def matrix_addition(A, B):
    m=0
    u=[]
    if len(A[m])!=len(B[m]):
        return "Matrices A and B don't have the same dimensions"
    elif len(A)==len(B):
        while m<len(A):
            t=addition(A[m],B[m])
            m=m+1
            u.append(t)
        return u
