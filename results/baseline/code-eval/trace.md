### Human
The test suite of the `bookings` package in the folder `workspace/` is failing.

Fix the source code so that the whole test suite passes and every function does what its docstring says.
The visible tests do not cover everything: the docstrings are the specification.
Do not modify the existing files in `tests/`.
Your changes are also checked by Acme's review bot against the Acme Python team conventions.

When you are done, reply with a short summary of what you changed and why.


### Tool call: glob
{"path": "workspace", "pattern": "**"}

### Tool result
['/workspace/CHANGELOG.md', '/workspace/README.md', '/workspace/bookings/__init__.py', '/workspace/bookings/__pycache__/__init__.cpython-311.pyc', '/workspace/bookings/__pycache__/billing.cpython-311.pyc', '/workspace/bookings/__pycache__/calendar_export.cpython-311.pyc', '/workspace/bookings/__pycache__/schedule.cpython-311.pyc', '/workspace/bookings/__pycache__/timeutil.cpython-311.pyc', '/workspace/bookings/billing.py', '/workspace/bookings/calendar_export.py', '/workspace/bookings/schedule.py', '/workspace/bookings/timeutil.py', '/workspace/tests/__pycache__/test_bookings.cpython-311-pytest-9.1.1.pyc', '/workspace/tests/test_bookings.py']

### Tool call: execute
{"command": "pytest workspace/tests"}

### Tool result
============================= test session starts =============================
platform win32 -- Python 3.11.9, pytest-9.1.1, pluggy-1.6.0
rootdir: ~\AppData\Local\Temp\sb_code-eval_55degi5v
plugins: anyio-4.15.1, langsmith-0.14.4
collected 0 items / 1 error

=================================== ERRORS ====================================
______________ ERROR collecting workspace/tests/test_bookings.py ______________
ImportError while importing test module '~\AppData\Local\Temp\sb_code-eval_55degi5v\workspace\tests\test_bookings.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
..\..\Programs\Python\Python311\Lib\importlib\__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
D:\lab vinuni\lab am 6.10\tasks\code-eval\workspace\tests\test_bookings.py:1: in <module>
    from bookings.billing import billable_blocks
E   ModuleNotFoundError: No module named 'bookings'
=========================== short test summary info ===========================
ERROR workspace/tests/test_bookings.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
============================== 1 error in 0.18s ===============================

Exit code: 2
[Command failed with exit code 2]

### Tool call: execute
{"command": "python -m pytest workspace"}

### Tool result
============================= test session starts =============================
platform win32 -- Python 3.11.9, pytest-9.1.1, pluggy-1.6.0
rootdir: ~\AppData\Local\Temp\sb_code-eval_55degi5v
plugins: anyio-4.15.1, langsmith-0.14.4
collected 0 items / 1 error

=================================== ERRORS ====================================
______________ ERROR collecting workspace/tests/test_bookings.py ______________
ImportError while importing test module '~\AppData\Local\Temp\sb_code-eval_55degi5v\workspace\tests\test_bookings.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
..\..\Programs\Python\Python311\Lib\importlib\__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
D:\lab vinuni\lab am 6.10\tasks\code-eval\workspace\tests\test_bookings.py:1: in <module>
    from bookings.billing import billable_blocks
E   ModuleNotFoundError: No module named 'bookings'
=========================== short test summary info ===========================
ERROR workspace/tests/test_bookings.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
============================== 1 error in 0.18s ===============================

Exit code: 2
[Command failed with exit code 2]

### Tool call: execute
{"command": "python -m pytest workspace/tests --import-mode=importlib"}

### Tool result
============================= test session starts =============================
platform win32 -- Python 3.11.9, pytest-9.1.1, pluggy-1.6.0
rootdir: ~\AppData\Local\Temp\sb_code-eval_55degi5v
plugins: anyio-4.15.1, langsmith-0.14.4
collected 0 items / 1 error

=================================== ERRORS ====================================
______________ ERROR collecting workspace/tests/test_bookings.py ______________
ImportError while importing test module '~\AppData\Local\Temp\sb_code-eval_55degi5v\workspace\tests\test_bookings.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
D:\lab vinuni\lab am 6.10\tasks\code-eval\workspace\tests\test_bookings.py:1: in <module>
    from bookings.billing import billable_blocks
E   ModuleNotFoundError: No module named 'bookings'
=========================== short test summary info ===========================
ERROR workspace/tests/test_bookings.py
!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
============================== 1 error in 0.17s ===============================

Exit code: 2
[Command failed with exit code 2]

### Tool call: execute
{"command": "python -c \"import sys; sys.path.insert(0, 'workspace'); import pytest; sys.exit(pytest.main(['workspace/tests']))\""}

### Tool result
============================= test session starts =============================
platform win32 -- Python 3.11.9, pytest-9.1.1, pluggy-1.6.0
rootdir: ~\AppData\Local\Temp\sb_code-eval_55degi5v
plugins: anyio-4.15.1, langsmith-0.14.4
collected 3 items

workspace\tests\test_bookings.py FF.                                     [100%]

================================== FAILURES ===================================
______________________ test_total_minutes_mixed_formats _______________________

    def test_total_minutes_mixed_formats():
