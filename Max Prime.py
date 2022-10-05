#N以下の最大の素数を求める


#　素数判定部分 （True or False）
def is_prime(K):
    for i in range(2,int(K**(1/2))+1):
        if K%i==0:
            return False
    if K==1:
        return False
    return True
    
N = int(input())
for i in range(N,0,-1):
    if is_prime(i):
        print(i)
        break
        
