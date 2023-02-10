# tic tac toe related logic

#TODO: need to pass in board state
def moves(space1: int, space2: int, space3: int, space4: int, space5: int, space6: int, space7: int, space8: int, space9: int, mark_in: int):
    global mark
    mark = mark_in
    m = win_moves(space1, space2, space3, space4, space5, space6, space7, space8, space9)
    if len(m) > 0:
        return m 
    if (mark == "1"):
        mark = "0"
    else:
        mark = "1"
    m = block_moves(space1, space2, space3, space4, space5, space6, space7, space8, space9)
    if len(m) > 0:
        return m
    if (mark == "1"):
        mark = "0"
    else:
        mark = "1"
    # NOT IMPLEMENTED YET
    '''
    m = fork_moves()
    if len(m) > 0:
        return m
    m = block_fork()
    if len(m) > 0:
        return m
    '''
    m = center_move(space5)
    if len(m) > 0:
        return m
    m = opposite_corner(space1, space3, space7, space9)
    if len(m) > 0:
        return m
    else:
        return []
    '''
    m = empty_corner()
    if len(m) > 0:
        return m
    m = empty_side()
    if len(m) > 0:
        return m
    return []
    '''
    
def win_moves(space1, space2, space3, space4, space5, space6, space7, space8, space9) -> []:
    m = []
    result = check_column_1(space1,space4,space7)
    if result != 0:
        m.append(result)
    result = check_column_2(space2,space5,space8)
    if result != 0:
        m.append(result)
    result = check_column_3(space3,space6, space9)
    if result != 0:
        m.append(result)
    result = check_row_1(space1,space2,space3)
    if result != 0:
        m.append(result)
    result = check_row_2(space4,space5,space6)
    if result != 0:
        m.append(result)
    result = check_row_3(space7,space8,space9)
    if result != 0:
        m.append(result)
    result = check_diagonal_1(space1,space5,space9)
    if result != 0:
        m.append(result)
    result = check_diagonal_2(space3,space5,space7)
    if  result != 0:
        m.append(result)
    return m  

#1,4,7
def check_column_1(space1,space2,space3) -> int:
    if(space1 == mark and space1 == space2 and space3 == None):
        return 7
    elif(space2 == mark and space2 == space3 and space1 == None):
        return 1
    elif(space1 == mark and space1 == space3 and space2 == None):
        return 4
    return 0

#2,5,8
def check_column_2(space1,space2,space3) -> int:
    if(space1 == mark and space1 == space2 and space3 == None):
        return 8
    elif(space2 == mark and space2 == space3 and space1 == None):
        return 2
    elif(space1 == mark and space1 == space3 and space2 == None):
        return 5
    return 0

#3,6,9
def check_column_3(space1,space2,space3) -> int:
    if(space1 == mark and space1 == space2 and space3 == None):
        return 9
    elif(space2 == mark and space2 == space3 and space1 == None):
        return 3
    elif(space1 == mark and space1 == space3 and space2 == None):
        return 6
    return 0 

#1,2,3
def check_row_1(space1,space2,space3) -> int:
    if(space1 == mark and space1 == space2 and space3 == None):
        return 3
    elif(space2 == mark and space2 == space3 and space1 == None):
        return 1
    elif(space1 == mark and space1 == space3 and space2 == None):
        return 2
    return 0

#4,5,6
def check_row_2(space1, space2,space3) -> int: 
    if(space1 == mark and space1 == space2 and space3 == None):
        return 6
    elif(space2 == mark and space2 == space3 and space1 == None):
        return 4
    elif(space1 == mark and space1 == space3 and space2 == None):
        return 5
    return 0

#7,8,9
def check_row_3(space1,space2,space3) -> int:
    if(space1 == mark and space1 == space2 and space3 == None):
        return 9
    elif(space2 == mark and space2 == space3 and space1 == None):
        return 7
    elif(space1 == mark and space1 == space3 and space2 == None):
        return 8
    return 0

#1,5,9
def check_diagonal_1(space1,space2,space3) -> int:
    if(space1 == mark and space1 == space2 and space3 == None):
        return 9
    elif(space2 == mark and space2 == space3 and space1 == None):
        return 1
    elif(space1 == mark and space1 == space3 and space2 == None):
        return 5
    return 0

#3,5,7
def check_diagonal_2(space1,space2,space3) -> int: 
    if(space1 == mark and space1 == space2 and space3 == None):
        return 7
    elif(space2 == mark and space2 == space3 and space1 == None):
        return 3
    elif(space1 == mark and space1 == space3 and space2 == None):
        return 5
    return 0

def block_moves(space1, space2, space3, space4, space5, space6, space7, space8, space9) -> []:
    m = []
    result = check_column_1(space1,space4,space7)
    if result != 0:
        m.append(result)
    result = check_column_2(space2,space5,space8)
    if result != 0:
        m.append(result)
    result = check_column_3(space3,space6, space9)
    if result != 0:
        m.append(result)
    result = check_row_1(space1,space2,space3)
    if result != 0:
        m.append(result)
    result = check_row_2(space4,space5,space6)
    if result != 0:
        m.append(result)
    result = check_row_3(space7,space8,space9)
    if result != 0:
        m.append(result)
    result = check_diagonal_1(space1,space5,space9)
    if result != 0:
        m.append(result)
    result = check_diagonal_2(space3,space5,space7)
    if  result != 0:
        m.append(result)
    return m

def fork_moves():
    print("Not implemented yet")

def block_fork():
    print("Not implemented yet")

def center_move(space5) -> []:
    if (space5 == None):
        return [5]
    return []

def opposite_corner(space1, space3, space7, space9) -> []:
    m = []
    result = check_opp_corner_1(space1,space9)
    if result != 0:
        m.append(result)
    result = check_opp_corner_2(space3,space7)
    if result != 0:
        m.append(result)
    return m

def check_opp_corner_1(space1,space9) -> int:
    if (space1 != mark and space9 == None):
        return 9
    if (space9 != mark and space1 == None):
        return 1
    return 0

def check_opp_corner_2(space3,space7) -> int:
    if (space3 != mark and space7 == None):
        return 7
    if (space7 != mark and space3 == None):
        return 3
    return 0


def empty_corner():
    print("Not implemented yet")

def empty_side():
    print("Not implemented yet")

