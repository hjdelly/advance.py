def get_file_contents(filename):         # create function named get_file contents and takes in a file name as arg
    queried_file = open(filename, 'r')   # now pull in the queried file and set it to open function pass in 2 args, filename and r (read)

    if queried_file.mode == 'r':         # quality check to make sure process works-if the queried file is equal to r now perform the task
        return queried_file.read()       # return the queried file and then the read function


content = get_file_contents('text_content.txt')   # create a variable content set equal to file contents and pass in file location

print(content)                                                 

print("Number of words", len(content.split()))                 # now we print the Number of words(string) and find the length of the content pass in the content and split function 