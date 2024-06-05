import re
import random

def replace_operations_with_preceding_process(file_path, num_instances):
    # Read the contents of the file
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    # Add the import and initialization lines at the start
    header = ["from Public.Orchid import Instance\n"]
    instances = set()

    # Define a function to replace each operation
    def replace_operations(line):
        indent = re.match(r'^(\s*)', line).group(1)
        segments = re.split(r'(\b\w+\b\s*=\s*\b\w+\b\s*[\+\-\*/]\s*\b\w+\b)', line)
        processed_line = ""

        for segment in segments:
            if re.match(r'\b\w+\b\s*=\s*\b\w+\b\s*[\+\-\*/]\s*\b\w+\b', segment):
                variable, operation = re.split(r'\s*=\s*', segment)
                operators = re.split(r'\s*[\+\-\*/]\s*', operation)
                
                if len(operators) != 2:
                    # Handle cases where the split didn't produce exactly two operands
                    processed_line += segment
                    continue
                
                operator1, operator2 = operators

                instance_number = random.randint(1, num_instances)
                instance = f"C{instance_number}"
                instances.add(instance_number)

                operation_type = re.findall(r'[\+\-\*/]', operation)[0]

                processed_line += f"{indent.replace("\t", "")}{instance}.Process({operator1.strip()}, {operator2.strip()}, '{operation_type}')\n"
                processed_line += f"{indent}{variable.strip()} = {instance}.Read()"
            else:
                processed_line += segment

        return processed_line

    # Use regular expressions to find lines with operations and create a new content list
    new_lines = []
    for line in lines:
        new_line = replace_operations(line)
        new_lines.append(new_line)

    # Add instance initialization to the header
    for instance_number in sorted(instances):
        header.append(f"C{instance_number} = Instance('{instance_number}')\n")

    # Write the modified content back to the file
    with open(file_path, 'w') as file:
        file.writelines(header + new_lines)

# Example usage
replace_operations_with_preceding_process('main.py', 3)
