##最小公倍数（LCM）

def GCD(N,M):

    if M==0:

        return N

    else:

        return GCD(M,N%M)
        


def LCM(X,Y):
    
    K = GCD(X,Y)
    
    return int((X/K)*(Y/K)*K)