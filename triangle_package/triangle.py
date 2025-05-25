def print_triangle(rows):
    """
    Prints a right-angled triangle pattern using asterisks.
    
    Args:
        rows (int): Number of rows in the triangle
    """
    if not isinstance(rows, int) or rows <= 0:
        print("Error: rows must be a positive integer")
        return
        
    for i in range(1, rows + 1):
        print('*' * i)
