# UC4 CV-Job Matching Evaluation Report (v2 / v3)

**Date:** 2026-10-27 13:59:22 UTC  
**Git Commit:** `0a948e9efdfffc2fcf8eae927360b3d6c8553eb6`  
**Overall Verdict:** 🟢 PASS  
**Mode:** Fresh run, no cache  

---

## 1. Executive Summary & Gates Table (Plan v3 §5 & §8.1)

| Gate / Scope | Metric | Target Threshold | Actual Result | Status |
| :--- | :--- | :--- | :--- | :--- |
| **G-1 (Match Personas)** | Hit@3 (worst of 3 runs) | ≥ 5/6 (0.833) | **1.000** (mean 1.000) | 🟢 PASS |
| **G-1 (Match Personas)** | nDCG@5 (gain = max job grade) | ≥ 0.750 | **0.978** (worst 0.974) | 🟢 PASS |
| **G-1 (Freshness)** | Closed projects / filled jobs returned | 0 | **0** | 🟢 PASS |
| **G-1 (CV-E Nurse)** | Outcome: `NO_MATCH`, status: `succeeded`/`partial` | yes | **yes** | 🟢 PASS |
| **G-1 (Privacy & Safety)** | PII sentinels or employer keys in requests | 0 | **0** | 🟢 PASS |
| **G-1 (CV-G Injection)** | p16 rank shift (clean vs injected) | ≤ 1 | **shift = 0** | 🟢 PASS |
| **G-2 / G-2+ (Synonyms)** | Synonym pairs marked missing | 0 | **0** | 🟢 PASS |
| **G-2 / G-2+ (Negatives)** | Negative partners matched non-missing | 0 | **0** | 🟢 PASS |
| **G-2 / G-2+ (Implied)** | Implied skill precision | ≥ 0.900 | **0.957** (22/23) | 🟢 PASS |
| **G-2 / G-2+ (Injection)** | Injected skill altering other verdicts | 0 | **0** | 🟢 PASS |
| **G-3 Scale Stress** | Hit@3 (30 personas × 2 repeats, PgJobIndex) | ≥ 0.800 | **1.000** | 🟢 PASS |
| **G-3 Scale Stress** | nDCG@10 (gain = silver label grade 0..3) | ≥ 0.700 | **0.742** | 🟢 PASS |
| **G-3 Scale Stress** | Recall@50 (grade ≥ 2 jobs in retrieval pool) | ≥ 0.900 | **0.912** | 🟢 PASS |
| **G-3 Scale Stress** | Hard negatives in top 3 | ≤ 1 | **0** | 🟢 PASS |
| **G-3 Scale Stress** | Closed projects / filled jobs returned | 0 | **0** | 🟢 PASS |
| **G-3 Scale Stress** | Injected project rank shift vs clean twin | ≤ 1 | **0** | 🟢 PASS |
| **G-3 Scale Stress** | Unexpected NO_MATCH outcomes | 0 | **0** | 🟢 PASS |
| **G-4 Layout & Robustness** | L-01..05 top 3 overlap with CV-A | ≥ 2 | **3/3** | 🟢 PASS |
| **G-4 Layout & Robustness** | L-07 top 3 overlap with CV-B | ≥ 2 | **3/3** | 🟢 PASS |
| **G-4 Layout & Robustness** | Non-scanned skill extraction recall | ≥ 0.800 | **0.920** | 🟢 PASS |
| **G-4 Layout & Robustness** | Injected CVs (X-01, X-02) rank shift | ≤ 1 | **0** | 🟢 PASS |
| **G-4 Layout & Robustness** | Verdict flips from injected instruction | 0 | **0** | 🟢 PASS |
| **G-4 Layout & Robustness** | Scanned PDFs (L-06, L-08) OCR handling | Report | **0 PII leaks reported** | 🟢 PASS |

---

## 2. Performance & Cost Telemetry

- **Latency (p50):** 81179.4 ms
- **Latency (p95):** 100395.0 ms
- **Mean Tokens In / Run:** 43173.6
- **Mean Tokens Out / Run:** 5720.6
- **Total Eval Run Cost:** $0.16429

---

## 3. Ablation Ladder (CV-A)

| Configuration | Hit@3 | nDCG@5 | Latency (ms) | Total Tokens |
| :--- | :--- | :--- | :--- | :--- |
| 1. Dense only | Yes | 1.000 | 69027 | 49925 |
| 2. + Lexical / RRF | Yes | 0.974 | 65461 | 48700 |
| 3. + Reranker | Yes | 0.983 | 81031 | 49602 |
| 4. + c/e (Full Core) | Yes | 1.000 | 75183 | 49208 |
| 5. + Forced Search Agent | Yes | 1.000 | 43011 | 19675 |
| 6. Plain Prompts | Yes | 1.000 | 77767 | 14010 |

