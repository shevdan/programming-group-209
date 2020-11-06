import random

'''
'''
# IMPORTANT: do not forget about thoughtful documentation
#
#
# TODO: documentation, everyone should look through the code,
# and propose some improvements.



def user_number_type(number: int, number_type: str) -> bool:
    ''' Just in case we will need to determine what
    type of number is inputed.
    '''

    # TODO: what if a number can be both prime and lucky, for instance?

    result = 'Number is '


    if number_type in ['lucky', 'Lucky']:
        if lucky_type(number):
            return True
    if number_type in ['prime', 'Prime']:
        if prime_number(number):
            return True
    if number_type in ['ulam', 'Ulam']:
        if ulam_number:
            return True
    return False

def lucky_type(number: int) -> bool:
    '''

    '''

    if number in sieve_flavius(number + 1):
        return True
    return False

'''
This program generates a list of Flavius sieve numbers
'''
def sieve_flavius(number: int) -> list:
    '''
    Function generates list similar to Erathosphen sieve
    for building lucky numbers sequence
    >>> sieve_flavius(100)
    [1, 3, 7, 9, 13, 15, 21, 25, 31, 33, 37, 43, 49, 51, 63, 67, 69, 73, 75, 79, 87, 93, 99]
    >>> sieve_flavius(10)
    [1, 3, 7, 9]
    >>> sieve_flavius(0)
    []
    '''
    flavius_list = list(range(1, number + 1, 2))
    id_list = 1
    while id_list < len(flavius_list):
        temporary_list = []
        num = flavius_list[id_list]
        for index, item in enumerate(flavius_list):
            if (index + 1) % num != 0:
                temporary_list.append(item)
        flavius_list = temporary_list
        id_list += 1
    return flavius_list

def prime_number(number: int) -> str:
    '''

    '''
    if number in sieve_eratosthene(number + 1):
        return True
    return False

def sieve_eratosthene(number: int) -> list:
    '''
    This function returns the list of prime numbers in range n

    Takes a posititve integer
    If the argument is not a positive int, returns blank list

    >>> sieve_eratosthene(30)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    >>> sieve_eratosthene(10)
    [2, 3, 5, 7]
    >>> sieve_eratosthene(-5)
    []
    >>> sieve_eratosthene(1)
    []
    >>> sieve_eratosthene('abc')
    []
    '''

    #Create a list containing all the numbers.
    #Initialize them as True. Later, prime[i] will be False
    #if it is composite and True if it is prime
    if not isinstance(number, int) or number < 1:
        return []

    prime = [True for i in range(number + 1)]
    prime[0], prime[1] = False, False
    curr_num = 2

    #Start loop beginning from 2, as 0 and 1 are not prime
    #The loop goes up to sqrt(number) to decrease the number 
    #of iterations and improve the time of work
    while(curr_num * curr_num < number):
        if prime[curr_num]:
            #if current number is prime, update all the
            #following numbers that are multiplied by curr_num
            #as composite, beginning from curr_numˆ2
            for i in range(curr_num * curr_num, number + 1, curr_num):
                prime[i] = False
        curr_num += 1
    prime_list = []
    for item in enumerate(prime):
        if item[1]:
            prime_list.append(item[0])
    return prime_list

def ulam_number(number: int) -> bool:
    '''
    '''
    if number in numbers_Ulam(number + 1):
        return True
    return False


def numbers_Ulam(number: int) -> list:
    """
    This fucntion returns list of n Ulam numbers
    >>> numbers_Ulam(10)
    [1, 2, 3, 4, 6, 8, 11, 13, 16, 18]
    >>> numbers_Ulam(2)
    [1, 2]
    >>> numbers_Ulam(1)
    [1]
    """
    ulam = []
    if number >= 1:
        ulam.append(1)
    if number >= 2:
        ulam.append(2)
    if number > 2:
        ulam_num = 3
        while len(ulam) < number:
            coincidence = 0
            for i in enumerate(ulam):
                for j in range(i[0] + 1, len(ulam)):
                    if (ulam[i[0]] + ulam[j]) == ulam_num:
                        coincidence += 1
                    if coincidence > 1:
                        break
                if coincidence > 1:
                    break
            if coincidence == 1:
                ulam.append(ulam_num)
            ulam_num += 1
    return ulam

