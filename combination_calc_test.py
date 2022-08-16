vals = [1, 2, 3, 4]
operators = ['+', '*', '-', '/']

def expressions(values):
    # Base case, only one value left
    if len(values) == 1:
        yield values

    # Iterate over the indexes
    for i in range(len(values)):
        # Pop value from given index and store the remaining values
        # to be used with next recursion
        forward = values[:]
        val = forward.pop(i)

        # Yield all value, operator, subexpression combinations
        for op in operators:
            for rest in expressions(forward):
                yield [val, op] + rest

for expr in expressions(vals):
    expr = ' '.join(str(x) for x in expr)
    print('{} = {}'.format(expr, eval(expr)))
