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
    mf = 0
    i = a[0][0][1] - a[0][0][0]
    sig_f = a[len(a)-1][len(a[0][0])-1][len(a[0][1])-1]
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
Q3([[[30,36],[2,33,66,2]],
    [[36,42],[6,39,234,8]],
    [[42,48],[10,45,450,18]],
    [[48,54],[7,51,357,25]],
    [[54,60],[4,57,228,29]],
    [[60,66],[1,63,63,30]]])