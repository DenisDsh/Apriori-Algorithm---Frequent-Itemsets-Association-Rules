from itertools import combinations
import pandas as pd


def count_singletons(filePath):
    n_buckets = 0
    # Use dictionary to store counting, as key use a frozenset of the items in the itemset
    c1 = {}
    with open(filePath) as f:
        for line in f:
            bucket = line.split(" ")
            if '\n' in bucket: bucket.remove('\n')
            for item in bucket:
                itemset = frozenset({item})
                if itemset in c1.keys():
                    c1[itemset] = c1[itemset] + 1
                else:
                    c1[itemset] = 1
            n_buckets = n_buckets + 1
    return c1, n_buckets


# Creates a new dict with only the itemsets that are frequent, which support is equal or above a threshold
def filter_frequent(c : dict, min_count):
    return {itemset: count for itemset, count in c.items() if count >= min_count}


def construct_candidates(frequent_itemsets, file_path):
    c = {}
    last_l = list(frequent_itemsets[-1].keys()) #take last L k-1
    l1  = list(frequent_itemsets[0].keys()) #take L 1
    # k is the size of the candidate itemsets
    k = len(last_l[0]) + 1

    #if there are less than k frequent subsets means that cannot exist a superset frequent so it is useless to parse the buckets
    if len(last_l) < k :
        return {}

    with open(file_path) as f:
        for line in f:
            bucket = line.split(" ")
            if '\n' in bucket: bucket.remove('\n')

            #filter out items that are not in L1
            filtered_items =  [item for item in bucket if frozenset({item}) in l1]

            #filter items that are present less than k-1 times in itemsets of L k-1
            filtered_items = [item for item in filtered_items if not count_presence(item, last_l) < k - 1 ]

            #generate itemsets of lenght k considering only the filtered elements
            comb = list(combinations(filtered_items, k))
            #filter out those itemsets that have non frequent subsets

            for itemset in comb:
                if frozenset(itemset) not in c.keys():
                    # create all possible subsets
                    subsets = list(combinations(itemset, k - 1))
                    # check if they are all frequent
                    if all(frozenset(s) in last_l for s in subsets):
                        # In the case all the subsets are frequent insert in the Candidates the itemset and assign 1 to count
                        c[frozenset(itemset)] = 1
                else:
                    c[frozenset(itemset)] = c[frozenset(itemset)] + 1

    return c


#NAIVE VERSION
def construct_candidates_naive(l : dict, filePath):
    c = {}
    # k is the size of the candidate itemsets
    k = len(l[0]) + 1
    #if there are less than k frequent subsets means that cannot exist a superset frequent so it is useless to parse the buckets
    if len(l) < k :
        return {}

    with open(filePath) as f:
        for line in f:
            bucket = line.split(" ")
            if '\n' in bucket: bucket.remove('\n')
            # generate all possible sets of n items from
            comb = list(combinations(bucket, k))

            # Monotonicity of Support : If a set I is frequent then every subset of I is frequent
            # filter out all the sets that have at least one subset that is not frequent

            for itemset in comb :
                if frozenset(itemset) not in c.keys():
                    #create all possible subsets
                    subsets = list(combinations(itemset, k - 1))
                    #check if they are all frequent
                    if all(frozenset(s) in l.keys() for s in subsets):
                        #In the case all the subsets are frequent insert in the Candidates the itemset and assign 1 to count
                        c[frozenset(itemset)] = 1
                else:
                    c[frozenset(itemset)] = c[frozenset(itemset)] + 1

    return c



def frequent_itemsets(file_path, s) :
    # Returns the counts of the Singletons and the number of buckets in the file
    c1, n_buckets = count_singletons(file_path)

    # Compute threshold
    min_count = n_buckets * s

    # Stores frequent_itemsets for each k
    frequent_itemsets = []

    c = c1
    while len(c) != 0:
        l = filter_frequent(c, min_count)
        frequent_itemsets.append(l)
        c = construct_candidates(frequent_itemsets, file_path)

    return frequent_itemsets

def count_presence(item, l):
    return sum(1 for i in l if item in i)

def output_itemsets(file_path,freq_itemsets):
    out = []
    for l in freq_itemsets[1:]:
        for itemset in l.keys():
            out.append(', '.join(itemset))
    df = pd.DataFrame(out, columns=["itemset"])
    df.to_csv(file_path, sep="\t")
