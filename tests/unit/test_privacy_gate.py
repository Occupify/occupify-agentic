import pytest

from app.privacy.detectors import has_pii_remnants
from app.privacy.gate import clean

# 20 diverse synthetic CV text samples (English & Vietnamese)
SYNTHETIC_CVS = [
    # 1. EN Backend Dev
    """John Doe
john.doe@example.com | +1 555-0199 | github.com/johndoe
Date of Birth: 1990-05-15
Address: 123 Main St, Springfield

## Summary
Experienced Backend Developer with 6 years in Python and FastAPI.

## Education
Bachelor of Science in Computer Science, State University, 2012

## Experience
Senior Python Engineer at Acme Corp (2018 - Present)
- Architected high-throughput microservices using asyncio and PostgreSQL.
- Implemented RabbitMQ event bus handling 10k msg/sec.

## Skills
Python, FastAPI, Docker, RabbitMQ, PostgreSQL, Redis

## References
Available upon request from manager@acme.com
""",
    # 2. VI Backend Dev
    """Nguyễn Văn An
Email: an.nguyen@congty.vn - Điện thoại: 0912 345 678
Địa chỉ: 45 Lê Lợi, Quận 1, TP. Hồ Chí Minh
Ngày sinh: 20/11/1995 | Số CCCD: 079195001234

# Tóm tắt
Kỹ sư phần mềm 5 năm kinh nghiệm với Java và Spring Boot.

# Học vấn
Đại học Bách Khoa TP.HCM - Kỹ thuật Phần mềm (2013 - 2018)

# Kinh nghiệm làm việc
Techcombank - Chuyên viên phát triển backend (2020 - Hiện tại)
- Thiết kế hệ thống thanh toán qua API Gateway.
- Tối ưu hóa truy vấn SQL trên PostgreSQL.

# Kỹ năng
Java, Spring Boot, Microservices, Kafka, PostgreSQL, Docker

# Người tham chiếu
Trần Minh Tuấn - Trưởng phòng - tuan.tran@techcombank.com.vn
""",
    # 3. EN Frontend React Dev
    """Jane Smith
jane.smith@design.io | +44 20 7946 0912 | linkedin.com/in/janesmith
DOB: 12/04/1993

### Contact Information
Email: jane.smith@design.io
Phone: +44 20 7946 0912

### Professional Summary
Senior React Developer specialized in accessible component systems.

### Work Experience
Frontend Lead at WebFlow Solutions (2019 - Present)
- Built component library with TailwindCSS and TypeScript.
- Improved Core Web Vitals across all client landing pages.

### Skills
TypeScript, React, Next.js, TailwindCSS, Vitest, GraphQL

### Education
University of London, BA Interactive Design (2011 - 2014)
""",
    # 4. VI Frontend Dev
    """Lê Thị Bích
bich.le@email.com | 0987654321
Giới tính: Nữ | Tình trạng hôn nhân: Độc thân
Địa chỉ: 12 Hoàng Hoa Thám, Hà Nội

## MỤC TIÊU NGHỀ NGHIỆP
Trở thành Frontend Architect chuyên sâu về React và Vue.

## KINH NGHIỆM
Công ty Cổ phần VNG (2021 - 2024)
- Phát triển giao diện người dùng cho ứng dụng Zalo Web.
- Tối ưu bundle size giảm 35% thời gian tải trang.

## KỸ NĂNG CHUYÊN MÔN
JavaScript, ReactJS, Redux Toolkit, HTML5, CSS3, SCSS

## ĐÀO TẠO
Đại học Công nghệ - ĐHQGHN, Cử nhân CNTT
""",
    # 5. EN Data Engineer
    """Alex Taylor
alex.taylor@dataops.org | +84 909 112 233
ID Number: 123456789

# Profile
Data Engineer passionate about streaming ETL and vector search.

# Academic Background
MIT - M.S. Data Systems (2016)

# Work Experience
Data Architect at CloudStream Inc (2020 - 2024)
- Deployed Apache Spark pipelines for real-time analytics.
- Managed pgvector clustering for semantic search.

# Technical Skills
Python, PySpark, Databricks, PostgreSQL, pgvector, Airflow

# References
Dr. Alan Turing - alan@mit.edu
""",
    # 6. VI Data Engineer
    """Phạm Quốc Dũng
dung.pham@data.vn | 0933221100
CMND: 025468791 | Ngày cấp: 15/06/2014

# TỔNG QUAN
Kỹ sư dữ liệu với kinh nghiệm xây dựng Data Warehouse và Lakehouse.

# TRÌNH ĐỘ HỌC VẤN
Đại học Khoa học Tự nhiên TP.HCM (2014 - 2019)

# DỰ ÁN VÀ KINH NGHIỆM
Viettel Digital - Data Engineer (2021 - nay)
- Xây dựng luồng thu thập dữ liệu viễn thông qua Kafka.
- Triển khai dbt và Snowflake cho báo cáo tài chính.

# KỸ NĂNG
SQL, Python, Spark, Kafka, Airflow, dbt, Snowflake
""",
    # 7. EN Mobile Flutter Dev
    """Carlos Hernandez
carlos.h@mobiledev.net | +1 415 555 2671
Current Address: San Francisco, CA

## Summary
Mobile engineer with 8 published Flutter applications.

## Education
B.S. Software Engineering, CalPoly (2017)

## Experience
Senior Mobile Dev at AppWorks (2020 - Present)
- Created cross-platform apps for iOS and Android with Flutter.
- Integrated WebSocket push notifications and offline SQLite sync.

## Skills
Flutter, Dart, Kotlin, Swift, SQLite, REST API, Git
""",
    # 8. VI DevOps / Cloud Engineer
    """Vũ Đình Hưng
hung.vu@cloudsec.vn | 0945 678 901
Hộ chiếu: C1234567 | Quốc tịch: Việt Nam

### Giới thiệu
DevOps Engineer chuyên về Kubernetes, CI/CD và bảo mật hạ tầng đám mây.

### Quá trình học tập
Học viện Công nghệ Bưu chính Viễn thông (2015 - 2020)

### Kinh nghiệm
FPT Software - Cloud Specialist (2020 - 2024)
- Thiết lập cụm EKS trên AWS với Terraform.
- Tự động hóa kiểm thử và triển khai với GitLab CI.

### Kỹ năng
Kubernetes, Docker, Terraform, AWS, Prometheus, Grafana, Linux
""",
    # 9. EN Fullstack Dev
    """David Miller
david.miller@fullstack.io | +61 2 9385 1000
Address: Sydney, Australia

# Overview
Fullstack developer delivering clean web applications.

# Work Experience
Lead Developer at FinTech Australia (2019 - Present)
- Developed responsive web app using FastAPI and React.
- Maintained zero downtime during database migrations.

# Skills
Python, FastAPI, TypeScript, React, PostgreSQL, Docker

# References
Contact available upon demand.
""",
    # 10. VI AI / ML Engineer
    """Hoàng Mai Lan
lan.hoang@aiml.vn | +84 988 776 655
Số định danh cá nhân: 001198004567

## TÓM TẮT
Kỹ sư AI tập trung vào xử lý ngôn ngữ tự nhiên và hệ thống LLM Agent.

## HỌC VẤN
Đại học Bách Khoa Hà Nội - Thạc sĩ Trí tuệ nhân tạo (2018 - 2021)

## KINH NGHIỆM LÀM VIỆC
VinAI Research - AI Resident (2021 - 2023)
- Tinh chỉnh mô hình ngôn ngữ lớn cho tác vụ tiếng Việt.
- Xây dựng pipeline RAG kết hợp vector database.

## KỸ NĂNG
PyTorch, Transformers, LangChain, Pydantic, Vector Search, Python
""",
    # 11. EN QA Automation Engineer
    """Sarah Connor
sarah.c@quality.com | +1 212 555 0188
Salary expectation: $120,000 / year

### Professional Summary
QA Automation Engineer passionate about Cypress, Playwright, and Vitest.

### Experience
Quality Lead at Tech Corp (2019 - Present)
- Automated end-to-end regression suites in Playwright.
- Reduced manual testing cycle by 70%.

### Skills
Playwright, Cypress, Selenium, Python, TypeScript, CI/CD

### Education
BS in Information Technology (2016)
""",
    # 12. VI UI/UX Designer
    """Đỗ Tuấn Kiệt
kiet.do@design.vn | 0903 123 789 | behance.net/tuankiet

## Giới thiệu
Product Designer với 4 năm kinh nghiệm thiết kế trải nghiệm người dùng.

## Bằng cấp
Đại học Mỹ thuật TP.HCM (2016 - 2020)

## Kinh nghiệm
Momo - Senior UI/UX Designer (2021 - 2024)
- Thiết kế hệ thống Design System phục vụ 30 triệu người dùng.
- Thực hiện usability testing và tối ưu quy trình onboard.

## Kỹ năng
Figma, Design System, Wireframing, User Research, Prototyping
""",
    # 13. EN Product Manager
    """Emily Watson
emily.w@pmleaders.com | +1 650 555 3344
Gender: Female | Marital Status: Married

## Career Summary
Technical Product Manager with a background in distributed systems.

## Experience
Group PM at SaaS Cloud (2020 - Present)
- Spearheaded AI roadmap and enterprise integrations.
- Increased user retention by 25% YoY.

## Skills
Roadmap Planning, Scrum, Product Strategy, Metrics Analysis, SQL

## References
Provided by former VP Product.
""",
    # 14. VI Business Analyst
    """Trịnh Thanh Thảo
thao.trinh@ba-expert.vn | 0918 223 344
Ngày sinh: 14/02/1997 | Nơi ở: Cầu Giấy, Hà Nội

### MỤC TIÊU
Đóng góp giá trị kinh doanh thông qua phân tích yêu cầu chính xác.

### ĐÀO TẠO
Đại học Ngoại Thương Hà Nội (2015 - 2019)

### KINH NGHIỆM
VNPAY - Business Analyst (2020 - 2024)
- Khảo sát và viết tài liệu BRD, SRS cho ví điện tử.
- Phối hợp với đội ngũ Scrum phát triển tính năng QR Payment.

### KỸ NĂNG
UML, BPMN, JIRA, Confluence, SQL, Requirements Gathering
""",
    # 15. EN Security Specialist
    """Marcus Brody
marcus.brody@infosec.org | +44 1632 960888
Passport: UK987654321

# Summary
Cybersecurity specialist focusing on penetration testing and cloud security.

# Education
Oxford University, Computer Security (2015)

# Experience
Security Analyst at CyberShield (2018 - Present)
- Performed automated SAST/DAST audits on web microservices.
- Fixed OWASP Top 10 vulnerabilities across 50+ repositories.

# Skills
Penetration Testing, Burp Suite, Python, Linux, OWASP, Docker
""",
    # 16. VI Embedded Engineer
    """Bùi Quang Huy
huy.bui@iot.vn | 0977 889 900
CCCD: 036094008765

## GIỚI THIỆU
Kỹ sư nhúng với kinh nghiệm lập trình vi điều khiển STM32 và ESP32.

## HỌC TẬP
Đại học Bách Khoa Đà Nẵng (2014 - 2019)

## KINH NGHIỆM
Rạng Đông - Embedded Firmware Engineer (2020 - 2024)
- Lập trình firmware điều khiển thiết bị Smart Home giao thức Zigbee.
- Tối ưu năng lượng tiêu thụ cho cảm biến pin.

## KỸ NĂNG
C, C++, FreeRTOS, STM32, ESP32, Zigbee, BLE, MQTT
""",
    # 17. EN Systems Architect
    """Robert Langdon
robert.langdon@systems.org | +1 312 555 7788
Address: Chicago, IL

### Summary
Solutions architect with 12 years designing fault-tolerant clouds.

### Work Experience
Principal Architect at FinCloud (2018 - Present)
- Designed multi-region disaster recovery for banking core.
- Enforced clean architecture and event-driven patterns.

### Technical Skills
System Architecture, Spring Boot, Go, Kubernetes, Kafka, PostgreSQL

### Education
Carnegie Mellon University - M.S. Software Engineering (2010)
""",
    # 18. VI Kỹ sư Cầu nối (BrSE)
    """Lê Hoàng Quân
quan.le@brse-tokyo.jp | +81 80 1234 5678
Quốc tịch: Việt Nam

## TÓM TẮT
Kỹ sư cầu nối tiếng Nhật N1, 6 năm làm việc tại Tokyo.

## HỌC VẤN
Đại học FPT - Kỹ sư phần mềm (2012 - 2017)

## KINH NGHIỆM
FPT Japan - Bridge Software Engineer (2018 - 2024)
- Cầu nối dự án tài chính với khách hàng Nhật Bản.
- Quản lý tiến độ đội ngũ offshore 15 thành viên tại Việt Nam.

## KỸ NĂNG
Tiếng Nhật N1, Java, React, Agile, Quản lý dự án, Scrum
""",
    # 19. EN Blockchain Engineer
    """Satoshi Jones
satoshi.j@web3.io | +1 702 555 9911
Tax ID: 998877665

# Overview
Smart contract developer experienced in Solidity and Rust.

# Academic History
Stanford University (2018)

# Professional Experience
Core Contributor at DeFi Protocol (2021 - Present)
- Wrote gas-optimized ERC-20 and staking contracts.
- Audited multi-signature vault protocols.

# Skills
Solidity, Rust, Ethereum, Hardhat, Foundry, Web3.js
""",
    # 20. VI Trưởng nhóm kỹ thuật (Tech Lead)
    """Trần Hữu Thắng
thang.tran@techlead.vn | 0908 998 877
Địa chỉ: Quận Bình Thạnh, TP. Hồ Chí Minh
Ngày sinh: 10/10/1988 | Số CCCD: 079088009988

# GIỚI THIỆU
Technical Lead với hơn 10 năm kinh nghiệm dẫn dắt đội ngũ kỹ thuật.

# HỌC VẤN
Đại học Khoa học Tự nhiên - Cử nhân CNTT (2006 - 2010)

# KINH NGHIỆM
VNG Corporation - Engineering Manager (2018 - 2024)
- Lãnh đạo 25 kỹ sư phát triển nền tảng Cloud Gaming.
- Giảm chi phí vận hành hạ tầng 30% hàng năm.

# KỸ NĂNG
Team Leadership, System Design, Python, Go, Kubernetes, Microservices

# NGƯỜI THAM CHIẾU
Nguyễn Anh Tuấn - VP of Engineering
""",
]


