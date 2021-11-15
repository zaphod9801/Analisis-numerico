class term:
    term_coef: float = 0
    term_exp: float = 0

    def __init__(self, n_term_coef: float, n_term_exp: float):
        self.term_coef = n_term_coef
        self.term_exp = n_term_exp
    
    def __add__(self, other):
        return term(self.term_coef + other.term_coef, self.term_exp)
    
    def __mul__(self, other):
        return term(self.term_coef * other.term_coef, self.term_exp + other.term_exp)
    
    def __str__(self) -> str:
        return "( " + str(self.term_coef) + " * X^" + str(self.term_exp) + " )"