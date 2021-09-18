from ch6_sort import mysort
def ch6_3(A:list,B:list,k:int):

    A.sort()
    B.sort(reverse=True)
    for i in range(k):
        if A[i] < B[i]:
            A[i],B[i] = B[i],A[i]
        else:
            break
    return sum(A)

if __name__ == "__main__":
    print(ch6_3(A=[1,2,5,4,3],B=[5,5,6,6,5],k=3))