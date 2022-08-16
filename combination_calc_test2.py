from itertools import chain, permutations

def powerset(iterable):
  xs = list(iterable)
  return print(chain.from_iterable(permutations(xs,n) for n in range(len(xs)+1)) )

lst_expr = []
for operands in map(list, powerset(['1','2','3','4'])):
    n = len(operands)
    #print operands
    if n > 1:
        all_operators = map(list, permutations(['+','-','*','/'],n-1))
        #print all_operators, operands
        for operators in all_operators:
            exp = operands[0]
            i = 1
            for operator in operators:
                exp += operator + operands[i]
                i += 1
            lst_expr += [exp]
