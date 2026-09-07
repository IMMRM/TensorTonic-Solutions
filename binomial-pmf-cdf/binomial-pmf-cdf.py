import math


def binomial_pmf_cdf(n: int, p: float, k: int) -> dict:
    """
    Returns a dictionary with pmf and cdf.
    """
    # Write code here
    pmf=math.comb(n,k)*(p**k)*((1-p)**(n-k))

    res=0
    for i in range(0,k+1):
        pmf_i=math.comb(n,i)*(p**i)*((1-p)**(n-i))
        res+=pmf_i
    return {"pmf":float(pmf),"cdf":float(res)}
    