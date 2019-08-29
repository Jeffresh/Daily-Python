funcion = { 'Computable': ["suma","multipicación","potencia","factorial"], 'No computable':{'nombre':["resta",'division']}}




if __name__ == '__main__':

    pistola =None
    k = list(funcion['No computable'].keys())

    for i in k:
        print(i)