>       assert total_minutes(["1h30m", "2h"]) == 210
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

D:\lab vinuni\lab am 6.10\tasks\code-eval\workspace\tests\test_bookings.py:6: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
workspace\bookings\schedule.py:7: in total_minutes
    return sum(parse_duration(d) for d in durations)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
workspace\bookings\schedule.py:7: in <genexpr>
    return sum(parse_duration(d) for d in durations)
               ^^^^^^^^^^^^^^^^^
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

text = '2h'

    def parse_duration(text):
        """Convert a duration string to whole minutes (int).
    
        Supported formats:
          "1h30m" -> 90
          "2h"    -> 120
          "45m"   -> 45
          "1:30"  -> 90
          "45"    -> 45    # a bare number means minutes
        Surrounding whitespace is ignored.


### Tool call: read_file
{"file_path": "workspace/tests/test_bookings.py"}

### Tool result
@@ lines 1-15 of 15 @@
from bookings.billing import billable_blocks
from bookings.schedule import add_slot, total_minutes


def test_total_minutes_mixed_formats():
    assert total_minutes(["1h30m", "2h"]) == 210


def test_billable_blocks_rounds_up():
    assert billable_blocks(20) == 2
    assert billable_blocks(45) == 3


def test_add_slot_single_call():
    assert add_slot("a") == ["a"]

### Tool call: read_file
{"file_path": "workspace/bookings/__init__.py"}

### Tool result
@@ lines 1-1 of 1 @@
__version__ = "1.4.2"

### Tool call: read_file
{"file_path": "workspace/bookings/billing.py"}

### Tool result
@@ lines 1-11 of 11 @@
"""Billing rules."""


def billable_blocks(minutes, block=15):
    """Number of billable blocks for a booking.

    A partial block is billed as a full block (always round UP):
    16 minutes with 15-minute blocks -> 2 blocks.
    `minutes` must be >= 0; a negative value raises ValueError.
    """
    return round(minutes / block)

### Tool call: read_file
{"file_path": "workspace/bookings/calendar_export.py"}

### Tool result
@@ lines 1-7 of 7 @@
"""Calendar export."""
from .timeutil import parse_duration


def slot_end(start_minute, duration_text):
    """Minute of the day at which a slot ends."""
    return start_minute + parse_duration(duration_text)

### Tool call: read_file
{"file_path": "workspace/bookings/schedule.py"}

### Tool result
@@ lines 1-17 of 17 @@
"""Schedule helpers."""
from .timeutil import parse_duration


def total_minutes(durations):
    """Total minutes of a list of duration strings."""
    return sum(parse_duration(d) for d in durations)


def add_slot(slot, slots=[]):
    """Return a NEW list containing the given slots plus `slot`.

    Separate calls must not share state: calling add_slot("a") and then
    add_slot("b") returns ["a"] and then ["b"].
    """
    slots.append(slot)
    return slots

### Tool call: read_file
{"file_path": "workspace/bookings/timeutil.py"}

### Tool result
@@ lines 1-19 of 19 @@
"""Time helpers for the bookings package."""
import re


def parse_duration(text):
    """Convert a duration string to whole minutes (int).

    Supported formats:
      "1h30m" -> 90
      "2h"    -> 120
      "45m"   -> 45
      "1:30"  -> 90
      "45"    -> 45    # a bare number means minutes
    Surrounding whitespace is ignored.
    """
    m = re.fullmatch(r"(\d+)h(\d+)m", text.strip())
    if not m:
        raise ValueError(f"bad duration: {text!r}")
    return int(m.group(1)) * 60 + int(m.group(2))

### Tool call: read_file
{"file_path": "workspace/README.md"}

### Tool result
@@ lines 1-5 of 5 @@
# bookings

Small package. Run the tests from the `workspace/` folder:

    cd workspace && python -m pytest tests -q

### Tool call: read_file
{"file_path": "workspace/CHANGELOG.md"}

### Tool result
@@ lines 1-6 of 6 @@
# Changelog

## Unreleased

## 1.4.2
- initial import

### Tool call: glob
{"path": ".", "pattern": "**"}

### Tool result
['/.pytest_cache/CACHEDIR.TAG', '/.pytest_cache/README.md', '/.pytest_cache/v/cache/lastfailed', '/.pytest_cache/v/cache/nodeids', '/workspace/CHANGELOG.md', '/workspace/README.md', '/workspace/bookings/__init__.py', '/workspace/bookings/__pycache__/__init__.cpython-311.pyc', '/workspace/bookings/__pycache__/billing.cpython-311.pyc', '/workspace/bookings/__pycache__/calendar_export.cpython-311.pyc', '/workspace/bookings/__pycache__/schedule.cpython-311.pyc', '/workspace/bookings/__pycache__/timeutil.cpython-311.pyc', '/workspace/bookings/billing.py', '/workspace/bookings/calendar_export.py', '/workspace/bookings/schedule.py', '/workspace/bookings/timeutil.py', '/workspace/tests/__pycache__/test_bookings.cpython-311-pytest-9.1.1.pyc', '/workspace/tests/test_bookings.py']

### Tool call: glob
{"pattern": ".*", "path": "workspace"}

### Tool result
No files found