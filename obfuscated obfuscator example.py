# this isn't obfuscated using my obfuscator, because it doesn't support obfuscation of an actual obfuscator

import ast as a
import random as b
import string as c

def d(e=8):
    return ''.join(b.choices(c.ascii_letters, k=e))

def f(g):
    h = ''.join([chr(i) for i in [112, 114, 105, 110, 116]])
    eval(f"{h}({repr(g)})")

class i(a.NodeTransformer):
    def __init__(j):
        j.k = {}
        j.l = set()
        j.m = {}
        j.l.update({'f','h','g','chr','eval','n','input','o','p','a','i','b','c','d','__name__','__main__'})

    def q(r,s):
        return s in dir(__builtins__)

    def t(u,v):
        if v not in u.k:
            u.k[v] = d()
        return u.k[v]

    def w(x,y):
        return a.Call(
            func=a.Attribute(value=a.Constant(value=''), attr='join', ctx=a.Load()),
            args=[a.List(
                elts=[a.Call(
                    func=a.Name(id='chr', ctx=a.Load()),
                    args=[a.Constant(value=ord(z))],
                    keywords=[]) for z in y],
                ctx=a.Load())],
            keywords=[]
        )

    def visit_Import(A,B):
        for C in B.names:
            A.l.add(C.asname or C.name.split('.')[0])
        return B

    def visit_ImportFrom(D,E):
        for F in E.names:
            D.l.add(F.asname or F.name)
        return E

    def visit_FunctionDef(G,H):
        if H.name not in G.l:
            H.name = G.t(H.name)
        for I in H.args.args:
            if I.arg not in ('self',) and I.arg not in G.l:
                I.arg = G.t(I.arg)
        G.generic_visit(H)
        return H

    def visit_ClassDef(J,K):
        if K.name not in J.l:
            K.name = J.t(K.name)
        J.generic_visit(K)
        return K

    def visit_Name(L,M):
        if M.id in L.l or L.q(M.id):
            return M
        if isinstance(M.ctx, (a.Load, a.Store, a.Del)):
            M.id = L.t(M.id)
        return M

    def visit_Attribute(N,O):
        N.generic_visit(O)
        if isinstance(O.value, a.Name) and O.value.id == 'self':
            if O.attr not in N.m:
                N.m[O.attr] = d()
            O.attr = N.m[O.attr]
        return O

    def visit_Expr(P,Q):
        if isinstance(Q.value, a.Constant) and isinstance(Q.value.value, str):
            return None
        return P.generic_visit(Q)

    def visit_Call(R,S):
        R.generic_visit(S)
        if isinstance(S.func, a.Name) and S.func.id == 'print':
            if len(S.args) == 1 and isinstance(S.args[0], a.Constant) and isinstance(S.args[0].value, str):
                T = S.args[0].value
                U = f"print({repr(T)})"
                return a.Expr(
                    value=a.Call(
                        func=a.Name(id='eval', ctx=a.Load()),
                        args=[R.w(U)],
                        keywords=[]
                    )
                )
        return S

    def visit_Constant(V,W):
        if isinstance(W.value, str):
            X = getattr(W, 'parent', None)
            if X and isinstance(X, a.JoinedStr):
                return W
            return V.w(W.value)
        return W

    def visit_JoinedStr(Y,Z):
        for aa in Z.values:
            aa.parent = Z
        return Z

def n(ab):
    for ac in a.iter_child_nodes(ab):
        ac.parent = ab
        n(ac)

def o():
    f(''.join([chr(i) for i in [69,110,116,101,114,32,99,111,100,101,58]]))
    f(''.join([chr(i) for i in [40,70,105,110,105,115,104,32,119,105,116,104,32,69,78,68,41,58]]))
    ad = []
    while True:
        try:
            ae = input()
        except EOFError:
            break
        if ae.strip() == 'END':
            break
        ad.append(ae)
    return '\n'.join(ad)

def p(af):
    return '\n'.join([ag.rstrip() for ag in af.strip().split('\n') if ag.strip()])

if __name__ == '__main__':
    ah = o()
    try:
        ai = a.parse(ah)
    except SyntaxError as aj:
        f(''.join([chr(i) for i in [83,121,110,116,97,120,32,69,114,114,111,114,58]]))
        f(str(aj))
        exit(1)

    n(ai)
    ak = i()
    al = ak.visit(ai)
    a.fix_missing_locations(al)
    am = a.unparse(al)
    an = p(am)

    f('\n' + ''.join([chr(i) for i in [79,98,102,117,115,99,97,116,101,100,32,67,111,100,101,58]]) + '\n')
    f(an)

