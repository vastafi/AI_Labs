import random
from production import (
    populate,
    instantiate,forward_chain,
    uniq,
    backward_chain,
)
from rules import TOURIST_RULES
from helpers.question_helper import (
    generate_question_tree,
    generate_multiple_choice_questions,
    extract_multiple_choice_answer,
    generate_yes_no_questions,
    interpret_yes_no_answer,
    resolve_formatting,
)

general_rules = TOURIST_RULES

def chain(
    session_data: dict,
) -> bool:
    """Chain function that will be called to run the chain methods of the expert system.
    
    Args:
        session_data (dict): A dictionary containing the session data.
        
    Returns:
        bool: A boolean value indicating if the expert system should stop.
    """
    if session_data["mode"] == 0:
        stop_system = forward(session_data)
    else:
        stop_system = backward(session_data)

    return stop_system


def forward(
    session_data: dict,
) -> bool:
    """Forward chain method of the expert system.
    
    Args:
        session_data (dict): A dictionary containing the session data.
        
    Returns:
        bool: A boolean value indicating if the expert system should stop.
    """
    print("Forward chain mode initiated.")

    known_rules = []
    used_rules = []

    # Create a set with known conditions
    not_start_nodes = set()
    for rule in general_rules:
        leaf_rule = rule.consequent().__repr__()
        not_start_nodes.add(leaf_rule)
    rules_tree = generate_question_tree(known_rules, used_rules)
    condition_nodes = rules_tree.keys()
    end_nodes = [populate(node, {"x": session_data.get("name")}) for node in not_start_nodes if node not in condition_nodes]

    while True:
        # get possible facts abut tourist by taking only nodes that weren't questioned
        possible_facts = list(rules_tree.keys())
        # in case no matching found, conclude it is a Loonie
        if not possible_facts:
            print("It seems you are describing a Loonie!")
            break
        current_fact = random.choice(possible_facts)
        choices = uniq([choice[0] for choice in rules_tree[current_fact]])
        # in case the condition is not single to lead to the result, ask multiple choice question
        if len(choices) > 1:
            question = generate_multiple_choice_questions(choices)
            print(question)
            answer = extract_multiple_choice_answer(choices)
            used_rules.append(choices[answer - 1])
            if answer != "None":
                known_rules = list(known_rules)
                known_rules.append(instantiate(choices[answer - 1], {"x": session_data.get("name")}))
                known_rules = forward_chain(general_rules, known_rules)
        # ask yes/no question otherwise
        else:
            question = generate_yes_no_questions(current_fact)
            print(question)
            answer = interpret_yes_no_answer()
            if answer == "YES":
                known_rules = list(known_rules)
                known_rules.append(instantiate(current_fact, {"x": session_data.get("name")}))
                known_rules = forward_chain(general_rules, known_rules)
            used_rules.append(current_fact)
        if len(list(set(known_rules) & set(end_nodes))) > 0:
            print(f"Results:\n {list(set(known_rules) & set(end_nodes))[0]}")
            break
        rules_tree.clear()
        rules_tree.update(generate_question_tree(known_rules, used_rules))
    return False


def backward(
    session_data: dict,
) -> bool:
    """Backward chain method of the expert system.
    
    Args:
        session_data (dict): A dictionary containing the session data.
        
    Returns:
        bool: A boolean value indicating if the expert system should stop.
    """
    print("Backward chain mode initiated.")
    
    # Prompt the user to provide the type of tourist for more information
    print(f"Provide the type of tourist of {session_data.get('name')} to find out more about the tourist.")
    user_type = "(?x) is " + input(f"{session_data.get('name')} type: ")
    
    # Perform backward chaining to retrieve character information
    character_info = backward_chain(general_rules, user_type)

    # Check if there is only one character information or more
    if len(character_info) <= 1:
        print("It seems you are describing a Loonie!")
    else:
        print(f"Detailed information about {session_data.get('name')}:\n")
        for fact in character_info:
            if fact == user_type:
                continue
            resolve_formatting(fact)
        print("\n")
    
    # Return False to indicate the expert system should not stop
    return False