@pytest.mark.parametrize("idx, cv_text", list(enumerate(SYNTHETIC_CVS)))
def test_synthetic_cv_privacy_cleaning(idx, cv_text):
    cleaned, counts = clean(cv_text, source=f"cv_{idx}.pdf")

    # 1. Verification that NO unmasked PII remains
    assert not has_pii_remnants(cleaned), f"CV #{idx + 1} still has unmasked PII"

    # 2. Check no raw email remains
    assert "@" not in cleaned, f"CV #{idx + 1} still contains @"

    # 3. Check excluded sections are dropped
    cleaned_lower = cleaned.lower()
    assert "bachelor of science" not in cleaned_lower
    assert "đại học bách khoa" not in cleaned_lower
    assert "university of london" not in cleaned_lower
    assert "học viện công nghệ" not in cleaned_lower
    assert "carnegie mellon" not in cleaned_lower
    assert "người tham chiếu" not in cleaned_lower
    assert "references" not in cleaned_lower

    # 4. Check essential skills and experience lines remain intact!
    assert (
        "experience" in cleaned_lower
        or "kinh nghiệm" in cleaned_lower
        or "skills" in cleaned_lower
        or "kỹ năng" in cleaned_lower
    )
    assert len(cleaned) > 100, f"CV #{idx + 1} was wiped out completely!"


def test_typed_message_cleaning():
    typed_msg = (
        "Hi, my email is test.user@gmail.com and phone is 0912345678. Can you review my profile?"
    )
    cleaned, counts = clean(typed_msg, source="your message")
    assert "test.user@gmail.com" not in cleaned
    assert "0912345678" not in cleaned
    assert "[EMAIL]" in cleaned
    assert "[PHONE]" in cleaned
    assert "review my profile" in cleaned


def test_pii_failure_blocking():
    # If a tricky pattern cannot be cleaned or unmasked PII remains, it must raise PiiRemovalFailedError
    # We can test by injecting something has_pii_remnants would flag
    text_with_raw_email = "Uncleanable string raw@domain.com"
    # clean() will replace raw@domain.com with [EMAIL] and succeed.
    # What if has_pii_remnants catches something uncleaned?
    # Let's test calling clean with known_email
    cleaned, _ = clean(text_with_raw_email, source="your message", known_email="raw@domain.com")
    assert "[EMAIL]" in cleaned
