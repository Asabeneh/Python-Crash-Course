import re


def wrapper_function():
    # this wrap all the functions below
    print("Hello world!") # print uses to print strings, numbers and any data type
    print("Washera Academy")
    print("Your name")
    print(100)
    print(200)
    print(True)
    print(False)
    name = "Washera"
    age = 100
    print("My name", "is", name, ". I am ", age, "years old. ")
    # 1. Looping and printing
    # Write code that prints every integer between 0 and 20.
    i = 0
    while i <= 20:
        print(i)
        i += 1
    for j in range(21):
        print("The value of j is", j)
    # 2. Defining functions
    """Modify the previous code and define the code snippet as a function.
    Also, put the numbers into an array instead of printing. 
    The function should take no input parameters and return an array. 
    Call the function and print the output (i.e. print(my_function())) """

    def looping():
        arr = []
        for k in range(21):
            arr.append(k)
        return arr

    print(looping())
    # 3. Reverse and return
    """ Define a function that takes an array as an input parameter.
    Return a reverse array of the input array. 
    (You may also reverse the original array in-place.
        Just make sure you know which way you're doing it.) """
    def array_reverse(arr):
        new_array = []
        for i in range(len(arr)):
            new_array.append(arr[len(arr)-i-1])
        return new_array

    print(array_reverse([10,20,30,40,50]))
    """4.Writing to files
    Define a function that:
    Takes an array as an input parameter
    Opens a file
    Writes each value from the input array to the file
    Closes the file"""
    def writefile(arr):
        f= open("example.txt","w")
        for i in range(len(arr)):
            f.write(str(arr[i]))

    writefile([10, 20, 30, 40])
    """
    5. Reading from files
    Define a function that:
    Opens a file. Give the filename as a parameter
    Reads the file line by line and parse for an integer on each line (Beware of newline characters in line-by-line reading!)
    Sum all integers you read from the file
    Return the sum"""

    def open_file():
        total = 0
        file_name = input("Enter file name(income or product): ")
        try:
            file_open = open(file_name)
        except:
            print("File wad not found!")
            exit()
        for line in file_open:
            if line:
                numbers = re.findall(r'\d+', line.strip())
                for n in numbers:
                    total += int(n)
        print(numbers)
        print("The sum is ", total)
    open_file()


wrapper_function()




















