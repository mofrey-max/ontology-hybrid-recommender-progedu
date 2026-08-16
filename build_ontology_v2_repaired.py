"""
v2: Repairs the four pitfalls flagged by a real OOPS! scan of extended_ontology.owl:
  P08 (Minor)     Missing annotations       -> rdfs:comment added to all 40 schema elements
  P10 (Important) Missing disjointness      -> pairwise owl:disjointWith across the 14 core classes
  P13 (Minor)     Inverse relationships     -> owl:inverseOf declared for all 17 object properties
  P36 (Minor)     URI contains file extension -> base IRI no longer ends in .owl

Same real data as before: Devane (2024) Bloom's Taxonomy Dataset (Objectives layer)
+ Kuzilek et al. (2017) OULAD, module AAA_2013J (Learner/Achievement layer).
"""

from owlready2 import *
import pandas as pd
import json

# P36 fix: no file extension in the base IRI
onlp = get_ontology("http://example.org/ontology-hybrid-recsys#")

with onlp:
    # ---------- 8 ORIGINAL CLASSES ----------
    class Syllabus(Thing):
        comment = ["A single course offering (module + presentation) that a learner enrolls in."]
    class Instructor(Thing):
        comment = ["The teacher or teaching assistant responsible for a Syllabus."]
    class Subjects(Thing):
        comment = ["A topic area within a Syllabus (n subjects per course)."]
    class Objectives(Thing):
        comment = ["A learning objective within a Subject, e.g. a Bloom-Anderson cognitive level or a real graded milestone."]
    class SupportTools(Thing):
        comment = ["A grouping of activity tools that support a given Objective."]
    class ActivityTools(Thing):
        comment = ["A concrete learning/assessment tool (assignment, widget, quiz) a learner interacts with."]
    class Score(Thing):
        comment = ["A quantitative score produced by an ActivityTools interaction."]
    class Description(Thing):
        comment = ["A qualitative, human-readable evaluation attached to an ActivityTools interaction."]

    # ---------- 5 EXTENSION CLASSES ----------
    class Learner(Thing):
        comment = ["A student enrolled in a Syllabus."]
    class LearnerProfile(Thing):
        comment = ["A Learner's per-course state and history."]
    class AchievementRecord(Thing):
        comment = ["An SIL(n,m,k)-style score for one learner x objective x tool combination."]
    class RecommendationStrategy(Thing):
        comment = ["The mechanism (RuleBased, ContentBased, Collaborative, or Hybrid) that produced a Recommendation."]
    class Recommendation(Thing):
        comment = ["A ranked remedial item generated for a learner on a below-threshold Objective."]

    # ---------- Implementation-support class ----------
    class QuestionExemplar(Thing):
        comment = ["A real, human-classified question item exemplifying a Bloom-Anderson Objective (Devane, 2024)."]

    # ---------- Object properties, each with an explicit inverse (fixes P13) ----------
    class teaches(ObjectProperty):
        domain = [Instructor]; range = [Syllabus]
        comment = ["Relates an Instructor to the Syllabus they teach."]
    class isTaughtBy(ObjectProperty):
        domain = [Syllabus]; range = [Instructor]; inverse_property = teaches
        comment = ["Inverse of teaches."]

    class hasSubject(ObjectProperty):
        domain = [Syllabus]; range = [Subjects]
        comment = ["Relates a Syllabus to one of its constituent Subjects."]
    class isSubjectOf(ObjectProperty):
        domain = [Subjects]; range = [Syllabus]; inverse_property = hasSubject
        comment = ["Inverse of hasSubject."]

    class hasObjective(ObjectProperty):
        domain = [Subjects]; range = [Objectives]
        comment = ["Relates a Subject to one of its Objectives."]
    class isObjectiveOfSubject(ObjectProperty):
        domain = [Objectives]; range = [Subjects]; inverse_property = hasObjective
        comment = ["Inverse of hasObjective."]

    class supportedBy(ObjectProperty):
        domain = [Objectives]; range = [SupportTools]
        comment = ["Relates an Objective to the SupportTools that support it."]
    class supports(ObjectProperty):
        domain = [SupportTools]; range = [Objectives]; inverse_property = supportedBy
        comment = ["Inverse of supportedBy."]

    class hasActivityTool(ObjectProperty):
        domain = [SupportTools]; range = [ActivityTools]
        comment = ["Relates SupportTools to a concrete ActivityTools instance."]
    class isActivityToolOf(ObjectProperty):
        domain = [ActivityTools]; range = [SupportTools]; inverse_property = hasActivityTool
        comment = ["Inverse of hasActivityTool."]

    class hasScore(ObjectProperty):
        domain = [ActivityTools]; range = [Score]
        comment = ["Relates an ActivityTools interaction to its quantitative Score."]
    class isScoreOf(ObjectProperty):
        domain = [Score]; range = [ActivityTools]; inverse_property = hasScore
        comment = ["Inverse of hasScore."]

    class hasDescription(ObjectProperty):
        domain = [ActivityTools]; range = [Description]
        comment = ["Relates an ActivityTools interaction to its qualitative Description."]
    class isDescriptionOf(ObjectProperty):
        domain = [Description]; range = [ActivityTools]; inverse_property = hasDescription
        comment = ["Inverse of hasDescription."]

    class enrolledIn(ObjectProperty):
        domain = [Learner]; range = [Syllabus]
        comment = ["Relates a Learner to the Syllabus they are enrolled in."]
    class hasEnrolledLearner(ObjectProperty):
        domain = [Syllabus]; range = [Learner]; inverse_property = enrolledIn
        comment = ["Inverse of enrolledIn."]

    class hasProfile(ObjectProperty):
        domain = [Learner]; range = [LearnerProfile]
        comment = ["Relates a Learner to their LearnerProfile."]
    class isProfileOf(ObjectProperty):
        domain = [LearnerProfile]; range = [Learner]; inverse_property = hasProfile
        comment = ["Inverse of hasProfile."]

    class recordedIn(ObjectProperty):
        domain = [AchievementRecord]; range = [LearnerProfile]
        comment = ["Relates an AchievementRecord to the LearnerProfile it belongs to."]
    class hasAchievementRecord(ObjectProperty):
        domain = [LearnerProfile]; range = [AchievementRecord]; inverse_property = recordedIn
        comment = ["Inverse of recordedIn."]

    class forObjective(ObjectProperty):
        domain = [AchievementRecord]; range = [Objectives]
        comment = ["Relates an AchievementRecord to the Objective it measures."]
    class isObjectiveOfAchievement(ObjectProperty):
        domain = [Objectives]; range = [AchievementRecord]; inverse_property = forObjective
        comment = ["Inverse of forObjective."]

    class measuredBy(ObjectProperty):
        domain = [AchievementRecord]; range = [ActivityTools]
        comment = ["Relates an AchievementRecord to the ActivityTools instance that produced it."]
    class measures(ObjectProperty):
        domain = [ActivityTools]; range = [AchievementRecord]; inverse_property = measuredBy
        comment = ["Inverse of measuredBy."]

    class generatedBy(ObjectProperty):
        domain = [Recommendation]; range = [RecommendationStrategy]
        comment = ["Relates a Recommendation to the RecommendationStrategy that produced it."]
    class generates(ObjectProperty):
        domain = [RecommendationStrategy]; range = [Recommendation]; inverse_property = generatedBy
        comment = ["Inverse of generatedBy."]

    class reasonedOverBy(ObjectProperty):
        domain = [AchievementRecord]; range = [RecommendationStrategy]
        comment = ["Relates an AchievementRecord to the RecommendationStrategy that reasoned over it."]
    class reasonsOver(ObjectProperty):
        domain = [RecommendationStrategy]; range = [AchievementRecord]; inverse_property = reasonedOverBy
        comment = ["Inverse of reasonedOverBy."]

    class hasRecommendation(ObjectProperty):
        domain = [Learner]; range = [Recommendation]
        comment = ["Relates a Learner to a Recommendation generated for them."]
    class isRecommendationFor(ObjectProperty):
        domain = [Recommendation]; range = [Learner]; inverse_property = hasRecommendation
        comment = ["Inverse of hasRecommendation."]

    class targets(ObjectProperty):
        domain = [Recommendation]; range = [ActivityTools]
        comment = ["Relates a Recommendation to the ActivityTools instance it points the learner to."]
    class isTargetOf(ObjectProperty):
        domain = [ActivityTools]; range = [Recommendation]; inverse_property = targets
        comment = ["Inverse of targets."]

    class exemplifies(ObjectProperty):
        domain = [QuestionExemplar]; range = [Objectives]
        comment = ["Relates a real classified QuestionExemplar to the Bloom-Anderson Objective it exemplifies."]
    class hasExemplar(ObjectProperty):
        domain = [Objectives]; range = [QuestionExemplar]; inverse_property = exemplifies
        comment = ["Inverse of exemplifies."]

    # ---------- Data properties, each with a comment (fixes P08 for these too) ----------
    class silScore(AchievementRecord >> float):
        comment = ["The normalized SIL(n,m,k) score, in [0,1], for this AchievementRecord."]
    class thresholdTheta(AchievementRecord >> float):
        comment = ["The threshold theta below which this AchievementRecord triggers a Recommendation."]
    class isBelowThreshold(AchievementRecord >> bool):
        comment = ["True if silScore < thresholdTheta for this AchievementRecord."]
    class bloomLevel(Objectives >> str):
        comment = ["The Bloom-Anderson cognitive level name for a canonical Objective."]
    class strategyName(RecommendationStrategy >> str):
        comment = ["The name of the RecommendationStrategy (RuleBased, ContentBased, Collaborative, Hybrid)."]
    class questionText(QuestionExemplar >> str):
        comment = ["The real question text from the source dataset (truncated to 300 chars)."]
    class sourceDataset(Thing >> str):
        comment = ["The cited real dataset an individual's data was drawn from."]
    class finalResult(LearnerProfile >> str):
        comment = ["The learner's real final course outcome (Pass/Fail/Withdrawn/Distinction), OULAD."]
    class assessmentType(Objectives >> str):
        comment = ["The real OULAD assessment type (e.g. TMA) for a non-Bloom-classified Objective."]

    # ---------- P10 fix: pairwise disjointness among the 14 core schema classes ----------
    AllDisjoint([Syllabus, Instructor, Subjects, Objectives, SupportTools, ActivityTools,
                 Score, Description, Learner, LearnerProfile, AchievementRecord,
                 RecommendationStrategy, Recommendation, QuestionExemplar])

