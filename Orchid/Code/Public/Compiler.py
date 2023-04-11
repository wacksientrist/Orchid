import re

pattern = r'^if\s+(.*)\s*:\s*(.*)\s*else\s*:\s*(.*)$'
if_statement = 'if x > 5: print("x is greater than 5")\nelse: print("x is less than or equal to 5")'

if_statement = open("Code/Input_Code/test.py", "r").read().splitlines()
if_statement = "if A != B: A+1else: pass"

match = re.match(pattern, if_statement)
out = open("Code\Input_Code\out.py", "a")

if match:
    condition = match.group(1)
    if_statements = match.group(2)
    else_statements = match.group(3)

    condition2 = condition.split(None)
    out.write(f'C1.Process({condition[0]},{condition[5]},"IF{condition[2]}")')
    out.write(f'\nif C1.Read(): \n\t{if_statements}')
    out.write(f'\nelse: \n\t{else_statements}')
else:
    print('No match found.')
