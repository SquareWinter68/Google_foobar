def solution_(i):

    digit_sum = sum(i)

    if not digit_sum%3:
        return "".join([str(i) for i in sorted(i, reverse=True)])
    else:
        non_devisible_elements = list(filter(lambda x: x%3, i))
        target = digit_sum%3
        potential_results = [_ for _ in non_devisible_elements if _%3== target]
        if len(potential_results) >= 1:
            result = i[:]
            result.pop(result.index(min(potential_results)))
            return "".join([str(_) for _ in sorted(result, reverse=True)])
        elif len(potential_results) == 0:
            #print non_devisible_elements
            for element in range(len(non_devisible_elements)-1):
                if not (non_devisible_elements[element] + non_devisible_elements[element+1])%3 == target:
                    i.pop(i.index(non_devisible_elements[element]))
                    i.pop(i.index(non_devisible_elements[element+1]))
                    return "".join([str(_) for _ in sorted(i, reverse=True)])
                else:
                    return 0

print solution_([1,1])