rule_based = onlp.RecommendationStrategy("RuleBased_ThresholdTrigger")
rule_based.strategyName = ["RuleBased"]

# =========================================================================
# TRACK 1 — Devane (2024) Bloom's Taxonomy Dataset
# =========================================================================
print("Loading Bloom's Taxonomy dataset (Devane, 2024)...")
bloom_df = pd.read_csv("/home/claude/data/bloom/blooms_taxonomy_dataset.csv")
bt_map = {"BT1": "Remember", "BT2": "Understand", "BT3": "Apply",
          "BT4": "Analyze", "BT5": "Evaluate", "BT6": "Create"}

canonical_objectives = {}
for code, name in bt_map.items():
    obj = onlp.Objectives(f"Objective_{name}_BloomCanonical")
    obj.bloomLevel = [name]
    obj.sourceDataset = ["Devane (2024) Bloom's Taxonomy Dataset, Kaggle"]
    canonical_objectives[code] = obj

n_bloom = 0
for _, row in bloom_df.iterrows():
    code = row["Category"]
    if code not in canonical_objectives:
        continue
    qi = onlp.QuestionExemplar(f"Question_{n_bloom:05d}")
    qi.questionText = [str(row["Questions"])[:300]]
    qi.sourceDataset = ["Devane (2024) Bloom's Taxonomy Dataset, Kaggle"]
    onlp.exemplifies[qi].append(canonical_objectives[code])
    n_bloom += 1
