### Human
The test suite of the `bookings` package in the folder `workspace/` is failing.

Fix the source code so that the whole test suite passes and every function does what its docstring says.
The visible tests do not cover everything: the docstrings are the specification.
Do not modify the existing files in `tests/`.
Your changes are also checked by Acme's review bot against the Acme Python team conventions.

When you are done, reply with a short summary of what you changed and why.


### Tool call: glob
{"path": "workspace", "pattern": "**/*"}

### Tool result
['/workspace/CHANGELOG.md', '/workspace/README.md', '/workspace/bookings/__init__.py', '/workspace/bookings/__pycache__/__init__.cpython-311.pyc', '/workspace/bookings/__pycache__/billing.cpython-311.pyc', '/workspace/bookings/__pycache__/calendar_export.cpython-311.pyc', '/workspace/bookings/__pycache__/schedule.cpython-311.pyc', '/workspace/bookings/__pycache__/timeutil.cpython-311.pyc', '/workspace/bookings/billing.py', '/workspace/bookings/calendar_export.py', '/workspace/bookings/schedule.py', '/workspace/bookings/timeutil.py', '/workspace/tests/__pycache__/test_bookings.cpython-311-pytest-9.1.1.pyc', '/workspace/tests/test_bookings.py']

### Tool call: execute
{"command": "pytest workspace/tests"}

### Tool result
============================= test session starts =============================
platform win32 -- Python 3.11.9, pytest-9.1.1, pluggy-1.6.0
rootdir: ~\AppData\Local\Temp\sb_code-eval_p4qbce9f
plugins: anyio-4.15.1, langsmith-0.14.4
collected 0 items / 1 error

=================================== ERRORS ====================================
______________ ERROR collecting workspace/tests/test_bookings.py ______________
ImportError while importing test module '~\AppData\Local\Temp\sb_code-eval_p4qbce9f\workspace\tests\test_bookings.py'.
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
============================== 1 error in 0.16s ===============================

Exit code: 2
[Command failed with exit code 2]

### Tool call: execute
{"command": "python -m pytest workspace"}

### Tool result
============================= test session starts =============================
platform win32 -- Python 3.11.9, pytest-9.1.1, pluggy-1.6.0
rootdir: ~\AppData\Local\Temp\sb_code-eval_p4qbce9f
plugins: anyio-4.15.1, langsmith-0.14.4
collected 0 items / 1 error

=================================== ERRORS ====================================
______________ ERROR collecting workspace/tests/test_bookings.py ______________
ImportError while importing test module '~\AppData\Local\Temp\sb_code-eval_p4qbce9f\workspace\tests\test_bookings.py'.
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
============================== 1 error in 0.16s ===============================

Exit code: 2
[Command failed with exit code 2]