### Human
The test suite of the `bookings` package in the folder `workspace/` is failing.

Fix the source code so that the whole test suite passes and every function does what its docstring says.
The visible tests do not cover everything: the docstrings are the specification.
Do not modify the existing files in `tests/`.
Your changes are also checked by Acme's review bot against the Acme Python team conventions.

When you are done, reply with a short summary of what you changed and why.


### Tool call: read_file
{"limit": 1000, "file_path": "skills/enforce-codebase-rules/SKILL.md"}

### Tool call: read_file
{"limit": 1000, "file_path": "skills/implement-spec-edge-cases/SKILL.md"}

### Tool call: read_file
{"file_path": "skills/verify-task-deliverables/SKILL.md", "limit": 1000}

### Tool result
@@ lines 1-8 of 8 @@
---
name: enforce-codebase-rules
description: Apply when modifying Python codebases to comply with project repository standards, type hints, regression tests, and documentation logs.
---
1. Annotate all public functions (names not starting with `_`) with type hints on all parameters and return types.
2. Add dedicated regression test files (e.g., `tests/test_regressions.py`) with test functions for each fixed bug without altering existing test files.
3. Update CHANGELOG files under designated headers (e.g., `## Unreleased`) using the project's exact line/bullet formatting.
4. Run the full test suite locally before submission to verify visible test passes and zero suite regressions.

### Tool result
@@ lines 1-9 of 9 @@
---
name: implement-spec-edge-cases
description: Apply when writing numerical, string parsing, or data formatting code to handle all required edge cases and rounding rules accurately.
---
1. Parse string formats thoroughly: handle thousands separators, currency symbols, and accounting negative notation with parentheses.
2. Perform exact financial and decimal arithmetic using explicit rounding modes (e.g., `decimal.ROUND_HALF_UP`) during quantization.
3. Check boundary conditions precisely (e.g., strictly below `<` versus less than or equal to `<=`).
4. Apply sorting requirements accurately (e.g., case-insensitive sorting using key functions like `key=str.lower`).
5. Ensure CSV escaping and quoting standards (e.g., RFC 4180 quotes for strings with commas or double quotes) are strictly respected.

### Tool result
@@ lines 1-8 of 8 @@
---
name: verify-task-deliverables
description: Apply before completing any task to confirm that all required output files and artifacts exist in their expected paths.
---
1. Audit task instructions, prompt rules, and conventions for all required output files.
2. Confirm each output file exists in the exact specified path (e.g., output data files, report JSONs, clean CSVs) before concluding the task.
3. Verify that original test files and baseline framework code remain unmodified unless explicitly requested.
4. Validate output files against required schema structures, headers, column order, and metadata blocks.

### Tool call: ls
{"path": "workspace"}

### Tool result
['/workspace/CHANGELOG.md', '/workspace/README.md', '/workspace/bookings/', '/workspace/tests/']

### Tool call: execute
{"command": "pytest workspace/tests"}

### Tool result
============================= test session starts =============================
platform win32 -- Python 3.11.9, pytest-9.1.1, pluggy-1.6.0
rootdir: ~\AppData\Local\Temp\sb_code-eval_vk9cio7j
plugins: anyio-4.15.1, langsmith-0.14.4
collected 0 items / 1 error

=================================== ERRORS ====================================
______________ ERROR collecting workspace/tests/test_bookings.py ______________
ImportError while importing test module '~\AppData\Local\Temp\sb_code-eval_vk9cio7j\workspace\tests\test_bookings.py'.
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
============================== 1 error in 0.30s ===============================

Exit code: 2
[Command failed with exit code 2]

### Tool call: execute
{"command": "python -m pytest workspace/tests"}

### Tool result
============================= test session starts =============================
platform win32 -- Python 3.11.9, pytest-9.1.1, pluggy-1.6.0
rootdir: ~\AppData\Local\Temp\sb_code-eval_vk9cio7j
plugins: anyio-4.15.1, langsmith-0.14.4
collected 0 items / 1 error