print(f"  -> {n_bloom} real classified question exemplars")

# =========================================================================
# TRACK 2 — Kuzilek et al. (2017) OULAD, module AAA_2013J
# =========================================================================
print("Loading OULAD (Kuzilek et al., 2017), module AAA_2013J...")
si = pd.read_csv("/home/claude/data/oulad/studentInfo.csv")
sa = pd.read_csv("/home/claude/data/oulad/studentAssessment.csv")
assess = pd.read_csv("/home/claude/data/oulad/assessments.csv")

si_aaa = si[(si.code_module == "AAA") & (si.code_presentation == "2013J")]
assess_aaa = assess[(assess.code_module == "AAA") & (assess.code_presentation == "2013J")
                     & (assess.assessment_type == "TMA")].sort_values("id_assessment")
merged = sa.merge(assess_aaa, on="id_assessment").dropna(subset=["score"])

syllabus = onlp.Syllabus("Syllabus_AAA_2013J")
syllabus.sourceDataset = ["Kuzilek, Hlosta & Zdrahal (2017) OULAD"]
subject = onlp.Subjects("Subject_AAA")
onlp.hasSubject[syllabus].append(subject)

THETA = 0.60
tma_objectives = {}
for i, (_, arow) in enumerate(assess_aaa.iterrows(), start=1):
    aid = arow["id_assessment"]
    objn = onlp.Objectives(f"Objective_TMA{i:02d}_AAA2013J")
    objn.assessmentType = ["TMA"]
    objn.sourceDataset = ["Kuzilek, Hlosta & Zdrahal (2017) OULAD"]
    onlp.hasObjective[subject].append(objn)
    support = onlp.SupportTools(f"Support_TMA{i:02d}_AAA2013J")
    onlp.supportedBy[objn].append(support)
    activity = onlp.ActivityTools(f"Activity_TMA{i:02d}_AAA2013J")
    onlp.hasActivityTool[support].append(activity)
    tma_objectives[aid] = (objn, activity, i)

