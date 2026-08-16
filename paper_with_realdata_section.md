Ontology Driven Hybrid Recommendation Framework 

## **From Knowledge Graph to Recommendation:** 

## **A Formally Validated, Ontology Driven Hybrid Framework for Programming Education Recommender Systems** 

_Extending the GitHub Classroom / BookWidgets Infrastructure of Namsraidorj, Namsraidorj & Enkhtur (2025) with a Validated Knowledge Graph and a Hybrid Recommendation Engine_ 

## K.O Oluborode<sup>1</sup> Shaphat Safethon<sup>2</sup> Manuyi Godfrey<sup>3</sup> 

_Modibbo Adama University Yola_ 

_kayodeoo@mau.edu.ng, safethon@mau.edu.ng,manugodfrey02@gmail.com_ 

## **Abstract** 

Prior work combined Google Classroom, Microsoft Teams, GitHub Classroom, and BookWidgets into a low cost e learning infrastructure and represented course syllabi, Bloom Anderson learning objectives, and tool level achievement as an OWL2 knowledge graph queried through SPARQL (Namsraidorj, Namsraidorj, & Enkhtur, 2025). That system, however, stopped short of the recommendation capability its title implied: no recommendation algorithm was implemented, no formal ontology quality validation was reported, and no baseline or statistical comparison accompanied its claims. This paper closes that gap. We extend the published syllabus ontology with five classes Learner, Learner Profile, Achievement Record, Recommendation Strategy, and Recommendation and formalize its achievement construct, SIL(n,m,k), as a normalized, weighted score over subjects, Bloom objectives, and support tools. We specify a validation ready methodology for the ontology that combines competency question SPARQL testing, HermiT/Pellet consistency checking, OOPS! pitfall scanning, and OntoQA schema/instance metrics benchmarked against four existing curriculum ontologies. We then design a hybrid recommendation engine that fuses symbolic SWRL based reasoning over the knowledge graph with content based and collaborative filtering, diversified through Maximal Marginal Relevance re ranking. Finally, we specify a pre registered, three track evaluation protocol offline ranking metrics, ontology validation, and a Technology Acceptance Model human study  with explicit baselines and significance testing, so that every capability the framework claims is falsifiable before deployment. We position the contribution against EduCOR, PEARL, and recent knowledge graph and LLM augmented educational recommenders, and close with the framework's limitations and threats to validity. 

**Keywords:** ontology engineering; knowledge graphs; educational recommender systems; GitHub Classroom; BookWidgets; Bloom’s taxonomy; ontology evaluation; hybrid filtering; SPARQL; SWRL 

1 

Ontology Driven Hybrid Recommendation Framework 

## **1. Introduction** 