=================================== ERRORS ====================================
______________ ERROR collecting workspace/tests/test_bookings.py ______________
ImportError while importing test module '~\AppData\Local\Temp\sb_code-eval_vk9cio7j\workspace\tests\test_bookings.py'.
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
============================== 1 error in 0.17s ===============================

Exit code: 2
[Command failed with exit code 2]

### Tool call: execute
{"command": "PYTHONPATH=workspace python -m pytest workspace/tests"}

### Tool result
============================= test session starts =============================
platform win32 -- Python 3.11.9, pytest-9.1.1, pluggy-1.6.0
rootdir: ~\AppData\Local\Temp\sb_code-eval_vk9cio7j
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


### Tool call: glob
{"path": "workspace", "pattern": "**/*"}

### Tool result
['/workspace/CHANGELOG.md', '/workspace/README.md', '/workspace/bookings/__init__.py', '/workspace/bookings/__pycache__/__init__.cpython-311.pyc', '/workspace/bookings/__pycache__/billing.cpython-311.pyc', '/workspace/bookings/__pycache__/calendar_export.cpython-311.pyc', '/workspace/bookings/__pycache__/schedule.cpython-311.pyc', '/workspace/bookings/__pycache__/timeutil.cpython-311.pyc', '/workspace/bookings/billing.py', '/workspace/bookings/calendar_export.py', '/workspace/bookings/schedule.py', '/workspace/bookings/timeutil.py', '/workspace/tests/__pycache__/test_bookings.cpython-311-pytest-9.1.1.pyc', '/workspace/tests/test_bookings.py']

### Tool call: read_file
{"limit": 1000, "file_path": "workspace/README.md"}

### Tool call: read_file
{"limit": 1000, "file_path": "workspace/CHANGELOG.md"}

### Tool call: read_file
{"limit": 1000, "file_path": "workspace/tests/test_bookings.py"}

### Tool result
@@ lines 1-5 of 5 @@
# bookings

Small package. Run the tests from the `workspace/` folder:

    cd workspace && python -m pytest tests -q

### Tool result
@@ lines 1-6 of 6 @@
# Changelog

## Unreleased

## 1.4.2
- initial import

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
{"limit": 1000, "file_path": "workspace/bookings/__init__.py"}

### Tool call: read_file
{"file_path": "workspace/bookings/billing.py", "limit": 1000}

### Tool call: read_file
{"limit": 1000, "file_path": "workspace/bookings/calendar_export.py"}

### Tool call: read_file
{"limit": 1000, "file_path": "workspace/bookings/schedule.py"}

### Tool call: read_file
{"limit": 1000, "file_path": "workspace/bookings/timeutil.py"}

### Tool result
@@ lines 1-1 of 1 @@
__version__ = "1.4.2"

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

### Tool result
@@ lines 1-7 of 7 @@
"""Calendar export."""
from .timeutil import parse_duration


def slot_end(start_minute, duration_text):
    """Minute of the day at which a slot ends."""
    return start_minute + parse_duration(duration_text)

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

### Tool call: glob
{"pattern": "**/*", "path": "workspace"}

### Tool result
['/workspace/CHANGELOG.md', '/workspace/README.md', '/workspace/bookings/__init__.py', '/workspace/bookings/__pycache__/__init__.cpython-311.pyc', '/workspace/bookings/__pycache__/billing.cpython-311.pyc', '/workspace/bookings/__pycache__/calendar_export.cpython-311.pyc', '/workspace/bookings/__pycache__/schedule.cpython-311.pyc', '/workspace/bookings/__pycache__/timeutil.cpython-311.pyc', '/workspace/bookings/billing.py', '/workspace/bookings/calendar_export.py', '/workspace/bookings/schedule.py', '/workspace/bookings/timeutil.py', '/workspace/tests/__pycache__/test_bookings.cpython-311-pytest-9.1.1.pyc', '/workspace/tests/test_bookings.py']

