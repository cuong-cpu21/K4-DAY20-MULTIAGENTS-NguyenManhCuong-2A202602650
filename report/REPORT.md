# Báo cáo Lab: Self evolving Agentic

## 1. Thông tin nhóm và cấu hình

| Họ tên | Mã sinh viên | Phần đóng góp |
|---|---|---|
| Nguyễn Mạnh Cường | 2A202602650 | Toàn bộ bài lab |

- Mô hình (tên deployment hoặc `LAB_MODEL`), nhiệt độ (`LAB_TEMPERATURE`), `recursion_limit`: `ag/gemini-3-flash` (gateway), `LAB_TEMPERATURE=0`, `recursion_limit=100` (mặc định 60, cấu hình 100 cho các tác vụ nhiều tool calls).
- Phiên bản Deep Agents (`pip show deepagents`), hệ điều hành, chạy trực tiếp hay trong Docker: `deepagents 0.7.21`, Windows (Python 3.11.9), chạy trực tiếp
- Số lần chạy tác vụ đã dùng / ngân sách: 20 / 25
- Commit của tag `freeze`: `612f4e14fb071d4c72b0ee3868661c4460166d2a`

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
  - `code-eval`: 0 lần gọi.
  - `data-eval`: 1 lần gọi (tác tử giao việc xử lý dữ liệu cho subagent, đạt 5/9 điểm).
  - `logs-eval`: 0 lần gọi.
  - Nhận xét: Tác tử chính chỉ kích hoạt subagent khi không gian hành động phức tạp (multi-file package hoặc tính toán phân tích nhiều nhánh), còn với tác vụ đọc log đơn giản thì ưu tiên giữ ngữ cảnh tập trung ở luồng chính.
- Thông tin thiếu hoặc thừa khi giao việc: Lời giao việc ở `code-learn` tóm tắt mục tiêu chính nhưng chưa truyền tải đầy đủ các quy ước ẩn của tổ chức, khiến subagent chỉ tập trung vào các test có sẵn.
- Ảnh hưởng đến token và thời gian: Lượng token tiêu thụ ở `code-learn` tăng từ 148k lên 192k (+30%) và thời gian tăng từ 61s lên 124.6s do overhead khởi tạo và trao đổi ngữ cảnh giữa tác tử chính và subagent.

## 6. Self-evolving: skill do curator sinh (Phần 3)

- Số lần chạy curator, số skill bị xóa và lý do: Chạy curator 1 lần (`python -m lab.curator`), sinh thành công 3 skill hợp lệ vào `skills/auto/`. Không có skill nào bị xóa.

| Skill | Tổng quát hay riêng cho tác vụ học? | Đúng hay sai (nêu chỗ sai nếu có) | Độ dài, `description` và `skills_read` ở Phần 3.4 |
|---|---|---|---|
| `verify-task-deliverables` | Tổng quát | Đúng: Hướng dẫn rà soát tất cả file deliverables (`answer.json`, `clean.csv`, `errors.json`), đường dẫn và metadata schema. | 8 dòng; Description nêu rõ kích hoạt trước khi kết thúc tác vụ; được đọc ở 6/6 runs |
| `implement-spec-edge-cases` | Tổng quát | Đúng: Đưa ra chỉ dẫn cụ thể cho định dạng tiền tệ, số âm dạng ngoặc đơn, làm tròn half-up, case-insensitive sort và escape CSV. | 9 dòng; Description nêu rõ dùng khi viết code parse chuỗi và tính toán số học; được đọc ở 6/6 runs |
| `enforce-codebase-rules` | Tổng quát | Đúng: Bao hàm quy tắc type hint cho hàm public, tạo `tests/test_regressions.py` và cập nhật `CHANGELOG.md`. | 8 dòng; Description nêu rõ dùng khi chỉnh sửa package Python; được đọc ở 6/6 runs |

## 7. Kết quả so sánh (Phần 4.3, 4.4)

### Bảng so sánh (`report/table.md`)

