"""GUIDE Phần 1 - Định nghĩa subagent (tác tử con).   >>> SINH VIÊN CÀI ĐẶT <<<

Pseudo-code: guides/pseudocode/02_subagents.md
Kiểm tra:    pytest tests/test_02_agent.py
"""


def get_subagents() -> list[dict]:
    """Trả về danh sách subagent (ít nhất 2, tên khác nhau).

    Mỗi phần tử là một dict có các khóa bắt buộc:
      "name":          tên duy nhất (chữ thường, có thể có dấu gạch ngang)
      "description":   khi nào tác tử chính nên giao việc cho subagent này (viết như một hướng dẫn hành động)
      "system_prompt": chỉ dẫn cho subagent
    Gợi ý vai trò: explorer (đọc và báo cáo), implementer (thực hiện), reviewer (kiểm tra độc lập).
    """
    return [
        {
            "name": "explorer",
            "description": "Use to inspect the workspace, read instructions, README, docstrings, schema, or log samples. Returns findings and factual evidence without modifying any files.",
            "system_prompt": "You are an exploratory subagent. Your role is strictly read-only: investigate file structures, inspect data formats, search code and logs, and summarize requirements. Do not write or edit files.",
        },
        {
            "name": "implementer",
            "description": "Use to implement code fixes, clean data, parse log files, or execute Python scripts and tests. Modifies files in workspace and reports execution outcomes.",
            "system_prompt": "You are an implementation subagent. Your role is to perform changes to workspace files, write clean code or data outputs, run shell commands or tests, and report the results and exit codes.",
        },
        {
            "name": "reviewer",
            "description": "Use to independently review work after changes are made. Verifies test outputs, format compliance, edge cases, and checks whether all task criteria are met without making further changes.",
            "system_prompt": "You are a quality assurance and verification subagent. Your role is to inspect modified files against task instructions, run verification tests, identify discrepancy or regression, and report pass/fail status.",
        },
    ]
