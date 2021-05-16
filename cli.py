import logging
import argparse
import entailment

from sympy import *
from belief_base import Belief_Base

u_input = ">>>"

#TODO:
#Write user input instructions for the user
#Ensure all methods convert to cnf
#Expand database but notify user that no logical check will verify validity
#
#
#

def initial_message():
    print("Welcome to belief base revision!")
    print(
        f"""Actions available:
        i = insert belief
        p = print base
        con = contraction
        c = clear belief base
        e = entail
        h = help
        q = quit
        """)
    print("select an action: ")


def test():
    test_bb = Belief_Base()
    #test_bb.expand_belief_base("p", 1)
    test_bb.expand_belief_base('p&q', 1)
    #test_bb.expand_belief_base('p|q', 1)
    #test_bb.expand_belief_base("~p&~q", 3)

    # new test
    #test_bb.contraction("p")
    #print("beliefs from test BB: {}".format(sorted(test_bb.beliefs)))
    test_bb.revise("p", 10)
    #test_bb.revise("~p")


def input_handler(belief_base):
    initial_message()
    action = input(u_input)
    action = action.lower()

    input_running = True
    while input_running:
        if action == "i":
            print("insert value(s) to add to your belief base")
            formula = input(u_input)
            try:
                belief_base.expand_belief_base(formula, 1)
            except SympifyError:
                print("invalid formula")
        elif action == "c":
            belief_base.clear()
        elif action == "con":
            formula = input("Write a formula to delete")
            #belief_base.contraction(formula)
        elif action == "t":
            test()
        elif action == "q":
            input_running = false
            exit()
        elif action == "h":
            initial_message()
        elif action == "p":
            for belief in bb.beliefs:
                print(belief.formula)
        elif action == "e":
            pass
        else:
            print("invalid user input. Press h for for help")
            print()

        input_handler(bb)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Belief base revision CLI tool.')
    parser.add_argument('--debug', action='store_true', help='enable debugging')
    args = parser.parse_args()

    bb = Belief_Base()
    input_handler(bb)


