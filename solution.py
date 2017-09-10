assignments = []

def assign_value(values, box, value):
    """
    Please use this function to update your values dictionary!
    Assigns a value to a given box. If it updates the board record it.
    """

    # Don't waste memory appending actions that don't actually change any values
    if values[box] == value:
        return values

    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values

def naked_twins(values):
    """Eliminate values using the naked twins strategy.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """
    for box in values:
        if len(values[box]) == 2:
            naked_peer = find_naked_twins(values, box)
            if len(naked_peer)>=1:
                for peer in naked_peer:
                    values = eliminate_naked_twin_values(values, peer, box)
    
    return values

def find_naked_twins(values, box):
    """
    Finding the naked twin pairs
    Args:
        values(dict): The sudoku in dictionary form
        box: A box in sudoku for which we are finding the naked twin
    Returns:
        A set of naked twins for the units[box]
    """
    return set(peer for unit in units[box] for peer in unit if values[peer] == values[box] and peer != box)

def eliminate_naked_twin_values(values, peer, box):
    """
    Updating the values in boxes of sudoku by eliminating the naked twin value
    Args:
        values(dict): The sudoku in dictionary form
        peer: A box in sudoku, which is an naked twin of box
        box: A box in sudoku for which we found the naked twin
    Returns:
        The resulting sudoku in dictionary form.
    """
    # Iterating over all the units of box which contains both naked twins(peer and box)
    for unit in units[box]:
        if peer in unit and box in unit:
            # Iterating over all the boxes other than naked twins(peer and box)
            for _box in unit:
                if _box not in box and _box not in peer:
                    # Eliminating the value in naked twin in other boxes
                    for digit in values[box]:
                        if digit in values[_box]:
                            values[_box] = values[_box].replace(digit, "")
    return values

def cross(A, B):
    """
    Cross product of elements in A and elements in B.
    """
    return [a+b for a in A for b in B]
    
def grid_values(grid):
    """
    Convert grid into a dict of {square: char} with '123456789' for empties.
    Args:
        grid(string) - A grid in string form.
    Returns:
        A grid in dictionary form
            Keys: The boxes, e.g., 'A1'
            Values: The value in each box, e.g., '8'. If the box has no value, then the value will be '123456789'.
    """
    values = {}
    for num in range(len(grid)):
        if grid[num] != '.':
            values[boxes[num]] = grid[num]
        else:
            values[boxes[num]] = '123456789'
    
    return values

def display(values):
    """
    Display the values as a 2-D grid.
    Args:
        values(dict): The sudoku in dictionary form
    """
    width = 1+max(len(values[s]) for s in boxes)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)
    return

def eliminate(values):
    """
    Go through all the boxes, and whenever there is a box with a value, eliminate this value from the values of all its peers.
    Input: A sudoku in dictionary form.
    Output: The resulting sudoku in dictionary form.
    """
    for key in values:
        if len(values[key])==1:
            req_units = units[key]
            for unit in req_units:
                for box in unit:
                    if box!=key:
                        values[box] = values[box].replace(values[key],"")
                
    return values

def only_choice(values):
    """
    Go through all the units, and whenever there is a unit with a value that only fits in one box, assign the value to this box.
    Input: A sudoku in dictionary form.
    Output: The resulting sudoku in dictionary form.
    """
    for unit in unitlist:
        for digit in '123456789':
            dplaces = [box for box in unit if digit in values[box]]
            if len(dplaces) == 1:
                values = assign_value(values, dplaces[0], digit)
    return values

def reduce_puzzle(values):  
    """
    Iterate eliminate() and only_choice(). If at some point, there is a box with no available values, return False.
    If the sudoku is solved, return the sudoku.
    If after an iteration of both functions, the sudoku remains the same, return the sudoku.
    Input: A sudoku in dictionary form.
    Output: The resulting sudoku in dictionary form.
    """
    before = len([box for box in values if len(values[box])==1])
    values = eliminate(values)
    values = naked_twins(values)
    values = only_choice(values)
    after = len([box for box in values if len(values[box])==1])
    if len([box for box in values.keys() if len(values[box]) == 0]):
        return False
    if before != after:
        reduce_puzzle(values)
    
    return values

def search(values):
    "Using depth-first search and propagation, create a search tree and solve the sudoku."
    # First, reduce the puzzle using the previous function
    values = reduce_puzzle(values)
    if values is False:
        return False
    isSolved = True
    for key in values:
        if len(values[key])!=1:
            isSolved = False
    
    if isSolved:
        return values
        
    # Choose one of the unfilled squares with the fewest possibilities
    box = find_min_box(values)
    # Now use recursion to solve each one of the resulting sudokus, and if one returns a value (not False), return that answer!
    items = values[box]
    for item in items:
        values_new = dict(values)
        values_new[box] = item
        ret = search(values_new)
        if ret:
            return ret
    
def find_min_box(values):
    """
    Finding the box with minimum length.
    Args:
        The dictionary representation of the final sudoku grid.
    Return:
        A box with minimum length.
    """
    box = None
    min = 10
    for key in values:
        size = len(values[key])
        if size != 1 and size<min:
            min = size
            box = key
    return box

def solve(grid):
    """
    Find the solution to a Sudoku grid.
    Args:
        grid(string): a string representing a sudoku grid.
            Example: '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    Returns:
        The dictionary representation of the final sudoku grid. False if no solution exists.
    """
    values = grid_values(grid)
    values = search(values)
    return values

rows = 'ABCDEFGHI'
cols = '123456789'
boxes = cross(rows, cols)
row_units = [cross(r, cols) for r in rows]
column_units = [cross(rows, c) for c in cols]
square_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]
diagonal_units = [['A1','B2','C3','D4','E5','F6','G7','H8','I9'], ['A9','B8','C7','D6','E5','F4','G3','H2','I1']]
unitlist = row_units + column_units + square_units + diagonal_units
units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)

if __name__ == '__main__':
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    display(solve(diag_sudoku_grid))
    
    try:
        from visualize import visualize_assignments
        visualize_assignments(assignments)

    except SystemExit:
        pass
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')