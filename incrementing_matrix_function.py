"""
[
    [0, 1, 2, 3, 4],
    [1, 2, 3, 4, 5],
    [2, 3, 4, 5, 6],
    [3, 4, 5, 6, 7],
    [4, 5, 6, 7, 8],
]
"""
def manual_incrementing_matrix(n): #function takes in how many items
    # matrix n x n
    matrix = [ [ None for y in range(n) ] for x in range(n) ]  # first step to generate an empty matrix, list comprehension...took nested item 
                                                               # added value of none (loop over range)
                                                               # and then return the value of none
    counter = 0 

    for idx, el in enumerate(matrix): # for index in element in matrix-now to keep track..so pass enumerate and matrix
                                      #(to know where to start off with)

        for nested_idx, nested_el in enumerate(el):   #nested loop-for nested index and nested element(value), (iterating through)...loop over 
                                                      # the element enumerate(el)
            matrix[idx][nested_idx] = counter + nested_idx  #now assign the value, grab matrix and index/grab index and index of nested 
                                                            #items..assign the counter which starts at zero
                                                           
        counter += 1    #break out of for loop by saying counter plus equals 1

    return matrix       #returned the variable matrix

print(manual_incrementing_matrix(100))  #printed the function name and passed in how many times to print