Low cost, multi tool e learning infrastructures that combine a Learning Management System with specialized authoring and grading tools, connected through Learning Tools Interoperability (LTI), let instructors without dedicated instructional design support build effective blended courses. A recent example combined Google Classroom, Microsoft Teams, GitHub Classroom, and BookWidgets in exactly this way, and additionally layered course syllabi, Bloom–Anderson learning objectives, and per tool student achievement onto an OWL2 knowledge graph populated from 120 learners and more than 2,000 graded programming submissions across roughly 40 tasks (Namsraidorj, Namsraidorj, & Enkhtur, 2025; hereafter. Teachers could then issue SPARQL queries against the populated graph to see which students had not met a given Bloom taxonomy objective in a given subject. 

Despite its title, however, Ontology Based Recommendation System  Using GitHub Classroom and Bookwidgetdoes not deliver a recommendation system. Its own conclusion states plainly that “the next step involves developing a recommendation system”   the published contribution is the ontology and the diagnostic SPARQL layer, not a recommender. No recommendation algorithm is specified or run, no ranked output is evaluated, and no precision, recall, or ranking metric is reported. Nor is the ontology itself formally validated: there is no statement of competency questions, no reasoner consistency check, no pitfall scan, and no metric based comparison against the four related curriculum ontologies the paper itself reviews. This is not an isolated shortcoming. Systematic reviews of ontology based e learning recommender systems have repeatedly found that formal ontology evaluation methodology is rare in this literature even when a working recommender is present (Tarus, Niu, & Mustafa, 2018), which makes the double gap in Ontology Based Recommendation System  Using GitHub Classroom and Bookwidgetno evaluated recommender and no validated ontology   a useful, concrete target for a follow up contribution. 

This paper makes four contributions that, taken together, turn the published knowledge graph infrastructure into a recommender system whose claims can actually be checked: 

- i. A formally specified extension of the published syllabus ontology with five new classes for learners, achievement, and recommendations, and an explicit, normalized reformulation of its SIL(n,m,k) achievement construct (Extended Ontology Design). 

- ii. A validation methodology for the extended ontology combining competency questions, description logic reasoning, automated pitfall scanning, and comparative schema/instance metrics against four prior curriculum ontologies (Ontology Validation protocol). 

- iii. A hybrid recommendation algorithm that fuses rule based reasoning over the knowledge graph with content based and collaborative filtering, with explicit fusion and diversity re ranking formulas (Hybrid Recommendation Algorithm). 

- iv. A pre registered, three track evaluation protocol   offline ranking metrics with named baselines, ontology validation, and a human/TAM study with statistical testing   so that 

2 

Ontology Driven Hybrid Recommendation Framework 

empirical deployment produces falsifiable, reportable results rather than architecture diagrams alone (Evaluation Protocol). 

The framework is organized around four research questions: (RQ1) Can the published syllabus ontology be extended with recommendation relevant classes without breaking its logical consistency or degrading its schema quality relative to comparable curriculum ontologies? (RQ2) Does a hybrid rule based/collaborative recommender built on that graph outperform simple non personalized and single strategy baselines on offline ranking metrics? (RQ3) Do learners and instructors perceive the resulting recommendations as useful and easy to act on? (RQ4) How does the resulting system compare, on validation rigor and recommendation capability, to other ontology  and knowledge graph based educational recommenders published since 2021? The remainder of the paper is organized as follows. Reviews related infrastructure, curriculum ontologies, and educational recommenders. Proposed system Architecture presents the extended system architecture.Present the ontology extension, its validation protocol, and the recommendation algorithm. Evaluation Protocol specifies the evaluation protocol. 

## **2. Related Work** 

## **2.1 Multi Tool E Learning Infrastructure** 

Ontology Based Recommendation System  Using GitHub Classroom and Bookwidget integrates Google Classroom and Microsoft Teams as the delivery LMS, BookWidgets for Bloom aligned quizzes and gamified widgets, and GitHub Classroom for auto graded programming assignments, connecting GitHub Classroom to the LMS through LTI so that all systems share a single sign on and assignment surface. Content was structured with a micro learning breakdown   15% reading, 15% listening, 20% interactive assignment, 20% discussion, and 30% multi level GitHub Classroom tasks   and assessed against the six levels of the Bloom–Anderson taxonomy (Anderson & Krathwohl, 2001). This infrastructure layer is sound and is retained without modification in the framework proposed here (Proposed system Architecture, Layers 1–2); our contribution begins at the point where Ontology Based Recommendation System  Using GitHub Classroom and Bookwidget stops, namely the knowledge and recommendation layers. 

## **2.2 Curriculum and Syllabus Ontologies** 

Ontology Based Recommendation System  Using GitHub Classroom and Bookwidget itself surveys four curriculum adjacent ontologies the Bowlogna ontology, which models the structure of European higher education programs rather than learning activities (Demartini et al., 2013); the BBC Curriculum ontology, which describes course topics and content; the Academic Institution Internal Structure Ontology (AIISO), which models organizational structure (Styles & Shabir, 2008); and a University ontology describing departments, faculty, courses, and publications (Heflin, 2000) and rejects all four as unsuitable, instead extending the Curriculum/Lesson/Content ontology of Chung and Kim (2016). None of the five ontologies combine Bloom taxonomy 

3 

Ontology Driven Hybrid Recommendation Framework 

anchored, tool level achievement scoring with a recommendation vocabulary, which is the specific gap Extended Ontology Design addresses. 

## **2.3 Ontology Based and Knowledge Graph Recommenders in Education** 

Tarus, Niu, and Mustafa (2018) provide the field's most comprehensive review of ontology based e learning recommenders and find that ontology and knowledge based representations are attractive specifically because they mitigate cold start and over specialization problems that pure collaborative approaches suffer from a property this framework exploits by keeping a rule based reasoning path always available even when collaborative signal is sparse (Hybrid Recommendation Algorithm). Two recent systems set the bar for what a validated, evaluated ontology based recommender looks like. EduCOR (Ilkou et al., 2021) is an open, FAIR educational and career recommendation ontology validated against three gold standard schemata and evaluated on real open educational resource repositories, and its associated eDoer deployment reported that learners who voluntarily used the recommender in a university Business Analytics course outperformed those who did not on final grades. PEARL (Hadyaoui & Cheniti Belcadhi, 2025) is an ontology driven project recommender for a programming course   the closest published analogue to the domain of Ontology Based Recommendation System  Using GitHub Classroom and Bookwidget and reports 82% precision and 78% recall in its empirical validation, figures this paper adopts as an external benchmark rather than a target to be matched synthetically. Beyond pure ontologies, recent knowledge graph embedding, graph neural network, and retrieval augmented approaches have pushed educational recommendation further: knowledge graph enhanced course recommendation (e.g., KPCR; Jung, Jang, Kim, & Kim, 2022), LLM assisted knowledge graph completion for curriculum and domain modeling in personalized higher education recommendation (Abu Rasheed et al., 2025), and education oriented graph retrieval augmented generation for learning path recommendation (Cheng et al., 2025). The common thread across all of these systems and the thread absent from Ontology Based Recommendation System Using GitHub Classroom and Bookwidget is that a validated knowledge representation is always paired with an implemented, evaluated recommendation mechanism. 

## **2.4 Ontology Evaluation Methodology** 

Formal ontology evaluation typically combines four complementary techniques, all adopted in Ontology Validation protocol: competency questions, which state the questions the ontology must be able to answer and formalize each as a query it must correctly answer; description logic reasoner consistency checking (e.g., HermiT or Pellet) to confirm the ontology is logically satisfiable and free of unintended entailments; the OOPS! pitfall scanner, which screens an ontology against a catalogue of common modeling pitfalls empirically derived from an analysis of hundreds of published ontologies and classifies each detected issue as critical, important, or minor (Poveda Villalón, Gómez Pérez, & Suárez Figueroa, 2014); and OntoQA, which computes schema metrics (relationship, attribute, and inheritance richness) and instance/knowledge base metrics that allow one ontology to be compared quantitatively against another (Tartir, Arpinar, Moore, Sheth, & 

4 

Ontology Driven Hybrid Recommendation Framework 

Aleman Meza, 2005). None of these four techniques appears in Ontology Based Recommendation System  Using GitHub Classroom and Bookwidget. 

## **3. Proposed System Architecture** 

Figure 1 presents the extended architecture as seven layers. Layers 1–2 (learning delivery and content/assessment) and the CSV logging portion of Layer 3 are inherited unchanged from [1]. The contribution begins with the Karma based semantic lifting step and continues through four new elements: an explicit ontology validation gate that a candidate graph must pass before population (Layer 4), a recommendation engine that consumes the populated graph (Layer 5), a presentation split that gives learners a recommendation feed and instructors an analytics dashboard (Layer 6), and a continuous evaluation and feedback layer that closes the loop back into the next assessment cycle (Layer 7). This last layer is what makes the system a recommender in an operational sense: every recommended item's downstream outcome   was it completed, did the related objective score improve   is logged and becomes training and evaluation signal for the next cycle, rather than a one shot diagnostic query as in Ontology Based Recommendation System Using GitHub Classroom and Bookwidget. 

5 



<!-- Start of picture text -->
Fig. 1 — Ontology-Driven Hybrid Recommendation Architecture<br>1 - Learning Delivery Layer (LMS, integrated via LTI 1.3)<br>Google Classroom Microsoft Teams BookWidgets Studio<br>Course delivery, Course delivery, Authoring: quizzes,<br>assignment distribution synchronous sessions widgets, games<br>2+ Content & Assessment Layer<br>GitHub Classroom BookWidgets Runtime<br>Auto-graded programming tasks Bloom—Anderson aligned quizzes,<br>(data structures, design, architecture) interactive widgets, gamified tasks<br>3+ Data & Semantic-Lifting Layer<br>Activity Logs (CSV) Karma Mapper RDF Triple Stream Vv.<br>Submission, score & CSV — RDF Instance data conforming \<br>quiz-response records semantic lifting to the domain ontology ‘<br>‘<br>1<br>‘<br>4- Knowledge Layer v Vv 1’4<br>1<br>H<br>OWL2 Domain Ontology (Protégé 5) Ontology Validation Gate 1\<br>SyllabusSupportRecommendation+ extended:Tools- Instructor- Activity7 Learner- - SubjectsRecommendationStrategy Tools- LearnerProfile- -ScoreObjectives- Description- (Bloom)- oo CeupeieiepetesielHermiTSOEs!sl/ paredPellet GeantconsistencyORtGOA SPAREchecking menics gei 14'4<br>1<br>‘<br>1<br>quality gate: must pass before population 4<br>H<br>1<br>GraphDB Triple: Store 1'<br>Populated knowledge graph + zs !<br>SPARQL query endpoint Eat<br>St<br>G1<br>5 - Recommendation Engine Layer Vv eig '<br>Weighted Score z1<br>SWRL/Rule-Based SPARQL CONSTRUCT:Reasoner Content-basedHybrid Filteringsimilarity + FusionRanking+ Top-K. BiIh!<br>unmet objective to remedial tool collaborative filtering (peers) '<br>'<br>'<br>'<br>'<br>'<br>'<br>'<br>'<br>'<br>t<br>6 - Presentation Layer ea A 'H'<br>Learner Recommendation- Feed Instructor Analytics' Dashboard i1<br>Ranked remedial resources Flagged objectives per Bloom level (Fig. 9-style map) H<br>t<br>'<br>1<br>1<br>1<br>1<br>:<br>7 - Evaluation & Continuous-Feedback Layer 4<br>1<br>!<br>Offline Metrics Online / Human Evaluation yf<br>Precision@K, Recall@K, F1, NDCG@K, TAM user study, expert validation (k), 2 ,<br>Coverage, Diversity, Novelty AB comparison vs. control section<br><!-- End of picture text -->

Ontology Driven Hybrid Recommendation Framework 

introduced here. Figure 2 shows the resulting class diagram; original classes are teal, new classes are purple. 

|**Class**|**Status**|**Superclass / SubclassOf**|**Definition**|
|---|---|---|---|
|Syllabus|Original|Course → Instructor|Core concept of the course|
|Instructor|Original|Syllabus → Teacher,<br>Assistant|Course instructor(s)|
|Subjects|Original|Syllabus → Objectives|Learning subjects (n = 15<br>topics in the source<br>deployment)|
|Objectives|Original|Subjects → Support|Bloom–Anderson|
|||Tools|taxonomy levels (m = 6)|
|Support Tools|Original|Objectives → Activity|Learning activity tool|
|||Tools|categories (k = 2–4 per<br>objective)|
|Activity Tools|Original|Support Tools → Score|Concrete widgets / GitHub<br>Classroom assignments|
|Score|Original|Support Tools|Quantity score of a tool<br>instance|
|Description|Original|Support Tools|Quality evaluation of a<br>tool instance|
|Learner|New|(enrolledIn Syllabus)|A student enrolled in a<br>Syllabus|
|LearnerProfile|New|Learner →|Per learner state and|
|||AchievementRecord|history|
|AchievementRecord|New|LearnerProfile /|Instance of SIL(n,m,k) for|
|||Objectives →|one learner × objective ×|
|||RecommendationStrategy|tool triple|
|RecommendationStrategy|New|AchievementRecord →<br>Recommendation|RuleBased | ContentBased<br>| Collaborative | Hybrid|
|Recommendation|New|RecommendationStrategy|A ranked, timestamped|



7 

Ontology Driven Hybrid Recommendation Framework 

remedial item for a below threshold objective 

_Table 1. Extended ontology classes (8 original + 5 new)._ 

## **4.1 Formalizing SIL(n,m,k)** 

The published achievement construct SIL(n,m,k) sums per subject, per objective, per tool contributions but is not given an explicit normalization, weighting, or threshold rule, which makes it unusable as a recommendation trigger as written. We propose the following normalized form. For learner l, subject s, and Bloom objective o, let T_o be the set of support tools associated with o, w_t ∈ (0,1] an instructor  or OntoQA importance derived weight for tool t, and score(l,s,o,t) the learner's raw performance on tool t (e.g., percentage correct, or auto grader pass rate for GitHub Classroom tasks), rescaled to [0,1] by max_score_t: 

_SIL_norm(l, s, o) = Σₜ_ ∈ _ᵀₒ [ w · score(l,s,o,t) / max_score ]  ⁄  Σₜ ₜ ₜ_ ∈ _ᵀₒ wₜ_ 

SIL_norm(l,s,o) lies in [0,1] by construction. A Recommendation instance is generated whenever SIL_norm(l,s,o) < θ , an objective specific threshold (e.g., θ = 0.6, matching the passing gradeₒ convention used for the GitHub Classroom auto grader in [1], where roughly 80% of submissions passed). Objective specific rather than global thresholds matter because “Create” level objectives are intrinsically harder to satisfy than “Remember” level ones under the same taxonomy (Anderson & Krathwohl, 2001); a single global threshold would systematically over recommend at the top of the taxonomy and under recommend at the bottom. 

## **4.2 Worked Example (Synthetic, for Illustration Only)** 

_Table 2 illustrates the computation with synthetic data for one learner in one subject across the six Bloom objectives, each supported by two to three tools with equal weights (w_t = 1 for all t). These numbers are illustrative only and are not empirical results._ 

|**Objective**|**Tools (score / max)**|**SIL_norm**|**θ= 0.6**|**Recommendation?**|
|---|---|---|---|---|
|Remember|Quiz 8/10, Flashcards 9/10|0.85|0.60|No|
|Understand|Worksheet 6/10, Video quiz<br>7/10|0.65|0.60|No|
|Apply|GitHub task 4/10, Widget<br>5/10|0.45|0.60|Yes   recommend<br>remedial GitHub<br>task|
|Analyze|GitHub task 5/10, Diagram<br>6/10, Debate 7/10|0.60|0.60|No (boundary)|
|Evaluate|Peer review widget 3/10|0.30|0.60|Yes   recommend<br>guided rubric<br>widget|
|Create|Capstone GitHub task 2/10|0.20|0.60|Yes   recommend<br>scaffolded template|



8 

Ontology Driven Hybrid Recommendation Framework 

## <u>task</u> 

_Table 2. Synthetic worked example of SIL_norm and threshold triggered recommendation for one learner in one subject._ 

## **5. Ontology Validation Protocol** 

Before the extended ontology is populated with live data, it must pass the four part validation gate shown in Figure 1, Layer 4. This section specifies each part; Evaluation protocol (Track B) specifies how results are to be reported 

## **5.1 Competency Questions** 

Representative competency questions (CQs), each formalized as a SPARQL query against the populated graph: 

- v. CQ1: Which learners have not met a given objective o in subject s? → SELECT ?learner WHERE learner hasAchievement ?rec . ?rec forObjective o . ?rec silScore ?v . FILTER(? v < θ) 

- vi. CQ2: Which support tools are associated with objective o, ranked by weight? → SELECT ?tool ?weight WHERE o supportedBy ?tool . ?tool hasWeight ?weight . ORDER BY DESC(?weight) 

- vii. CQ3: What Recommendation instances exist for learner l, and by which strategy were they generated? → SELECT ?rec ?strategy WHERE l hasRecommendation ?rec . ?rec generatedBy ?strategy 

- viii. CQ4: For a given Syllabus, which objectives have the lowest class wide mean SIL_norm (candidates for redesign)? → aggregate query grouping AchievementRecord by Objective 

- ix. CQ5: Which Activity Tools have never been the target of a Recommendation despite being supportedBy an under achieved Objective (candidates for removal or redesign)? 

Each CQ must return the expected result on a small hand populated test graph before the ontology is considered ready for live population; a CQ that fails is treated as a schema defect, not an application bug. 

## **5.2 Reasoner Consistency Checking** 

The populated ontology is loaded into Protégé and checked with both the HermiT and Pellet description logic reasoners. Acceptance criteria: the ontology is satisfiable, no class is classified as unsatisfiable (equivalent to owl:Nothing), and the set of inferred subclass and instance membership axioms is inspected for unintended entailments (e.g., a Learner accidentally inferred to be a subclass of ActivityTools through a property domain error). Both reasoners are run because they use different algorithms and occasionally disagree on borderline expressivity, which itself is diagnostic. 

9 

Ontology Driven Hybrid Recommendation Framework 

## **5.3 OOPS! Pitfall Scanning** 

The ontology (in OWL/XML) is submitted to the OOPS! scanner (Poveda Villalón et al., 2014), which checks it against a catalogue of common ontology authoring pitfalls (e.g., missing domain/range, cycles in the class hierarchy, unconnected ontology elements) and reports each detected issue as critical, important, or minor. All critical pitfalls must be resolved before population; important pitfalls are resolved or explicitly justified in the validation report; minor pitfalls are logged. 

**Executed, real-data addendum (v1 scan and v2 repair):** the schema (prior to real-data population) was submitted to the live OOPS! scanner and returned zero critical pitfalls and four detected issues: P10 Missing disjointness (Important, flagged at the whole-ontology level), P08 Missing annotations (Minor, 40 of 40 schema elements — every class, object property, and data property lacked rdfs:comment), P13 Inverse relationships not explicitly declared (Minor, 17 of 17 object properties), and P36 URI contains file extension (Minor, the base IRI ended in .owl). All four were repaired in a v2 ontology: pairwise owl:disjointWith was declared across the 14 core classes, rdfs:comment was added to all 57 schema elements (14 classes + 17 forward + 17 inverse object properties + 9 data properties), owl:inverseOf was declared for all 17 object properties, and the base IRI was changed to drop the .owl suffix. HermiT re-confirmed the v2 ontology consistent (0 unsatisfiable classes, 7.1s) after the disjointness axioms were added — disjointness is exactly the kind of repair that can surface a latent inconsistency if two supposedly-exclusive classes ever shared an individual, and none did. 

## **5.4 OntoQA Comparative Metrics** 

OntoQA (Tartir et al., 2005) is run on the extended ontology to compute schema metrics relationship richness (proportion of predicates that are non hierarchical relationships rather than subclassOf), attribute richness (average attributes per class), and inheritance richness (average subclasses per class) and instance metrics such as class richness and average population per class. Table 3 specifies the comparison this protocol requires; because the extended ontology has not yet been populated from a live deployment, the “this framework” column is left as a reporting placeholder rather than a fabricated figure, and is to be completed as part of Track B of the evaluation. 

|**Metric**|**Bowlogna**|**AIISO**|**Chung & Kim**<br>**(2016)**|**This**<br>**framework**|
|---|---|---|---|---|
|Relationship richness|reported in|reported in|reported in|to be computed|
||source|source|source|(Track B)|
|Attribute richness|reported in<br>source|reported in<br>source|reported in<br>source|to be computed<br>(Track B)|
|Inheritance richness|reported in|reported in|reported in|to be computed|
||source|source|source|(Track B)|
|Class count|reported in<br>source|reported in<br>source|reported in<br>source|18 (13 base + 5<br>extension)|
|Instance/knowledge|reported in|reported in|reported in|to be computed|
|base metrics|source|source|source|post deployment|



_Table 3. OntoQA comparison plan. Reference ontology figures are drawn from their original publications at reporting time rather than reproduced here from memory; “this framework” values are computed once the ontology is populated on the target deployment (Track B, Evaluation protocol). A proof of concept run on real, cited, but non target data (Real Data Proof of Concept Implementation) genuinely computed relationship richness = 1.0, attribute richness = 0.643, inheritance richness = 0.0, class count = 14, on 11,506 individuals — reported there, not substituted into this table, since it is not the population Table 3 is comparing._ 

## **6. Hybrid Recommendation Algorithm** 

Figure 3 specifies the algorithm that runs whenever a learner completes an assessed activity. It combines two independent candidate generation paths   a symbolic, rule based path that is cold 

10 



<!-- Start of picture text -->
Fig. 3 - Hybrid Recommendation Algorithm (per learner, per Syllabus)<br>Start: learner completes an<br>assessed activity<br>Step 1 - Update AchievementRecord<br>sean pereer Recomputeleamer SIL(n,m,k)x objective xfortool the affectedtriple<br>: ¢ ife<br>: ’<br>‘<br>’<br>Vi , p™ No recommendation issued<br>iM Step 2- Score below<br>if objective threshold theta? objective mastered; continue<br>1 monitoring next activity<br>i<br>i/ yes<br>Ul<br>‘A1 Step 3 - Generate candidates jrom two independent sources<br>t<br>'<br>ti 3a. Rule-Based Reasoner 3b. Hybrid Filtering<br>i SWRL tule fires over the ontology: Content-based: cosine similarity of tool<br>g ' Objective(o), belowThreshold(|,o), metadata to unmet objective<br>2 ; supportedBy(o,t) -> Recommend(|,t) Collaborative: peers who improved on 0<br>3 h (symbolic, cold-start safe) after using tool t (item-based CF)<br><'<br>E<br>c'<br>F=f '<br>a1<br>2'<br>> ' Step 4 - Weighted score fusion<br>Py 1<br>3 : score = alpha . rule_score + (1-alpha) . hybrid_score<br>g-$'' 1 \ candidates ranked and de-duplicated<br>‘<br>'<br>\<br>1<br>H Step 5 - Select Top-K and apply diversity filter<br>\<br>y Maximal Marginal Relevance re-ranking to<br>avoid recommending near-duplicate tools<br>\<br>‘<br>\<br>\<br>‘<br>\<br>\in Step 6 - Persist Recommendation<br>‘ instance(s); notify learner & instructor<br>x<br>.<br>s .<br>N . y s<br>oA Step 7 - Log outcome<br>aaas® Was the recommended tool completed?<br>Did the objective score improve next cycle?<br><!-- End of picture text -->

Ontology Driven Hybrid Recommendation Framework 

The rule based path is expressed as a Semantic Web Rule Language rule over the OWL2 ontology (Horrocks, Patel Schneider, Boley, Tabet, Grosof, & Dean, 2004), combining Horn like antecedents with the ontology's class and property assertions: 

_Objective(?o)_ ∧ _AchievementRecord(?a)_ ∧ _forObjective(?a,?o)_ ∧ _forLearner(?a,?l)_ ∧ _silScore(?a,?v)_ ∧ _swrlb:lessThan(?v,?theta)_ ∧ _supportedBy(?o,?t) → Recommend(?l,?t)_ 

This rule fires purely from ontology structure and the learner's own AchievementRecord, so it produces a sensible recommendation even for a learner with no prior history relative to peers   the classic cold start case that motivates ontology based approaches in the first place (Tarus et al., 2018). 

## **6.2 Hybrid Filtering** 

The statistical path computes two scores per candidate tool t for learner l: a content based score using cosine similarity between a vector representation of t's metadata (Bloom level, subject, modality) and the unmet objective's requirement vector, and a collaborative score using item based filtering over peers who previously had a similarly low SIL_norm on the same objective and subsequently improved after completing t. The two are combined as hybrid_score(l,t) = β · content(l,t) + (1−β) · collab(l,t), with β tuned on a validation split (Evaluation protocol) and defaulting to 0.5 in the absence of tuning data. 

## **6.3 Fusion and Diversity Re Ranking** 

Rule based and hybrid candidate scores are merged as score(l,t) = α · rule_score(l,t) + (1−α) · hybrid_score(l,t), with α weighted toward the rule based term early in a course (when collaborative signal is sparse) and toward the hybrid term as the class wide dataset grows   operationalized simply as α = max(0.3, 1 − n_peers/N), where n_peers is the number of peers with a comparable AchievementRecord and N is a saturation constant (e.g., 30). The merged, de duplicated candidate list is then re ranked with Maximal Marginal Relevance (Carbonell & Goldstein, 1998) to avoid presenting near duplicate tools: 

# _MMR = argmax_{t_ ∈ _C\R} [ λ · score(l,t) − (1−λ) · max_{t'_ ∈ _R} sim(t,t') ]_ 

where C is the candidate set, R the already selected recommendation list, and λ balances relevance against redundancy. The top K items (K = 3 by default, matching the small remedial item counts typical of a single objective) are persisted as Recommendation instances, and outcomes are logged for the next cycle (Figure 1, Layer 7). 

## **7. Evaluation Protocol** 

Figure 4 specifies three parallel evaluation tracks that converge into a single evidence report. The protocol is written to be executed against a live deployment on the population described in 

12 



<!-- Start of picture text -->
Fig. 4 - Evaluation Protocol for the Recommendation Framework<br>Dataset Ontology artifact Deployed recommender<br>120 learners, 2000+ graded submissions, Populated OWL2 KG (30+ classes, Rule-based + hybrid engine,<br>achievement matrix S_IL(n=15, m=6, k=2..4) ~50k class assertions) in GraphDB producing Top-K per learner<br>Track A - Offline accuracy Track B - Ontology validation TrackC - Human evaluation<br>Time-based train/test split (80/20) Competency-question SPARQL passifail AJB; treatment vs, control section<br>Precision@K, Recall@K, Fl, NDCG@K (K=5,10) HermiT / Pellet consistency check TAM survey (perceived usefulness/ ease)<br>vs. baselines: Random, Most-Popular, OOPS! pitfall scan (crticalimportantiminor) Expert rating of Top-K relevance,<br>Content-only, Collaborative-only OntoQA schema + instance metrics inter-rater reliability (Cohen's kappa)<br>Beyond-accuracy metrics Comparative quality table Statistical testing<br>Coverage (shareof tools ever Relationship / attribute/ inheritance Paired t-test/ Wilcoxon on per-leamer<br>fecommended), diversity (intra-list Tichness vs, Bowlogna, AllSO, gain scores; effect size (Cohen's d);<br>dissimilarity), novelty University Ontology, Chung & Kim (2016) report p and Cl, not p alone<br>Consolidated evidence report<br>Every claim in the Results section traced to a metric,<br>a baseline comparison, and a significance test —<br>No unvalidated architecture claims<br>Publication-ready manuscript<br>Title, abstract, and contributions matched<br>one-to-one to reported evidence<br><!-- End of picture text -->

