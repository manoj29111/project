c= "ccd"
e = "jjd"
x = {}; 
y = {};
def is_isomorphic(c, e):
    if len(c) != len(e):
        return False
    else:
        for i, v in enumerate(e):
            if v in x and x[v] != c[i]:
                return False
            else:
                x[v] = e[i]
            if e[i] in y and y[e[i]] != v:
                return False
            else:
                y[e[i]] = v
        return True
print is_isomorphic(c, e)