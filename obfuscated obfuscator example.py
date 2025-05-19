# this isn't obfuscated using my obfuscator, because it doesn't support obfuscation of an actual obfuscator

import ast as vAQuWsxt
import random as ALYQxuRe
import string as gAVTWaXD

def dPnfiuyC(length=8):
    return ''.join(ALYQxuRe.choices(gAVTWaXD.ascii_letters, k=length))

def JIXMaVbK(BVzHzkdc):
    LYAdgVNF = ''.join([chr(i) for i in [112, 114, 105, 110, 116]])
    eval(f"{LYAdgVNF}({repr(BVzHzkdc)})")

class ZmBExlYO(vAQuWsxt.NodeTransformer):
    def __init__(rlddyWSN):
        rlddyWSN.qGgtFZnb = {}
        rlddyWSN.YTxHgvdS = set()
        rlddyWSN.DApwmQol = {}
        rlddyWSN.YTxHgvdS.update({
            'JIXMaVbK', 'LYAdgVNF', 'BVzHzkdc', 'chr', 'eval', 'cYxKzNuL', 'input',
            'yBNCuEZq', 'SxgrwDEa', 'vAQuWsxt', 'ZmBExlYO',
            'ALYQxuRe', 'gAVTWaXD', 'dPnfiuyC', '__name__', '__main__'
        })

    def SygZCEjl(DwNBglQo, jfnEjPHp):
        return jfnEjPHp in dir(__builtins__)

    def oUxFLCem(jAzpgVKi, tpEfsGZv):
        if tpEfsGZv not in jAzpgVKi.qGgtFZnb:
            jAzpgVKi.qGgtFZnb[tpEfsGZv] = dPnfiuyC()
        return jAzpgVKi.qGgtFZnb[tpEfsGZv]

    def hEQvWcBJ(gOdxuqiA, AvftUYbQ):
        return vAQuWsxt.Call(
            func=vAQuWsxt.Attribute(
                value=vAQuWsxt.Constant(value=''),
                attr='join',
                ctx=vAQuWsxt.Load()
            ),
            args=[vAQuWsxt.List(
                elts=[
                    vAQuWsxt.Call(
                        func=vAQuWsxt.Name(id='chr', ctx=vAQuWsxt.Load()),
                        args=[vAQuWsxt.Constant(value=ord(c))],
                        keywords=[]
                    ) for c in AvftUYbQ
                ],
                ctx=vAQuWsxt.Load()
            )],
            keywords=[]
        )

    def visit_Import(EpTczrFW, node):
        for n in node.names:
            EpTczrFW.YTxHgvdS.add(n.asname or n.name.split('.')[0])
        return node

    def visit_ImportFrom(zItvUdnp, node):
        for n in node.names:
            zItvUdnp.YTxHgvdS.add(n.asname or n.name)
        return node

    def visit_FunctionDef(EobfAmCg, node):
        if node.name not in EobfAmCg.YTxHgvdS:
            node.name = EobfAmCg.oUxFLCem(node.name)
        for arg in node.args.args:
            if arg.arg not in ('self',) and arg.arg not in EobfAmCg.YTxHgvdS:
                arg.arg = EobfAmCg.oUxFLCem(arg.arg)
        EobfAmCg.generic_visit(node)
        return node

    def visit_ClassDef(XEyuwblc, node):
        if node.name not in XEywblc.YTxHgvdS:
            node.name = XEywblc.oUxFLCem(node.name)
        XEywblc.generic_visit(node)
        return node

    def visit_Name(PEUrMfNb, node):
        if node.id in PEUrMfNb.YTxHgvdS or PEUrMfNb.SygZCEjl(node.id):
            return node
        if isinstance(node.ctx, (vAQuWsxt.Load, vAQuWsxt.Store, vAQuWsxt.Del)):
            node.id = PEUrMfNb.oUxFLCem(node.id)
        return node

    def visit_Attribute(ZZPbNQVx, node):
        ZZPbNQVx.generic_visit(node)
        if isinstance(node.value, vAQuWsxt.Name) and node.value.id == 'self':
            if node.attr not in ZZPbNQVx.DApwmQol:
                ZZPbNQVx.DApwmQol[node.attr] = dPnfiuyC()
            node.attr = ZZPbNQVx.DApwmQol[node.attr]
        return node

    def visit_Expr(LRgQbUCF, node):
        if isinstance(node.value, vAQuWsxt.Constant) and isinstance(node.value.value, str):
            return None
        return LRgQbUCF.generic_visit(node)

    def visit_Call(PTwEFZXq, node):
        PTwEFZXq.generic_visit(node)
        if isinstance(node.func, vAQuWsxt.Name) and node.func.id == 'print':
            if len(node.args) == 1 and isinstance(node.args[0], vAQuWsxt.Constant) and isinstance(node.args[0].value, str):
                text = node.args[0].value
                payload = f"print({repr(text)})"
                return vAQuWsxt.Expr(
                    value=vAQuWsxt.Call(
                        func=vAQuWsxt.Name(id='eval', ctx=vAQuWsxt.Load()),
                        args=[PTwEFZXq.hEQvWcBJ(payload)],
                        keywords=[]
                    )
                )
        return node

    def visit_Constant(aHeESuGf, node):
        if isinstance(node.value, str):
            parent = getattr(node, 'parent', None)
            if parent and isinstance(parent, vAQuWsxt.JoinedStr):
                return node
            return aHeESuGf.hEQvWcBJ(node.value)
        return node

    def visit_JoinedStr(YUMEkDwV, node):
        for value in node.values:
            value.parent = node
        return node

def cYxKzNuL(node):
    for child in vAQuWsxt.iter_child_nodes(node):
        child.parent = node
        cYxKzNuL(child)

def yBNCuEZq():
    JIXMaVbK(''.join([chr(i) for i in [69, 110, 116, 101, 114, 32, 99, 111, 100, 101, 58]]))
    JIXMaVbK(''.join([chr(i) for i in [40, 70, 105, 110, 105, 115, 104, 32, 119, 105, 116, 104, 32, 69, 78, 68, 41, 58]]))
    LZZKgNBc = []
    while True:
        try:
            qPmpfBFo = input()
        except EOFError:
            break
        if qPmpfBFo.strip() == 'END':
            break
        LZZKgNBc.append(qPmpfBFo)
    return '\n'.join(LZZKgNBc)

def SxgrwDEa(code):
    return '\n'.join([line.rstrip() for line in code.strip().split('\n') if line.strip()])

if __name__ == '__main__':
    UyuygSRo = yBNCuEZq()
    hXjZGErs = vAQuWsxt.parse(UyuygSRo)
    cYxKzNuL(hXjZGErs)
    vNyiRjAc = ZmBExlYO()
    YpLBdRfX = vNyiRjAc.visit(hXjZGErs)
    vAQuWsxt.fix_missing_locations(YpLBdRfX)
    DzFElIti = vAQuWsxt.unparse(YpLBdRfX)
    XxdHmvKl = SxgrwDEa(DzFElIti)

    JIXMaVbK('\n' + ''.join([chr(i) for i in [79, 98, 102, 117, 115, 99, 97, 116, 101, 100, 32, 67, 111, 100, 101, 58]]) + '\n')
    JIXMaVbK(XxdHmvKl)
