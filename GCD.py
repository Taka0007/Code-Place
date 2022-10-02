
##最大公約数(GCD)

def GCD(N,M):

    if M==0:

        return N

    else:

        return GCD(M,N%M)