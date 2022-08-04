def sum(list):
    sum = 0 
    for number in list:
        sum = sum + number
    return sum

    #takes in list of numbers and returns the biggest number
def biggest_number(list):
    biggest_so_far = 0
    for num in list:
        if (num > biggest_so_far):
            biggest_so_far = num 
            return biggest_so_far

            #takes in a list of numbers and return if there is an even number
def has_evens(list):
    found_even = False
    for num in list:
        #check if num is even
        if  (num % 2 == 0):
            found_even = True
    return found_even

#Takes in a list of numbers and return if every number is even
def all_even(list):
    all_even = True
    for num in list:
        if (num % 2 == 1):
            all_even = False
    return all_even

    # Take in a list of numbers and remove every odd number
    def filter_odds(list):
        for num in list:
            if (num % 2 == 1):
                list.remove(num)
        return list