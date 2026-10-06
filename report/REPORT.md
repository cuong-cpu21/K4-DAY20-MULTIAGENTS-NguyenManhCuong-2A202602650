# Báo cáo Lab: Self evolving Agentic

> Sao chép tệp này thành `report/REPORT.md` (đã làm ở Phần 0) và điền dần qua các Phần của lab. Xóa các dòng hướng dẫn dạng trích dẫn (bắt đầu bằng `>`). Văn phong kỹ thuật, ngắn gọn, mọi nhận định đi kèm số liệu hoặc bằng chứng. Trong buổi học: điền mục 1 đến 7 (bản nháp). Sau buổi học: hoàn thiện mục 8 đến 10.

## 1. Thông tin nhóm và cấu hình

| Họ tên | Mã sinh viên | Phần đóng góp |
|---|---|---|
| Nguyễn Mạnh Cường | 2A202602650 | Toàn bộ bài lab |

- Mô hình (tên deployment hoặc `LAB_MODEL`), nhiệt độ (`LAB_TEMPERATURE`), `recursion_limit`: `ag/gemini-3-flash` (gateway), `LAB_TEMPERATURE=0`, `recursion_limit=60`
- Phiên bản Deep Agents (`pip show deepagents`), hệ điều hành, chạy trực tiếp hay trong Docker: `deepagents 0.7.21`, Windows (Python 3.11.9), chạy trực tiếp
- Số lần chạy tác vụ đã dùng / ngân sách: 0 / 25
- Commit của tag `freeze`: (chưa tạo)

## 2. Giả thuyết (commit TRƯỚC tag `freeze`, Phần 4.0)

- H1 (subagents so với baseline): Điều kiện `subagents` sẽ có điểm tương đương hoặc chỉ nhỉnh hơn nhẹ so với `baseline` trên tác vụ đánh giá, nhưng tiêu tốn lượng token và thời gian cao hơn đáng kể (tăng khoảng 30-60%) do chi phí context isolation và overhead trao đổi thông tin giữa các agent.
- H2 (skills-auto so với baseline): Điều kiện `skills-auto` sẽ cải thiện điểm rõ rệt trên các tác vụ học nhờ khắc phục được các quy ước tổ chức (nhóm E) và bẫy định dạng (nhóm D), nhưng trên tác vụ đánh giá mức tăng điểm sẽ khiêm tốn hơn do tác vụ đánh giá xuất hiện các quy ước mới chưa từng có trong tập học (hiện tượng overfitting tri thức thủ tục theo nghiên cứu SkillEvolBench).
- H3 (tác vụ học so với tác vụ đánh giá): Điểm trung bình trên tác vụ học sẽ cao hơn tác vụ đánh giá trên mọi điều kiện, do tác vụ đánh giá bổ sung thêm các quy ước mới và dữ liệu biên phức tạp mà không có vòng lặp phản hồi (zero feedback loop) trong quá trình thực thi.

## 3. Làm quen Deep Agents (Phần 0.3)

1. Tác tử mặc định có 9 công cụ:
   - Các công cụ thao tác tệp: `ls`, `read_file`, `write_file`, `edit_file`, `delete`, `glob`, `grep`.
   - Công cụ chạy lệnh shell: `execute` (cho phép chạy lệnh shell trong môi trường sandbox cách ly).
   - Công cụ giao việc cho subagent: `task`.
   Trong đó, công cụ duy nhất cho phép chạy lệnh thực thi là `execute`.

2. Mô tả của công cụ `task` về subagent `general-purpose`:
   - Định nghĩa: Là subagent đa năng dùng để nghiên cứu các câu hỏi phức tạp, tìm kiếm tệp tin & nội dung, và thực hiện các tác vụ nhiều bước ("General-purpose agent for researching complex questions, searching for files and content, and executing multi-step tasks. ... This agent has access to all tools as the main agent.").
   - Về ngữ cảnh: Subagent được khởi tạo dạng phi trạng thái (stateless) theo mặc định, nó **chỉ nhìn thấy prompt/chỉ dẫn** mà tác tử chính gửi trực tiếp qua lời gọi tool `task`, không kế thừa lịch sử hội thoại hay ngữ cảnh trước đó của tác tử chính ("Each invocation is stateless by default: the agent sees only the prompt you give it and returns a single final report").

3. Trích dẫn câu hướng dẫn hành vi:
   - Từ mô tả công cụ `task`: *"Put full detail in the prompt and state exactly what it should return – unless an agent type below says it inherits your conversation instead."* (hoặc *"Tell the agent whether to create content, analyze, or only research, since it can't necessarily see the user's intent unless it inherits your conversation"*).
   - Từ mô tả công cụ `execute`: *"You MUST avoid using search commands like find and grep. Instead use the grep, glob tools to search. Use read_file rather than cat/head/tail."* (và *"Use absolute paths and avoid `cd` so the working directory stays stable"*).

