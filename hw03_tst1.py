
for n in range(0, 101):
    pi_series = (4*((-1)**i)/(2*i+1) for i in range(0, n+1))
    print("When n = {:,} : \u03C0 = {}".format(n, sum(pi_series)))
