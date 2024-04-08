from rules import TOURIST_RULES
from production import populate, AND, OR
import random

general_rules = TOURIST_RULES

def extract_multiple_choice_answer(choices):
    """Extracts the multiple choice answer from the list of choices.
    
    Args:
        choices (list): A list of choices.
        
    Returns:
        int: The index of the selected choice.

    """
    choice = input("Please choose between the following:\n" + "\n".join([f"{i+1}. {choice}" for i, choice in enumerate(choices)]) + "\n")
    try:
        choice = int(choice)
        if choice < 1 or choice > len(choices):
            raise ValueError
    except ValueError:
        print("Invalid choice. Please try again.")
        return extract_multiple_choice_answer(choices)

    return choice - 1


def generate_question_tree(known_rules, used_rules):
    """Generates the question tree based on the known and used rules.
    
    Args:
        known_rules (list): A list of known rules.
        used_rules (list): A list of used rules.
        
    Returns:
        dict: A dictionary containing the question tree.

    """
    rules_tree = dict()
    for rule in general_rules:
        # extract all conditions that weren't asked yet
        new_rules = [new_rule for new_rule in rule.antecedent() if new_rule not in used_rules]
        for current_rule in new_rules:
            if current_rule not in rules_tree:
                rules_tree[current_rule] = []
            # remove from list with possible additional facts the facts that are already known
            additional_rules = \
                [dif_rule for dif_rule in new_rules if (dif_rule != current_rule and dif_rule not in known_rules)]
            # append in case not empty list
            if additional_rules:
                rules_tree[current_rule].append(additional_rules)
    return rules_tree

def generate_multiple_choice_questions(question_choices):
    """Generates a multiple choice question based on the question choices.

    Args:
        question_choices (list): A list of question choices.

    Returns:
        str: The generated question.
    """
    question_choices.append("None")
    subject_list = ["the person", "him/her", "the tourist"]  # list of entities to address to the tourist
    subject = random.choice(subject_list)
    question = f"What is true about {subject}:\n" + \
               "\n".join([f"{i + 1}. {question_choices[i].replace('(?x) ', '')}" for i in range(len(question_choices))])
    return question


def generate_yes_no_questions(question_content):
    """Generates a yes/no question based on the question content.
    
    Args:
        question_content (str): The question content.
        
    Returns:
        str: The generated question.
    """
    subject_list = ["the person", "he/she", "the tourist"]  # list of entities to address to the tourist
    subject = random.choice(subject_list)
    # replace holder with the input name
    question_body = populate(question_content, {"x": subject})
    # build the structure of the question according to its grammatical specifics
    if ' is ' in question_body:
        question_body = question_body.replace('is ', "")
        question = f"Is {question_body}?"
    elif ' has ' in question_body:
        question_body = question_body.replace("has", "have")
        question = f"Does {question_body}"
    else:
        words = question_body.split()
        question_body = question_body.replace(words[1], words[1][:-1])
        question = f"Does {question_body}"
    return question


def interpret_yes_no_answer():
    """Interprets the yes/no answer.
    
    Returns:
        str: The interpreted answer.
    """
    answer = input("Answer: ").upper()
    if answer not in ["YES", "NO"]:
        return interpret_yes_no_answer()
    return answer


def resolve_formatting(cond_instance):
    """Resolves the AND/OR condition instance."""
    for element in cond_instance:
        for fact in element:
            if isinstance(fact, (AND, OR)) or isinstance(fact, list):
                resolve_formatting(fact)
            else:
                print(fact[4:], end=",\n")