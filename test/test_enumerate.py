def test_enumerate():
    # check that enumerate is used
    with open("chapter5/enumerate.py") as file:
        lines = file.read()
    assert "enumerate(lunch)" in lines