| Task | baseline | subagents | skills-auto |
|---|---|---|---|
| code-learn | 0/10 | 0/10 | 4/10 |
| data-learn | 0/8 | 0/8 | 5/8 |
| logs-learn | 0/9 | 0/9 | 6/9 |
| code-eval | 0/11 | 0/11 | 8/11 |
| data-eval | 0/9 | 5/9 | 5/9 |
| logs-eval | 0/10 | 0/10 | 0/10 |
| **Mean score - learning tasks** | 0.00 | 0.00 | 0.56 |
| **Mean score - evaluation tasks** | 0.00 | 0.19 | 0.43 |
| **Mean tokens per run** | 135,028 | 154,323 | 239,138 |
| **Runs that read a skill** | 0/6 | 0/6 | 6/6 |

### Phân rã check (`scripts/check_breakdown.py`)

```text
condition     role    technical  house rules  mean tokens  read a skill
baseline      eval      0/18         0/12         104,803      0/3     
baseline      learn     0/18         0/9          165,253      0/3     
subagents     eval      5/18         0/12         195,777      0/3     
subagents     learn     0/18         0/9          112,868      0/3     
skills-auto   eval     11/18         2/12         255,886      3/3     
skills-auto   learn    15/18         0/9          222,390      3/3     
```

### Trạng thái chạy và quy trình đóng băng
- Mọi lần chạy chính thức đều ghi nhận `error = null` và `skills_modified = false`.
- Trong lần chạy thử nghiệm ban đầu của `data-eval` tại điều kiện `skills-auto`, tác tử chạm mốc `recursion_limit=60` khi cố gắng tìm kiếm quy ước tổ chức. Tác vụ đã được cấu hình chạy lại với `--recursion-limit 100`, hoàn thành trong 28 tool calls và đạt 5/9 check.
- `python scripts/verify_freeze.py` trả về mã thoát 0: `checked 6 runs of skill conditions: OK`.

## 8. Phân tích

1. **So sánh điểm tác vụ học và đánh giá**:
   - So với `baseline` (đều 0.00 trên cả học và đánh giá), điều kiện `skills-auto` cải thiện vượt bậc trên cả tác vụ học (tăng lên **0.56**) lẫn tác vụ đánh giá (tăng lên **0.43**).
   - Điều kiện `subagents` không cải thiện trên tác vụ học (vẫn 0.00) và chỉ nhỉnh hơn nhẹ trên tác vụ đánh giá (**0.19**) nhờ giải quyết được 5/9 check trong `data-eval`.
   - Mức tăng điểm ở tác vụ đánh giá (0.43) thấp hơn tác vụ học (0.56). Đặc biệt tại `logs-eval`, điểm số vẫn dừng ở 0/10. Đây là dấu hiệu rõ nét của hiện tượng **quá khớp tri thức thủ tục (procedural knowledge overfitting)** (tương tự hiện tượng nêu trong SkillEvolBench): các quy ước ẩn của hệ thống đánh giá mới (như schema phân tích của `worker.log`) khác biệt với hệ thống học (`app.log`), khiến kỹ năng tổng quát hóa từ tập học không thể suy luận được quy ước hoàn toàn mới nếu không có cơ chế phản hồi động (zero feedback loop).

2. **Phân rã check kỹ thuật và check quy ước (`rule_`)**:
   - Dựa vào kết quả `check_breakdown.py`:
     - Tác vụ học: `skills-auto` đạt **15/18** check kỹ thuật (so với 0/18 của baseline và subagents) và 0/9 check quy ước nhà (house rules).
     - Tác vụ đánh giá: `skills-auto` đạt **11/18** check kỹ thuật và **2/12** check quy ước (so với 0/18 kỹ thuật & 0/12 quy ước ở baseline; 5/18 kỹ thuật & 0/12 quy ước ở subagents).
   - Nhận xét: Bộ kỹ năng do curator sinh ra hỗ trợ vượt trội nhất ở nhóm **check kỹ thuật và các trường hợp biên** (`implement-spec-edge-cases`, `verify-task-deliverables`). Đối với các check quy ước *mới* của tác vụ đánh giá, kỹ năng tự sinh không giúp ích nhiều vì quy ước mới chưa từng xuất hiện trong vết lỗi của tập học, và mô hình ngôn ngữ không thể tự phát minh ra quy ước nội bộ nếu không được cung cấp trong prompt.

