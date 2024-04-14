# TODO: add your imports here:
# from rules import my_rules

from rules import TOURIST_RULES, TOURIST_DATA
from production import forward_chain, backward_chain

if __name__=='__main__':

    hypothesis = "Tourists is Homo Naledi"

    # Forward Chaining
    print("Performing Forward Chaining")
    results = forward_chain(TOURIST_RULES, TOURIST_DATA)
    print("Result of Forward Chaining:", results)

    # Backward Chaining
    print("\nPerforming Backward Chaining")
    print("\nHypothesis:", hypothesis)
    results = backward_chain(TOURIST_RULES, hypothesis)
    print("Result of Backward Chaining:", results)