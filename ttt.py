# tic tac toe related logic

#TODO: need to pass in board state
def moves():
    m = win_moves()
    if len(m) > 0:
        return m
    m = block_moves()
    if len(m) > 0:
        return m
    m = fork_moves()
    if len(m) > 0:
        return m
    m = block_fork()
    if len(m) > 0:
        return m
    m = center_move()
    if len(m) > 0:
        return m
    m = opposite_corner()
    if len(m) > 0:
        return m
    m = empty_corner()
    if len(m) > 0:
        return m
    m = empty_side()
    if len(m) > 0:
        return m

    return []

#need to pass in board state
def win_moves():
    print("Not implemented yet")
    m = check_column_1()
    if len(m) > 0 :
        return m 
    m = check_column_2()
    if len(m) > 0 :
        return m 
    m = check_column_3()
    if len(m) > 0 :
        return m 
    m = check_row_1()
    if len(m) > 0 :
        return m 
    m = check_row_2()
    if len(m) > 0 :
        return m 
    m = check_row_3()
    if len(m) > 0 :
        return m 
    m = check_diagonal_1()
    if len(m) > 0 :
        return m 
    m = check_diagonal_2()
    if len(m) > 0 :
        return m 

def check_column_1(space1,space4,space7) -> []:
    print("Not implemented yet")
    return[]

def check_column_2(space2,space5,space8) -> []:
    print("Not implemented yet")
    return[]

def check_column_3(space3,space6,space9) -> []:
    print("Not implemented yet")
    return[]

def check_row_1(space1,space2,space3) -> []:
    print("Not implemented yet")
    return[]

def check_row_2(space4, space5,space6) -> []: 
    print("Not implemented yet")
    return[]

def check_row_3(space7,space8,space9) -> []:
    print("Not implemented yet")
    return[]

def check_diagonal_1(space1,space5,space9) -> []:
    print("Not implemented yet")
    return[]

def check_diagonal_2(space3,space5,space7) -> []:
    print("Not implemented yet")
    return[]

def block_moves():
    print("Not implemented yet")

def fork_moves():
    print("Not implemented yet")

def block_fork():
    print("Not implemented yet")

def center_move():
    print("Not implemented yet")

def opposite_corner():
    print("Not implemented yet")

def empty_corner():
    print("Not implemented yet")

def empty_side():
    print("Not implemented yet")