### Tool call: glob
{"path": "workspace", "pattern": ".*"}

### Tool result
No files found

### Tool call: edit_file
{"file_path": "workspace/bookings/billing.py", "new_string": "\"\"\"Billing rules.\"\"\"\nimport math\n\n\ndef billable_blocks(minutes: int, block: int = 15) -> int:\n    \"\"\"Number of billable blocks for a booking.\n\n    A partial block is billed as a full block (always round UP):\n    16 minutes with 15-minute blocks -> 2 blocks.\n    `minutes` must be >= 0; a negative value raises ValueError.\n    \"\"\"\n    if minutes < 0:\n        raise ValueError(f\"minutes must be >= 0, got {minutes}\")\n    if block <= 0:\n        raise ValueError(f\"block must be > 0, got {block}\")\n    return math.ceil(minutes / block)", "old_string": "\"\"\"Billing rules.\"\"\"\n\n\ndef billable_blocks(minutes, block=15):\n    \"\"\"Number of billable blocks for a booking.\n\n    A partial block is billed as a full block (always round UP):\n    16 minutes with 15-minute blocks -> 2 blocks.\n    `minutes` must be >= 0; a negative value raises ValueError.\n    \"\"\"\n    return round(minutes / block)"}

### Tool result
Successfully replaced 1 instance(s) of the string in '/workspace/bookings/billing.py'