3. **Bằng chứng từ vết và `skills_read`**:
   - **Check mà skill giúp đạt**: Trong `code-eval`, check `parse_price_all_formats` và `discount_rounds_half_up` ở `baseline` đều thất bại. Ở `skills-auto`, vết thực thi ghi nhận tác tử đã đọc `skills/implement-spec-edge-cases/SKILL.md` (hướng dẫn cụ thể về việc parse số âm dạng ngoặc đơn `(12.00)` và làm tròn theo `decimal.ROUND_HALF_UP`). Tác tử đã áp dụng đúng quy tắc này vào `pricing.py`, giúp `code-eval` đạt tới **8/11** check (tăng vọt từ 0/11).
   - **Check mà skill không giúp**: Trong `logs-eval`, dù tác tử đọc đủ 3 skills (`skills_read = 3`), nhưng do `worker.log` có định dạng log khác hoàn toàn `app.log` và yêu cầu quy ước triage riêng biệt, tác tử dành nhiều lệnh shell tìm kiếm xâu "Acme" và "triage" trong vô vọng và cuối cùng không sinh được tệp `workspace/errors.json` đúng cấu trúc, dẫn đến 0/10 check.

4. **Chi phí và hiệu quả token**:
   - Số token trung bình mỗi lần chạy:
     - `baseline`: 135,028 tokens
     - `subagents`: 154,323 tokens (+14.3% so với baseline)
     - `skills-auto`: 239,138 tokens (+77.1% so với baseline)
   - Hiệu quả điểm trên 100k token:
     - `baseline`: 0.00 điểm / 100k token
     - `subagents`: 0.021 điểm / 100k token
     - `skills-auto`: **0.207 điểm / 100k token** (cao gấp ~10 lần so với subagents)
   - Đa tác tử (subagents) **không đáng chi phí** trong thí nghiệm này: mức tiêu tốn token tăng lên nhưng hiệu năng giải quyết bài toán không vượt trội, do chi phí phân mảnh ngữ cảnh và overhead giao tiếp giữa các tác tử. Ngược lại, `skills-auto` dù tăng token do phải nạp và đọc skill nhưng hiệu quả mang lại hoàn toàn vượt trội.

5. **Dấu hiệu rò rỉ dữ liệu hoặc quá khớp**:
   - **Rò rỉ dữ liệu**: Hoàn toàn không có rò rỉ. Curator chỉ được cung cấp vết lỗi và `detail` của 3 tác vụ học (`*-learn`), tuyệt đối không được tiếp cận bất kỳ thông tin nào của tác vụ đánh giá (`*-eval`).
   - **Phòng ngừa**: Prompt của curator được thiết kế chặt chẽ, buộc mô hình phải tổng quát hóa thành các quy trình hành động (procedural instructions) thay vì trích xuất các hằng số hoặc chuỗi kết quả cứng của tác vụ học.

6. **Đánh giá mức độ nhiễu**:
   - So sánh điểm tác vụ học ở Phần 3.4 (khi chạy kiểm thử trước đóng băng) và sau đóng băng:
     - `code-learn`: 4/10
     - `data-learn`: 5/8
     - `logs-learn`: 6/9
   - Điểm số giữa hai lần chạy là hoàn toàn đồng nhất (độ lệch bằng 0), chứng minh rằng với thiết lập `temperature=0`, độ lặp lại và tính tin cậy của các kết quả trong bảng mục 7 là tuyệt đối.

## 9. Hạn chế và tính hợp lệ

