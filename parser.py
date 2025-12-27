import re

def extract_questions_and_options(input_file, output_file):
    with open(input_file, 'r') as f:
        content = f.read()

    # Regex to find questions and options
    pattern = re.compile(r'(\d+\.\nQuestion \d+.*?)(?=\d+\.\nQuestion \d+|\Z)', re.DOTALL)
    matches = pattern.findall(content)

    with open(output_file, 'w') as f:
        for match in matches:
            # Extract the question
            question_pattern = re.compile(r'Question \d+\n(.*?)\n\nYou are a helpful AI assistant.', re.DOTALL)
            question_match = question_pattern.search(match)
            if question_match:
                question = question_match.group(1).strip()
                f.write(f"Question: {question}\n")

            # Extract options
            options_pattern = re.compile(r'To uphold Coursera\'s academic integrity policy.*?\n\n(.*?)\n\n1 point', re.DOTALL)
            options_match = options_pattern.search(match)
            if options_match:
                options = options_match.group(1).strip().split('\n\n\n\n')
                for i, option in enumerate(options):
                    f.write(f"  Option {i+1}: {option.strip()}\n")
            f.write('\n')

if __name__ == "__main__":
    extract_questions_and_options('/Users/mounusha/Downloads/code_coursera/input.txt', '/Users/mounusha/Downloads/code_coursera/output.txt')
