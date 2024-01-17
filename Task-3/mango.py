def distribute_mangoes(bags, students):
    bags.sort()
    mango_diff = float('inf')

    for i in range(students - 1):
        min_bags = bags[:i+1]
        max_bags = bags[students-i-2:]

        min_mangoes = sum(min_bags)
        max_mangoes = sum(max_bags)

        current_diff = max_mangoes - min_mangoes
        mango_diff = min(mango_diff, current_diff)

    return mango_diff

bags = [3, 7, 2, 5, 9, 1]
students = 5
print(distribute_mangoes(bags,students))

