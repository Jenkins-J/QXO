# tic tac toe related logic

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

def win_moves():
    print("Not implemented yet")

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