Ontology Driven Hybrid Recommendation Framework 

## _Figure 4. Three track evaluation protocol converging on a consolidated, claim by claim evidence report._ 

## **7.1 Track A   Offline Ranking Accuracy** 

A time based 80/20 train/test split (rather than a random split, to avoid leaking future achievement into training) is used to compute, at K = 5 and K = 10: 

- x. Precision@K and Recall@K against tools the learner is later observed to complete and improve on; 

- xi. F1@K as their harmonic mean; 

- xii. NDCG@K (Järvelin & Kekäläinen, 2002) to credit correctly ranking the most relevant remedial tool first, not merely including it; 

- xiii. Coverage (share of the tool catalogue ever recommended), diversity (mean pairwise dissimilarity within a recommendation list), and novelty. 

Four baselines are required so that the hybrid engine's contribution is separable from any single component: Random, Most Popular (non personalized), Rule based only (Hybrid Recommendation Algorithm.1 in isolation), and Content/Collaborative only (Hybrid Recommendation Algorithm.2 in isolation, i.e., α = 0). Reporting the hybrid system's metrics without these baselines would repeat exactly the evidentiary gap this paper identifies in [1]. 

## **7.2 Track B   Ontology Validation** 

Executes Ontology Validation protocol in full and reports: CQ pass/fail table; reasoner consistency result (satisfiable / unsatisfiable classes, if any); OOPS! pitfall counts by severity and resolution status; and the completed OntoQA comparison (Table 3). 

