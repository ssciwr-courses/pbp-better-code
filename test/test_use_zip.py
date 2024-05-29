def test_use_zip():
    # check that zip is used
    with open("chapter5/use_zip.py") as file:
        lines = file.read()
    assert "zip(days, lunch)" in lines