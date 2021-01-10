def tower_builder(n):
    star = "*"
    space = " "
    tower = []
    ends = []

    for i in range(1, n+1):
        if len(tower) == 0:
            value = (space * (n//2)) + star + (space * (n//2))
            tower.append(value)
            ends = [(n//2)-1, (n//2)+1]
        tower.append(space * (n+1)  )
        for el in ends:
            tower[i][el] = star
            # ends[el] = ends[el] - 1

    return tower

        

print(tower_builder(7))
