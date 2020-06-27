# TASK
# You are given a set A and N number of other sets.
# These N number of sets have to perform some specific mutation operations on set A .

if __name__ == '__main__':
    max_value = int(input())
    s = set(map(int, input().split()))
    instruction_number = int(input())

    instructions = {"intersection_update": s.intersection_update,
                    "symmetric_difference_update": s.symmetric_difference_update,
                    "difference_update": s.difference_update,
                    "update": s.update}

    for _ in range(instruction_number):
        input_ = input().split()
        instruction = input_[0]
        value = set(map(int, input().split()))
        instructions[instruction](value)

    print(sum(s))
