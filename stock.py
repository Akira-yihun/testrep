from matplotlib import pyplot as plt

def bondprice(cr, r, c, t):
    tlis = list(range(1,t+1))
    def discount(cr, r, c, n):
        cashlis = [(c*r)/(1+cr)**a for a in range(1,n+1)]
        cashlis.append(c/(1+cr)**n)
        return sum(cashlis)
    ylis = [discount(cr, r, c, i) for i in tlis]
    plt.plot(tlis,ylis)
    plt.show()

# little ytm
# test add to main
bondprice(0.15,0.03,100,30)