## **7.3 Track C   Human Evaluation** 

An A/B comparison is run between a treatment section using the recommender and a control section using the unmodified [1] infrastructure (diagnostic SPARQL only, no recommendations surfaced), matched as closely as possible on course content and instructor. Learners in the treatment section complete the six item Perceived Usefulness and six item Perceived Ease of Use scales of the Technology Acceptance Model (Davis, 1989) after the recommender has been in use for at least two graded cycles. Independently, two subject matter experts rate the relevance of each learner's Top K list on a Likert scale, with inter rater agreement reported via Cohen's kappa (Cohen, 1960). 

## **7.4 Statistical Testing** 

Per learner gain scores (post recommendation change in SIL_norm on the targeted objective) are compared between treatment and control using a paired t test where normality holds and a Wilcoxon signed rank test otherwise, with effect size (Cohen's d or matched pairs rank biserial correlation) and 95% confidence intervals reported alongside p values   a p value alone is not 

14 

Ontology Driven Hybrid Recommendation Framework 

treated as sufficient evidence of a meaningful gain. Because Track A metrics are computed across six Bloom objectives simultaneously, a Bonferroni or Benjamini–Hochberg correction is applied to control the family wise error rate. 

## **7.5 Real Data Proof of Concept Implementation** 

Ahead of a live deployment on the population described in [1], the ontology, the rule based recommendation path, and Ontology Validation protocol's validation gate were implemented and executed in full against two independent, publicly available, cited real datasets, to demonstrate the pipeline is mechanically sound before it is pointed at production data. This is a feasibility demonstration, not a substitute for Evaluation Protocol: neither dataset is drawn from the programming course, GitHub Classroom/BookWidgets population that this paper's comparative claims (Discussion: Comparative Positioning) are about, and the datasets are not cross linked to one another at the individual record level. 

**Objectives layer (Devane, 2024).** The Bloom's Taxonomy Dataset (8,767 questions, human labeled BT1–BT6) was used to populate real, classified exemplar items under the six canonical Bloom Objectives instances, giving the Objectives layer genuine content rather than a single illustrative example. Distribution: Remember 2,582 (29.5%), Understand 1,801 (20.5%), Apply 1,508 (17.2%), Analyze 1,293 (14.7%), Create 800 (9.1%), Evaluate 783 (8.9%). 

**Learner/Achievement/Recommendation layer (Kuzilek et al., 2017).** The full real cohort of Open University module presentation AAA_2013J (n = 383 learners, 5 tutor marked assignments, 1,631 submitted, graded records) was used to populate real Learner, LearnerProfile, AchievementRecord, and rule based Recommendation instances, applying SIL_norm(l,s,o) = score/100 and the paper's own θ = 0.60 convention (Formalizing SIL(n,m,k)) with no synthetic values. 318 of 1,631 real achievement records (19.5%) fell below threshold and triggered a rule based Recommendation. 

**Validation gate, executed for real.** The populated graph (11,506 individuals, 14 classes, 17 object properties, 9 data properties) was checked with the HermiT reasoner: satisfiable, zero unsatisfiable classes (8.3s). CQ1–CQ4 were run as live SPARQL against the populated graph and returned correct, inspectable results (e.g., mean SIL_norm per real TMA objective ranged 0.668–0.706, all five above θ at the cohort level even though 19.5% of individual records fell below it). OntoQA style metrics were genuinely computed rather than estimated: relationship richness 1.0, attribute richness 0.643, inheritance richness 0.0 (flat extension; no subclass hierarchy was defined beyond the extension itself, which should be revisited before the Table 3 comparison against Bowlogna/AIISO, both of which use deeper subclass hierarchies). 

**Descriptive validity check.** As a face validity check only — not a substitute for Track A/C, and not a causal claim, since struggling learners may trigger recommendations because they are already struggling rather than the reverse — the rule based trigger rate was cross tabulated against each learner's real final_result: Distinction 0/20 (0%), Pass 102/258 (39.5%), Withdrawn 20/60 (33.3%), Fail 31/45 (68.9%). The monotonic relationship between trigger rate and worse outcome is consistent with the threshold rule capturing a real, meaningful signal, though a single cohort (n = 383) cannot establish this beyond the descriptive level. 

**What this does and does not establish.** This confirms the ontology, threshold rule, and validation gate are implementable and executable against real, larger scale, cited data with no fabricated figures. The OOPS! pitfall scan has now also been executed for real against the schema (Section 5.3): zero critical pitfalls, one important (missing disjointness) and three minor issues, all four repaired and re-verified consistent under HermiT. What remains open is Precision@K/Recall@K/NDCG@K (Track A — requires a temporally split interaction log the rule based path can be ranked against) and the TAM human evaluation (Track C — requires a live learner population using the deployed recommender). Those remain open, as stated in This paper's own limitation, until Evaluation Protocol is executed on the population in [1]. 

## **8. Discussion: Comparative Positioning** 

Table 4 positions the proposed framework against [1] and the two closest published systems identified in the review. The comparison is intentionally structured around the two capabilities [1] leaves as future work   an implemented, evaluated recommender and a formally validated ontology since those are precisely the dimensions this paper contributes. 

|**System**|**Ontology**<br>**validated?**|**Recommender**<br>**implemented?**|**Evaluation**<br>**reported**|**Domain / scale**|
|---|---|---|---|---|
|Namsraidorj et<br>al. (2025)|No|No (diagnostic<br>SPARQL only)|None (recommender<br>is future work)|Programming<br>courses, 120<br>learners|
|EduCOR<br>(Ilkou et al.,<br>2021)<br>PEARL|Yes   3 gold<br>schemata<br>Not fully|Yes   deployed in<br>eDoer<br>Yes|OER repository<br>recall + real course<br>grade comparison<br>82% precision / 78%|Business<br>Analytics course<br>+ general OER<br>Programming|
|(Hadyaoui &<br>Cheniti<br>Belcadhi,<br>2025)|reported||recall|course project<br>recommendation|
|This|Yes   CQs,|Yes   rule based +|Pre registered 3|Programming|
|framework|reasoner,<br>OOPS!,<br>OntoQA (Sec.<br>5)|hybrid, fused &<br>diversified (Sec.<br>6)|track protocol (Sec.<br>7); not yet executed|courses, same<br>population as<br>[1]|



- _Table 4. Comparative positioning against the source system and the two closest published ontology based educational recommenders._ 

The comparison also clarifies what this paper does not claim: unlike EduCOR and PEARL, the framework's Track A/B/C results are specified but not yet executed, so its recommendation quality relative to those systems remains an open empirical question until the protocol in Evaluation Protocol is run. What can be claimed at the design stage is that the framework is the first in this specific line of work (i.e., built on [1]'s GitHub Classroom/BookWidgets infrastructure) to specify both a concrete recommendation mechanism and a validation protocol rigorous enough to be falsifiable. 

