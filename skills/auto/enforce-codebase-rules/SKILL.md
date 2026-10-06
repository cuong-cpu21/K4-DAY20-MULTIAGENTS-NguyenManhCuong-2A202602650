---
name: enforce-codebase-rules
description: Apply when modifying Python codebases to comply with project repository standards, type hints, regression tests, and documentation logs.
---
1. Annotate all public functions (names not starting with `_`) with type hints on all parameters and return types.
2. Add dedicated regression test files (e.g., `tests/test_regressions.py`) with test functions for each fixed bug without altering existing test files.
3. Update CHANGELOG files under designated headers (e.g., `## Unreleased`) using the project's exact line/bullet formatting.
4. Run the full test suite locally before submission to verify visible test passes and zero suite regressions.
