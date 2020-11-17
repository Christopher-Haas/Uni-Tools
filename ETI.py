import itertools

def ConvertfromBaste10(x, n):
    buf = []
    while x != 0:
        print (x," / ",n," = ",x//n," Rest ", x % n)
        buf.append(x%n)
        x = x//n
    buf.reverse()
    return int(''.join([str(i) for i in buf]))

def ConvertfromBaste10Latex(x, n):
    buf = []
    while x != 0:
        print (x," / ",n," &= ",x//n,"\\text{ Rest }", x % n, "\\\\")
        buf.append(x%n)
        x = x//n
    buf.reverse()
    return ''.join([str(i) for i in buf])

class Logic(object):
    def __init__(self, expr, name):
        self.expr = expr
        self.name = name
    def __eq__(self, other):
        return self.name == other.name
def Wahrheitstabelle(Variablen,Terme):
    out = ""
    laenge = len(Variablen) + len(Terme)
    v = itertools.product([1,0], repeat = len(Variablen))
    v = [x for x in v]
    v.reverse()
    tab_sub = "|"
    for i in range(laenge):
        tab_sub += "c|"
    out += "\\begin{tabular}{"+tab_sub+"} \n \\hline\n"
    for Var in Variablen:
        if Var == Variablen[-1]:
            out += str(Var)
        else:
            out += str(Var) + " & "
    if Terme:
        out += " & "
    for Term in Terme:
        if Term == Terme[-1]:
            out += Term.name
        else:
            out += Term.name + " & "
    out += "\\\\\n\\hline\n"
    for line in v:
        for n in line:
            out += str(n) + " & "
        for k in Terme:
            out += str(k.expr(*line)) + " & "
        out = out[:-3]
        out += "\\\\\n"
    out += "\\hline\n\\end{tabular}"

    return out
    pass


# Hier die Funktionen definieren
f = Logic(lambda a, b, c : 1 if a+b+c >= 2 else 0,"f_1")
mint = Logic(lambda a,b,c : "", "Minterm")
maxt = Logic(lambda a,b,c : "", "Maxterm")
print(Wahrheitstabelle(["c","b","a"], [f,mint,maxt]))

