def is_balanced(expression):
    tracker = []
    mapping = {'(': ')',
               '{': '}',
               '[': ']'}

    for char in expression:
        if char in mapping.keys():
            tracker.append(mapping[char])
        elif char in tracker:
            tracker.remove(char)
        elif char in mapping.values():
            tracker.append(char)

    return not bool(tracker)


def main():
    examples = [
        ('((()))', True),
        ('(){}[]', True),
        ('[](){x.open(){{[a + 7]}}}', True),
        ('[]()()((([x - 3]))', False),
        (')))((()))', False)]

    for i, (example, answer) in enumerate(examples, start=1):
        result = is_balanced(example)
        mark = 'PASSED'
        if result != answer:
            mark = 'FAILED!'

        print(f'{i}\tstatement: "{example}"')
        print(f'\tresult: {result}')
        print(f'\tanswer: {answer}')
        print(f'\t{mark}')


if __name__ == '__main__':
    main()
