from itertools import combinations
import pandas as pd

def generate_rules(frequent_itemsets : list, c = 0.5):

    rules = []
    for l in frequent_itemsets :

        for itemset, support in l.items():
            k = len(itemset)
            #create subsets of size i
            for i in range(1,k):
                subsets = list(combinations(set(itemset), i))
                #for each subset A check if the rule A -> I \ A has confidence above the threshold
                for a in subsets :
                    support_a = get_support(frequent_itemsets,a)
                    #confidence = support(I) / support(A)
                    confidence = support / support_a

                    if confidence >= c :
                        #add rule tuple (A, I\A, confidence) to rules
                        rules.append((set(a),set(itemset).difference(set(a)),confidence))

    return rules


#get support of a specific itemset from the
def get_support(frequent_itemsets, itemset):
    l = frequent_itemsets[len(itemset)-1]
    return l[frozenset(itemset)]


def output_rules(file_path, rules):
    df = pd.DataFrame([[create_str_rule(rule[0],rule[1]),rule[2]] for rule in rules],columns=["rule","confidence"])
    df.to_csv(file_path, sep = "\t")


def create_str_rule(left, right):
    return  ', '.join(left) + " -> " + ', '.join(right)