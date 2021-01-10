def delete_nth(order, max_e):
    result = []

    for i in range(len(order)):
        counted = result.count(order[i])
        if counted != max_e:
            result.append(order[i])
    return result


    


print(delete_nth([20, 37, 20, 21], 1))
