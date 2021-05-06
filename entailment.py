from sympy.logic.boolalg import to_cnf, Or

from utils import conjuncts, disjuncts, unique, removeall, associate, dissociate

def entail(belief_base, formula):
    formula = to_cnf(formula)
    clauses = []
    for belief in belief_base:
        clauses.append(to_cnf(belief))
    clauses.append(to_cnf(-formula))

    result = set()

    while True:
        clauses_len = len(clauses)



def resolve(ci, cj):

        disjunction_ci = disjuncts(ci)
        disjunction_cj = disjuncts(cj)

        clauses = []

        for literal_i in disjunction_ci:
            for literal_j in disjunction_cj:
                if literal_i == -literal_j or -literal_i == literal_j:
                    remaining = removeall(literal_i, disjunction_ci) + removeall(literal_j, disjunction_cj)
                    remaining = unique(remaining)
                    new_clause = associate(Or, remaining)

                    clauses.append(new_clause)

        return clauses