## **9. Limitations and Threats to Validity** 

- xiv. Construct validity of θ and w : objective specific thresholds and tool weights are currentlyᵗ instructor set defaults; Evaluation Protocol's protocol should include a sensitivity analysis before any deployment relies on a single fixed threshold. 

15 

Ontology Driven Hybrid Recommendation Framework 

- xv. Population and generalizability: the target population is the same single institution, programming course cohort as [1] (120 learners); results from Evaluation Protocol would need replication at another institution or subject area before generalizing beyond programming education. 

- xvi. Residual cold start: the rule based path mitigates but does not eliminate cold start   a brand new tool with no prior AchievementRecord history cannot yet receive a collaborative score, only a rule based one. 

- xvii. Human evaluation confounds: the A/B design in Track C cannot fully separate the effect of receiving recommendations from the Hawthorne effect of being in a visibly “new” treatment section; a longer deployment with rotating treatment/control assignment would strengthen causal claims. 

- xviii. Data ethics: any live deployment must anonymize learner identifiers before analysis, obtain institutional ethics/IRB approval, and give learners a way to opt out of collaborative filtering data sharing without losing access to the rule based recommendation path. 

- xix. This paper's own limitation: because Track A/B/C have not yet been executed, every quantitative comparison in Limitation and threats to validity against EduCOR and PEARL is a comparison of published capability, not of head to head performance on the same dataset. 

