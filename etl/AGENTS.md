# AGENTS.md

## 🎯 Objective

Build a **statistical ETL pipeline in Python** based on **JSON input data**, with a strong focus on:

- data cleaning and preparation,
- **descriptive and inferential statistics**,
- structured analytical reasoning,

while respecting:
- **SOLID principles**,
- a **light Clean Architecture**,
- the existing repository guidelines.

This project is **statistics-first**, not machine learning.

---

## 🧠 Global Instructions for the Agent

- Language: **Python**
- Avoid ML frameworks and models
- Allowed libraries: `json`, `pandas`, `numpy`, `scipy.stats` (optional)
- Prioritize **statistical correctness and clarity**
- Prefer explicit computations over abstractions
- Keep code understandable by a **data analyst / statistics student**

---

## 🧱 Expected Project Structure

Follow the repository structure exactly:

```

src/
├── extract/
│   └── json_reader.py
├── transform/
│   └── clean_data.py
├── load/
│   ├── descriptive_stats.py
│   └── inferential_stats.py
├── pipelines/
│   └── stats_pipeline.py
│
tests/
├── extract/
├── transform/
├── load/
│
data/
└── input.json

```

Do not add layers or folders beyond this.

---

## 🔑 Responsibilities by Layer

### Extract (`src/extract/`)
**Goal:** Load raw observations.

- Read JSON files
- Validate basic schema (presence of required fields)
- Return raw Python objects (`list[dict]`)

❌ No cleaning  
❌ No statistics  

---

### Transform (`src/transform/`)
**Goal:** Make data statistically usable.

- Remove invalid observations (`null`, incoherent values)
- Enforce correct types (`str → float`, `int`)
- Apply explicit statistical assumptions:
  - exclusion rules
  - value bounds
- Return a **clean numerical dataset**

➡️ Decisions here must be **documented and deterministic**

---

### Load / Analyze (`src/load/`)

#### `descriptive_stats.py`
**Goal:** Describe the data.

Required statistics:
- mean
- median
- variance
- standard deviation
- min / max
- counts per group

All computations must be:
- explicit
- reproducible
- unit-tested

---

#### `inferential_stats.py`
**Goal:** Compare and validate hypotheses.

Allowed analyses:
- group mean comparison
- pooled vs non-pooled variance
- simple statistical tests (e.g. t-test)
- confidence intervals (if relevant)

❌ No ML
❌ No black-box models

---

### Pipeline (`src/pipelines/`)
**Goal:** Orchestrate the statistical workflow.

- Call extract → transform → descriptive → inferential
- Keep execution linear and readable
- No computation logic inside the pipeline

➡️ The pipeline expresses **statistical reasoning**, not implementation detail.

---

## 🧩 Statistical Principles to Respect

- Always distinguish:
  - **descriptive statistics** (what is observed)
  - **inferential statistics** (what is concluded)
- Explicitly state assumptions:
  - independence
  - sample size limitations
  - distribution shape (if assumed)
- Never imply causality without experimental design
- Prefer effect sizes over raw significance

---

## 🧩 SOLID Principles (Applied to Statistics)

- **S**: Each file handles one statistical responsibility
- **O**: New statistics can be added without modifying existing ones
- **L**: Statistical modules can be replaced independently
- **I**: Separate descriptive and inferential concerns
- **D**: Pipelines depend on statistical interfaces, not implementations

---

## 📊 Input Data Expectations

Input data must:
- contain multiple numerical variables,
- include a grouping variable (for comparison),
- allow missing or invalid values to justify cleaning,
- support hypothesis testing.

---

## 📈 Expected Statistical Outputs

At minimum:
- global descriptive statistics
- group-level statistics
- comparison of group means
- interpretation of observed differences

Outputs must be:
- numeric
- interpretable
- traceable to input data

---

## 🧪 Testing Expectations

- Unit tests per statistical function
- Test edge cases:
  - empty data
  - single observation
  - identical values
- Numerical tolerances must be explicit

---

## ❌ What to Avoid

- Machine learning terminology
- Predictive language
- Over-abstraction
- Hidden statistical assumptions
- Silent data exclusion

---

## ✅ Expected Outcome

A **statistically rigorous ETL example** that demonstrates:
- clean separation of concerns,
- sound statistical reasoning,
- disciplined code structure,
- explicit assumptions and limitations.

This repository should read like a **statistical analysis pipeline**, not a data engineering demo.

---

## 📝 Optional Bonus (Only if Simple)

- A short markdown explaining:
  - hypotheses tested
  - assumptions
  - interpretation limits
- One statistical test implemented twice (manual + library) for comparison
