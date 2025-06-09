import argparse
from csv_reader import read_subject_csv
# from llm_api import call_anthropic  # Uncomment if using Anthropic in your solution

def main():
    parser = argparse.ArgumentParser(description="Intern Test Task: Question to Concept Mapping")
    parser.add_argument('--subject', required=True, choices=['ancient_history', 'math', 'physics', 'economics'], help='Subject to process')
    args = parser.parse_args()

    data = read_subject_csv(args.subject)
    print(f"Loaded {len(data)} questions for subject: {args.subject}")

    # --- PLACEHOLDER FOR USER CODE ---
    # TODO: Implement your question-to-concept mapping logic here.
    # For example, iterate over data and map questions to concepts.
    # You can use the call_anthropic function from llm_api.py if needed.
    # Example:
    # for row in data:
    #     question = row['question']
    #     # concept = call_anthropic(f"Map this question to a concept: {question}")
    #     # print({"question": question, "concept": concept})
    # ----------------------------------

if __name__ == "__main__":
    main()
