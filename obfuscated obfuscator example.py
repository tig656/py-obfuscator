# this isn't obfuscated using my obfuscator, because it doesn't support obfuscation of an actual obfuscator

import ast as a
import random as b
import string as c

def aF(): return ''.join([chr(i) for i in [112, 114, 105, 110, 116]])

def c0(msg):
    eval(f"{aF()}({repr(msg)})")

def rA(l=8):
    return ''.join(b.choices(c.ascii_letters, k=l))

class V4(a.NodeTransformer):
    def __init__(self):
        self.a1 = {}
        self.a2 = set()
        self.a3 = {}
        self.a2.update({'c0', 'aF', 'msg', 'chr', 'eval', 'a9', 'input', 'b7', 'b5', 'a', 'V4', 'b', 'c', 'rA', '__name__', '__main__'})

    def a6(self, name): return name in dir(__builtins__)

    def a7(self, name):
        if name not in self.a1:
            self.a1[name] = rA()
        return self.a1[name]

    def b0(self, text):
        return a.Call(
            func=a.Attribute(value=a.Constant(value=''), attr='join', ctx=a.Load()),
            args=[a.List(
                elts=[a.Call(func=a.Name(id='chr', ctx=a.Load()), args=[a.Constant(value=ord(c))], keywords=[]) for c in text],
                ctx=a.Load()
            )],
            keywords=[]
        )

    def visit_Import(self, node):
        for n in node.names:
            self.a2.add(n.asname or n.name.split('.')[0])
        return node

    def visit_ImportFrom(self, node):
        for n in node.names:
            self.a2.add(n.asname or n.name)
        return node

    def visit_FunctionDef(self, node):
        if node.name not in self.a2:
            node.name = self.a7(node.name)
        for arg in node.args.args:
            if arg.arg not in ('self',) and arg.arg not in self.a2:
                arg.arg = self.a7(arg.arg)
        self.generic_visit(node)
        return node

    def visit_ClassDef(self, node):
        if node.name not in self.a2:
            node.name = self.a7(node.name)
        self.generic_visit(node)
        return node

    def visit_Name(self, node):
        if node.id in self.a2 or self.a6(node.id):
            return node
        if isinstance(node.ctx, (a.Load, a.Store, a.Del)):
            node.id = self.a7(node.id)
        return node

    def visit


