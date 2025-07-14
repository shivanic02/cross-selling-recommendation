import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder

def prepare_basket(transactions_list, min_support=0.01, metric='lift', min_threshold=1):
    """
    Given list of transactions, return frequent itemsets and rules.
    """
    te = TransactionEncoder()
    te_ary = te.fit(transactions_list).transform(transactions_list)
    basket = pd.DataFrame(te_ary, columns=te.columns_)

    # Frequent itemsets
    frequent_itemsets = apriori(basket, min_support=min_support, use_colnames=True)

    # Association rules
    rules = association_rules(frequent_itemsets, metric=metric, min_threshold=min_threshold)

    # Convert frozensets to strings for readability
    rules['antecedents_str'] = rules['antecedents'].apply(lambda x: ', '.join(list(x)))
    rules['consequents_str'] = rules['consequents'].apply(lambda x: ', '.join(list(x)))

    return frequent_itemsets, rules

if __name__ == "__main__":
    # Example dummy usage
    sample_transactions = [['milk', 'bread', 'eggs'],
                           ['milk', 'bread'],
                           ['milk', 'diapers'],
                           ['bread', 'butter'],
                           ['milk', 'bread', 'butter', 'eggs']]

    freq_items, assoc_rules = prepare_basket(sample_transactions, min_support=0.2, min_threshold=1)

    print("Frequent Itemsets:")
    print(freq_items)

    print("\nAssociation Rules:")
    print(assoc_rules[['antecedents_str', 'consequents_str', 'support', 'confidence', 'lift']])
