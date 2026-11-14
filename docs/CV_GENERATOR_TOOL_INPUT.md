# Contract JSON đầu vào cho CV Generator Tool

Tài liệu đề xuất cấu trúc JSON mà AI Agent gửi khi gọi tool `generate_cv` trong UC2 — CV–Job Description Matching & Improvement Agent. Đây là contract để triển khai; chưa phải mô tả một tool đã có trong code.

## 1. Phạm vi và luồng xử lý

```text
Người dùng cung cấp CV, JD và yêu cầu
  → Agent phân tích và chuẩn bị nội dung CV hoàn chỉnh
  → Agent gọi generate_cv bằng JSON theo tài liệu này
  → Tool kiểm tra cấu trúc dữ liệu
  → Tool ghép thông tin liên hệ từ context backend
  → Tool điền template LaTeX
  → Tool biên dịch và kiểm tra PDF
  → Tool upload .tex và .pdf lên Storage
  → Tool trả kết quả và thông tin tải file
  → Agent phản hồi người dùng
```

- **Agent chịu trách nhiệm nội dung:** chọn lọc thông tin theo JD, viết lại câu, sắp xếp mục và bảo đảm không tự tạo kinh nghiệm, kỹ năng, bằng cấp hoặc số liệu.
- **Tool chịu trách nhiệm tài liệu:** kiểm tra input, render template, compile PDF, kiểm tra giới hạn trang, upload và trả thông tin tải file. Tool không cần gọi thêm LLM.
- JSON chứa nội dung đã xử lý, không phải yêu cầu bằng ngôn ngữ tự nhiên gửi lại cho một agent khác.
- Không truyền JD, prompt, lời khuyên học thêm hoặc báo cáo matching vào nội dung CV.
- Không có `source_cv_ref`, `source_entry_id` hoặc `evidence_ids` trong contract này. Tool render không đọc lại CV gốc để kiểm chứng từng phát biểu.
- Thông tin xác thực, OCI bucket, object key, credentials, URL upload, đường dẫn template và lệnh compile do backend quản lý.

## 2. JSON đầy đủ

Ví dụ dưới đây sử dụng **dữ liệu giả lập**, không lấy thông tin cá nhân từ CV mẫu. Giá trị `classic` là ID template dự kiến, cần đăng ký với backend sau khi tích hợp source LaTeX.

```json
{
  "template_id": "classic",
  "language": "vi",
  "cv": {
    "headline": "Backend Developer",
    "summary": "Lập trình viên backend có kinh nghiệm xây dựng REST API bằng Spring Boot, làm việc với PostgreSQL và triển khai ứng dụng bằng container.",
    "skill_groups": [
      {
        "label": "Ngôn ngữ lập trình",
        "items": ["Java", "Python", "SQL"]
      },
      {
        "label": "Backend",
        "items": ["Spring Boot", "Spring Security", "REST API"]
      },
      {
        "label": "Cơ sở dữ liệu và triển khai",
        "items": ["PostgreSQL", "Redis", "Docker"]
      }
    ],
    "experience": [
      {
        "company": "Trung tâm Giáo dục Demo",
        "roles": ["Backend Developer", "DevOps Engineer"],
        "employment_type": "Freelance",
        "location": "TP. Hồ Chí Minh, Việt Nam",
        "start_date": "2025-06",
        "end_date": "2025-09",
        "is_current": false,
        "team_size": 4,
        "bullets": [
          "Phát triển REST API quản lý khóa học và tài khoản người dùng bằng Spring Boot.",
          "Triển khai phân quyền truy cập bằng Spring Security và JWT.",
          "Thiết lập pipeline CI/CD để tự động hóa build và triển khai ứng dụng."
        ]
      }
    ],
    "projects": [
      {
        "name": "Student Companion Demo",
        "roles": ["Backend Developer", "Team Leader"],
        "start_date": "2025-02",
        "end_date": "2025-05",
        "is_current": false,
        "team_size": 3,
        "technologies": ["Java", "Spring Boot", "PostgreSQL"],
        "bullets": [
          "Xây dựng API quản lý tài khoản và lưu trữ tài liệu học tập.",
          "Tích hợp tác vụ đồng bộ lịch học từ hệ thống bên ngoài."
        ]
      }
    ],
    "education": [
      {
        "institution": "Trường Đại học Demo",
        "degree": "Cử nhân",
        "major": "Kỹ thuật phần mềm",
        "location": "TP. Hồ Chí Minh, Việt Nam",
        "start_date": "2023",
        "end_date": "2027",
        "is_current": true,
        "is_expected": true,
        "gpa": "3.4/4.0",
        "highlights": [
          "Đồ án chuyên ngành về xây dựng hệ thống backend."
        ]
      }
    ],
    "certifications": [
      {
        "name": "Chứng chỉ ngoại ngữ Demo",
        "issuer": "Đơn vị Khảo thí Demo",
        "issued_date": "2025",
        "expiry_date": null,
        "result": "6.5"
      }
    ],
    "additional_sections": [
      {
        "title": "Thực hành kỹ thuật",
        "items": [
          {
            "label": "Kiến trúc",
            "text": "Áp dụng kiến trúc ba lớp và Repository Pattern."
          },
          {
            "label": "Quan sát hệ thống",
            "text": "Thiết lập metrics và dashboard bằng Prometheus, Grafana."
          }
        ]
      }
    ]
  }
}
```

