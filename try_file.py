import numpy_financial as npf
p = 5000
r = .09
n = 5

pmt =  npf.pmt(rate=r, nper=n, pv=-p)
print(pmt)
