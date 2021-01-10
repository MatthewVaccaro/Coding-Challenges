# Implement the function unique_in_order which takes as argument a sequence and returns a
# list of items without any elements with the same value next to each other and preserving
# the original order of elements.

def unique_in_order(iterable):
    result = []

    if len(iterable) > 0:
        result.append(iterable[0])

        for i in range(len(iterable)):
            if iterable[i] is not result[-1]:
                result.append(iterable[i])

        return result
    
    else:
        return result

print(unique_in_order('A'))