## 3. Quy ước kiểu dữ liệu

| Ký hiệu | Ý nghĩa |
|---|---|
| `string` | Chuỗi văn bản thuần; tool chịu trách nhiệm escape LaTeX. |
| `string \| null` | Có thông tin thì dùng chuỗi không rỗng; chưa biết hoặc không có thì dùng `null`. |
| `boolean` | Giá trị JSON `true` hoặc `false`, không phải chuỗi `"true"`/`"false"`. |
| `integer \| null` | Số nguyên hoặc `null`; không truyền số dưới dạng chuỗi. |
| `array<string>` | Mảng chuỗi, ví dụ `["Java", "Python"]`. |
| `array<object>` | Mảng object theo schema tương ứng; không phải đoạn văn bản hoặc chuỗi JSON. |

**Quy tắc hiện diện trường:** mọi trường được liệt kê trong các bảng bên dưới đều phải có khi object tương ứng xuất hiện. Trường được phép thiếu giá trị sử dụng `null` hoặc `[]` theo kiểu dữ liệu. Không truyền trường ngoài contract.

**Chuỗi:** bỏ khoảng trắng đầu/cuối; chuỗi khác `null` phải có nội dung. Không dùng `"N/A"`, `"unknown"`, `"Đang cập nhật"` để thay cho dữ liệu thiếu.

**Ngày tháng:** dùng `YYYY` hoặc `YYYY-MM` theo độ chính xác nguồn cung cấp. Ví dụ chỉ biết năm thì gửi `"2025"`, không tự thêm tháng. Không truyền `"Present"`, `"Hiện tại"` hoặc `"Expected 2027"` vào trường ngày; tool trình bày dựa trên các cờ boolean.

## 4. Các trường cấp cao nhất

| Trường | Kiểu | Giá trị/ràng buộc | Cách tool sử dụng |
|---|---|---|---|
| `template_id` | `string` | ID nằm trong danh sách template đã đăng ký, ví dụ `classic`. | Chọn template được backend quản lý. Không diễn giải thành đường dẫn do agent cung cấp. |
| `language` | `string` | Enum `vi`, `en`. | Chọn nhãn section, cách hiển thị ngày và các từ như “Hiện tại”/“Present”. Tool không dịch nội dung. |
| `cv` | `object` | Object theo các mục bên dưới. | Nguồn nội dung để điền vào template. |

## 5. Object `cv`

