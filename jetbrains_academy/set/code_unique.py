# Imagine you have information about subjects three students study. It could be in the following format:
#
# Belov = ["Physics", "Math", "Russian"]
# Smith = ["Math", "Geometry", "English"]
# Sarada = ["Japanese", "Math", "Physics"]
#
# The subjects can be the same or differ. Your task is to find the number of unique subjects. For example,
# in the lists above we have 6 different subjects: Physics, Math, Russian, Geometry, English, and Japanese,
# so you should print 6 as the answer.
#
# In this task, you're given the variables to work with: Belov, Smith, and Sarada.

if __name__ == '__main__':
    # The following code is needed for us to check your answer, do not modify it, please.

    students = json.loads(input())
    Belov = students['Belov']
    Smith = students['Smith']
    Sarada = students['Sarada']

    # Your code here. Work with the variables 'Belov', 'Smith', and 'Sarada'
    print(len(set(Belov + Smith + Sarada)))
