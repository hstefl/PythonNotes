"""
Testing doubles are objects used in place of real ones during tests, to isolate the unit under test and control
or observe behavior. The term comes from the concept of "stunt doubles" in film — they're stand-ins.

There are five classic types of test doubles (from Gerard Meszaros' xUnit Patterns):

Type    Purpose                                      Behavior
-------------------------------------------------------------------------------------------------------------------
Dummy   Passed around but never used                 Fulfills parameter requirement (e.g., a dummy object or value)
Fake    Works but is simplified                      Like an in-memory DB or simplified service
Stub    Provides canned answers                      Used to control the test flow (e.g., fixed return values)
Mock    Verifies interactions                        Expects certain calls and validates them
Spy     Records interactions, but runs real code     Lets you assert calls after the fact, without altering logic

```
class DummyUser:
    pass

# Used just to satisfy an argument
service.process(DummyUser())
```

```
class FakeEmailService:
    def send(self, to, subject):
        self.sent = (to, subject)
```

```
def get_user_stub():
    return User(id=1, name="Stub")

user_service.get_user = get_user_stub
```

```
mock = Mock()
mock.send_email.return_value = True

assert mock.send_email("test@example.com")
mock.send_email.assert_called_once()
```

```
spy = mocker.spy(MyService, "process")
MyService.process("data")
spy.assert_called_with("data")
```

When to Use What:
 * Use dummies for irrelevant parameters
 * Use fakes to avoid external systems (e.g., DB, network)
 * Use stubs to control data flow or simulate failures
 * Use mocks to test interactions
 * Use spies when you want to verify a real call happened without changing logic

"""

# ======================================
# 1. Basic Mocking with unittest.mock
from unittest.mock import Mock
from unittest.mock import patch


# 1.1 Simple mock
def test_using_mock():
    mock = Mock()
    mock.method.return_value = "mocked value"

    assert mock.method() == "mocked value"


# ---------------------------------

# 1.2 Using patch

def fetch_data():
    # Imagine this function makes an external API call
    pass


@patch('test_mocking.fetch_data')
def test_fetch_data(mock_fetch):
    mock_fetch.return_value = "mocked data"

    assert fetch_data() == "mocked data"


# ======================================
# 2. Using pytest-mock
# ======================================

def fetch_data2():
    # Imagine this function makes an external API call
    pass


def test_fetch_data2(mocker):
    mock_fetch = mocker.patch('test_mocking.fetch_data2')
    mock_fetch.return_value = "mocked data"

    assert fetch_data2() == "mocked data"


# ======================================
# 3. Advanced Mocking Techniques
# ======================================
#
# Mocking Attributes and Methods
#
class MyClass:
    def method(self):
        pass


def test_my_class(mocker):
    mocked_my_class = mocker.Mock(spec=MyClass)
    mocked_my_class.method.return_value = "mocked method"

    assert mocked_my_class.method() == "mocked method"


#
# Mocking side effect
#
from unittest.mock import Mock


def side_effect_function():
    return "side effect"


mock = Mock()
mock.method.side_effect = side_effect_function
assert mock.method() == "side effect"


#
# Mocking with Context managers
# TODO This does not work
# def open_file():
#     with open('some_file.txt', 'r') as file:
#         return file.read()
#
#
# @patch('builtins.open', new_callable=Mock)
# def test_open_file(mock_open):
#     mock_open.return_value.__enter__.return_value.read.return_value = "mocked file content"
#
#     result = open_file()
#     assert result == "mocked file content"

#
# Mocking classes and objects
# TODO This does not work
# class MyClass2:
#     def method(self):
#         pass
#
#
# @patch('test_mocking.MyClass2')
# def test_class(mock_class):
#     instance = mock_class.return_value
#     instance.method.return_value = "mocked method"
#
#     my_obj = MyClass()
#     assert my_obj.method() == "mocked method"


#
#
#
def test_spy(mocker):
    class MyClass3:
        def method(self):
            return "real value"

    obj = MyClass3()
    spy = mocker.spy(obj, 'method')

    result = obj.method()
    assert result == "real value"
    spy.assert_called_once()
