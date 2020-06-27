# Task
#
# You have a non-empty set s, and you have to execute N commands given in Nlines.
# The commands will be pop, remove and discard.


if __name__ == '__main__':
    max_value = int(input())
    s = set(map(int, input().split()))
    instructions = {"discard": s.discard, "pop": s.pop, "remove": s.remove}
    instruction_number = int(input())

    for _ in range(instruction_number):
        input_ = input().split()
        instruction = input_[0]
        instructions[instruction](int(input_[1])) if len(input_) > 1 else instructions[instruction]()

    print(sum(s))
