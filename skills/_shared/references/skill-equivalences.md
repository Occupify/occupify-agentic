# Skill Equivalences and Implication Rules

## 1. Exact Matches (weight 1.0)
Case and whitespace insensitive identical spelling:
- `React` <-> `React`
- `Docker` <-> `Docker`
- `Python` <-> `Python`

## 2. Equivalent Variations (weight 1.0)
Different spellings, acronyms, or standard framework notations for the exact same technology:
- `React` <-> `React.JS` <-> `ReactJS`
- `Node.js` <-> `NodeJS` <-> `Node`
- `PostgreSQL` <-> `Postgres`
- `TypeScript` <-> `TS`
- `JavaScript` <-> `JS`
- `Tailwind CSS` <-> `TailwindCSS`
- `Next.js` <-> `NextJS`
- `Vue.js` <-> `VueJS` <-> `Vue`
- `Golang` <-> `Go`
- `Amazon Web Services` <-> `AWS`
- `Google Cloud Platform` <-> `GCP`
- `Google Ads` <-> `Google AdWords`
- `Content writing` <-> `Copywriting`
- `Phân tích dữ liệu` <-> `Data analysis` <-> `Data Analytics`
- `Nhập liệu` <-> `Data entry`
- `Kế toán thuế` <-> `Tax accounting`
- `Kế toán` <-> `Accounting`
- `Quản trị hệ thống` <-> `System administration`
- `Phát triển web` <-> `Web development`

## 3. Implied Skills (weight 0.8)
Deep domain frameworks that inherently require or imply underlying platform or architectural skills:
- `Spring Boot` or `Spring Framework` implies `Java` and `Spring`
- `NestJS` implies `Node.js` and `TypeScript`
- `FastAPI` implies `Python` and `REST API`
- `Django` implies `Python` and `SQL`
- `Laravel` implies `PHP` and `MVC`
- `Express.js` implies `Node.js`
- `Redux` implies `React` and `JavaScript`
- `Next.js` implies `React` and `JavaScript`
- `Kubernetes` implies `Docker`
- `Ruby on Rails` implies `Ruby`
- `Flutter` implies `Dart`
- `ASP.NET Core` implies `.NET` and `C#`
- `Angular` implies `TypeScript`
- `Virtual assistant` implies `Data entry`
- `Tax accounting` implies `Accounting`

**Decision Rule:** Deep domain frameworks and specialized roles inherently imply their underlying languages, foundational platforms, and standard architectures (as listed above). However, base programming languages (e.g. Python, PHP, Java, C#) NEVER imply specific frameworks or tools.

## 4. STRICT Negative Pairs (NEVER Match or Imply!)
Under NO circumstances may the following technologies be marked as equivalent or implied:
- `Java` IS NOT `JavaScript` (and vice-versa)
- `React` IS NOT `React Native` (web vs mobile framework, and vice-versa)
- `Figma` IS NOT `Photoshop` (vector UI/UX vs raster image editor, and vice-versa)
- `C` IS NOT `C#` (and vice-versa)
- `C++` IS NOT `C#` (and vice-versa)
- `C` IS NOT `C++` (and vice-versa)
- `Angular` IS NOT `AngularJS` (breaking, completely incompatible frameworks, and vice-versa)
- `Python 2` IS NOT `Python 3` (major breaking version incompatibilities, and vice-versa)
- `Vue 2` IS NOT `Vue 3` (and vice-versa)
- `OAuth 1.0` IS NOT `OAuth 2.0` (incompatible protocol versions, and vice-versa)
- `Kafka` IS NOT `RabbitMQ` (different message broker architectures, and vice-versa)
- `AWS` IS NOT `Azure` or `GCP` (different cloud providers, never interchangeable)
- `Data Entry` / `Nhập liệu` IS NOT `Data Analysis` / `Phân tích dữ liệu` (clerical vs analytical)
- `Google Ads` IS NOT `Facebook Ads` (different advertising platforms, and vice-versa)
- `Technical writing` IS NOT `Creative writing` (analytical/engineering documentation vs fictional/creative narrative, and vice-versa)

## 5. STRICT One-Way Implications (NEVER Infer in Reverse!)
Frameworks imply core languages, but core languages NEVER imply specific frameworks or higher-level tools:
- `TypeScript` or `JavaScript` DOES NOT imply `Angular`, `React`, `Vue`, `NestJS` (verdict MUST be `missing`)
- `Python` DOES NOT imply `Django`, `FastAPI`, `Flask` (verdict MUST be `missing`)
- `PHP` DOES NOT imply `Laravel`, `Symfony` (verdict MUST be `missing`)
- `Node.js` DOES NOT imply `NestJS`, `Express.js` (verdict MUST be `missing`)
- `React` DOES NOT imply `Next.js`, `Redux` (verdict MUST be `missing`)
- `Java` DOES NOT imply `Spring Boot` (verdict MUST be `missing`)
- `C#` DOES NOT imply `ASP.NET Core` (verdict MUST be `missing`)
- `Dart` DOES NOT imply `Flutter` (verdict MUST be `missing`)
- `Ruby` DOES NOT imply `Ruby on Rails` (verdict MUST be `missing`)
- `Docker` DOES NOT imply `Kubernetes` (verdict MUST be `missing`)

