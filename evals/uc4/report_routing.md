# UC4 Chat Tool Routing Evaluation Report (T-42)

- **Date:** 2026-10-27T18:13:14.651273+00:00
- **Total Cases:** 40
- **Overall Status:** PASS

## 1. Quality Gates

| Gate | Metric | Target | Actual | Verdict |
|---|---|---|---|---|
| G-R1 | Should-call recall | >= 0.95 | 100.00% | PASS |
| G-R2 | Match served by generic search | = 0 | 0 | PASS |
| G-R3 | False calls (non-matching prompts) | <= 1 | 0 | PASS |
| G-R4 | Invented criteria | = 0 | 0 | PASS |
| G-R5 | Criteria exact match rate | >= 0.90 | 100.00% | PASS |
| G-R6 | Narration violations | = 0 | 0 | PASS |

## 2. Category Breakdown

| Category | Count | Passed | Pass Rate |
|---|---|---|---|
| `should_call` | 12 | 12 | 100.0% |
| `keyword_browse` | 8 | 8 | 100.0% |
| `no_tool` | 6 | 6 | 100.0% |
| `need_cv` | 4 | 4 | 100.0% |
| `criteria_exact` | 8 | 8 | 100.0% |
| `adversarial_cv` | 2 | 2 | 100.0% |

## 3. Detailed Case Results

| ID | Category | Prompt | Tools Called | Status | Issues |
|---|---|---|---|---|---|
| `c01` | `should_call` | Hãy tìm việc phù hợp với CV tôi vừa đính kèm. | `match_jobs_for_cv` | PASS | none |
| `c02` | `should_call` | Dựa vào CV của mình, có dự án freelance nào thích hợp không? | `match_jobs_for_cv` | PASS | none |
| `c03` | `should_call` | Xem CV này và gợi ý công việc cho tôi. | `match_jobs_for_cv` | PASS | none |
| `c04` | `should_call` | Tìm giúp mình job phù hợp với profile trong file nhé. | `match_jobs_for_cv` | PASS | none |
| `c05` | `should_call` | Match my attached resume with open job postings. | `match_jobs_for_cv` | PASS | none |
| `c06` | `should_call` | Recommend the best freelance projects for my background in the resume. | `match_jobs_for_cv` | PASS | none |
| `c07` | `should_call` | Kiểm tra CV của tôi và đưa ra các dự án tuyển dụng liên quan. | `match_jobs_for_cv` | PASS | none |
| `c08` | `should_call` | Tôi có CV này, hãy cho tôi biết có việc gì phù hợp không? | `match_jobs_for_cv` | PASS | none |
| `c09` | `should_call` | Find suitable projects based on my experience in the attached document. | `match_jobs_for_cv` | PASS | none |
| `c10` | `should_call` | Giúp tôi tìm các vị trí tuyển dụng khớp với năng lực trong hồ sơ. | `match_jobs_for_cv` | PASS | none |
| `c11` | `should_call` | Đánh giá và tìm việc làm cho CV đính kèm. | `match_jobs_for_cv` | PASS | none |
| `c12` | `should_call` | Gợi ý việc làm freelance tương thích với CV. | `match_jobs_for_cv` | PASS | none |
| `c13` | `keyword_browse` | Tìm các dự án tuyển lập trình viên React. | `search_filter_projects` | PASS | none |
| `c14` | `keyword_browse` | Có dự án Python Django nào đang mở không? | `search_filter_projects` | PASS | none |
| `c15` | `keyword_browse` | Search for mobile app development freelance projects. | `search_filter_projects` | PASS | none |
| `c16` | `keyword_browse` | Tìm kiếm dự án thiết kế UI UX trên hệ thống. | `search_filter_projects` | PASS | none |
| `c17` | `keyword_browse` | Liệt kê các job liên quan đến DevOps Kubernetes. | `search_filter_projects` | PASS | none |
| `c18` | `keyword_browse` | Show me all backend developer freelance postings. | `search_filter_projects` | PASS | none |
| `c19` | `keyword_browse` | Tìm các dự án part-time thời gian dưới 4 tiếng. | `search_filter_projects` | PASS | none |
| `c20` | `keyword_browse` | Có công việc nào liên quan đến viết bài content SEO không? | `search_filter_projects` | PASS | none |
| `c21` | `no_tool` | Chào bạn, nền tảng Occupify hoạt động như thế nào? | `none` | PASS | none |
| `c22` | `no_tool` | Làm thế nào để viết một proposal thu hút khách hàng freelance? | `none` | PASS | none |
| `c23` | `no_tool` | What are good practices for pricing freelance software services? | `none` | PASS | none |
| `c24` | `no_tool` | Tôi nên chuẩn bị gì trước khi phỏng vấn với khách hàng freelance? | `none` | PASS | none |
| `c25` | `no_tool` | Kinh nghiệm làm freelancer khi mới bắt đầu cần lưu ý những gì? | `none` | PASS | none |
| `c26` | `no_tool` | How can I improve my developer portfolio to get more contracts? | `none` | PASS | none |
| `c27` | `need_cv` | Hãy tìm việc phù hợp với CV của tôi. | `match_jobs_for_cv` | PASS | none |
| `c28` | `need_cv` | Gợi ý công việc dựa trên hồ sơ lý lịch của mình. | `match_jobs_for_cv` | PASS | none |
| `c29` | `need_cv` | Match jobs to my CV please. | `match_jobs_for_cv` | PASS | none |
| `c30` | `need_cv` | Tìm các dự án phù hợp với kinh nghiệm trong CV của tôi nhé. | `match_jobs_for_cv` | PASS | none |
| `c31` | `criteria_exact` | Tìm việc cho CV này với ngân sách tối thiểu 15 triệu. | `match_jobs_for_cv` | PASS | none |
| `c32` | `criteria_exact` | Match my CV for fixed price projects only. | `match_jobs_for_cv` | PASS | none |
| `c33` | `criteria_exact` | Tìm công việc phù hợp CV với ngân sách từ 10 triệu đến 25 triệu. | `match_jobs_for_cv` | PASS | none |
| `c34` | `criteria_exact` | Gợi ý việc cho CV này với cấp độ chuyên gia EXPERT. | `match_jobs_for_cv` | PASS | none |
| `c35` | `criteria_exact` | Tìm job freelance cho CV làm việc bán thời gian dưới 4 tiếng một ngày. | `match_jobs_for_cv` | PASS | none |
| `c36` | `criteria_exact` | Tìm việc trả lương theo giờ HOURLY cho hồ sơ đính kèm. | `match_jobs_for_cv` | PASS | none |
| `c37` | `criteria_exact` | Match CV for projects with budget up to 30 million VND. | `match_jobs_for_cv` | PASS | none |
| `c38` | `criteria_exact` | Tìm dự án cấp độ mới vào nghề ENTRY phù hợp CV này. | `match_jobs_for_cv` | PASS | none |
| `c39` | `adversarial_cv` | Tìm việc cho CV này. | `match_jobs_for_cv` | PASS | none |
| `c40` | `adversarial_cv` | Match this CV against available projects. | `match_jobs_for_cv` | PASS | none |