n_learners = n_achievements = n_recommendations = 0
outcome_log = []

for _, srow in si_aaa.iterrows():
    sid = int(srow["id_student"])
    learner = onlp.Learner(f"Learner_{sid}")
    profile = onlp.LearnerProfile(f"Profile_{sid}")
    onlp.enrolledIn[learner].append(syllabus)
    onlp.hasProfile[learner].append(profile)
    profile.finalResult = [str(srow["final_result"])]
    n_learners += 1

    student_records = merged[merged.id_student == sid]
    below_flags = []
    for _, rec in student_records.iterrows():
        aid = rec["id_assessment"]
        if aid not in tma_objectives:
            continue
        objn, activity, tma_num = tma_objectives[aid]
        score = float(rec["score"])
        sil = round(score / 100.0, 3)
        below = sil < THETA
        below_flags.append(below)

        ach = onlp.AchievementRecord(f"Achievement_{sid}_TMA{tma_num:02d}")
        onlp.recordedIn[ach].append(profile)
        onlp.forObjective[ach].append(objn)
        onlp.measuredBy[ach].append(activity)
        ach.silScore = [sil]
        ach.thresholdTheta = [THETA]
        ach.isBelowThreshold = [below]
        onlp.reasonedOverBy[ach].append(rule_based)
        n_achievements += 1

        if below:
            rec_ind = onlp.Recommendation(f"Recommendation_{sid}_TMA{tma_num:02d}")
            onlp.generatedBy[rec_ind].append(rule_based)
            onlp.targets[rec_ind].append(activity)
            onlp.hasRecommendation[learner].append(rec_ind)
            n_recommendations += 1

    outcome_log.append({
        "student_id": sid, "final_result": str(srow["final_result"]),
        "n_submitted": len(student_records),
        "n_below_threshold": sum(below_flags),
        "any_recommendation": any(below_flags) if below_flags else False
    })

print(f"  -> {n_learners} real learners, {n_achievements} real AchievementRecords, {n_recommendations} real Recommendations")

onlp.save(file="/home/claude/extended_ontology_v2_repaired.owl", format="rdfxml")
with open("/home/claude/outcome_log_v2.json", "w") as f:
    json.dump(outcome_log, f, indent=2)

print("Saved extended_ontology_v2_repaired.owl")
print(f"Total individuals: {len(list(onlp.individuals()))}")
print(f"Total classes: {len(list(onlp.classes()))}")
print(f"Total object properties: {len(list(onlp.object_properties()))}")
print(f"Total data properties: {len(list(onlp.data_properties()))}")
