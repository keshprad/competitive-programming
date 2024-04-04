#include <iostream>
#include <map>
#include <vector>
// Problem: https://leetcode.com/problems/parse-lisp-expression/

using namespace std;

// define headers
class Expr;
std::ostream &operator<<(std::ostream &os, const Expr *expr);
typedef map<string, int> var_map;

class Expr {
public:
  virtual int eval(var_map &map) = 0;
  virtual std::ostream &print(std::ostream &os) const = 0;
  virtual ~Expr(){};
};

class Number : public Expr {
private:
  int val;

public:
  Number(int val) : val(val) {}
  ~Number(){};
  int eval(var_map &vars) override { return val; }
  std::ostream &print(std::ostream &os) const override {
    os << "Number(" << val << ")";
    return os;
  };
};

class Variable : public Expr {
private:
  string name;

public:
  Variable(string name) : name(name) {}
  ~Variable(){};
  int eval(var_map &vars) override { return vars[name]; }
  std::ostream &print(std::ostream &os) const override {
    os << "Variable(" << '"' << name << '"' << ")";
    return os;
  }
};

class Add : public Expr {
private:
  Expr *expr1;
  Expr *expr2;

public:
  Add(Expr *expr1, Expr *expr2) : expr1(expr1), expr2(expr2) {}
  ~Add() {
    delete expr1;
    delete expr2;
  };
  int eval(var_map &vars) override {
    return expr1->eval(vars) + expr2->eval(vars);
  }
  std::ostream &print(std::ostream &os) const override {
    os << "Add(" << expr1 << ", " << expr2 << ")";
    return os;
  }
};

class Mult : public Expr {
private:
  Expr *expr1;
  Expr *expr2;

public:
  Mult(Expr *expr1, Expr *expr2) : expr1(expr1), expr2(expr2) {}
  ~Mult() {
    delete expr1;
    delete expr2;
  };
  int eval(var_map &vars) override {
    return expr1->eval(vars) * expr2->eval(vars);
  }
  std::ostream &print(std::ostream &os) const override {
    os << "Mult(" << expr1 << ", " << expr2 << ")";
    return os;
  }
};

class Let : public Expr {
private:
  vector<pair<string, Expr *>> bindings;
  Expr *inner_expr;

public:
  Let(vector<pair<string, Expr *>> &bindings, Expr *inner_expr)
      : bindings(bindings), inner_expr(inner_expr){};
  ~Let() {
    for (auto p : bindings) {
      delete p.second;
    }
    delete inner_expr;
  };
  int eval(var_map &vars) override {
    var_map newvars = vars;
    for (auto p : bindings) {
      newvars[p.first] = p.second->eval(newvars);
    }
    return inner_expr->eval(newvars);
  }
  std::ostream &print(std::ostream &os) const override {
    os << "Let({";
    for (auto p : bindings) {
      os << "(\"" << p.first << "\", " << p.second << "), ";
    }
    os << "}, " << inner_expr << ")";
    return os;
  }
};

std::ostream &operator<<(std::ostream &os, const Expr *expr) {
  return expr->print(os);
}

class Solution {
private:
  vector<string> make_toks(string &expression) {
    vector<string> res;
    int prev = 0;
    int i = 0;

    while (i < expression.size()) {
      if (expression[i] == '(') {
        res.push_back("(");
        i++;
        prev++;
      } else if (expression[i] == ')') {
        if (prev != i)
          res.push_back(expression.substr(prev, i - prev));
        res.push_back(")");
        i++;
        prev = i;
      } else if (expression[i] == ' ') {
        if (prev != i)
          res.push_back(expression.substr(prev, i - prev));
        i++;
        prev = i;
      } else {
        i++;
      }
    }

    return res;
  }

  Expr *parse(vector<string> &toks) {
    int i = 0;
    return parse(toks, i);
  }

  Expr *parse(vector<string> &toks, int &i) {
    if (toks[i] == "(") {
      return parse_op(toks, i);
    } else {
      return parse_lit(toks, i);
    }
  }

  Expr *parse_lit(vector<string> &toks, int &i) {
    if (isalpha(toks[i][0])) {
      // variable name
      return new Variable(toks[i++]);
    } else {
      // number
      return new Number(stoi(toks[i++]));
    }
  }

  Expr *parse_op(vector<string> &toks, int &i) {
    i++; // skip '('
    if (toks[i] == "add") {
      i++; // consume opname
      Expr *e1 = parse(toks, i);
      Expr *e2 = parse(toks, i);
      i++; // skip ')'
      return new Add(e1, e2);
    } else if (toks[i] == "mult") {
      i++; // consume opname
      Expr *e1 = parse(toks, i);
      Expr *e2 = parse(toks, i);
      i++; // skip ')'
      return new Mult(e1, e2);
    } else {
      // toks[i] == "let"
      i++; // consume opname
      vector<pair<string, Expr *>> bindings;
      while (true) {
        if (toks[i] != "(" && isalpha(toks[i][0]) && toks[i + 1] != ")") {
          string varname = toks[i++]; // consume varname
          Expr *e1 = parse(toks, i);
          bindings.push_back({varname, e1});
        } else {
          Expr *inner = parse(toks, i);
          i++; // skip ')'
          return new Let(bindings, inner);
        }
      }
    }
  }

  int evaluate(Expr *e) {
    var_map vars;
    return e->eval(vars);
  }

public:
  int evaluate(string expression) {
    vector<string> toks = make_toks(expression);
    Expr *expr = parse(toks);
    int res = evaluate(expr);
    delete expr;
    return res;
  }
};