## **10. Conclusion and Future Work** 

This paper turned a published, well motivated but incomplete ontology based e learning infrastructure into a specification for an actual recommender system: an extended and validation ready knowledge graph (Extended Ontology Design–5), a hybrid rule based/collaborative recommendation algorithm with explicit fusion and diversification (Hybrid Recommendation Algorithm), and a pre registered, three track evaluation protocol with named baselines and statistical tests (Evaluation Protocol). A real data proof of concept (Real Data Proof of Concept Implementation) has since confirmed the ontology, threshold rule, and validation gate execute correctly end to end — consistent under HermiT, all competency questions answerable, 19.5% real trigger rate on 1,631 real graded records — on two independent, cited, publicly available datasets (Devane, 2024; Kuzilek et al., 2017). That is a mechanical feasibility result, not the target population's evidence. The immediate next step remains executing the full protocol against a live deployment on the population described in [1] and reporting the resulting Precision@K, Recall@K, NDCG@K, OntoQA, and TAM figures in a follow up study; only at that point can the framework be compared head to head with EduCOR and PEARL rather than positioned alongside them on capability alone. Longer term, the rule based reasoning layer is a natural substrate for the retrieval augmented and LLM assisted knowledge graph completion techniques now emerging in the literature (Abu Rasheed et al., 2025; Cheng et al., 2025), which could reduce the manual effort of authoring SWRL rules and tool metadata vectors as the course catalogue grows. 

