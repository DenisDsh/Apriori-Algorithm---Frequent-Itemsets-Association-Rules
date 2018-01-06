import timeit
import argparse
from frequent_itemsets import frequent_itemsets, output_itemsets
from association_rules import generate_rules, output_rules

parser = argparse.ArgumentParser()

parser.add_argument('-input',
                    action='store',
                    dest='input_path',
                    help='Define the input path for baskets',
                    type=str,
                    default='data/T10I4D100K.dat')

parser.add_argument('-s',
                    action='store',
                    dest='support_threshold',
                    help='Define the support threshold for the itemsets',
                    type=float,
                    default=0.01)

parser.add_argument('-c',
                    action='store',
                    dest='confidence_threshold',
                    help='Define the confidence threshold for the rules',
                    type=float,
                    default=0.5)


parser.add_argument('-outSets',
                    action='store',
                    dest='output_path_itemsets',
                    help='Define the output path for itemsets',
                    type=str,
                    default='data/out_sets.csv')

parser.add_argument('-outRules',
                    action='store',
                    dest='output_path_rules',
                    help='Define the output path for association rules',
                    type=str,
                    default='data/out_rules.csv')

args = parser.parse_args()
s = args.support_threshold
c = args.confidence_threshold
input_path = args.input_path
rules_path = args.output_path_rules
itemsets_path = args.output_path_itemsets

print("SUPPORT THRESHOLD : %s" %s )
print("CONFIDENCE THRESHOLD : %s" %c )

print("Finding frequent itemsets...")

freq_itemsets = frequent_itemsets(input_path, s)

#write on file the itemsets
output_itemsets(itemsets_path,freq_itemsets)

print("Frequent itemsets written in " + itemsets_path)

rules = generate_rules(freq_itemsets, c)

print("Generating association rules...")

#write on file the rules
output_rules(rules_path, rules)

print("Association rules written in " + rules_path)
