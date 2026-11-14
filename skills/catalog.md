# Skills Catalog

Auto-generated catalog of all verified skills in the service.

| Skill Name | Version | Output Model | Tools | Description |
|---|---|---|---|---|
| `apply-cv-revisions` | `10105bb42460` | `app.skill_schemas.cv_improvement.ResumeData` | none | Applies approved and user-modified revisions to the CV, producing structured ResumeData for PDF rendering. |
| `assess-job-fit` | `19220757af3d` | `app.skill_schemas.matching.ProjectAssessment` | none | Assesses candidate fit against specific project job requirements and deliverables without calculating scores. |
| `extract-candidate-profile` | `0256e461c9d9` | `app.skill_schemas.candidate.CandidateProfile` | none | Extracts structured candidate profile, technical skills, employment roles, and domain expertise from cleaned CV text. |
| `match-skills` | `c62e3902a6c8` | `app.skill_schemas.matching.SkillMatchResult` | none | Matches candidate profile skills against required project job skills using exact, equivalent, and implied rules. |
| `plan-job-search` | `0b55b9e267ea` | `app.skill_schemas.search.SearchDecision` | search_more | Formulates search strategies and invokes search_more to find additional relevant opportunities when initial candidate fit is low. |
| `suggest-cv-improvements` | `68f03c3c81be` | `app.skill_schemas.cv_improvement.CvImprovementProposal` | none | Evaluates CV against JD, detects weak points (e.g., excessive CRUD cliches, lack of STAR metrics), and proposes concrete, structured improvement suggestions. |
