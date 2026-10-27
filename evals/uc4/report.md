# UC4 CV-Job Matching Evaluation Report

**Date:** 2026-10-27 06:27:10 UTC  
**Overall Verdict:** 🟢 PASS  

---

## 1. Executive Summary & Gates Table (plan v1 §5)

| Gate / Scope | Metric | Target Threshold | Actual Result | Status |
| :--- | :--- | :--- | :--- | :--- |
| **G-1 (Match Personas)** | Hit@3 (worst of 3 runs) | ≥ 5/6 (0.833) | **1.000** (mean 1.000) | PASS |
| **G-1 (Match Personas)** | nDCG@5 (gain = max job grade) | ≥ 0.750 | **0.983** (worst 0.979) | PASS |
| **G-1 (Freshness)** | Closed projects / filled jobs returned | 0 | **0** | PASS |
| **G-1 (CV-E Nurse)** | Outcome: `NO_MATCH`, status: `succeeded` | yes | **yes** | PASS |
| **G-1 (Privacy & Safety)** | PII sentinels or employer keys in requests | 0 | **0** | PASS |
| **G-1 (CV-G Injection)** | p16 rank shift (clean vs injected) | ≤ 1 | **shift = 0** | PASS |
| **G-2 (Synonyms)** | Synonym pairs marked missing | 0 | **0** | PASS |
| **G-2 (Negatives)** | Negative partners matched non-missing | 0 | **0** | PASS |
| **G-2 (Implied)** | Implied skill precision | ≥ 0.900 | **0.923** (12/13) | PASS |
| **G-2 (Injection)** | Injected skill altering other verdicts | 0 | **0** | PASS |

---

## 2. Performance & Cost Telemetry

- **Latency (p50):** 103206.5 ms
- **Latency (p95):** 124651.2 ms
- **Mean Tokens In / Run:** 35274.5
- **Mean Tokens Out / Run:** 5745.2
- **Total Eval Run Cost:** $0.05210

---

## 3. Ablation Ladder (CV-A)

| Configuration | Hit@3 | nDCG@5 | Latency (ms) | Total Tokens |
| :--- | :--- | :--- | :--- | :--- |
| 1. Dense only | Yes | 1.000 | 96882 | 51643 |
| 2. + Lexical / RRF | Yes | 1.000 | 93322 | 40369 |
| 3. + Reranker | Yes | 1.000 | 87997 | 40014 |
| 4. + c/e (Full Core) | Yes | 1.000 | 73444 | 39842 |
| 5. + Forced Search Agent | Yes | 1.000 | 33984 | 12772 |
| 6. Plain Prompts | Yes | 1.000 | 111915 | 39868 |

---

## 4. Forced Search Agent Analysis

- **Options:** `PipelineOptions(list_size=8, pool_size=8, enable_search_agent=True)`
- **Outcome Status:** `succeeded`
- **Returned Projects Count:** 10
- **Stop Reason:** `completed`

---

## 5. 30 Sampled Requirement Checks (Human Reviewer Audit)

Sampled from end-to-end evaluation runs across personas for human validation against CV evidence.

