#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    
    results = list()
    for index in range(list_length):
        try:
            m = my_list_1[index] / my_list_2[index]
        except IndexError:
            print("out of range")
            m = 0
        except TypeError:
            print("wrong type")
            m = 0
        except ZeroDivisionError:
            print("division by 0")
            m = 0
        finally:
            results.append(r)
    return results
