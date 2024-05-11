def arithmetic_arranger(problems, show_answers=False):
    # Check if there are too many problems
    if len(problems) > 5:
        return "Error: Too many problems."

    # Split each problem into its components
    components = [problem.split() for problem in problems]

    # Check if each problem has only two operands and a valid operator
    valid_operators = ['+', '-']
    for component in components:
        if len(component) != 3:
            return "Error: Each problem should have exactly 3 components."
        elif component[1] not in valid_operators:
            return "Error: Operator must be '+' or '-'."
        elif not component[0].isdigit() or not component[2].isdigit():
            return "Error: Operands must be integers."

    # Calculate the answers
    answers = []
    for component in components:
        if component[1] == '+':
            answer = int(component[0]) + int(component[2])
        else:
            answer = int(component[0]) - int(component[2])
        answers.append(str(answer))

    # Arrange the problems and optionally the answers
    arranged_problems = ''
    for i in range(len(components)):
        component = components[i]
        length1 = len(component[0])
        length2 = len(component[2])
        length = max(length1, length2) + 2
        arranged_problems += component[0].rjust(length) + ' '
        arranged_problems += component[1] + ' '
        arranged_problems += component[2].rjust(length-1) + ' '
        arranged_problems += '\n'

    if show_answers:
        for i in range(len(components)):
            answer = answers[i]
            length = len(components[i][2]) + 2
            arranged_problems += '-' * length + ' '
            arranged_problems += '\n'
            arranged_problems += answer.rjust(length) + ' '
            arranged_problems += '\n'

    return arranged_problems.rstrip()

problems = ['32 + 698', '3801 - 2', '45 + 43', '123 + 49']
print(arithmetic_arranger(problems, show_answers=True))

