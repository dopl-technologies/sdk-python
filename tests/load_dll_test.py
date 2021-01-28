from dopltech.sdk import Sdk

def test_dll_loads():
    result = Sdk.test()
    assert result == -1