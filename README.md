# Ontology-Driven Hybrid Recommendation Framework for Programming Education

A formally validated, ontology-driven hybrid recommender framework for programming education, extending the GitHub Classroom / BookWidgets knowledge-graph infrastructure of Namsraidorj, Namsraidorj & Enkhtur (2025) with a validated OWL 2 ontology, a rule-based + content-based + collaborative hybrid recommendation engine, and a real-data proof-of-concept implementation.

> **Status:** Ontology repaired and re-verified against real data (11,506 individuals). Recommendation algorithm and evaluation protocol specified in the paper; offline ranking (Track A) and TAM human evaluation (Track C) are scoped as future work — see [Section 9](#whats-not-yet-done).

---

## Overview

Prior work (Namsraidorj, Namsraidorj & Enkhtur, 2025) combined Google Classroom, Microsoft Teams, GitHub Classroom, and BookWidgets into a low-cost e-learning stack and modeled course syllabi, Bloom–Anderson learning objectives, and tool-level achievement as an OWL 2 knowledge graph — but stopped short of an actual recommender: no recommendation algorithm, no formal ontology validation, and no baseline comparison.

This project closes that gap by contributing:

1. **An extended ontology** — five new classes (`Learner`, `LearnerProfile`, `AchievementRecord`, `RecommendationStrategy`, `Recommendation`) added to the original 8, plus an explicit, normalized reformulation of the `SIL(n,m,k)` achievement construct.
2. **A validation protocol** — competency-question SPARQL testing, HermiT/Pellet consistency checking, OOPS! pitfall scanning, and OntoQA schema/instance metrics benchmarked against four prior curriculum ontologies.
3. **A hybrid recommendation algorithm** — SWRL/rule-based reasoning over the knowledge graph fused with content-based and collaborative filtering, diversified via Maximal Marginal Relevance re-ranking.
4. **A pre-registered, three-track evaluation protocol** — offline ranking metrics with named baselines (Track A), ontology validation (Track B), and a Technology Acceptance Model human study with significance testing (Track C).

The framework is positioned against **EduCOR**, **PEARL**, and recent knowledge-graph/LLM-augmented educational recommenders, with explicit limitations and threats to validity.

---

## Repository Structure

```
.
├── paper_with_realdata_section.md         # Full paper (Sections 1–7, incl. 7.5 real-data POC)
├── Real_Data_Implementation_Report.md     # Real-data implementation log & results
├── build_ontology_v2_repaired.py          # Ontology build script (owlready2)
├── extended_ontology_v2_repaired.owl      # Populated OWL 2 ontology (11,506 individuals)
└── ontoqa_metrics_v2.json                 # Computed OntoQA schema/instance metrics
```

---

## Ontology

The ontology is built programmatically with [`owlready2`](https://owlready2.readthedocs.io/) in `build_ontology_v2_repaired.py` and populated with two real, non-linked datasets:

- **Objectives layer:** Devane (2024), *Bloom's Taxonomy Dataset* (Kaggle) — 8,767 human-classified questions.
- **Learner/Achievement layer:** Kuzilek, Hlosta & Zdrahal (2017), *Open University Learning Analytics Dataset* (OULAD), module `AAA_2013J` — 383 real learners, 1,631 graded submissions.

| Metric | Value |
|---|---|
| Classes | 14 (8 original + 5 extension + 1 implementation-support) |
| Object properties | 34 (17 forward + 17 declared inverses) |
| Data properties | 9 |
| Individuals | 11,506 |
| Relationship richness | 1.0 |
| Attribute richness | 0.643 |
| Inheritance richness | 0.0 (flat extension — see notes below) |
| Reasoner (HermiT) | Consistent, 0 unsatisfiable classes, 7.1s |

Full metrics: [`ontoqa_metrics_v2.json`](./ontoqa_metrics_v2.json).

### OOPS! Pitfall Scan & Repair

The schema was submitted to the live [OOPS!](https://oops.linkeddata.es/) scanner. Four pitfalls were found — **zero critical** — and all were repaired in `v2`:

| Pitfall | Severity | Fix |
|---|---|---|
| P10 — Missing disjointness | Important | Pairwise `owl:disjointWith` across all 14 core classes |
| P08 — Missing annotations | Minor | `rdfs:comment` added to all 57 schema elements |
| P13 — Inverse relationships not declared | Minor | `owl:inverseOf` declared for all 17 object properties |
| P36 — URI contains file extension | Minor | Base IRI changed to `.../ontology-hybrid-recsys#` |

HermiT was re-run on the full repaired graph after adding disjointness axioms (a change that can surface latent inconsistencies) — **still consistent**.

### Running the build script

```bash
pip install owlready2 pandas
python build_ontology_v2_repaired.py
```

Loads directly into [Protégé](https://protege.stanford.edu/) 5.x.

---

## Real-Data Proof of Concept

`Real_Data_Implementation_Report.md` documents a genuine, at-scale execution of the ontology and validation pipeline — **not** the paper's target Track A/B/C evaluation (that requires the 120-learner GitHub Classroom/BookWidgets population from the original paper). Highlights:

- **4 competency questions (CQ1–CQ4)** answered with real SPARQL queries over real data (e.g., 59 of 358 learners below threshold θ on TMA01).
- **318 real, rule-triggered recommendations** generated from `RuleBased_ThresholdTrigger`.
- **Descriptive validity check:** rule-trigger rate rises monotonically with worse real course outcomes (Distinction 0.0% → Fail 68.9%, n = 383) — encouraging but correlational, not causal.

See the full report for methodology, caveats, and what this proof-of-concept does and does not establish.

---

## What's Not Yet Done

- **Track A (Precision@K / Recall@K / NDCG@K):** needs a temporally split interaction log; OULAD's `vle.csv` clickstream data could support a future proxy version.
- **Track C (TAM human evaluation):** needs a live learner population using the deployed recommender.
- **Content-based/collaborative fusion:** scoped as a substantial follow-up modeling task using OULAD clickstream data.

---

## Citation

If you use this work, please cite the paper (full reference list in `paper_with_realdata_section.md`) and the underlying datasets:

- Devane, V. (2024). *Bloom's Taxonomy Dataset* [Data set]. Kaggle. https://www.kaggle.com/datasets/vijaydevane/blooms-taxonomy-dataset
- Kuzilek, J., Hlosta, M., & Zdrahal, Z. (2017). Open University Learning Analytics dataset. *Scientific Data*, 4, 170171. https://doi.org/10.1038/sdata.2017.171
- Namsraidorj, Namsraidorj, & Enkhtur (2025). *Ontology Based Recommendation System Using GitHub Classroom and BookWidget.*

## Authors

K.O. Oluborode¹, Shaphat Safethon², Manuyi Godfrey³ — Modibbo Adama University, Yola

## License

Add a license (e.g., MIT, CC-BY-4.0) appropriate for your intended use before publishing.