| Trường | Kiểu | Giá trị/ràng buộc | Ý nghĩa |
|---|---|---|---|
| `headline` | `string \| null` | Chức danh hoặc định hướng nghề nghiệp ngắn; không nâng seniority khi thiếu bằng chứng. | Dòng định hướng nghề nghiệp dưới phần tên/liên hệ nếu template hỗ trợ. |
| `summary` | `string \| null` | Một đoạn giới thiệu ngắn đã viết hoàn chỉnh, không phải danh sách gợi ý. | Phần Summary/Professional Summary của CV. |
| `skill_groups` | `array<object>` | Không có thì `[]`; mỗi phần tử theo mục 6. | Các nhóm kỹ năng đã có của ứng viên. |
| `experience` | `array<object>` | Không có thì `[]`; mỗi phần tử theo mục 7. | Kinh nghiệm làm việc, thực tập hoặc freelance. |
| `projects` | `array<object>` | Không có thì `[]`; mỗi phần tử theo mục 8. | Dự án cá nhân, học tập hoặc dự án khác cần trình bày riêng. |
| `education` | `array<object>` | Không có thì `[]`; mỗi phần tử theo mục 9. | Học vấn và chương trình đào tạo. |
| `certifications` | `array<object>` | Không có thì `[]`; mỗi phần tử theo mục 10. | Chứng chỉ đã đạt; không chứa chứng chỉ dự định học. |
| `additional_sections` | `array<object>` | Không có thì `[]`; mỗi phần tử theo mục 11. | Các mục bổ sung như thực hành kỹ thuật, giải thưởng hoặc hoạt động. |

`summary` là **một chuỗi**; `skill_groups[].items` và các `bullets` là **mảng chuỗi**. Contract render này không dùng object `text`/`evidence_ids` của phương án trước.

## 6. Phần tử `cv.skill_groups[]`

| Trường | Kiểu | Giá trị/ràng buộc | Ý nghĩa |
|---|---|---|---|
| `label` | `string` | Tên nhóm không rỗng. | Ví dụ `Backend`, `Databases`, `Ngôn ngữ lập trình`. |
| `items` | `array<string>` | Ít nhất một kỹ năng; không có thì bỏ cả nhóm. | Từng kỹ năng riêng biệt; tool tự nối và xuống dòng. |

Không ghi “Cần học Kubernetes” trong `items`. Đây là kỹ năng cần bổ sung, thuộc phản hồi tư vấn của agent, không phải kỹ năng hiện có.

## 7. Phần tử `cv.experience[]`

| Trường | Kiểu | Giá trị/ràng buộc | Ý nghĩa |
|---|---|---|---|
| `company` | `string` | Tên tổ chức hoặc nhãn công việc có căn cứ; không tự tạo công ty. | Tên đơn vị nơi ứng viên làm việc. |
| `roles` | `array<string>` | Một hoặc nhiều chức danh theo nguồn; không nâng cấp vai trò. Không rõ thì `[]`. Chuỗi không rỗng, không trùng. | Ví dụ `["Backend Developer", "DevOps Engineer"]`; template nối các vai trò và cho phép xuống dòng. |
| `employment_type` | `string \| null` | Nhãn có trong nguồn như `Freelance`, `Internship`, `Full-time`. | Hình thức làm việc; ẩn khi `null`. |
| `location` | `string \| null` | Thành phố/quốc gia hoặc `Remote` nếu nguồn có. Không đưa địa chỉ nhà riêng. | Địa điểm làm việc. |
| `start_date` | `string \| null` | `YYYY` hoặc `YYYY-MM`. | Thời điểm bắt đầu. |
| `end_date` | `string \| null` | `YYYY` hoặc `YYYY-MM`; phải là `null` khi `is_current=true`. | Thời điểm kết thúc; `null` với `is_current=false` nghĩa là chưa biết ngày kết thúc. |
| `is_current` | `boolean` | `true` chỉ khi nguồn xác nhận đang làm; không suy ra từ ngày kết thúc bị thiếu. | Cho phép tool in “Hiện tại”/“Present”. |
| `team_size` | `integer \| null` | Số nguyên dương nếu biết; không tự ước lượng. | Quy mô nhóm; template có thể hiển thị cạnh vai trò. |
| `bullets` | `array<string>` | Ít nhất một câu có nội dung. | Mỗi chuỗi là một đóng góp/kết quả; không thêm ký tự bullet ở đầu. |

## 8. Phần tử `cv.projects[]`

