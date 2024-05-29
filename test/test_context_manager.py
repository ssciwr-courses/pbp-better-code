def test_context_manager():
    # check that context manager is used
    with open("chapter5/context_managers.py") as file:
        lines = file.read()
    assert "with open" in lines