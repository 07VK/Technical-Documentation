def chomp(r, c):
    """ Determine the first move for a winning strategy for
    Player A in a game of chomp with a chocolate bar
    
    Parameters:
    r (int): The number of rows in the chocolate bar
    c (int): The number of columns in the chocolate bar
    
    Returns:
    "none" if player A is not guaranteed a win
    i,j: The first square player A should choose if player A
         is guaranteed a win.  If more than one move exists,
         return the one that minimizes: i * 100 + j   
    """
    if c < 1 or c > 10 or r < 1 or r > 10:
        raise ValueError("Invalid size for chocolate bar.")
    
    # Dictionary to cache results of game positions
    memo = {}
    
    def can_win(position):
        
        # Base case: if all rows have 0 columns, the bar is empty, so the player loses
        if all(length == 0 for length in position):
            return False
        
        # Check if this position was computed before
        if position in memo:
            return memo[position]
        
        # Try all possible moves by selecting a cell to chomp
        for row in range(r):
            for col in range(position[row]):
                # Create new position after chomping at (row, col)
                new_position = list(position)
                # Update rows from 'row' downward to have at most 'col' columns
                for i in range(row, r):
                    new_position[i] = min(new_position[i], col)
                new_position = tuple(new_position)
                
                # Check if the new position is non-empty and leads to a losing position for the opponent
                if any(length > 0 for length in new_position) and not can_win(new_position):
                    memo[position] = True
                    return True
        
        # No winning move found, so this is a losing position
        memo[position] = False
        return False
    
    # Create initial game position: all rows have 'c' columns
    initial_bar = tuple([c] * r)
    
    # Check if Player A can win from the initial position
    if not can_win(initial_bar):
        return "none"
    
    # Find the first winning move that minimizes row * 100 + col
    for row in range(r):
        for col in range(c):
            # Simulate chomping at (row, col): rows before 'row' unchanged, others set to 'col'
            new_position = [c] * row + [col] * (r - row)
            new_position = tuple(new_position)
            # If the move is valid and leads to a losing position for Player B, return it
            if any(length > 0 for length in new_position) and not can_win(new_position):
                return (row, col)
    
    # Shouldn't reach here if can_win is True, but included for safety
    return "none"

def main():
	tests = [((3,2),(2,1)), \
	         ((4,5),(2,2)), \
			 ((9,9),(1,1))]

	for input,expected in tests:
		assert chomp(input) == expected
		
if __name__ == "__main__":
    main()
