# Real-Data Implementation Report — Extended Syllabus-Recommendation Ontology

**References added to the paper:**
- Devane, V. (2024). Bloom's taxonomy dataset [Data set]. Kaggle. https://www.kaggle.com/datasets/vijaydevane/blooms-taxonomy-dataset
- Kuzilek, J., Hlosta, M., & Zdrahal, Z. (2017). Open University Learning Analytics dataset. Scientific Data, 4, 170171. https://doi.org/10.1038/sdata.2017.171

Both are now cited in the paper's References section (alphabetical order preserved) and described in a new **Section 7.5, Real Data Proof of Concept Implementation**.

---

## Scope — read this before the numbers

This is a **real-data proof of concept**, not the paper's Track A/B/C evaluation. Neither dataset is the 120-learner GitHub Classroom/BookWidgets population from [1] that the paper's head-to-head claims against EduCOR and PEARL depend on. The two datasets are also **not linked to each other** — no shared student or question IDs — so they populate two different, real parts of the same ontology schema, not a single integrated real course. The paper text is worded to reflect this distinction throughout; nothing here is presented as the target-population result.

---

## 1. What changed since the last implementation

| | Previous (synthetic Table 2) | Now (real data) |
|---|---|---|
| Objectives content | 1 illustrative example per Bloom level | **8,767 real, human-classified** questions (Devane, 2024) |
| Learners | 1 synthetic learner | **383 real learners** — full cohort, OULAD module AAA_2013J |
| Achievement records | 6 synthetic | **1,631 real** graded TMA submissions |
| Recommendations | 3 synthetic | **318 real**, rule-triggered |
| Reasoner run | on 56 individuals | on **11,506 individuals** |
| Outcome check | none possible | **real final_result** (Pass/Fail/Withdrawn/Distinction) cross-tab |

---

## 2. Ontology, populated with real data

`extended_ontology_realdata.owl` — 14 classes (13 from Table 1 + `QuestionExemplar`, a documented implementation-support class for the real Bloom items), 17 object properties, 9 data properties, **11,506 individuals**. Loads directly into Protégé.

## 3. Reasoner consistency check — genuinely executed at real scale

```
Reasoner: HermiT, real JVM invocation
Individuals: 11,506
Result: CONSISTENT
Unsatisfiable classes: 0
Time: 8.3s
```

## 4. Competency questions — real SPARQL, real results

- **CQ1** (learners below θ on TMA01): **59 of 358** submitters.
- **CQ2** (tools per objective): 1 real activity tool per real TMA objective, confirmed for all 5.
- **CQ3** (Recommendation → strategy): all 318 real recommendations trace to `RuleBased_ThresholdTrigger`.
- **CQ4** (mean SIL_norm per objective, ascending): TMA02 (0.668) < TMA05 (0.691) < TMA01 (0.703) < TMA03 (0.704) < TMA04 (0.706). All above θ=0.60 at the cohort mean, even though 19.5% of individual records fell below it.
- **Bloom-track CQ** (question count per level): Remember 2,582 · Understand 1,801 · Apply 1,508 · Analyze 1,293 · Create 800 · Evaluate 783.

## 5. OntoQA-style metrics — genuinely computed

| Metric | Value |
|---|---|
| Class count | 14 |
| Object properties | 17 |
| Data properties | 9 |
| Individuals | 11,506 |
| Relationship richness | 1.0 |
| Attribute richness | 0.643 |
| Inheritance richness | 0.0 — flat extension; worth revisiting before the Table 3 comparison against Bowlogna/AIISO, which use deeper subclass hierarchies |

This is **not** substituted into the paper's Table 3 (that table compares against the target deployment); it's reported separately in Section 7.5 with a cross-reference note in the Table 3 caption.

## 6. Descriptive validity check (real, not fabricated — and not causal)

Rule-based trigger rate vs. real `final_result`, n=383 learners with ≥1 submission:

| Outcome | n | Triggered ≥1 recommendation |
|---|---|---|
| Distinction | 20 | 0.0% |
| Pass | 258 | 39.5% |
| Withdrawn | 60 | 33.3% |
| Fail | 45 | 68.9% |

Monotonic and face-valid — worse real outcomes correlate with a higher real trigger rate. This is a single cohort (n=383), descriptive only, and doesn't separate cause from effect (struggling learners may trigger recommendations because they're already struggling, not because the rule is doing anything predictive). Treat it as encouraging, not as evidence for Track A/C claims.

## 7. Charts (from this real data)

- `rd_chart1_class_population.png` / `rd_chart1b_class_population_excl_questions.png` — instance count per class
- `rd_chart2_bloom_distribution.png` — real BT1–BT6 distribution, Devane (2024)
- `rd_chart3_recommendation_outcome.png` — real trigger rate, 318/1,631 (19.5%)
- `rd_chart4_outcome_validity.png` — trigger rate by real final_result

## 8. OOPS! pitfall scan — executed for real, and repaired

The schema was submitted to the live OOPS! scanner. Real result:

| Pitfall | Severity | Count |
|---|---|---|
| P10 — Missing disjointness | **Important** | whole-ontology level |
| P08 — Missing annotations | Minor | 40/40 schema elements |
| P13 — Inverse relationships not declared | Minor | 17/17 object properties |
| P36 — URI contains file extension | Minor | whole-ontology level |

**Zero critical pitfalls.** All four were repaired in `extended_ontology_v2_repaired.owl`:

- **P10 fixed**: pairwise `owl:disjointWith` declared across all 14 core classes (`AllDisjoint`).
- **P08 fixed**: `rdfs:comment` added to all 57 schema elements (14 classes, 17 forward + 17 inverse object properties, 9 data properties).
- **P13 fixed**: `owl:inverseOf` declared for all 17 original object properties (e.g. `hasObjective` / `isObjectiveOfSubject`), bringing the total to 34 object properties.
- **P36 fixed**: base IRI changed from `.../ontology-hybrid-recsys-realdata.owl#` to `.../ontology-hybrid-recsys#`.

**Re-verification, not assumption**: adding disjointness axioms is exactly the kind of change that can surface a latent inconsistency (if any individual had accidentally been typed under two classes meant to be mutually exclusive). HermiT was re-run on the full 11,506-individual repaired graph: **still consistent, 0 unsatisfiable classes, 7.1s**. This is a genuine diagnosis→repair→re-verify cycle, not a description of one.

## 9. Still not possible without the target population or external services

- **Precision@K/Recall@K/NDCG@K (Track A)**: needs a temporally split interaction log — OULAD's VLE logs could support a *future* proxy version of this, but it wasn't requested here and would need its own scoping.
- **OOPS! pitfall scan**: ~~needs `oops.linkeddata.es`~~ **done** — see Section 8 above. Zero critical, 1 important + 3 minor, all repaired and re-verified.
- **TAM human evaluation (Track C)**: needs a live learner population using the deployed recommender — cannot be simulated honestly from either dataset.
- **Content-based/collaborative fusion**: OULAD's `vle.csv` has real per-student clickstream data that could support this in a follow-up; not built here since it's a substantial separate modeling task.

## 9. Paper file

`paper_with_realdata_section.md` — References updated (2 new entries, alphabetical), new Section 7.5 added, Table 3 caption cross-referenced, Conclusion updated to reflect the proof-of-concept without overclaiming it as the target-population result.
