# Lab 1: Introduction to AI & Paradigms
# Review = flag for a human reviewer, not an award decision.
# All thresholds are synthetic lab assumptions, not real policy.

# ---------- Part 1: symbolic rule vs probability threshold (Sec 1.5) ----------
def symbolic(score, complete):
    if complete and score >= 70:
        return "Review"
    return "Hold"

def threshold(probability):
    if probability >= 0.70:
        return "Review"
    return "Hold"

print("Part 1: symbolic vs threshold")
print("case | symbolic | threshold | disagreement")
for name, score, complete, prob in [
    ("complete_high", 82, True, 0.81),
    ("complete_low", 68, True, 0.74),
    ("incomplete_high", 91, False, 0.88),
    ("boundary", 70, True, 0.70),
]:
    a, b = symbolic(score, complete), threshold(prob)
    print(name, "|", a, "|", b, "|", a != b)

# ---------- Part 2: Task 2 - two extra conditions ----------
# Old: score >= 70, documents complete
# New 1: attendance >= 75 | New 2: fee cleared
def rule(score, documents, attendance, fee):
    if score >= 70 and documents and attendance >= 75 and fee:
        return "Review"
    return "Hold"

print("\nPart 2: Task 2 rule tests")
for name, score, docs, att, fee, expected, reason in [
    ("pass_all", 82, True, 90, True, "Review", "All four conditions pass"),
    ("fail_attendance", 85, True, 60, True, "Hold", "Attendance 60 < 75"),
    ("fail_fee", 88, True, 92, False, "Hold", "Fee not cleared"),
    ("boundary_score", 70, True, 80, True, "Review", "Score exactly 70, boundary passes"),
]:
    actual = rule(score, docs, att, fee)
    print("case:", name, "| input: score =", score, "documents =", docs,
          "attendance =", att, "fee =", fee)
    print("expected:", expected, "| actual:", actual, "| reason:", reason)
