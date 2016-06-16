import copy

def solution(numberlist):
    """Simplification 1:
       number is [2, 2, 3, 4, 5]

    return:
        A list of lists: permutation of solutions
    Delet when there are adjacent digits that are the same.
    only delete one such digit
    care for duplicate delete
    it's save to come to the last copy of the above digit and then delete it
    """
    delete_indexes = []
    before = -1
    same_as_last = False
    for idx, i in enumerate(numberlist):
        if same_as_last and (i == before):
            same_as_last = True
        elif same_as_last and (i != before):
            same_as_last = False
            delete_indexes.append(idx - 1)
        elif not same_as_last and (i == before):
            same_as_last = True

        elif not same_as_last and (i != before):
            same_as_last = False

        before = i

    possible_lists = []
    for idx in delete_indexes:
        take_away_list = copy.copy(numberlist)
        take_away_list.pop(idx)
        print take_away_list

mylist = [2, 3, 3, 4, 5, 6, 6, 4, 4, 3]
idxes = solution(mylist)

"""
def listify(number):
    #Args:
    #    number(int):
    #Return:
    #    list of number like [2, 2, 3, 4, 6]


mynumber = 2233456667822

numberlist = listify(mynumber)

childnumberlists = solution(numberlist)

final_solution = max(childnumberlists)
"""


