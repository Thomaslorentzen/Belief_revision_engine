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
        pairings = [
            (clauses[i], clauses[j])
            for i in range(clauses_len)
            for j in range(i + 1, clauses_len)
        ]

        for ci, cj in pairings:
            resolutions = resolve(ci, cj)

            if False in resolutions:
                return True
            #result.add(set(resolutions))
            #udkommetneret alternativ fra git for at tjekke om det her er bedre end vores foreslåede løsning eller ej
            result = result.union(set(resolutions))


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