| Trường | Kiểu | Giá trị/ràng buộc | Ý nghĩa |
|---|---|---|---|
| `name` | `string` | Tên dự án không rỗng. | Tiêu đề dự án. |
| `roles` | `array<string>` | Một hoặc nhiều vai trò thực tế; không rõ thì `[]`. Chuỗi không rỗng, không trùng. | Ví dụ `["Backend Developer", "Team Leader"]`; không nhận công lao của cả nhóm thành của cá nhân. |
| `start_date` | `string \| null` | `YYYY` hoặc `YYYY-MM`. | Ngày bắt đầu. |
| `end_date` | `string \| null` | `YYYY` hoặc `YYYY-MM`; `null` khi `is_current=true`. | Ngày kết thúc; có thể chưa rõ khi `is_current=false`. |
| `is_current` | `boolean` | `true` nếu nguồn xác nhận dự án đang được thực hiện. | Hiển thị trạng thái đang thực hiện. |
| `team_size` | `integer \| null` | Số nguyên dương hoặc `null`. | Số thành viên dự án. |
| `technologies` | `array<string>` | Không có thì `[]`; chỉ công nghệ có căn cứ từ dự án. | Stack sử dụng trong dự án. |
| `bullets` | `array<string>` | Ít nhất một câu. | Đóng góp, phạm vi công việc và kết quả có căn cứ. |

Contract phiên bản này không yêu cầu agent gửi URL GitHub/portfolio cá nhân. Nếu cần giữ các link từ CV gốc, backend phải ghép chúng từ dữ liệu cục bộ được phép sử dụng; cơ chế liên kết này cần được thiết kế khi triển khai, không để LLM đoán URL.

## 9. Phần tử `cv.education[]`

| Trường | Kiểu | Giá trị/ràng buộc | Ý nghĩa |
|---|---|---|---|
| `institution` | `string` | Tên cơ sở đào tạo không rỗng. | Tên trường hoặc tổ chức đào tạo. |
| `degree` | `string \| null` | Bậc/bằng theo nguồn. | Ví dụ `Cử nhân`, `Bachelor of Science`. |
| `major` | `string \| null` | Ngành/chuyên ngành theo nguồn. | Ví dụ `Kỹ thuật phần mềm`. |
| `location` | `string \| null` | Thành phố/quốc gia nếu có. | Địa điểm học. |
| `start_date` | `string \| null` | `YYYY` hoặc `YYYY-MM`. | Thời điểm bắt đầu chương trình. |
| `end_date` | `string \| null` | `YYYY` hoặc `YYYY-MM`. | Ngày hoàn thành hoặc ngày dự kiến hoàn thành nếu `is_expected=true`. |
| `is_current` | `boolean` | Chỉ `true` nếu nguồn xác nhận đang học. | Phân biệt học hiện tại và chương trình đã kết thúc. |
| `is_expected` | `boolean` | `true` yêu cầu có `end_date` và `is_current=true`. | Cho biết ngày kết thúc là dự kiến, không phải đã tốt nghiệp. |
| `gpa` | `string \| null` | Giữ cả thang điểm, ví dụ `3.4/4.0`; không tự đổi thang điểm. | Điểm trung bình nếu nguồn có và agent chọn đưa vào. |
| `highlights` | `array<string>` | Không có thì `[]`. | Thành tích, đồ án hoặc môn học liên quan có căn cứ. |

Khi `is_current=true`, `is_expected=true`, `end_date="2027"`, tool có thể in `2023 – Dự kiến 2027`. Khi đang học nhưng chưa biết ngày tốt nghiệp, dùng `end_date=null`, `is_expected=false`, `is_current=true`.

## 10. Phần tử `cv.certifications[]`

| Trường | Kiểu | Giá trị/ràng buộc | Ý nghĩa |
|---|---|---|---|
| `name` | `string` | Tên chứng chỉ không rỗng. | Ví dụ tên chứng chỉ ngoại ngữ hoặc chuyên môn đã đạt. |
| `issuer` | `string \| null` | Đơn vị cấp theo nguồn; không tự suy ra từ tên chứng chỉ. | Tổ chức cấp chứng chỉ. |
| `issued_date` | `string \| null` | `YYYY` hoặc `YYYY-MM`. | Thời điểm được cấp. |
| `expiry_date` | `string \| null` | `YYYY` hoặc `YYYY-MM`. | Ngày hết hạn nếu biết. `null` không khẳng định chứng chỉ vô thời hạn. |
| `result` | `string \| null` | Điểm/xếp loại nếu có, ví dụ `6.5`. | Kết quả chứng chỉ. |

