# -*- coding: utf-8 -*-
"""
LING571 HW2

# This is a class used to convert CFG to CNF
# converter.py

Created on Thu Jan 23 22:16:23 2014

@author: Haotian He
"""

import sys

productions = {}
single_nter = []
mix_rules = []
long_rules = []

def convert(cfg, cnf):
    
    global productions, single_nter, mix_rules, long_rules

    sort(cfg)
    sort_mix(mix_rules)
    sort_long(long_rules)
#sort_single(single_nter)
    print productions

# type different productions, and put them into different lists
# the first step
def sort(cfg):
    
    global productions, single_nter, mix_rules, long_rules
    init_appr = True

    for line in cfg.readlines():

        if '->' in line:
            line = line.split('->')

            lhs = line[0].split()
            left = line[0].strip()
            
            rhs = line[1:][0].split()
            right = line[1:][0].strip()
            
            rule = lhs + rhs

            if not "'" in right:
                if len(rhs) == 2:
                    if productions.has_key(rule[0]) == False:
                        productions[rule[0]] = []
                    productions[rule[0]].append(rule[1] + " " + rule[2])
                elif len(rhs) == 1:
                        single_nter.append(rule)
                else:
                    long_rules.append(rule)
            elif len(rhs) == 1:
                if productions.has_key(rule[0]) == False:
                    productions[rule[0]] = []
                productions[rule[0]].append(rule[1])
            else:
                mix_rules.append(rule)


# handle the mix productions
# the second step
def sort_mix(mix_rules):

    global productions, single_nter, long_rules
    
    for i in range(0, len(mix_rules)):
        for j in range(0, len(mix_rules[i])):
            if "'" in mix_rules[i][j]:
                word = mix_rules[i][j]
                
                key = list(productions.keys())
                found_match = ""
                for k in range(0, len(key)):
                    if word in productions[key[k]]:
                        mix_rules[i][j] = key[k]
                        found_match = key[k]
                if mix_rules[i][j] != found_match:
                    name = "M" + str(i)
                    if productions.has_key(name) == False:
                        productions[name] = []
                    productions[name].append(word)
                    mix_rules[i][j] = name
    
        if (len(mix_rules[i]) == 3):
            if productions.has_key(mix_rules[i][0]) == False:
                productions[mix_rules[i][0]] = []
            productions[mix_rules[i][0]].append(mix_rules[i][1] + " " + mix_rules[i][2])
        elif (len(mix_rules[i]) == 2):
            single_nter.append(mix_rules[i])
        else:
            long_rules.append(mix_rules[i])


# handle the long non-terminal productions
# the third step
def sort_long(long_rules):
    for i in range(0, len(long_rules)):
        recur(long_rules[i], i * 10)

# sub-function helping to hand the long non-terminal productions
# the nested step
def recur(rule, x):
    if len(rule) == 3:
        if productions.has_key(rule[0]) == False:
            productions[rule[0]] = []
        productions[rule[0]].append(rule[1] + " " + rule[2])
    else:
        name = "X" + str(x)
        if productions.has_key(rule[0]) == False:
            productions[rule[0]] = []
        productions[rule[0]].append(name + " " + rule[len(rule) - 1])
        rule = rule[1:len(rule)-1]
        rule.insert(0, name)
        return recur(rule, x + 1)


# handle the single non-terminal productions
# the last step
def sort_single(single_nter):

    global productions

    for i in range(0, len(single_nter)):
        key = list(productions.keys())
        for t in range(0, len(key)):
            if (key[t] == single_nter[i][1]):
                



if __name__ == "__main__":

    if (len(sys.argv) == 2):
        cfg_path = sys.argv[0]
        cnf_path = sys.argv[1]
    else:
        cfg_path = "grammar.cfg"
        cnf_path = "grammar.cnf"

    cfg = open(cfg_path, 'r')
    cnf = open(cnf_path, 'a')

    convert(cfg, cnf)

    cfg.close()
    cnf.close()
