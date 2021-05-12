import logging
import argparse

from sympy import *
from belief_base import Belief_Base

u_input = ">>>"


def initial_message():
    print("Welcome to belief abse revision!")
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
            belief_base.contraction(formula)
        elif action == "t":
            pass
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

# Available actions:
# i: insert belief
# p: print belief base
# con: contraction
# c: clear/reset belief base
# e: entail
# h: help

# action = input(u_input)
# action = action.lower()

# if action == "r":
#   form = to_cnf(form)