Không truyền số định danh chứng chỉ hoặc đường dẫn tài liệu cá nhân qua LLM trong contract này. Nếu cần xuất, ghép cục bộ theo chính sách dữ liệu của backend.

## 11. Phần tử `cv.additional_sections[]`

| Trường | Kiểu | Giá trị/ràng buộc | Ý nghĩa |
|---|---|---|---|
| `title` | `string` | Tiêu đề không rỗng, cùng ngôn ngữ CV. | Ví dụ `Thực hành kỹ thuật`, `Giải thưởng`, `Hoạt động`. |
| `items` | `array<object>` | Ít nhất một phần tử theo bảng sau. | Các nội dung của section. |

### Phần tử `cv.additional_sections[].items[]`

| Trường | Kiểu | Giá trị/ràng buộc | Ý nghĩa |
|---|---|---|---|
| `label` | `string \| null` | Nhãn ngắn hoặc `null`. | Ví dụ `Kiến trúc`; tool có thể in đậm trước nội dung. |
| `text` | `string` | Nội dung không rỗng và có căn cứ. | Văn bản được xuất vào CV. |

Không dùng section mở rộng để nhúng chỉ dẫn cho tool, JD, đánh giá độ phù hợp hoặc kỹ năng chưa có. Không lặp lại nguyên phần Experience/Projects dưới một tiêu đề khác.

## 12. Thông tin cá nhân và context backend

Theo quy tắc dự án, tên, email, số điện thoại và thông tin liên hệ cá nhân không được gửi sang LLM ngoài hệ thống. Vì vậy input agent gửi **không có object `personal_info`**.

| Dữ liệu | Nguồn cung cấp | Xử lý |
|---|---|---|
| Tên hiển thị trên CV | Context backend hoặc biểu mẫu người dùng xác nhận. | Ghép vào template ở phía backend. Không dùng tên tài khoản làm tên CV nếu chưa có cơ sở. |
| Email, điện thoại, link cá nhân | Dữ liệu cục bộ được người dùng cung cấp/xác nhận. | Ghép cục bộ; không yêu cầu LLM khôi phục từ placeholder. |
| Chủ sở hữu artifact | User đã xác thực từ request/tool context. | Backend quyết định quyền upload/tải; không nhận `user_id` từ agent. |
| Bucket, object key, thời hạn link | Cấu hình và chính sách Storage của backend. | Không nằm trong input agent. |

Nếu backend chỉ giữ CV đã xóa PII thì **không thể tự khôi phục thông tin liên hệ**. Cần thu thập/xác nhận cục bộ trước khi xuất bản hoàn chỉnh. Header chỉ hiển thị trường đã có; thiếu tên cần trả trạng thái cần bổ sung thông tin. Đây là yêu cầu tích hợp, không phải khả năng đang có sẵn trong code.

Các chuỗi còn lại cũng phải qua chính sách privacy hiện có trước khi tới LLM; tên công ty, tên dự án hoặc bullet không được dùng để lách việc gửi PII.

## 13. Quy tắc render LaTeX và PDF