### Tool call: edit_file
{"file_path": "workspace/bookings/timeutil.py", "new_string": "\"\"\"Time helpers for the bookings package.\"\"\"\nimport re\n\n\ndef parse_duration(text: str) -> int:\n    \"\"\"Convert a duration string to whole minutes (int).\n\n    Supported formats:\n      \"1h30m\" -> 90\n      \"2h\"    -> 120\n      \"45m\"   -> 45\n      \"1:30\"  -> 90\n      \"45\"    -> 45    # a bare number means minutes\n    Surrounding whitespace is ignored.\n    \"\"\"\n    if not isinstance(text, str):\n        raise TypeError(f\"expected str, got {type(text).__name__}\")\n\n    s = text.strip()\n\n    m_hm = re.fullmatch(r\"(\\d+)h(\\d+)m\", s)\n    if m_hm:\n        return int(m_hm.group(1)) * 60 + int(m_hm.group(2))\n\n    m_h = re.fullmatch(r\"(\\d+)h\", s)\n    if m_h:\n        return int(m_h.group(1)) * 60\n\n    m_m = re.fullmatch(r\"(\\d+)m\", s)\n    if m_m:\n        return int(m_m.group(1))\n\n    m_colon = re.fullmatch(r\"(\\d+):(\\d+)\", s)\n    if m_colon:\n        return int(m_colon.group(1)) * 60 + int(m_colon.group(2))\n\n    m_num = re.fullmatch(r\"(\\d+)\", s)\n    if m_num:\n        return int(m_num.group(1))\n\n    raise ValueError(f\"bad duration: {text!r}\")", "old_string": "\"\"\"Time helpers for the bookings package.\"\"\"\nimport re\n\n\ndef parse_duration(text):\n    \"\"\"Convert a duration string to whole minutes (int).\n\n    Supported formats:\n      \"1h30m\" -> 90\n      \"2h\"    -> 120\n      \"45m\"   -> 45\n      \"1:30\"  -> 90\n      \"45\"    -> 45    # 

### Tool result
Successfully replaced 1 instance(s) of the string in '/workspace/bookings/timeutil.py'

### Tool call: edit_file
{"old_string": "\"\"\"Schedule helpers.\"\"\"\nfrom .timeutil import parse_duration\n\n\ndef total_minutes(durations):\n    \"\"\"Total minutes of a list of duration strings.\"\"\"\n    return sum(parse_duration(d) for d in durations)\n\n\ndef add_slot(slot, slots=[]):\n    \"\"\"Return a NEW list containing the given slots plus `slot`.\n\n    Separate calls must not share state: calling add_slot(\"a\") and then\n    add_slot(\"b\") returns [\"a\"] and then [\"b\"].\n    \"\"\"\n    slots.append(slot)\n    return slots", "new_string": "\"\"\"Schedule helpers.\"\"\"\nfrom collections.abc import Iterable\nfrom .timeutil import parse_duration\n\n\ndef total_minutes(durations: Iterable[str]) -> int:\n    \"\"\"Total minutes of a list of duration strings.\"\"\"\n    return sum(parse_duration(d) for d in durations)\n\n\ndef add_slot(slot: str, slots: list[str] | None = None) -> list[str]:\n    \"\"\"Return a NEW list containing the given slots plus `slot`.\n\n    Separate calls must not share state: calling add_slot(\"a\") and then\n    add_slot(\"b\") returns [\"a\"] and then [\"b\"].\n    \"\"\"\n    if slots is None:\n        return [slot]\n    return list(slots) + [slot]", "file_path": "workspace/bookings/schedule.py"}

### Tool result
Successfully replaced 1 instance(s) of the string in '/workspace/bookings/schedule.py'

### Tool call: edit_file
{"old_string": "\"\"\"Calendar export.\"\"\"\nfrom .timeutil import parse_duration\n\n\ndef slot_end(start_minute, duration_text):\n    \"\"\"Minute of the day at which a slot ends.\"\"\"\n    return start_minute + parse_duration(duration_text)", "file_path": "workspace/bookings/calendar_export.py", "new_string": "\"\"\"Calendar export.\"\"\"\nfrom .timeutil import parse_duration\n\n\ndef slot_end(start_minute: int, duration_text: str) -> int:\n    \"\"\"Minute of the day at which a slot ends.\"\"\"\n    return start_minute + parse_duration(duration_text)"}

### Tool result
Successfully replaced 1 instance(s) of the string in '/workspace/bookings/calendar_export.py'

### Tool call: write_file
{"content": "import pytest\nfrom bookings.billing import billable_blocks\nfrom bookings.calendar_export import slot_end\nfrom bookings.schedule import add_slot, total_minutes\nfrom bookings.timeutil import parse_duration\n\n\n# Test timeutil.parse_duration\ndef test_parse_duration_valid():\n    assert parse_duration(\"1h30m\") == 90\n    assert parse_duration(\"2h\") == 120\n    assert parse_duration(\"45m\") == 45\n    assert parse_duration(\"1:30\") == 90\n    assert parse_duration(\"45\") == 45\n    assert parse_duration(\" 1h30m \") == 90\n    assert parse_duration(\"  0h0m  \") == 0\n    assert parse_duration(\"0:00\") == 0\n\n\ndef test_parse_duration_invalid():\n    with pytest.raises(ValueError):\n        parse_duration(\"invalid\")\n    with pytest.raises(ValueError):\n        parse_duration(\"1h30\")\n    with pytest.raises(ValueError):\n        parse_duration(\"1m30h\")\n    with pytest.raises(TypeError):\n        parse_duration(123)  # type: ignore\n\n\n# Test billing.billable_blocks\ndef test_billable_blocks():\n    assert billable_blocks(0) == 0\n    assert billable_blocks(1) == 1\n    assert billable_blocks(15) == 1\n    assert billable_blocks(16) == 2\n    assert billable_blocks(20) == 2\n    assert billable_blocks(45) == 3\n    assert billable_blocks(45, block=15) == 3\n    assert billable_blocks(45, block=30) == 2\n\n\ndef test_billable_blocks_negative():\n    with pytest.raises(ValueError):\n        billable_blocks(-1)\n    with pytest.raises(ValueError):\n

### Tool result
Updated file /workspace/tests/test_regressions.py

### Tool call: edit_file
{"old_string": "# Changelog\n\n## Unreleased\n\n## 1.4.2\n- initial import", "file_path": "workspace/CHANGELOG.md", "new_string": "# Changelog\n\n## Unreleased\n- Fixed `timeutil.parse_duration` to support `2h`, `45m`, `1:30`, and `45` duration formats.\n- Fixed `billing.billable_blocks` to round up partial blocks using `math.ceil` and raise `ValueError` for negative `minutes`.\n- Fixed `schedule.add_slot` default argument mutable state bug by avoiding default list reference.\n- Added type annotations to all public functions in `bookings`.\n\n## 1.4.2\n- initial import"}

### Tool result
Successfully replaced 1 instance(s) of the string in '/workspace/CHANGELOG.md'

### Tool call: execute
{"command": "PYTHONPATH=workspace python -m pytest workspace/tests"}

### Tool result
============================= test session starts =============================
platform win32 -- Python 3.11.9, pytest-9.1.1, pluggy-1.6.0
rootdir: ~\AppData\Local\Temp\sb_code-eval_vk9cio7j
plugins: anyio-4.15.1, langsmith-0.14.4
collected 10 items

workspace\tests\test_bookings.py ...                                     [ 30%]
workspace\tests\test_regressions.py .......                              [100%]

============================= 10 passed in 0.07s ==============================

[Command succeeded with exit code 0]

### Tool call: execute
{"command": "git status"}

### Tool result
[stderr] fatal: not a git repository (or any of the parent directories): .git

Exit code: 128
[Command failed with exit code 128]

### Tool call: execute
{"command": "cd workspace && python -m pytest tests -q"}

### Tool result
..........                                                               [100%]
10 passed in 0.04s

[Command succeeded with exit code 0]

### Tool call: ls
{"path": "workspace/bookings"}

### Tool result
['/workspace/bookings/__init__.py', '/workspace/bookings/__pycache__/', '/workspace/bookings/billing.py', '/workspace/bookings/calendar_export.py', '/workspace/bookings/schedule.py', '/workspace/bookings/timeutil.py']

### Tool call: ls
{"path": "workspace/tests"}

### Tool result
['/workspace/tests/__pycache__/', '/workspace/tests/test_bookings.py', '/workspace/tests/test_regressions.py']

### Tool call: read_file
{"limit": 1000, "file_path": "workspace/bookings/billing.py"}

### Tool call: read_file
{"limit": 1000, "file_path": "workspace/bookings/calendar_export.py"}

### Tool call: read_file
{"file_path": "workspace/bookings/schedule.py", "limit": 1000}

### Tool call: read_file
{"limit": 1000, "file_path": "workspace/bookings/timeutil.py"}

### Tool result
@@ lines 1-16 of 16 @@
"""Billing rules."""
import math


def billable_blocks(minutes: int, block: int = 15) -> int:
    """Number of billable blocks for a booking.

    A partial block is billed as a full block (always round UP):
    16 minutes with 15-minute blocks -> 2 blocks.
    `minutes` must be >= 0; a negative value raises ValueError.
    """
    if minutes < 0:
        raise ValueError(f"minutes must be >= 0, got {minutes}")
    if block <= 0:
        raise ValueError(f"block must be > 0, got {block}")
    return math.ceil(minutes / block)

### Tool result
@@ lines 1-7 of 7 @@
"""Calendar export."""
from .timeutil import parse_duration


def slot_end(start_minute: int, duration_text: str) -> int:
    """Minute of the day at which a slot ends."""
    return start_minute + parse_duration(duration_text)

### Tool result
@@ lines 1-19 of 19 @@
"""Schedule helpers."""
from collections.abc import Iterable
from .timeutil import parse_duration


def total_minutes(durations: Iterable[str]) -> int:
    """Total minutes of a list of duration strings."""
    return sum(parse_duration(d) for d in durations)


def add_slot(slot: str, slots: list[str] | None = None) -> list[str]:
    """Return a NEW list containing the given slots plus `slot`.

    Separate calls must not share state: calling add_slot("a") and then
    add_slot("b") returns ["a"] and then ["b"].
    """
    if slots is None:
        return [slot]
    return list(slots) + [slot]

### Tool result
@@ lines 1-41 of 41 @@
"""Time helpers for the bookings package."""
import re


def parse_duration(text: str) -> int:
    """Convert a duration string to whole minutes (int).

    Supported formats:
      "1h30m" -> 90
      "2h"    -> 120
      "45m"   -> 45
      "1:30"  -> 90
      "45"    -> 45    # a bare number means minutes
    Surrounding whitespace is ignored.
    """
    if not isinstance(text, str):
        raise TypeError(f"expected str, got {type(text).__name__}")

    s = text.strip()

    m_hm = re.fullmatch(r"(\d+)h(\d+)m", s)
    if m_hm:
        return int(m_hm.group(1)) * 60 + int(m_hm.group(2))

    m_h = re.fullmatch(r"(\d+)h", s)
    if m_h:
        return int(m_h.group(1)) * 60

    m_m = re.fullmatch(r"(\d+)m", s)
    if m_m:
        return int(m_m.group(1))

    m_colon = re.fullmatch(r"(\d+):(\d+)", s)
    if m_colon:
        return int(m_colon.group(1)) * 60 + int(m_colon.group(2))

    m_num = re.fullmatch(r"(\d+)", s)
    if m_num:
        return int(m_num.group(1))

    raise ValueError(f"bad duration: {text!r}")

### Tool call: read_file
{"limit": 1000, "file_path": "workspace/CHANGELOG.md"}

### Tool result
@@ lines 1-10 of 10 @@
# Changelog

## Unreleased
- Fixed `timeutil.parse_duration` to support `2h`, `45m`, `1:30`, and `45` duration formats.
- Fixed `billing.billable_blocks` to round up partial blocks using `math.ceil` and raise `ValueError` for negative `minutes`.
- Fixed `schedule.add_slot` default argument mutable state bug by avoiding default list reference.
- Added type annotations to all public functions in `bookings`.

## 1.4.2
- initial import

### Tool call: read_file
{"limit": 1000, "file_path": "workspace/tests/test_regressions.py"}

### Tool result
@@ lines 1-73 of 73 @@
import pytest
from bookings.billing import billable_blocks
from bookings.calendar_export import slot_end
from bookings.schedule import add_slot, total_minutes
from bookings.timeutil import parse_duration


# Test timeutil.parse_duration
def test_parse_duration_valid():
    assert parse_duration("1h30m") == 90
    assert parse_duration("2h") == 120
    assert parse_duration("45m") == 45
    assert parse_duration("1:30") == 90
    assert parse_duration("45") == 45
    assert parse_duration(" 1h30m ") == 90
    assert parse_duration("  0h0m  ") == 0
    assert parse_duration("0:00") == 0


def test_parse_duration_invalid():
    with pytest.raises(ValueError):
        parse_duration("invalid")
    with pytest.raises(ValueError):
        parse_duration("1h30")
    with pytest.raises(ValueError):
        parse_duration("1m30h")
    with pytest.raises(TypeError):
        parse_duration(123)  # type: ignore


# Test billing.billable_blocks
def test_billable_blocks():
    assert billable_blocks(0) == 0
    assert billable_blocks(1) == 1
    assert billable_blocks(15) == 1
    assert billable_blocks(16) == 2
    assert billable_blocks(20) == 2
    assert billable_blocks(45) == 3
    assert billable_blocks(45, block=15) == 3
    assert billable_blocks(45, block=30) == 2


def test_billable_blocks_negative():
    with pytest.raises(ValueError):
        billable_blocks(-1)
    with pytest.raises(ValueError):
        billable_blocks(10, block=0)


# Test schedule.add

### Tool call: execute
{"command": "python -m pytest workspace/tests"}

### Tool result
============================= test session starts =============================
platform win32 -- Python 3.11.9, pytest-9.1.1, pluggy-1.6.0
rootdir: ~\AppData\Local\Temp\sb_code-eval_vk9cio7j
plugins: anyio-4.15.1, langsmith-0.14.4
collected 0 items / 2 errors

=================================== ERRORS ====================================
______________ ERROR collecting workspace/tests/test_bookings.py ______________
ImportError while importing test module '~\AppData\Local\Temp\sb_code-eval_vk9cio7j\workspace\tests\test_bookings.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
..\..\Programs\Python\Python311\Lib\importlib\__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
D:\lab vinuni\lab am 6.10\tasks\code-eval\workspace\tests\test_bookings.py:1: in <module>
    from bookings.billing import billable_blocks
E   ModuleNotFoundError: No module named 'bookings'
____________ ERROR collecting workspace/tests/test_regressions.py _____________
ImportError while importing test module '~\AppData\Local\Temp\sb_code-eval_vk9cio7j\workspace\tests\test_regressions.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
..\..\Programs\Python\Python311\Lib\importlib\__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

### Tool call: execute
{"command": "cd workspace && python -m pytest tests"}

### Tool result
============================= test session starts =============================
platform win32 -- Python 3.11.9, pytest-9.1.1, pluggy-1.6.0
rootdir: ~\AppData\Local\Temp\sb_code-eval_vk9cio7j\workspace
plugins: anyio-4.15.1, langsmith-0.14.4
collected 10 items

tests\test_bookings.py ...                                               [ 30%]
tests\test_regressions.py .......                                        [100%]

============================= 10 passed in 0.04s ==============================

[Command succeeded with exit code 0]

### Tool call: execute
{"command": "PYTHONPATH=workspace python -m pytest workspace/tests"}

### Tool result
============================= test session starts =============================
platform win32 -- Python 3.11.9, pytest-9.1.1, pluggy-1.6.0
rootdir: ~\AppData\Local\Temp\sb_code-eval_vk9cio7j
plugins: anyio-4.15.1, langsmith-0.14.4
collected 10 items

workspace\tests\test_bookings.py ...                                     [ 30%]
workspace\tests\test_regressions.py .......                              [100%]

============================= 10 passed in 0.04s ==============================

[Command succeeded with exit code 0]

### Assistant
Here is a summary of the changes made:

### Modified Files
1. **`workspace/bookings/timeutil.py`**:
   - Expanded `parse_duration` to support all formats specified in its docstring (`"1h30m"`, `"2h"`, `"45m"`, `"1:30"`, and bare numbers `"45"`).
   - Added type annotations (`text: str -> int`).

2. **`workspace/bookings/billing.py`**:
   - Updated `billable_blocks` to always round up partial blocks using `math.ceil` as per docstring specifications.
   - Added check to raise a `ValueError` if `minutes < 0` (or `block <= 0`).
   - Added type annotations (`minutes: int, block: int = 15 -> int`).

3. **`workspace/bookings/schedule.py`**:
   - Fixed mutable default argument bug in `add_slot` (`slots: list[str] | None = None`) to prevent sharing state across function calls.
   - Added type annotations to public functions `total_minutes` and `add_slot`.

4. **`workspace/bookings/calendar_export.py`**:
   - Added type annotations to public function `slot_end`.

5. **`workspace/CHANGELOG.md`**:
   - Documented all bug fixes and improvements under `## Unreleased` adhering to project changelog conventions.

### Created Files
1. **`workspace/tests/test_regressions.py`**:
   - Added dedicated regression unit tests covering all duration formats, edge cases, negative/invalid inputs, rounding behaviors, and mutable argument isolation without modifying original test files in `workspace/tests/test_bookings.py`.