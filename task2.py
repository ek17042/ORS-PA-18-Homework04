"""
===================   TASK 2   ====================
* Name: Even and Odd Numbers
*
* Write a script that will populate list with as
* many elements as user defines. For taken number
* of elements the script should take the input from
* user for each element. You should expect that user
* will always provide integer numbers. At the end,
* script should print how many even and odd numbers
* were present in list.
*
*
* Note: Please describe in details possible cases
* in which your solution might not work.
===================================================
"""
def evenodd():
    a = input("Please enter an intiger value:")
    number_of_even = 0
    number_of_odd = 0
    for i in range(0,len(a)):
        if int(a[i]) % 2 == 0:
            number_of_even += 1
        else:
            number_of_odd += 1

    print("Number of even numbers is",number_of_even)
    print("Number of odd numbers is",number_of_odd)


evenodd()