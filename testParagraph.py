


# Unit test cases to check the functionality

import paragraph



def test_case_1():

    Input = """This is a sample text but a complicated problem to be solved, 
so we are adding more text to see that it actually works."""
    Width = 20

    result = paragraph.logic(Input, Width)
    assert len(result[4]) == 20

def test_case_2():

    Input = """This is a sample text but a complicated problem to be solved, 
so we are adding more text to see that it actually works."""
    Width = 30

    result = paragraph.logic(Input, Width)
    assert  len(result[-1]) == 30
