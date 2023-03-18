# algoritma tum degerlere gecer
# frequency girmek yeter
# ( m, mf, sigma f) program kendi hesapliyo

def Q1(a):
    print(f"1. Mean age is: {sum(a)/len(a)}")

def Q2(a):
    a.sort()
    a.append(0)
    b = [0,0]
    d = {}
    for c in range(len(a)-1):
        if a[c] != a[c+1]:
            d[a[c]] = 1
    for c in range(len(a)-1):
        if a[c] == a[c+1]:
            d[a[c]] += 1
    for c in d:
        b[0] += d[c] * c
        b[1] += d[c]
    print(f"\n2. Mean women's shoes size is: {round(b[0]/b[1],2)}")

def Q3(a):
    e = 0
    for c in range(len(a)):
        e += a[c][1][0]
        d = [(a[c][0][1]+a[c][0][0])/2,(a[c][0][1]+a[c][0][0])/2*a[c][1][0],e]
        for b in range(3):
            a[c][1].append(d[b])

    mf = 0
    i = a[c][0][1] - a[c][0][0]
    sig_f = d[2]
    for c in range(len(a)):
        mf += a[c][1][2]
    for c in range(len(a)):
        if a[c][1][3] >= sig_f / 2:
            l_med = a[c][0][0] 
            up_med = sig_f/2-(a[c][1][3]-a[c][1][0])
            under_med = a[c][1][0]
            break
    mode = 0
    for c in range(len(a)):
        if a[c][1][0] > mode:
            mode = a[c][1][0]
            l_mod = a[c][0][0]
            tn, tp = a[c][1][0], a[c][1][0]
            if c != 0:
                tp -= a[c-1][1][0]
            if c != len(a)-1:
                tn -= a[c+1][1][0]

    print(f"\n3. Mean: {round(mf/sig_f,2)}\n   Mode: {round(l_mod+tp/(tp+tn)*i,2)}\n   median: {round(l_med+up_med/under_med*i,2)}")                                      

Q1([24,26,20,18,24])
Q2([35,38,36,37,36,38,35,39,37])
Q3([[[0,10],[12]],
    [[10,20],[6]],
    [[20,30],[4]],
    [[30,40],[2]],
    [[40,50],[1]]])