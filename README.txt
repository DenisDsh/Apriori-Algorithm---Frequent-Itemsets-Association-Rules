
usage: main.py [-h] [-input INPUT_PATH] [-s SUPPORT_THRESHOLD]
               [-c CONFIDENCE_THRESHOLD] [-outSets OUTPUT_PATH_ITEMSETS]
               [-outRules OUTPUT_PATH_RULES]

optional arguments:
  -h, --help            show this help message and exit
  -input INPUT_PATH     Define the input path for baskets
  -s SUPPORT_THRESHOLD  Define the support threshold for the itemsets
  -c CONFIDENCE_THRESHOLD
                        Define the confidence threshold for the rules
  -outSets OUTPUT_PATH_ITEMSETS
                        Define the output path for itemsets
  -outRules OUTPUT_PATH_RULES
                        Define the output path for association rules



“python main.py”  will execute the program with the following default arguments : 

INPUT_PATH = “data/T10I4D100K.dat”
SUPPORT_THRESHOLD = 0.01
CONFIDENCE_THRESHOLD = 0.5
OUTPUT_PATH_ITEMSETS = “data/out_sets.csv”
OUTPUT_PATH_RULES = “data/out_rules.csv”

