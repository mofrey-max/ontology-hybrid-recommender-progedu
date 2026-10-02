# Ontology-Driven Hybrid Recommendation Framework for Programming Education

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
![OWL 2](https://img.shields.io/badge/Ontology-OWL%202-green)
![Reasoner](https://img.shields.io/badge/Reasoner-HermiT%20consistent-brightgreen)
![Python](https://img.shields.io/badge/Python-3.9%2B-yellow)

A formally validated, ontology-driven hybrid recommender framework for programming education. It extends the GitHub Classroom / BookWidgets knowledge-graph infrastructure of Namsraidorj, Namsraidorj & Enkhtur (2025) with a validated OWL 2 ontology, a rule-based recommendation path, and a real-data proof of concept.

> **Status: research prototype.** The ontology is built, repaired and re-verified against real data (11,506 individuals). The full hybrid recommender (content-based and collaborative fusion) and the Track A and Track C evaluations are specified in the paper but **not yet implemented**. See [Limitations and Roadmap](#limitations-and-roadmap).

---

## Table of Contents

1. [Overview](#overview)
2. [Key Contributions](#key-contributions)
3. [Results at a Glance](#results-at-a-glance)
4. [Repository Structure](#repository-structure)
5. [Ontology Design](#ontology-design)
6. [Getting Started](#getting-started)
7. [Validation](#validation)
8. [Limitations and Roadmap](#limitations-and-roadmap)
9. [Data Sources and Licensing](#data-sources-and-licensing)
10. [Citation](#citation)
11. [Authors](#authors)
12. [License](#license)

---

## Overview

Namsraidorj, Namsraidorj & Enkhtur (2025) combined Google Classroom, Microsoft Teams, GitHub Classroom and BookWidgets into a low-cost e-learning stack. They modelled course syllabi, Bloom-Anderson learning objectives and tool-level achievement as an OWL 2 knowledge graph queried with SPARQL. That work did not include a recommendation algorithm, a formal ontology validation, or a baseline comparison.

This project addresses those gaps. It extends the ontology with learner, achievement and recommendation concepts, validates it with standard ontology-engineering methods, and demonstrates the rule-based recommendation path on two real, public datasets.

## Key Contributions

1. **Extended ontology.** Five new classes (`Learner`, `LearnerProfile`, `AchievementRecord`, `RecommendationStrategy`, `Recommendation`) are added to the original eight. The `SIL(n,m,k)` achievement construct is reformulated as a normalized score (`SIL_norm = score / 100`).
2. **Validation protocol.** Competency-question SPARQL testing, HermiT consistency checking, OOPS! pitfall scanning, and OntoQA schema and instance metrics.
3. **Hybrid recommendation design.** SWRL and rule-based reasoning over the knowledge graph, fused with content-based and collaborative filtering and diversified with Maximal Marginal Relevance (MMR) re-ranking. This is specified in the paper; only the rule-based path is implemented here.
4. **Pre-registered evaluation protocol.** Three tracks: offline ranking metrics (A), ontology validation (B), and a Technology Acceptance Model study (C). Tracks A and C are scoped as future work.

## Results at a Glance

| Measure | Result |
| --- | --- |
| Classes | 14 (8 original, 5 extension, 1 implementation-support) |
| Object properties | 34 (17 forward and 17 declared inverses) |
| Data properties | 9 |
| Individuals | 11,506 |
| Relationship richness | 1.0 |
| Attribute richness | 0.643 |
| Inheritance richness | 0.0 (flat extension, see [Limitations](#limitations-and-roadmap)) |
| Annotated schema elements | 57 / 57 |
| HermiT reasoner | Consistent, 0 unsatisfiable classes, 7.1 s |
| OOPS! pitfalls | 4 found (0 critical), all repaired |
| Rule-triggered recommendations | 318 of 1,631 achievement records (19.5%) |

Populated individuals per class: `QuestionExemplar` 8,767 · `AchievementRecord` 1,631 · `Learner` 383 · `LearnerProfile` 383 · `Recommendation` 318 · `Objectives` 11 · `SupportTools` 5 · `ActivityTools` 5 · `Syllabus` 1 · `Subjects` 1 · `RecommendationStrategy` 1.

Full metrics are in [`ontoqa_metrics_v2.json`](ontoqa_metrics_v2.json).

## Repository Structure

```
.
├── LICENSE                              # MIT License
├── README.md                            # This file
├── paper_with_realdata_section.md       # Full paper (incl. Section 7.5, real-data proof of concept)
├── Real_Data_Implementation_Report.md   # Implementation log and detailed results
├── build_ontology_v2_repaired.py        # Ontology build script (owlready2)
├── extended_ontology_v2_repaired.owl    # Populated OWL 2 ontology (11,506 individuals)
└── ontoqa_metrics_v2.json               # Computed OntoQA schema and instance metrics
```

## Ontology Design

The ontology is built programmatically with [owlready2](https://owlready2.readthedocs.io/) and serialized as RDF/XML.

**Core classes**

| Layer | Classes |
| --- | --- |
| Original (Namsraidorj et al., 2025) | `Syllabus`, `Instructor`, `Subjects`, `Objectives`, `SupportTools`, `ActivityTools`, `Score`, `Description` |
| Extension (this work) | `Learner`, `LearnerProfile`, `AchievementRecord`, `RecommendationStrategy`, `Recommendation` |
| Implementation support | `QuestionExemplar` (real, human-classified Bloom items) |

**Design choices**

- Every object property has a declared inverse (for example `hasObjective` / `isObjectiveOfSubject`).
- All 14 core classes are declared pairwise disjoint (`AllDisjoint`).
- All 57 schema elements carry an `rdfs:comment`.
- The base IRI has no file extension.
- The recommendation threshold is `θ = 0.60`. An `AchievementRecord` with `SIL_norm < θ` triggers a `Recommendation` through the `RuleBased_ThresholdTrigger` strategy.

## Getting Started

### Requirements

- Python 3.9 or later
- `owlready2` and `pandas`
- Java, only if you want to re-run the HermiT reasoner
- [Protégé](https://protege.stanford.edu/) 5.x, optional, for browsing the ontology

```bash
pip install owlready2 pandas
```

### Option 1: Explore the prebuilt ontology

Open `extended_ontology_v2_repaired.owl` in Protégé, or load it in Python:

```python
from owlready2 import get_ontology

onto = get_ontology("extended_ontology_v2_repaired.owl").load()
print(len(list(onto.classes())), "classes")
print(len(list(onto.individuals())), "individuals")
```

### Option 2: Rebuild the ontology from the source datasets

1. Download the two datasets (see [Data Sources and Licensing](#data-sources-and-licensing)).
2. Place the files in a local `data/` folder:

   ```
   data/
   ├── bloom/
   │   └── blooms_taxonomy_dataset.csv
   └── oulad/
       ├── studentInfo.csv
       ├── studentAssessment.csv
       └── assessments.csv
   ```

3. In `build_ontology_v2_repaired.py`, update the hard-coded input and output paths (currently `/home/claude/...`) to point to your local `data/` folder and output location.
4. Run the build:

   ```bash
   python build_ontology_v2_repaired.py
   ```

   The script writes `extended_ontology_v2_repaired.owl` and an `outcome_log_v2.json` file with per-learner trigger results.

### Re-running the reasoner

Open the `.owl` file in Protégé and run **Reasoner → HermiT**. Alternatively, call `sync_reasoner()` from owlready2 (requires Java). Expected result: consistent, with no unsatisfiable classes.

## Validation

### Competency questions (real SPARQL over real data)

| ID | Question | Result |
| --- | --- | --- |
| CQ1 | Which learners fall below θ on TMA01? | 59 of 358 submitters |
| CQ2 | Which activity tools support each objective? | One real activity tool per TMA objective, confirmed for all 5 |
| CQ3 | Which strategy generated each recommendation? | All 318 trace to `RuleBased_ThresholdTrigger` |
| CQ4 | Mean `SIL_norm` per objective (ascending) | TMA02 0.668 < TMA05 0.691 < TMA01 0.703 < TMA03 0.704 < TMA04 0.706 |
| Bloom | Questions per Bloom level | Remember 2,582 · Understand 1,801 · Apply 1,508 · Analyze 1,293 · Create 800 · Evaluate 783 |

### OOPS! pitfall scan and repair

The schema was submitted to the [OOPS! scanner](https://oops.linkeddata.es/). No critical pitfalls were found, and all four findings were repaired in v2.

| Pitfall | Severity | Repair |
| --- | --- | --- |
| P10: Missing disjointness | Important | Pairwise `owl:disjointWith` across all 14 core classes |
| P08: Missing annotations | Minor | `rdfs:comment` added to all 57 schema elements |
| P13: Inverse relationships not declared | Minor | `owl:inverseOf` declared for all 17 object properties |
| P36: URI contains file extension | Minor | Base IRI changed to `.../ontology-hybrid-recsys#` |

After the repairs, HermiT was re-run on the full 11,506-individual graph. The result is still consistent.

### Descriptive validity check

The rule-trigger rate rises with worse real course outcomes (single cohort, n = 383):

| Final result | Learners | Triggered at least one recommendation |
| --- | --- | --- |
| Distinction | 20 | 0.0% |
| Pass | 258 | 39.5% |
| Withdrawn | 60 | 33.3% |
| Fail | 45 | 68.9% |

This is a face-validity check only. It is correlational, not causal, and it is not evidence for the Track A or Track C claims.

## Limitations and Roadmap

**Limitations**

- This is a **proof of concept**, not the paper's target evaluation. The two datasets are real but **not linked** to each other (no shared learner or question IDs), and neither is the 120-learner GitHub Classroom / BookWidgets population the paper's comparative claims depend on.
- Inheritance richness is 0.0 because the extension is a flat class hierarchy. Deeper subclass structure should be considered before comparing against hierarchical curriculum ontologies such as Bowlogna or AIISO.
- Results come from a single OULAD module presentation (AAA_2013J) and are descriptive only.
- The build script contains hard-coded local paths and must be adapted before use.

**Roadmap**

- [ ] Track A: Precision@K, Recall@K and NDCG@K on a temporally split interaction log (OULAD `vle.csv` clickstream could support a proxy version)
- [ ] Content-based and collaborative filtering fusion with MMR re-ranking
- [ ] Track C: Technology Acceptance Model (TAM) study with a live learner population
- [ ] Introduce subclass hierarchies to raise inheritance richness
- [ ] Parameterize file paths in the build script

## Data Sources and Licensing

The source code and original files in this repository are released under the [MIT License](LICENSE). The two datasets below are **not** covered by that license. They remain under their own terms, and the populated ontology contains individuals derived from them. Check each dataset's license before redistributing or reusing the derived data.

- **Bloom's Taxonomy Dataset.** Devane, V. (2024). *Bloom's Taxonomy Dataset* [Data set]. Kaggle. <https://www.kaggle.com/datasets/vijaydevane/blooms-taxonomy-dataset>
- **Open University Learning Analytics Dataset (OULAD).** Kuzilek, J., Hlosta, M., & Zdrahal, Z. (2017). Open University Learning Analytics dataset. *Scientific Data*, 4, 170171. <https://doi.org/10.1038/sdata.2017.171>

## Citation

If you use this work, please cite the paper (full reference list in [`paper_with_realdata_section.md`](paper_with_realdata_section.md)) and the underlying datasets above.

```bibtex
@misc{oluborode_safethon_godfrey_ontology_hybrid_recsys,
  author = {Oluborode, K.O. and Safethon, Shaphat and Godfrey, Manuyi},
  title  = {From Knowledge Graph to Recommendation: A Formally Validated,
            Ontology-Driven Hybrid Framework for Programming Education
            Recommender Systems},
  year   = {2026},
  note   = {Manuscript and source code},
  url    = {https://github.com/mofrey-max/ontology-hybrid-recommender-progedu}
}
```

Also cite the work this project extends:

> Namsraidorj, Namsraidorj, & Enkhtur (2025). *Ontology Based Recommendation System Using GitHub Classroom and BookWidget.*

## Authors

- K.O. Oluborode¹
- Shaphat Safethon²
- Manuyi Godfrey³

Modibbo Adama University, Yola, Nigeria

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details. Third-party datasets are subject to their own licenses, as described in [Data Sources and Licensing](#data-sources-and-licensing).
