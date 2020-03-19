__author__ = 'Alexa Lewis'


def one_to_one(s1, s2):
    my_dict = dict()
    my_bool = True
    i = 0

    # check if strings have same length
    if len(s1) == len(s2):
        first = list(s1)
        second = list(s2)

        # loop through both strings for one-to-one mapping
        while i < len(s1):
            # checks if a character is already in dictionary
            if my_dict.__contains__(first[i]):
                # the value of the key cannot be different
                if second[i] != my_dict.get(first[i]):
                    my_bool = False
            else:
                # make dictionary for each character in string
                my_dict[first[i]] = second[i]
            i += 1

        # print(my_dict)
    else:
        my_bool = False

    return my_bool


def main():
    while True:
        s1 = input("String 1: ")
        s2 = input("String 2: ")

        print(one_to_one(s1, s2))

        q = input("Continue (any key) or quit (q): ")
        if q == 'q':
            quit()

        print()


if __name__ == "__main__":
    main()
