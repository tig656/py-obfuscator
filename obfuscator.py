import ast
import random
import string

def rand_name(length=8):
    return ''.join(random.choices(string.ascii_letters, k=length))

def _p(msg):
    fn = ''.join([chr(i) for i in [112, 114, 105, 110, 116]])
    eval(f"{fn}({repr(msg)})")

class Obfuscator(ast.NodeTransformer):
    def __init__(self):
        self.name_mapping = {}
        self.protected_names = set()
        self.class_attr_names = {}

        self.protected_names.update({
            '_p', 'fn', 'msg', 'chr', 'eval', 'set_parents', 'input',
            'get_input', 'clean_code', 'ast', 'Obfuscator',
            'random', 'string', 'rand_name', '__name__', '__main__'
        })

    def is_builtin(self, name):
        return name in dir(__builtins__)

    def get_obfuscated_name(self, name):
        if name not in self.name_mapping:
            self.name_mapping[name] = rand_name()
        return self.name_mapping[name]

    def obfuscate_string(self, text):
        return ast.Call(
            func=ast.Attribute(
                value=ast.Constant(value=''),
                attr='join',
                ctx=ast.Load()
            ),
            args=[ast.List(
                elts=[
                    ast.Call(
                        func=ast.Name(id='chr', ctx=ast.Load()),
                        args=[ast.Constant(value=ord(c))],
                        keywords=[]
                    ) for c in text
                ],
                ctx=ast.Load()
            )],
            keywords=[]
        )

    def visit_Import(self, node):
        for n in node.names:
            self.protected_names.add(n.asname or n.name.split('.')[0])
        return node

    def visit_ImportFrom(self, node):
        for n in node.names:
            self.protected_names.add(n.asname or n.name)
        return node

    def visit_FunctionDef(self, node):
        if node.name not in self.protected_names:
            node.name = self.get_obfuscated_name(node.name)
        for arg in node.args.args:
            if arg.arg not in ('self',) and arg.arg not in self.protected_names:
                arg.arg = self.get_obfuscated_name(arg.arg)
        self.generic_visit(node)
        return node

    def visit_ClassDef(self, node):
        if node.name not in self.protected_names:
            node.name = self.get_obfuscated_name(node.name)
        self.generic_visit(node)
        return node

    def visit_Name(self, node):
        if node.id in self.protected_names or self.is_builtin(node.id):
            return node
        if isinstance(node.ctx, (ast.Load, ast.Store, ast.Del)):
            node.id = self.get_obfuscated_name(node.id)
        return node

    def visit_Attribute(self, node):
        self.generic_visit(node)
        if isinstance(node.value, ast.Name) and node.value.id == 'self':
            if node.attr not in self.class_attr_names:
                self.class_attr_names[node.attr] = rand_name()
            node.attr = self.class_attr_names[node.attr]
        return node

    def visit_Expr(self, node):
        if isinstance(node.value, ast.Constant) and isinstance(node.value.value, str):
            return None
        return self.generic_visit(node)

    def visit_Call(self, node):
        self.generic_visit(node)
        if isinstance(node.func, ast.Name) and node.func.id == 'print':
            if len(node.args) == 1 and isinstance(node.args[0], ast.Constant) and isinstance(node.args[0].value, str):
                text = node.args[0].value
                payload = f"print({repr(text)})"
                return ast.Expr(
                    value=ast.Call(
                        func=ast.Name(id='eval', ctx=ast.Load()),
                        args=[self.obfuscate_string(payload)],
                        keywords=[]
                    )
                )
        return node

    def visit_Constant(self, node):
        if isinstance(node.value, str):
            parent = getattr(node, 'parent', None)
            if parent and isinstance(parent, ast.JoinedStr):
                return node
            return self.obfuscate_string(node.value)
        return node

    def visit_JoinedStr(self, node):
        # ✅ Fix applied here
        new_values = []
        for value in node.values:
            if isinstance(value, ast.FormattedValue):
                value.value = self.visit(value.value)
            new_values.append(value)
        node.values = new_values
        return node

def set_parents(node):
    for child in ast.iter_child_nodes(node):
        child.parent = node
        set_parents(child)

def get_input():
    _p(''.join([chr(i) for i in [69, 110, 116, 101, 114, 32, 99, 111, 100, 101, 58]]))
    _p(''.join([chr(i) for i in [40, 70, 105, 110, 105, 115, 104, 32, 119, 105, 116, 104, 32, 69, 78, 68, 41, 58]]))
    lines = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        if line.strip() == 'END':
            break
        lines.append(line)
    return '\n'.join(lines)

def clean_code(code):
    return '\n'.join([line.rstrip() for line in code.strip().split('\n') if line.strip()])

if __name__ == '__main__':
    src = get_input()
    try:
        tree = ast.parse(src)
    except SyntaxError as e:
        _p(''.join([chr(i) for i in [83, 121, 110, 116, 97, 120, 32, 69, 114, 114, 111, 114, 58]]))
        _p(str(e))
        exit(1)

    set_parents(tree)
    ob = Obfuscator()
    new_tree = ob.visit(tree)
    ast.fix_missing_locations(new_tree)
    ob_code = ast.unparse(new_tree)
    final = clean_code(ob_code)

    _p('\n' + ''.join([chr(i) for i in [79, 98, 102, 117, 115, 99, 97, 116, 101, 100, 32, 67, 111, 100, 101, 58]]) + '\n')
    _p(final)
