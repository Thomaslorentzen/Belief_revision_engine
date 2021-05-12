import math
import logging
from operator import neg

from sympy.logic.boolalg import to_cnf, And, Or, Equivalent
from sortedcontainers import SortedList

from entailment import entail
from utils import associate


class Belief_Base:

    def __init__(self):
        self.beliefs = SortedList(key=lambda b: neg(b.order))
        self.sorting_queue = []

    def add_sorting_queue(self, belief, order):
        self.sorting_queue.append((belief, order))

    def group_by_order(self, belief_base, order):
        result = []
        last_order = None

        for belief in self.beliefs:
            if last_order is None:
                result.append(belief)
                last_order = belief.order
                continue
            if math.isclose(belief.order, last_order):
                result.append(belief)

            else:
                yield last_order, result
                result = []
                result.append(belief)
                last_order = belief.order


    def run_sorting_queue(self):
        for belief, order in self.sorting_queue:
            self.beliefs.remove(belief)
            if order >= 0:
                belief.order = order
                self.beliefs.add(belief)
        self.sorting_queue = []

    def expand_belief_base(self, formula, order):
        new_belief = Belief(formula, order)
        for belief in self.beliefs:
            belief.order += 1
        self.beliefs.add(new_belief)

    def deg_order(self, belief_base):
        for belief in belief_base:
            belief.order += 1

    def remove_from_belief_base(self, formula, order):
        for belief in self.beliefs:
            if belief.formula == formula:
                self.beliefs.remove(belief)

    def contraction(self, formula):
        #Contraction is the removal of a belief and all other beliefs that could entail that belief
        #this means that 1) we have to remove the belief from the belief base
        # 2) we have to remove every belief that would entail the stated belief
        # We can do this by using the entail method to identify the clauses that would entail the formula
        #
        cnf_formula = to_cnf(formula)

        for belief in self.beliefs:
            if cnf_formula == belief:
                self.beliefs.remove(belief)

    def clear(self):
        self.beliefs.clear()

    #def is_close(self):


class Belief:
    def __init__(self, formula, order=None):
        self.formula = formula
        self.order = order

    def __lt__(self, other):
        return self.order < other.order

    def __eq__(self, other):
        return self.order == other.order and self.formula == other.formula

    def __repr__(self):
        return f'Belief({self.formula}, order={self.order})'