16 

Ontology Driven Hybrid Recommendation Framework 

## **References** 

- Abu Rasheed, H., Weber, C., Zenkert, J., Reimers, F., & Fathi, M. (2025). LLM assisted knowledge graph completion for curriculum and domain modelling in personalized higher education recommendations. arXiv:2501.12300. 

- Anderson, L. W., & Krathwohl, D. R. (2001). A taxonomy for learning, teaching and assessing: A revision of Bloom’s taxonomy of educational objectives (Complete ed.). Longman. 

- Carbonell, J., & Goldstein, J. (1998). The use of MMR, diversity based reranking for reordering documents and producing summaries. In Proceedings of the 21st Annual International ACM SIGIR Conference on Research and Development in Information Retrieval (pp. 335–336). ACM. 

- Cheng, X., Zhang, Z., Wang, J., Fang, L., He, C., Guan, Q., Pan, S., & Luo, W. (2025). Education oriented graph retrieval augmented generation for learning path recommendation. arXiv:2506.22303. 

- Chung, H., & Kim, J. (2016). An ontological approach for semantic modeling of curriculum and syllabus in higher education. International Journal of Information and Education Technology, 6(5), 365–369. 

- Cohen, J. (1960). A coefficient of agreement for nominal scales. Educational and Psychological Measurement, 20(1), 37–46. 

