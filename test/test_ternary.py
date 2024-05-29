def test_ternary():
    # check that the ternary conditional is used
    with open("chapter5/ternary.py") as file:
        lines = file.readlines()
    assert "y = 1 if x >= 10 else 0\n" in lines