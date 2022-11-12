from coin_change import min_coins

def test_case_1():
    print("\nTest min_coins function - Test case 1:")
    try:
        min_coins([], 0)
    except Exception as e:
        print("Failed")
        print(e)

def test_case_2():
    print("\nTest min_coins function - Test case 2:")
    try:
        min_coins([], 1)
    except Exception as e:
        print("Failed")
        print(e)

def test_case_3():
    print("\nTest min_coins function - Test case 3:")
    try:
        min_coins([2], 0)
    except Exception as e:
        print("Failed")
        print(e)

def test_case_4():
    print("\nTest min_coins function - Test case 4:")
    try:
        min_coins([3], 2)
    except Exception as e:
        print("Failed")
        print(e)

def test_case_5():
    print("\nTest min_coins function - Test case 5:")
    try:
        min_coins([0], 0)
    except Exception as e:
        print("Failed")
        print(e)

def test_case_6():
    print("\nTest min_coins function - Test case 6:")
    try:
        min_coins([1], 3)
    except Exception as e:
        print("Failed")
        print(e)

def test_case_7():
    print("\nTest min_coins function - Test case 7:")
    try:
        min_coins([3,1], 2)
    except Exception as e:
        print("Failed")
        print(e)

def test_case_8():
    print("\nTest min_coins function - Test case 8:")
    try:
        min_coins([3,0], 2)
    except Exception as e:
        print("Failed")
        print(e)

def test_case_9():
    print("\nTest min_coins function - Test case 9:")
    try:
        min_coins([3,5,7,2], 6)
    except Exception as e:
        print("Failed")
        print(e)

def test_case_10():
    print("\nTest min_coins function - Test case 10:")
    try:
        min_coins([1,2,3,4], 10)
    except Exception as e:
        print("Failed")
        print(e)

test_case_1()
test_case_2()
test_case_3()
test_case_4()
test_case_5()
test_case_6()
test_case_7()
test_case_8()
test_case_9()
test_case_10()