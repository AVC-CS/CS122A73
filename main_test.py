import main
import pytest

@pytest.mark.basic
def test_main_1():
    print (f'\n******************* test_main_1: insert 25 ***********************')
    numbers = [5, 20, 30, 35, 50]
    print(f'The original value {numbers}')
    main.insertOne(numbers, 25)
    print(f'After insertion 25 {numbers}')
    assert numbers == [5, 20, 25, 30, 35, 50]


@pytest.mark.edge
def test_main_2():
    print (f'\n******************* test_main_2: insert 100 ***********************')
    numbers = [5, 20, 30, 35, 50]
    print(f'The original value {numbers}')
    main.insertOne(numbers, 100)
    print(f'After insertion 100 {numbers}')
    assert numbers == [5, 20, 30, 35, 50, 100]
    
@pytest.mark.edge
def test_main_3():
    numbers = [1, 2, 3, 4, 5]
    print (f'\n******************* test_main_3: insert 0 ***********************')
    print(f'The original value {numbers}')
    main.insertOne(numbers, 0)
    print(f'After insertion 0 {numbers}')
    assert numbers == [0, 1, 2, 3, 4, 5]

@pytest.mark.bonus
def test_main_4():
    numbers = [1, 2, 3, 4, 5]
    print(f'\n******************* test_main_4: insert 6 ***********************')
    print(f'The original value: {numbers}')
    main.insertOne(numbers, 6)
    print(f'After insertion 6 {numbers}')
    assert numbers == [1, 2, 3, 4, 5, 6]

