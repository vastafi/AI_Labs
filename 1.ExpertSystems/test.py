from helpers.question_helper import extract_multiple_choice_answer
from helpers.chain_helper import chain

def run_expert_system():
    stop_system = False

    while not stop_system:

        input_name = input("Please provide the name of the tourist:")
        input_mode = extract_multiple_choice_answer(["Forward chain", "Backward chain"])
        session_data = {"name": input_name, "mode": input_mode}

        stop_system = chain(session_data)


if __name__=='__main__':
    print("Welcome to Expert System!")

    run_expert_system()
