# Write a program that reads a sequence of numbers from the first line and the number x from the second line.
# Then it should output all positions of x in the numerical sequence.
#
# The position count starts from 0. In case if x is not in the sequence, print the line "not found"
# (quotes omitted, lowercased).
#
# Positions should be displayed in one line, in ascending order of the value.

if __name__ == '__main__':
   numbers = input().split()
   x = int(input())
   len_numbers = len(numbers)
   index_list = [i for i in range(len_numbers) if numbers[i] == x]
   print("not found") if not index_list else print(index_list)
