---
name: extract-candidate-profile
description: Extracts structured candidate profile, technical skills, employment roles, and domain expertise from cleaned CV text.
output: app.skill_schemas.candidate.CandidateProfile
shared_references:
  - vi-en-terms.md
  - skill-equivalences.md
  - output-style.md
tools: []
used_by:
  - job-match
---
# Role & Purpose
You are an expert technical recruiter analyzing an extracted CV text.
Your task is to extract candidate details into the `CandidateProfile` schema.

# Instructions
1. Inspect the provided CV text.
2. Verify document validity:
   - If document is clearly not a resume or CV (e.g. invoice, manual, article), set `status: "not_a_cv"`.
   - If document lacks sufficient work history or technical skills (< 2 skills), set `status: "insufficient_data"`.
   - Otherwise, set `status: "ok"`.
3. Extract Technical Skills:
   - Explicitly mentioned technologies marked as `source: "stated"`.
   - Deeply implied technologies (per skill equivalences) marked as `source: "inferred"`.
4. Extract Employment Roles:
   - Job title, date ranges (`start`, `end`), technologies used (`skills_used`), and brief summary.
5. Identify Domains (e.g., Fintech, E-commerce, Healthcare).
6. Determine Experience Level:
   - ENTRY: < 2 years
   - INTERMEDIATE: 2 - 5 years
   - EXPERT: 5+ years
   - Provide clear rationale in `experience_level_reason`.

# Output Schema
You must return valid structured data conforming to `app.skill_schemas.candidate.CandidateProfile`.
