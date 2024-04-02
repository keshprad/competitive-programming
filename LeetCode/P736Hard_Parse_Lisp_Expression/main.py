# Problem: https://leetcode.com/problems/parse-lisp-expression/description/

class Number:
    def __init__(self, val):
        self.val = val

    def evaluate(self, env):
        return self.val


class Var:
    def __init__(self, name):
        self.name = name

    def evaluate(self, env):
        return env[self.name]


class Add:
    def __init__(self, expr1, expr2):
        self.expr1 = expr1
        self.expr2 = expr2

    def evaluate(self, env):
        return self.expr1.evaluate(env) + self.expr2.evaluate(env)


class Mult:
    def __init__(self, expr1, expr2):
        self.expr1 = expr1
        self.expr2 = expr2

    def evaluate(self, env):
        return self.expr1.evaluate(env) * self.expr2.evaluate(env)


class Let:
    def __init__(self, bindings, expr):
        self.bindings = bindings
        self.expr = expr

    def evaluate(self, env):
        newenv = dict(env)
        for var, expr in self.bindings:
            newenv[var] = expr.evaluate(newenv)
        return self.expr.evaluate(newenv)


class Solution:
    def make_toks(self, expression, i=0):
        res = []
        # assume i points to open brace
        i += 1

        while i < len(expression):
            if expression[i] == ' ':
                i += 1
            elif expression[i] == '(':
                newres, i = self.make_toks(expression, i)
                res.append(newres)
            elif expression[i] == ')':
                return res, i+1
            else:
                nxt = min(filter(lambda x: x >= 0,
                                 (expression.find(' ', i), expression.find(')', i))))
                res.append(expression[i:nxt])
                i = nxt
        return res, i

    def parse(self, toks):
        if type(toks) == list:
            return self.parse_op(toks)
        else:
            return self.parse_literal(toks)

    def parse_op(self, toks):
        if toks[0] == 'let':
            bindings = []
            for i in range(1, len(toks)-2, 2):
                bindings.append((toks[i], self.parse(toks[i+1])))
            return Let(bindings, self.parse(toks[-1]))
        elif toks[0] == 'mult':
            return Mult(self.parse(toks[1]), self.parse(toks[2]))
        elif toks[0] == 'add':
            return Add(self.parse(toks[1]), self.parse(toks[2]))

    def parse_literal(self, tok):
        if tok.isnumeric() or (tok[0] == '-' and tok[1:].isnumeric()):
            return Number(int(tok))
        else:
            return Var(tok)

    def evaluate(self, expression: str) -> int:
        toks, _ = self.make_toks(expression)
        expr = self.parse(toks)
        return expr.evaluate({})