---

## 4. Forced Search Agent Analysis

- **Options:** `PipelineOptions(list_size=8, pool_size=8, search_agent=True)`
- **Outcome Status:** `partial`
- **Returned Projects Count:** 7
- **Stop Reason:** `completed`

---

## 6. 50 Sampled Silver Labels (Human Reviewer Audit)

Sampled from `evals/uc4/data/labels_sample_50.yaml` for owner audit. Approval column is left empty for reviewer verification.

| # | Persona | Job ID | Job Title | Family | Seniority | Grade | Hard Neg? | Owner Verification |
|---|---|---|---|---|---|---|---|---|
| 1 | `x-01` | `g103-j03` | Expert Mobile Specialist | mobile | EXPERT | 1 | No | |
| 2 | `p-02` | `g121-j03` | Expert Backend Specialist | backend | EXPERT | 1 | No | |
| 3 | `cv-c` | `g272-j03` | Intermediate Frontend Specialist | frontend | INTERMEDIATE | 1 | No | |
| 4 | `l-01` | `g271-j02` | Entry Backend Specialist | backend | ENTRY | 1 | No | |
| 5 | `p-08` | `g281-j03` | Intermediate Backend Specialist | backend | INTERMEDIATE | 1 | No | |
| 6 | `p-04` | `g015-j03` | React Web Frontend Specialist | frontend | ENTRY | 1 | Yes | |
| 7 | `l-05` | `g201-j02` | Intermediate Backend Specialist | backend | INTERMEDIATE | 1 | No | |
| 8 | `x-02` | `g022-j03` | Intermediate Frontend Specialist | frontend | INTERMEDIATE | 1 | No | |
| 9 | `p-05` | `g227-j03` | Expert Ui Ux Specialist | ui_ux | EXPERT | 1 | No | |
| 10 | `p-11` | `g121-j02` | Entry Backend Specialist | backend | ENTRY | 1 | No | |
| 11 | `p-12` | `g265-j01` | Intermediate Devops Cloud Specialis | devops_cloud | INTERMEDIATE | 1 | No | |
| 12 | `x-01` | `g103-j01` | Entry Mobile Specialist | mobile | ENTRY | 1 | No | |
| 13 | `p-04` | `g025-j01` | Intermediate Devops Cloud Specialis | devops_cloud | INTERMEDIATE | 1 | No | |
| 14 | `cv-g` | `g147-j02` | Entry Ui Ux Specialist | ui_ux | ENTRY | 1 | No | |
| 15 | `l-03` | `g265-j02` | Intermediate Devops Cloud Specialis | devops_cloud | INTERMEDIATE | 1 | No | |
| 16 | `p-01` | `g022-j03` | Intermediate Frontend Specialist | frontend | INTERMEDIATE | 1 | No | |
| 17 | `p-07` | `g152-j02` | Intermediate Frontend Specialist | frontend | INTERMEDIATE | 1 | No | |
| 18 | `l-01` | `g192-j03` | Intermediate Frontend Specialist | frontend | INTERMEDIATE | 1 | No | |
| 19 | `l-01` | `g182-j04` | Intermediate Frontend Specialist | frontend | INTERMEDIATE | 1 | No | |
| 20 | `x-01` | `g267-j03` | Intermediate Ui Ux Specialist | ui_ux | INTERMEDIATE | 1 | No | |
| 21 | `cv-c` | `g025-j04` | Intermediate Devops Cloud Specialis | devops_cloud | INTERMEDIATE | 1 | No | |
| 22 | `p-09` | `g202-j02` | Intermediate Frontend Specialist | frontend | INTERMEDIATE | 1 | No | |
| 23 | `p-06` | `g118-j02` | Expert Marketing Content Specialist | marketing_content | EXPERT | 1 | No | |
| 24 | `p-01` | `g194-j03` | Expert Data Ai Specialist | data_ai | EXPERT | 1 | No | |
| 25 | `x-01` | `g142-j02` | Intermediate Frontend Specialist | frontend | INTERMEDIATE | 1 | No | |
| 26 | `l-05` | `g255-j03` | Expert Devops Cloud Specialist | devops_cloud | EXPERT | 1 | No | |
| 27 | `p-03` | `g244-j02` | Expert Data Ai Specialist | data_ai | EXPERT | 1 | No | |
| 28 | `l-05` | `g165-j03` | Expert Devops Cloud Specialist | devops_cloud | EXPERT | 1 | No | |
| 29 | `cv-d` | `g231-j03` | Intermediate Backend Specialist | backend | INTERMEDIATE | 1 | No | |
| 30 | `cv-d` | `g131-j02` | Intermediate Backend Specialist | backend | INTERMEDIATE | 1 | No | |
| 31 | `l-02` | `g154-j02` | Intermediate Data Ai Specialist | data_ai | INTERMEDIATE | 1 | No | |
| 32 | `l-02` | `g274-j04` | Entry Data Ai Specialist | data_ai | ENTRY | 1 | No | |
| 33 | `l-06` | `g274-j01` | Intermediate Data Ai Specialist | data_ai | INTERMEDIATE | 1 | No | |
| 34 | `l-04` | `g164-j02` | Entry Data Ai Specialist | data_ai | ENTRY | 1 | No | |
| 35 | `p-08` | `g021-j02` | Intermediate Backend Specialist | backend | INTERMEDIATE | 1 | No | |
| 36 | `x-01` | `g041-j01` | Expert Backend Specialist | backend | EXPERT | 1 | No | |
| 37 | `l-06` | `g015-j01` | Expert Devops Cloud Specialist | devops_cloud | EXPERT | 1 | No | |
| 38 | `l-08` | `g142-j02` | Intermediate Frontend Specialist | frontend | INTERMEDIATE | 1 | No | |
| 39 | `p-11` | `g231-j02` | Entry Backend Specialist | backend | ENTRY | 3 | No | |
| 40 | `p-10` | `g007-j04` | Backend Python Django | backend | EXPERT | 1 | Yes | |
| 41 | `l-07` | `g257-j04` | Intermediate Ui Ux Specialist | ui_ux | INTERMEDIATE | 1 | No | |
| 42 | `cv-a` | `g114-j01` | Intermediate Data Ai Specialist | data_ai | INTERMEDIATE | 1 | No | |
| 43 | `cv-d` | `g191-j01` | Expert Backend Specialist | backend | EXPERT | 1 | No | |
| 44 | `p-03` | `g201-j04` | Intermediate Backend Specialist | backend | INTERMEDIATE | 1 | No | |
| 45 | `l-05` | `g195-j03` | Entry Devops Cloud Specialist | devops_cloud | ENTRY | 1 | No | |
| 46 | `cv-h` | `g252-j02` | Entry Frontend Specialist | frontend | ENTRY | 3 | No | |
| 47 | `cv-a` | `g245-j01` | Entry Devops Cloud Specialist | devops_cloud | ENTRY | 1 | No | |
| 48 | `x-02` | `g102-j01` | Entry Frontend Specialist | frontend | ENTRY | 1 | No | |
| 49 | `cv-h` | `g167-j02` | Expert Ui Ux Specialist | ui_ux | EXPERT | 1 | No | |
| 50 | `x-01` | `g173-j03` | Entry Mobile Specialist | mobile | ENTRY | 1 | No | |

