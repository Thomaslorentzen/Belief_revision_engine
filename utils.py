from sympy.logic.boolalg import Or, And


def removeall(item, seq):
    return [x for x in seq if x != item]


def unique(seq):
    return list(set(seq))


def disjuncts(clause):
    return dissociate(Or, [clause])


def conjuncts(clause):
    return dissociate(And, [clause])


def associate(op, args):
    args = dissociate(op, args)
    if len(args) == 0:
        return op.identity
    elif len(args) == 1:
        return args[0]
    else:
        return op(*args)


def dissociate(op, args):
    result = []

    def collect(subargs):
        for arg in subargs:
            if isinstance(arg, op):
                collect(arg.args)
            else:
                result.append(arg)

    collect(args)
    return result
