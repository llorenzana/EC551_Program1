from itertools import product
class BooleanFunction:
    def __init__(self, expression, variables):
        self.expression = expression
        self.variables = variables

    def generate_terms(self):
        minterms = []
        maxterms = []

        num_variables = len(self.variables)
        truth_values = list(product([0, 1], repeat=num_variables))

        for values in truth_values:
            assignment = dict(zip(self.variables, values))
            result = eval(self.expression, assignment)

            if result == 1:
                minterm = ''.join(str(value) for value in values)
                minterms.append(minterm)
                
            if result == 0:
                maxterm = ''.join(str(value) for value in values)
                maxterms.append(maxterm)
    
        # Convert minterms to an expanded sum of minterms
        expanded_sum_of_minterms = self.expand_minterms(minterms)
        expanded_product_of_maxterms = self.expand_maxterms(maxterms)

        return minterms, expanded_sum_of_minterms, maxterms, expanded_product_of_maxterms

    def expand_minterms(self, minterms):
        expanded_sum_of_minterms = []

        for minterm in minterms:
            term = ""
            for i, value in enumerate(minterm):
                if value == '0':
                    term += f"~{self.variables[i]}   "
                elif value == '1':
                    term += f"{self.variables[i]}   "
                    
            # Remove the trailing "&"
            term = term[:-2]
            expanded_sum_of_minterms.append(term)

        return " + ".join(expanded_sum_of_minterms)

    def expand_maxterms(self, maxterms):
        expanded_product_of_maxterms = []

        for maxterm in maxterms:
            term = ""
            for i, value in enumerate(maxterm):
                if value == '0':
                    term += f"{self.variables[i]} | "
                elif value == '1':
                    term += f"~{self.variables[i]} | "

            # Remove the trailing "|"
            term = term[:-2]
            expanded_product_of_maxterms.append(term)

        return " & ".join(expanded_product_of_maxterms)


def countPI_EPI(mt):

    def findEPI(x): # Function to find essential prime implicants from prime implicants chart
        res = []
        for i in x:
            if len(x[i]) == 1:
                res.append(x[i][0]) if x[i][0] not in res else None
        return res

    def flatten(x): # Flattens a list
        flattened_items = []
        for i in x:
            flattened_items.extend(x[i])
        return flattened_items

    def findminterms(a): #Function for finding out which minterms are merged. For example, 10-1 is obtained by merging 9(1001) and 11(1011)
        gaps = a.count('-')
        if gaps == 0:
            return [str(int(a,2))]
        x = [bin(i)[2:].zfill(gaps) for i in range(pow(2,gaps))]
        temp = []
        for i in range(pow(2,gaps)):
            temp2,ind = a[:],-1
            for j in x[0]:
                if ind != -1:
                    ind = ind+temp2[ind+1:].find('-')+1
                else:
                    ind = temp2[ind+1:].find('-')
                temp2 = temp2[:ind]+j+temp2[ind+1:]
            temp.append(str(int(temp2,2)))
            x.pop(0)
        return temp

    def compare(a,b): # Function for checking if 2 minterms differ by 1 bit only
        c = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                mismatch_index = i
                c += 1
                if c>1:
                    return (False,None)
        return (True,mismatch_index)
         
    mt.sort()
    minterms = mt
    minterms.sort()
    size = len(bin(minterms[-1]))-2
    groups,all_pi = {},set()

    # Primary grouping starts
    for minterm in minterms:
        try:
            groups[bin(minterm).count('1')].append(bin(minterm)[2:].zfill(size))
        except KeyError:
            groups[bin(minterm).count('1')] = [bin(minterm)[2:].zfill(size)]

    while True:
        tmp = groups.copy()
        groups,m,marked,should_stop = {},0,set(),True
        l = sorted(list(tmp.keys()))
        for i in range(len(l)-1):
            for j in tmp[l[i]]: # Loop which iterates through current group elements
                for k in tmp[l[i+1]]: # Loop which iterates through next group elements
                    res = compare(j,k) # Compare the minterms
                    if res[0]: # If the minterms differ by 1 bit only
                        try:
                            groups[m].append(j[:res[1]]+'-'+j[res[1]+1:]) if j[:res[1]]+'-'+j[res[1]+1:] not in groups[m] else None # Put a '-' in the changing bit and add it to corresponding group
                        except KeyError:
                            groups[m] = [j[:res[1]]+'-'+j[res[1]+1:]] # If the group doesn't exist, create the group at first and then put a '-' in the changing bit and add it to the newly created group
                        should_stop = False
                        marked.add(j) # Mark element j
                        marked.add(k) # Mark element k
            m += 1
        local_unmarked = set(flatten(tmp)).difference(marked) # Unmarked elements of each table
        all_pi = all_pi.union(local_unmarked) # Adding Prime Implicants to global list
        if should_stop: # If the minterms cannot be combined further
            break        

    # Prime Implicant Chart begin
    sz = len(str(mt[-1])) # The number of digits of the largest minterm
    chart = {}
    for i in all_pi:
        merged_minterms,y = findminterms(i),0
        for j in merged_minterms:
            x = mt.index(int(j))*(sz+1) # The position where we should put 'X'
            y = x+sz
            try:
                chart[j].append(i) if i not in chart[j] else None # Add minterm in chart
            except KeyError:
                chart[j] = [i]
    # Printing and processing of Prime Implicant chart ends

    EPI = findEPI(chart) # Finding essential prime implicants
    return all_pi, EPI


print("Welcome: Please select which you would like to do 1 or 2")
expression = input("Boolean Equation, please use ~ to indicate a NOT: ")
v_in = input("Enter input variables separated by a space: ")
vars = v_in.split()

boolean_function = BooleanFunction(expression, vars)
minterms, _, maxterms, _ = boolean_function.generate_terms()

print("Generated Minterms:", minterms)
print("Generated Maxterms:", maxterms)

PI, EPI =  countPI_EPI([int(minterm, 2) for minterm in minterms] )
print("Number of Prime Implicants:", len(PI))
print("Number of Essential Prime Implicants:", len(EPI))
