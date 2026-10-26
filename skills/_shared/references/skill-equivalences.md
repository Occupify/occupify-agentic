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

## 3. Implied Skills (weight 0.8)
Deep domain frameworks that inherently require or imply underlying platform skills:
- `Spring Boot` or `Spring Framework` implies `Java`
- `NestJS` implies `Node.js` and `TypeScript`
- `FastAPI` or `Django` implies `Python`
- `Laravel` implies `PHP`
- `Express.js` implies `Node.js`
- `Redux` or `Next.js` implies `React`

**Decision Rule:** When uncertain between `implied` and `missing`, favor `implied`. It is better to show an inferred skill label than to miss a fitting job.

## 4. STRICT Negative Pairs (NEVER Match or Imply!)
Under NO circumstances may the following technologies be marked as equivalent or implied:
- `Java` IS NOT `JavaScript`
- `JavaScript` IS NOT `Java`
- `React` IS NOT `React Native` (web vs mobile framework)
- `React Native` IS NOT `React`
- `Figma` IS NOT `Photoshop` (vector UI/UX vs raster image editor)
- `C` IS NOT `C#`
- `C++` IS NOT `C#`