1. Toàn bộ chuỗi là văn bản thuần. Agent không gửi LaTeX, HTML hoặc Markdown để điều khiển bố cục. Xuống dòng và danh sách do template quản lý.
2. Tool escape ký tự đặc biệt như `&`, `%`, `$`, `#`, `_`, `{`, `}`, `~`, `^`, `\` trước khi điền template. Không diễn giải chúng thành lệnh LaTeX.
3. Mảng `[]` làm ẩn section; trường `null` làm ẩn thông tin tương ứng. Tool không tự thêm nội dung thiếu.
4. Tool giữ thứ tự phần tử trong mỗi mảng. Agent sắp xếp kinh nghiệm/dự án trước khi gọi; thứ tự section do template quản lý.
5. Cho phép tự ngắt thành **một hoặc hai trang A4**. Giới hạn hai trang thuộc backend, không phải trường input.
6. Nếu vượt hai trang, tool trả `content_too_long`. Agent rút gọn và gọi lại; tool không tự bỏ bullet hoặc liên tục thu nhỏ font.
7. Template, font và compiler do backend kiểm soát. Compile trong môi trường cách ly, có giới hạn thời gian/tài nguyên; không để nội dung đầu vào thực thi lệnh tùy ý.
8. Kiểm tra số trang, PDF đọc được và các cảnh báo bố cục. Compile thành công chưa đủ để khẳng định không tràn chữ hoặc thiếu glyph.
9. Nếu muốn người dùng tự compile `.tex`, file phải tự chứa các macro cần thiết, hoặc trả kèm bundle chứa class/style/font phụ thuộc và hướng dẫn compiler. Không trả riêng một file phụ thuộc các file chỉ tồn tại trên server.
10. Chỉ trả thành công toàn phần khi cả LaTeX và PDF đã được tạo, kiểm tra và upload thành công.

## 14. Kiểm tra input và nội dung

| Kiểm tra | Hành vi yêu cầu |
|---|---|
| Sai kiểu, thiếu key, key ngoài schema hoặc enum không hợp lệ | Trả lỗi theo đường dẫn trường, ví dụ `cv.projects[0].bullets`. |
| `template_id` chưa đăng ký | Trả lỗi template không hợp lệ; không tự thay bằng template khác. |
| Object danh sách không có trường định danh bắt buộc | Trả lỗi; không tự tạo tên công ty, trường học hoặc dự án. |
| Mảng chuỗi có chuỗi rỗng | Trả lỗi để agent sửa. |
| `experience[].roles` hoặc `projects[].roles` có vai trò trùng nhau | Trả lỗi để agent loại trùng. Giữ thứ tự vai trò; mảng `[]` làm ẩn dòng vai trò. |
| Ngày sai định dạng hoặc khoảng thời gian mâu thuẫn | Trả lỗi; chỉ so sánh theo độ chính xác nguồn, không tự bổ sung tháng. |
| `is_current=true` nhưng Experience/Project có `end_date` | Trả lỗi mâu thuẫn. Education dùng quy tắc dự kiến riêng. |
| `is_expected=true` nhưng thiếu ngày dự kiến hoặc không đang học | Trả lỗi mâu thuẫn. |
| `team_size` bằng 0, âm hoặc không phải số nguyên | Trả lỗi. |
| Không có nội dung nghề nghiệp/học vấn để tạo CV | Trả trạng thái cần bổ sung thông tin; không tạo tài liệu chỉ có header. |
| Text có ký tự LaTeX đặc biệt | Escape khi render; không yêu cầu agent tự escape trước. |
| PDF vượt hai trang | Trả `content_too_long`; chưa upload như một kết quả hoàn chỉnh. |
| Compile hoặc upload thất bại | Trả lỗi tương ứng; không trả link thành công giả. |

**Giới hạn trách nhiệm:** kiểm tra JSON và compile không chứng minh nội dung CV đúng sự thật. Yêu cầu không bịa phải được thực hiện trong bước agent chuẩn bị nội dung và kiểm chứng ở cấp ứng dụng. Các thiếu sót kỹ năng, câu hỏi cần xác nhận và giải thích chỉnh sửa nằm trong phản hồi tư vấn, không chèn vào CV như thành tích đã có.

## 15. JSON tối thiểu hợp lệ về nội dung

Một ứng viên chưa có kinh nghiệm hoặc chứng chỉ không cần tạo mục giả để lấp đầy template:

```json
{
  "template_id": "classic",
  "language": "vi",
  "cv": {
    "headline": "Ứng viên thực tập Backend",
    "summary": null,
    "skill_groups": [
      {
        "label": "Ngôn ngữ lập trình",
        "items": ["Java"]
      }
    ],
    "experience": [],
    "projects": [],
    "education": [],
    "certifications": [],
    "additional_sections": []
  }
}
```

Ví dụ này giả định kỹ năng Java có trong dữ liệu người dùng và backend đã có tên hiển thị được xác nhận. Các giới hạn kích thước payload, số mục và độ dài chuỗi phải được quy định khi triển khai để tránh input quá lớn; không phụ thuộc duy nhất vào giới hạn hai trang sau compile.