## 4. Đường cơ sở và phân loại lỗi (Phần 2.2)

| Tác vụ | Check thất bại | Nhóm lỗi (A-G) | Bằng chứng (trích ngắn từ `detail` hoặc vết) |
|---|---|---|---|
| `code-learn` | `rule_type_hints` | E | `RULE: every public function (name not starting with '_') in the package has type annotations on all parameters and on the return value.` |
| `code-learn` | `rule_regression_tests` | E | `RULE: add tests/test_regressions.py with one test function per bug you fixed (at least 3); the file must pass.` |
| `code-learn` | `rule_changelog` | E | `RULE: record each fix in CHANGELOG.md under the heading '## Unreleased' as a bullet '- fix(<function name>): <short description>' (at least 3 bullets).` |
| `code-learn` | `parse_price_all_formats` | D | `wrong for: ['$1,299.50', '(12.00)', '$1,000,000.00']` (chuỗi tiền tệ có dấu phẩy và ngoặc đơn âm) |
| `code-learn` | `discount_rounds_half_up` | A | `wrong for: [('10.05', 10, '9.05'), ('0.05', 50, '0.03'), ('2.665', 0, '2.67')]` (không đọc docstring về quy tắc làm tròn ROUND_HALF_UP) |
| `code-learn` | `low_stock_follows_docstring` | A | `low_stock returned ['b', 'A', 'c']` (bỏ qua yêu cầu sort case-insensitive trong docstring) |
| `code-learn` | `csv_quoting_follows_docstring` | A | `to_csv_row returned 'Desk, large "oak",10.00,2'` (chưa escape dấu ngoặc kép theo chuẩn RFC 4180) |
| `data-learn` | `rule_clean_csv` | E | `RULE: write workspace/clean.csv with the header order_id,timestamp_utc,region,amount_cents...` |
| `data-learn` | `rule_money_in_cents` | E | `RULE: money values in answer.json are integer cents (1606.67 USD is written 160667).` |
| `data-learn` | `rule_meta_block` | E | `RULE: answer.json has an object meta = {"source": <input file name>, "rows_in": ..., "rows_used": ...}` |
| `data-learn` | `north_q1_revenue` | D | Không chuẩn hóa múi giờ không đồng nhất (ISO 8601 offset vs UTC) và bỏ qua giá trị thiếu `-999`. |
| `logs-learn` | `rule_service_names` | E | `RULE: service names in errors.json are lowercase (e.g. auth, api, billing)` |
| `logs-learn` | `rule_sorted_errors` | E | `RULE: errors array is sorted chronologically by timestamp_utc ascending` |
| `logs-learn` | `rule_schema_header` | E | `RULE: errors.json includes a top-level schema header {"version": "1.0", ...}` |

Nhận xét: nhóm lỗi chiếm đa số là **Nhóm E (Vi phạm quy ước tổ chức / House rules)** và **Nhóm D (Bỏ sót định dạng/dữ liệu bẩn)**.
- Các quy ước tổ chức (bắt đầu bằng `rule_`) hoàn toàn không được mô tả tường minh trong đề bài ban đầu, chỉ do bot kiểm tra nội bộ chấm. Do đó, tác tử `baseline` không thể tự suy luận được.
- Skill hoàn toàn **có thể phòng ngừa** nhóm lỗi này: việc curator trích xuất các quy tắc này thành checklist bắt buộc trong `SKILL.md` sẽ giúp tác tử ở các lần chạy sau đọc và thực hiện đầy đủ ngay từ bước đầu tiên.

## 5. Điều kiện `subagents` (Phần 2.3)

- Các subagent đã định nghĩa (tên, vai trò, lý do thiết kế):
  1. `explorer`: Đóng vai trò khảo sát, đọc cấu trúc tệp, README, docstring và mẫu dữ liệu; trả về dữ liệu khách quan mà không sửa đổi tệp tin.
  2. `implementer`: Đóng vai trò thực thi, trực tiếp viết mã nguồn, sửa lỗi, chạy test và sinh các tệp output yêu cầu.
  3. `reviewer`: Đóng vai trò kiểm định độc lập, đối chiếu các deliverable với yêu cầu đề bài và kiểm tra các trường hợp biên trước khi kết thúc.
- `subagent_calls` ở từng tác vụ và nhận xét (kể cả trường hợp bằng 0):
  - `code-learn`: 1 lần gọi (tác tử chính giao việc khảo sát và thực thi cho subagent khi cấu trúc dự án có nhiều tệp tin).
  - `data-learn`: 0 lần gọi (tác tử chính nhận thấy đây là tệp đơn lẻ nên tự thực hiện trực tiếp).
  - `logs-learn`: 0 lần gọi (tác tử chính chọn tự phân tích luồng log thay vì chia nhỏ).
  - Nhận xét: Tác tử chính chỉ kích hoạt subagent khi không gian hành động phức tạp (multi-file package), còn với tác vụ xử lý tệp đơn lẻ thì ưu tiên giữ ngữ cảnh tập trung ở luồng chính.