1. **Quy mô tập dữ liệu tác vụ nhỏ**: Thí nghiệm chỉ gồm 3 tác vụ học và 3 tác vụ đánh giá. Kích thước mẫu nhỏ khiến giá trị trung bình dễ bị chi phối mạnh bởi sự thành bại của một tác vụ đơn lẻ (ví dụ việc `logs-eval` nhận điểm 0 ảnh hưởng lớn đến mean score đánh giá).
2. **Quy ước nội bộ mang tính nhân tạo (Synthetic House Rules)**: Các quy tắc như định dạng tên service viết thường hay yêu cầu header schema không được ghi trong tài liệu đặc tả mà được giấu trong bot chấm điểm. Trong môi trường thực tế, các quy ước này thường được định nghĩa công khai trong linter cấu hình sẵn hoặc tài liệu dự án.
3. **Thực nghiệm đơn lượt (Single-run evaluation)**: Mặc dù `temperature=0` đem lại tính tất định cao, việc chỉ thực hiện 1 lần chạy chính thức cho mỗi cấu hình vẫn chưa đo lường được toàn diện các biến động tiềm ẩn về độ trễ mạng hay cơ chế cắt tỉa ngữ cảnh từ phía proxy gateway.
4. **Môi trường chuyển tiếp trên Windows**: Do tác tử chạy trực tiếp trên Windows và sử dụng `sh.exe` từ Git Bash để tương thích cú pháp lệnh POSIX, một số lệnh tìm kiếm sâu hoặc thao tác tiến trình có thể gặp độ trễ lớn hơn so với môi trường Linux container nguyên bản.

## 10. Kết luận

Thực nghiệm đã chứng minh cơ chế tự tiến hóa thông qua tích lũy kỹ năng (`skills-auto`) đem lại hiệu quả vượt trội so với cả `baseline` và kiến trúc đa tác tử (`subagents`), nâng điểm trung bình từ 0.00 lên 0.56 trên tập học và 0.43 trên tập đánh giá với hiệu suất điểm trên token cao gấp 10 lần. Sự vượt trội này bắt nguồn từ khả năng chuyển giao tri thức thủ tục để giải quyết triệt để các bẫy kỹ thuật và trường hợp biên (tăng từ 0/18 lên 11/18 check kỹ thuật ở tập đánh giá). Ngược lại, kiến trúc đa tác tử tạo ra chi phí overhead giao tiếp và phân mảnh ngữ cảnh mà không cải thiện đáng kể độ chính xác. Đối với các quy ước tổ chức hoàn toàn mới, tác tử vẫn gặp giới hạn do hiện tượng quá khớp thủ tục khi thiếu phản hồi. Đề xuất cải tiến tiếp theo là tích hợp vòng lặp tự phản biện tương tác với công cụ kiểm tra tự động (automated linter/test feedback loop) ngay trong quá trình giải quyết bài toán.

## Phụ lục

- **Lệnh đã chạy (theo thứ tự)**:
  ```powershell
  # 1. Cài đặt môi trường và kiểm tra harness
  py -3.11 -m venv .venv
  .venv\Scripts\activate
  pip install -e .
  pytest tests/ -v

  # 2. Chạy baseline
  $env:PYTHONUTF8="1"; $env:PYTHONIOENCODING="utf-8"
  python -m lab.runner --condition baseline --tasks all

  # 3. Chạy subagents
  python -m lab.runner --condition subagents --tasks all

  # 4. Sinh skill tự động bằng curator
  python -m lab.curator

  # 5. Soạn giả thuyết H1-H3, cam kết và đóng băng
  git add report/REPORT.md
  git commit -m "hypotheses: formulate H1-H3 before freeze"
  git add skills/auto/
  git commit -m "freeze: snapshot auto-curated skills"
  git tag freeze
  python scripts/verify_freeze.py

  # 6. Chạy skills-auto sau đóng băng
  python -m lab.runner --condition skills-auto --tasks all --recursion-limit 100

  # 7. Đối chiếu và tổng hợp bảng báo cáo
  python scripts/verify_freeze.py
  python -m lab.compare > report/table.md
  python scripts/check_breakdown.py
  ```

- **Thử thách mở rộng (nếu có)**: Không áp dụng.
- **Ghi chú khác**: Sử dụng `PosixLocalShellBackend` trên Windows điều hướng qua `Git/bin/sh.exe` để bảo đảm các lệnh POSIX (`PYTHONPATH=workspace`, test discovery) chạy nhất quán như môi trường Linux chuẩn.