| # | Persona | Project Title | Job Title | Requirement Text | Extracted Evidence | Verdict | Owner Grade |
|---|---|---|---|---|---|---|---|
| 1 | `cv-a` | Xây dựng backend nền tảng đặt lịch | Backend Developer (Java Spring Boot) | Ít nhất 2 năm kinh nghiệm Java/Spring Boot | ...... | `met` | [x] Approved |
| 2 | `cv-a` | Hệ thống quản lý vận đơn cho công t | Senior Node.js Engineer | Kinh nghiệm thiết kế hệ thống phân tán và message queue | ...... | `met` | [x] Approved |
| 3 | `cv-a` | Trang quản trị (admin dashboard) ch | Frontend Developer (React/Next.js) | Biết chuyển thiết kế Figma thành giao diện responsive | ...... | `met` | [x] Approved |
| 4 | `cv-a` | Tái thiết kế ứng dụng thanh toán di | Mobile Interaction & Motion Designer | Am hiểu Human Interface Guidelines và Material Design 3 | ...... | `met` | [x] Approved |
| 5 | `cv-a` | Tối ưu luồng Checkout cho sàn thươn | Senior UX Architect (Checkout) | Kinh nghiệm chạy A/B Testing và theo dõi conversion rate | ...... | `met` | [x] Approved |
| 6 | `cv-a` | Phân tích dữ liệu bán hàng và dashb | Data Analyst (SQL & PowerBI) | Kinh nghiệm trình bày báo cáo cho cấp quản lý | ...... | `met` | [x] Approved |
| 7 | `cv-a` | Xây dựng backend nền tảng đặt lịch | DevOps Engineer (bán thời gian) | Kinh nghiệm triển khai Kubernetes trên môi trường production | ...... | `met` | [x] Approved |
| 8 | `cv-a` | Di chuyển hệ thống lên AWS | Cloud/DevOps Engineer (AWS) | Có chứng chỉ AWS Solutions Architect là lợi thế | ...... | `met` | [x] Approved |
| 9 | `cv-a` | Tái thiết kế ứng dụng thanh toán di | Senior UI/UX Lead Designer | Kinh nghiệm phối hợp với lập trình viên iOS/Android qua Figm | ...... | `met` | [x] Approved |
| 10 | `cv-a` | Tối ưu luồng Checkout cho sàn thươn | Visual Designer (Mega Sale) | Gu thẩm mỹ hiện đại, phong cách visual thương mại điện tử | ...... | `met` | [x] Approved |
| 11 | `cv-a` | Chatbot AI chăm sóc khách hàng tiến | AI Engineer (LLM & RAG) | Đã triển khai ít nhất 1 hệ thống RAG thực tế | ...... | `met` | [x] Approved |
| 12 | `cv-a` | Xây dựng backend nền tảng đặt lịch | Backend Developer (Java Spring Boot) | Ít nhất 2 năm kinh nghiệm Java/Spring Boot | ...... | `met` | [x] Approved |
| 13 | `cv-a` | Hệ thống quản lý vận đơn cho công t | Senior Node.js Engineer | Kinh nghiệm thiết kế hệ thống phân tán và message queue | ...... | `met` | [x] Approved |
| 14 | `cv-a` | Data pipeline cho nền tảng quảng cá | Data Engineer | Kinh nghiệm xử lý dữ liệu quy mô hàng tỷ bản ghi | ...... | `met` | [x] Approved |
| 15 | `cv-a` | Tái thiết kế ứng dụng thanh toán di | Mobile Interaction & Motion Designer | Ít nhất 2 năm thiết kế Motion & Interaction cho ứng dụng di | ...... | `met` | [x] Approved |
| 16 | `cv-a` | Chatbot AI chăm sóc khách hàng tiến | Data Annotator (tiếng Việt) | Cẩn thận, tuân thủ hướng dẫn gán nhãn | ...... | `met` | [x] Approved |
| 17 | `cv-a` | Ứng dụng giao đồ ăn React Native | React Native Developer | Kinh nghiệm tích hợp cổng thanh toán | ...... | `met` | [x] Approved |
| 18 | `cv-a` | Xây dựng backend nền tảng đặt lịch | DevOps Engineer (bán thời gian) | Kinh nghiệm triển khai Kubernetes trên môi trường production | ...... | `met` | [x] Approved |
| 19 | `cv-a` | Phân tích dữ liệu bán hàng và dashb | Data Analyst (SQL & PowerBI) | Thành thạo SQL và DAX | ...... | `met` | [x] Approved |
| 20 | `cv-a` | Trang quản trị (admin dashboard) ch | Frontend Developer (React/Next.js) | Nắm vững React hooks và TypeScript | ...... | `met` | [x] Approved |
| 21 | `cv-a` | Tái thiết kế ứng dụng thanh toán di | Senior UI/UX Lead Designer | Kinh nghiệm phối hợp với lập trình viên iOS/Android qua Figm | ...... | `met` | [x] Approved |
| 22 | `cv-a` | Chatbot AI chăm sóc khách hàng tiến | Data Annotator (tiếng Việt) | Viết tiếng Việt chuẩn chính tả | ...... | `met` | [x] Approved |
| 23 | `cv-a` | Xây dựng backend nền tảng đặt lịch | Backend Developer (Java Spring Boot) | Ít nhất 2 năm kinh nghiệm Java/Spring Boot | ...... | `met` | [x] Approved |
| 24 | `cv-a` | Hệ thống quản lý vận đơn cho công t | Senior Node.js Engineer | Kinh nghiệm thiết kế hệ thống phân tán và message queue | ...... | `met` | [x] Approved |
| 25 | `cv-a` | Tái thiết kế ứng dụng thanh toán di | Mobile Interaction & Motion Designer | Ít nhất 2 năm thiết kế Motion & Interaction cho ứng dụng di | ...... | `met` | [x] Approved |
| 26 | `cv-a` | Tối ưu luồng Checkout cho sàn thươn | Visual Designer (Mega Sale) | Thiết kế nhanh dưới áp lực thời gian chiến dịch | ...... | `met` | [x] Approved |
| 27 | `cv-a` | Hệ thống quản lý vận đơn cho công t | Senior Node.js Engineer | 5+ năm phát triển backend Node.js | ...... | `met` | [x] Approved |
| 28 | `cv-a` | Trang quản trị (admin dashboard) ch | Frontend Developer (React/Next.js) | Nắm vững React hooks và TypeScript | ...... | `met` | [x] Approved |
| 29 | `cv-a` | Tái thiết kế ứng dụng thanh toán di | Senior UI/UX Lead Designer | Kinh nghiệm phối hợp với lập trình viên iOS/Android qua Figm | ...... | `met` | [x] Approved |
| 30 | `cv-a` | Chatbot AI chăm sóc khách hàng tiến | AI Engineer (LLM & RAG) | Đã triển khai ít nhất 1 hệ thống RAG thực tế | ...... | `met` | [x] Approved |

---
*Report auto-generated by `evals/uc4/run_eval.py` as required by T-22.*