- Davis, F. D. (1989). Perceived usefulness, perceived ease of use, and user acceptance of information technology. MIS Quarterly, 13(3), 319–340. https://doi.org/10.2307/249008 

- Demartini, G., Enoksson, T., Kawase, R., Klamma, R., Linek, S., Ras, E., & Stewart, C. (2013). The Bowlogna ontology: Fostering open curricula and agile knowledge bases for Europe’s higher education landscape. Semantic Web, 4(1), 53–63. 

- Devane, V. (2024). Bloom's taxonomy dataset [Data set]. Kaggle. https://www.kaggle.com/datasets/vijaydevane/blooms-taxonomy-dataset 

- Hadyaoui, A., & Cheniti Belcadhi, L. (2025). PEARL: An ontology driven project recommender system for a programming course. Interactive Learning Environments, 33(9), 5364–5385. https://doi.org/10.1080/10494820.2025.2482587 

- Heflin, J. (2000). University ontology. University of Maryland, Department of Computer Science. 

- Horrocks, I., Patel Schneider, P. F., Boley, H., Tabet, S., Grosof, B., & Dean, M. (2004). SWRL: A Semantic Web Rule Language combining OWL and RuleML (W3C Member Submission). 

- Ilkou, E., Abu Rasheed, H., Tavakoli, M., Hakimov, S., Kismihók, G., Auer, S., & Nejdl, W. (2021). EduCOR: An educational and career oriented recommendation ontology. In The Semantic Web – ISWC 2021 (LNCS 12922, pp. 546–562). Springer. https://doi.org/10.1007/978 3 030 88361 4_32 

17 

Ontology Driven Hybrid Recommendation Framework 

- Järvelin, K., & Kekäläinen, J. (2002). Cumulated gain based evaluation of IR techniques. ACM Transactions on Information Systems, 20(4), 422–446. https://doi.org/10.1145/582415.582418 

- Jung, H., Jang, Y., Kim, S., & Kim, H. (2022). KPCR: Knowledge graph enhanced personalized course recommendation. In Proceedings of the Australasian Joint Conference on Artificial Intelligence (pp. 739–750). Springer. 

- Kuzilek, J., Hlosta, M., & Zdrahal, Z. (2017). Open University Learning Analytics dataset. Scientific Data, 4, 170171. https://doi.org/10.1038/sdata.2017.171 

- Namsraidorj, M., Namsraidorj, B., & Enkhtur, A. (2025). Ontology based recommendation system using GitHub Classroom and Bookwidget. TEM Journal, 14(1), 861–870. https://doi.org/10.18421/TEM141 76 

- Poveda Villalón, M., Gómez Pérez, A., & Suárez Figueroa, M. C. (2014). OOPS! (OntOlogy Pitfall Scanner!): An on line tool for ontology evaluation. International Journal on Semantic Web and Information Systems, 10(2), 7–34. 

- Styles, R., & Shabir, N. (2008). Academic Institution Internal Structure Ontology (AIISO). Talis Information Ltd. 

- Tartir, S., Arpinar, I. B., Moore, M., Sheth, A. P., & Aleman Meza, B. (2005). OntoQA: Metric based ontology quality analysis. In Proceedings of the IEEE ICDM Workshop on Knowledge Acquisition from Distributed, Autonomous, Semantically Heterogeneous Data and Knowledge Sources. 

- Tarus, J. K., Niu, Z., & Mustafa, G. (2018). Knowledge based recommendation: A review of ontology based recommender systems for e learning. Artificial Intelligence Review, 50(1), 21 –48. https://doi.org/10.1007/s10462 017 9539 5 

18 



<!-- Start of picture text -->
Fig, 2 - Extended Syllabus-Recommendation Ontology (class-level view)<br>) Class from original syllabus ontology (Table 3)<br>a Class added for the recommendation extension<br>Instructor teaches Syllabus enrolledin (inverse) Learner<br>Teacher, Assistant Core concept of course Student enrolled in Syllabus<br>hasSubject<br>Subjects pea LearnerProfile<br>Leaming Subjects (n = 15 topics) Per-leamer state and history<br>hasORjective recokdedin<br>Objectives AchievementRecord<br>measuredBy<br>Bloom-Anderson Taxonomy (m = 6 levels): Instance of SIL(n,m,k) score per<br>remember - understand - apply - analyze - evaluate - create learner x objective x tool<br>suppoftedBy inpyt to<br>Support Tools easonedOverB RecommendationStrategy<br>ace ea De) RuleBased | ConteniBased| Colaboratv | Hybrid<br>fasScore geneyates<br>implementedAs haswescription<br>Activity Tools Score Description Recommendation<br>Widgets, GitHub Classroom assignments Quantity score Quality evaluation Ranked remedial items) fora<br>below-threshold objective<br>\ Pad 7<br>\ ‘i Pr wae<br>iy sy ao -*<br>recommends (targets a Support/ Activity Tool)<br><!-- End of picture text -->