- Thông tin thiếu hoặc thừa khi giao việc (nếu có giao việc): Lời giao việc ở `code-learn` tóm tắt mục tiêu chính nhưng chưa truyền tải đầy đủ các quy ước ẩn của tổ chức, khiến subagent chỉ tập trung vào các test có sẵn.
- Ảnh hưởng đến token và thời gian: Lượng token tiêu thụ ở `code-learn` tăng từ 148k lên 192k (+30%) và thời gian tăng từ 61s lên 124.6s do overhead khởi tạo và trao đổi ngữ cảnh giữa tác tử chính và subagent.

## 6. Self-evolving: skill do curator sinh (Phần 3)

- Số lần chạy curator, số skill bị xóa và lý do: Chạy curator 1 lần (`python -m lab.curator`), sinh thành công 3 skill hợp lệ vào `skills/auto/`. Không có skill nào bị xóa.

| Skill | Tổng quát hay riêng cho tác vụ học? | Đúng hay sai (nêu chỗ sai nếu có) | Độ dài, `description` và `skills_read` ở Phần 3.4 |
|---|---|---|---|
| `verify-task-deliverables` | Tổng quát | Đúng: Hướng dẫn rà soát tất cả file deliverables (`answer.json`, `clean.csv`, `errors.json`), đường dẫn và metadata schema. | 9 dòng; Description nêu rõ kích hoạt trước khi kết thúc tác vụ; |
| `implement-spec-edge-cases` | Tổng quát | Đúng: Đưa ra chỉ dẫn cụ thể cho định dạng tiền tệ, số âm dạng ngoặc đơn, làm tròn half-up, case-insensitive sort và escape CSV. | 10 dòng; Description nêu rõ dùng khi viết code parse chuỗi và tính toán số học; |
| `enforce-codebase-rules` | Tổng quát | Đúng: Bao hàm quy tắc type hint cho hàm public, tạo `tests/test_regressions.py` và cập nhật `CHANGELOG.md`. | 9 dòng; Description nêu rõ dùng khi chỉnh sửa package Python; |

## 7. Kết quả so sánh (Phần 4.3, 4.4)

> Dán nội dung `report/table.md` và kết quả `python scripts/check_breakdown.py`. Nêu các lần chạy có `error` hoặc `skills_modified = true` (nếu có) và cách xử lý.

```text
(dán bảng ở đây)
```

## 8. Phân tích

> Trả lời từng câu bằng số liệu từ mục 7 và bằng chứng từ vết. Kết quả âm hoặc không có khác biệt vẫn hợp lệ nếu được phân tích tốt.

1. So với `baseline`, điều kiện nào cải thiện điểm tác vụ **học**? Điều kiện nào cải thiện điểm tác vụ **đánh giá**? Có điều kiện nào cải thiện tác vụ học nhưng không cải thiện tác vụ đánh giá? Nếu có, đó là dấu hiệu gì?
2. Tách điểm thành check kỹ thuật và check quy ước (`rule_`). Skill do curator sinh giúp nhóm check nào? Check quy ước **mới** của tác vụ đánh giá có được skill giúp không, và vì sao?
3. Dựa vào vết và `skills_read`, giải thích một check mà skill giúp đạt và một check mà skill không giúp (skill chưa được đọc, đọc nhưng không làm theo, skill thiếu hoặc sai).
4. Chi phí: so sánh số token trung bình giữa các điều kiện. Điều kiện nào có hiệu quả tốt nhất theo điểm trên mỗi token? Đa tác tử có đáng chi phí trong thí nghiệm này không?
5. Có dấu hiệu rò rỉ dữ liệu hoặc quá khớp nào trong skill sinh ra không? Nhóm đã phòng tránh như thế nào?
6. Nhiễu: so sánh điểm tác vụ học của cùng bộ skill ở Phần 3.4 (đã sao lưu) và sau đóng băng. Chênh lệch bao nhiêu? Nó cho biết điều gì về độ tin cậy của các chênh lệch trong bảng ở mục 7?

## 9. Hạn chế và tính hợp lệ

> Nêu ít nhất 3 hạn chế và ảnh hưởng của từng hạn chế đến kết luận (ví dụ: chỉ 3 tác vụ mỗi vai trò, mỗi cấu hình chạy một lần, nhiễu của mô hình, tác vụ do giảng viên thiết kế sẵn quy ước, chỉ một mô hình).

1.
2.
3.

## 10. Kết luận

> Tối đa 5 câu. Chỉ khẳng định điều số liệu hỗ trợ. Nêu một đề xuất cải tiến tiếp theo.

## Phụ lục

- Lệnh đã chạy (theo thứ tự):
- Thử thách mở rộng (nếu có): hướng chọn, kết quả, nhận xét.
- Ghi chú khác:
