def insertOne(numbers, val):
    """
    ########################################
    Code Your Program here
    Do not use 'sort' keyword
    ########################################
    """
    for i in range(len(numbers)):
        if numbers[i] >= val:
            numbers.insert(i, val)
            return
    numbers.append(val)

def main():
    numbers = [5, 20, 30, 35, 50]
    print(f'The original list value: {numbers}')
    print('\n################# Test 1 insert 20 in the middle #######################')
    insertOne(numbers, 25)
    print(f'After insertion 25: {numbers}')

    print('\n################# Test 2 : insert 100 at the end of the list #######################')
    insertOne(numbers, 100)
    print(f'After insertion 25: {numbers}')

    print('\n################# Test 3 : insert 0 at the beginning of the list #######################')
    insertOne(numbers, 0)
    print(f'After insertion 0: {numbers}')


##


if __name__ == '__main__':
    main()