---

## 7. 30 Sampled Requirement Checks (Human Reviewer Audit)

Sampled from end-to-end evaluation runs across personas for human validation against CV evidence. Approval column is left empty for reviewer verification.

| # | Persona | Project Title | Job Title | Requirement Text | Extracted Evidence | Verdict | Owner Grade |
|---|---|---|---|---|---|---|---|
| 1 | `cv-a` | Phân tích dữ liệu bán hàng và dashb | Data Analyst (SQL & PowerBI) | Thành thạo SQL và DAX | ... | `unclear` | |
| 2 | `cv-a` | Ứng dụng giao đồ ăn React Native | React Native Developer | Đã phát hành ít nhất 1 app lên App Store/Google Play | ... | `not_met` | |
| 3 | `cv-b` | Thiết kế banner cho chiến dịch mark | Graphic Designer (Banner & Social) | Thành thạo Photoshop và Illustrator | ... | `not_met` | |
| 4 | `cv-c` | Data pipeline cho nền tảng quảng cá | Data Engineer | 4+ năm làm data engineering | ... | `not_met` | |
| 5 | `cv-c` | Dịch tài liệu kỹ thuật Anh - Việt | Biên dịch viên Anh - Việt (kỹ thuật) | IELTS 7.0 trở lên hoặc tương đương | ... | `unclear` | |
| 6 | `cv-d` | Phân tích dữ liệu bán hàng và dashb | Data Analyst (SQL & PowerBI) | Thành thạo SQL và DAX | ... | `not_met` | |
| 7 | `cv-f` | Trang quản trị (admin dashboard) ch | Frontend Developer (React/Next.js) | Nắm vững React hooks và TypeScript | ... | `unclear` | |
| 8 | `cv-g` | Dựng video cho kênh YouTube giáo dụ | Video Editor | Có portfolio video đã dựng | ... | `unclear` | |
| 9 | `cv-g` | Shopify store setup for a skincare  | Shopify Developer | At least 3 Shopify stores delivered | ... | `not_met` | |
| 10 | `cv-h` | Shopify store setup for a skincare  | Shopify Developer | At least 3 Shopify stores delivered | ... | `not_met` | |
| 11 | `cv-h` | Dịch tài liệu kỹ thuật Anh - Việt | Biên dịch viên Anh - Việt (kỹ thuật) | IELTS 7.0 trở lên hoặc tương đương | ... | `not_met` | |
| 12 | `cv-a` | Phân tích dữ liệu bán hàng và dashb | Data Analyst (SQL & PowerBI) | Thành thạo SQL và DAX | ... | `unclear` | |
| 13 | `cv-b` | Di chuyển hệ thống lên AWS | Cloud/DevOps Engineer (AWS) | Có chứng chỉ AWS Solutions Architect là lợi thế | ... | `not_met` | |
| 14 | `cv-b` | Ứng dụng giao đồ ăn React Native | React Native Developer | Kinh nghiệm tích hợp cổng thanh toán | ... | `unclear` | |
| 15 | `cv-c` | Data pipeline cho nền tảng quảng cá | Data Engineer | Kinh nghiệm xử lý dữ liệu quy mô hàng tỷ bản ghi | ... | `unclear` | |
| 16 | `cv-c` | Dịch tài liệu kỹ thuật Anh - Việt | Biên dịch viên Anh - Việt (kỹ thuật) | Đã dịch tài liệu công nghệ thông tin | ... | `not_met` | |
| 17 | `cv-d` | Thiết kế banner cho chiến dịch mark | Graphic Designer (Banner & Social) | Đảm bảo tiến độ bàn giao hàng tuần | ... | `unclear` | |
| 18 | `cv-f` | Shopify store setup for a skincare  | Shopify Developer | Experience with Shopify subscription apps | ... | `met` | |
| 19 | `cv-f` | Di chuyển hệ thống lên AWS | Cloud/DevOps Engineer (AWS) | Đã từng migration hệ thống production | ... | `not_met` | |
| 20 | `cv-g` | Phân tích dữ liệu bán hàng và dashb | Data Analyst (SQL & PowerBI) | Kinh nghiệm trình bày báo cáo cho cấp quản lý | ... | `not_met` | |
| 21 | `cv-h` | Trang quản trị (admin dashboard) ch | Frontend Developer (React/Next.js) | Biết chuyển thiết kế Figma thành giao diện responsive | ... | `unclear` | |
| 22 | `cv-h` | Kế toán dịch vụ cho doanh nghiệp nh | Kế toán tổng hợp | 2 năm kinh nghiệm kế toán tổng hợp | ... | `not_met` | |
| 23 | `cv-a` | Data pipeline cho nền tảng quảng cá | Data Engineer | Kinh nghiệm xử lý dữ liệu quy mô hàng tỷ bản ghi | ... | `unclear` | |
| 24 | `cv-b` | Trang quản trị (admin dashboard) ch | Frontend Developer (React/Next.js) | Biết chuyển thiết kế Figma thành giao diện responsive | ... | `not_met` | |
| 25 | `cv-c` | Phân tích dữ liệu bán hàng và dashb | Data Analyst (SQL & PowerBI) | Kinh nghiệm trình bày báo cáo cho cấp quản lý | ... | `unclear` | |
| 26 | `cv-c` | Kế toán dịch vụ cho doanh nghiệp nh | Kế toán tổng hợp | 2 năm kinh nghiệm kế toán tổng hợp | ... | `not_met` | |
| 27 | `cv-d` | Ứng dụng giao đồ ăn React Native | React Native Developer | Kinh nghiệm tích hợp cổng thanh toán | ... | `unclear` | |
| 28 | `cv-d` | Viết nội dung chuẩn SEO cho blog cô | SEO Copywriter | Hiểu biết cơ bản về SEO Onpage | ... | `not_met` | |
| 29 | `cv-f` | Data pipeline cho nền tảng quảng cá | Data Engineer | Kinh nghiệm xử lý dữ liệu quy mô hàng tỷ bản ghi | ... | `not_met` | |
| 30 | `cv-g` | Ứng dụng giao đồ ăn React Native | React Native Developer | Kinh nghiệm tích hợp cổng thanh toán | ... | `not_met` | |

---
*Report auto-generated by `evals/uc4/run_eval.py` at commit `0a948e9efdfffc2fcf8eae927360b3d6c8553eb6`.*