#!/usr/bin/env python3
"""Recompute Sackett et al. (2022) structured-interview operational validity.

One command, from the repository root:

    python experiments/sackett2022/repro.py

Inputs are the means printed in the open accepted manuscript. The script does
not download the paper and does not invent any input. Missing inputs stay
UNKNOWN.

The arithmetic is deterministic. SEED is set because the packet requires a
pinned seed; no random draws are used.
"""

from __future__ import annotations

import random
import sys
from decimal import Decimal, ROUND_HALF_UP, getcontext
from typing import Optional

# Pinned environment. CI installs experiments/sackett2022/requirements.txt
# and runs this file under Python 3.12.
PINNED_PYTHON = "3.12"
PINNED_PYTEST = "8.3.5"
SEED = 20221013

getcontext().prec = 50
random.seed(SEED)


def D(value: str) -> Decimal:
    return Decimal(value)


def round_half_up(value: Decimal, places: int) -> Decimal:
    quantum = Decimal("1").scaleb(-places)
    return value.quantize(quantum, rounding=ROUND_HALF_UP)


def correct_for_criterion_unreliability(observed_r: Decimal, ryy: Decimal) -> Decimal:
    """Spearman correction: r / sqrt(ryy).

    Sackett et al. apply this before any range-restriction correction
    (open PDF p. 2). The same division reproduces their job-knowledge
    worked example, observed .31 with ryy = .60 equaling .40 (open PDF p. 18).
    """
    if ryy <= 0 or ryy > 1:
        raise ValueError(f"criterion reliability out of range: {ryy}")
    return observed_r / ryy.sqrt()


def correct_for_direct_range_restriction(reliability_corrected_r: Decimal, U: Decimal) -> Decimal:
    """Direct range-restriction correction (Thorndike Case II).

    U is unrestricted SDx / restricted SDx, which is how Sackett et al.
    define U (open PDF p. 2). Lowercase u = 1/U. The open PDF cites Hunter
    and Schmidt (2004) for the algebra and does not print it. This is the
    standard formula that turns their McDaniel reliability-corrected .37
    and U = 1.47 into .51 (Table 2).
    """
    if U <= 0:
        raise ValueError(f"U must be positive: {U}")
    r = reliability_corrected_r
    return (U * r) / (1 + (r ** 2) * (U ** 2 - 1)).sqrt()


# Table 2, open PDF p. 11. Values are copied as printed. ryy ".6" is the
# one-decimal printing of .60, the criterion reliability Sackett et al.
# adopt on open PDF p. 10.
MCDANIEL_N = 3069
MCDANIEL_K = 36
MCDANIEL_OBSERVED_R = D("0.28")
MCDANIEL_RYY = D("0.60")
MCDANIEL_U = D("1.47")
MCDANIEL_PAPER_RELIABILITY_CORRECTED = D("0.37")
MCDANIEL_PAPER_RANGE_CORRECTED = D("0.51")
MCDANIEL_PAPER_CURRENT = D("0.37")

HUFFCUTT_N = 4795
HUFFCUTT_K = 69
HUFFCUTT_OBSERVED_R = D("0.35")  # Table 2. Prose on p. 17 prints .36.
HUFFCUTT_SOURCE_RYY = D("0.52")  # reliability Huffcutt et al. used
HUFFCUTT_SACKETT_RYY = D("0.60")  # reliability Sackett et al. substitute
HUFFCUTT_U = D("1.64")  # Table 2; paper marks this correction not credible
HUFFCUTT_PREDICTIVE_U = D("1.63")  # p. 17, Salgado & Moscoso (2002), predictive studies only
HUFFCUTT_PAPER_RELIABILITY_CORRECTED = D("0.48")
HUFFCUTT_PAPER_RANGE_CORRECTED = D("0.70")
HUFFCUTT_PAPER_CURRENT = D("0.45")
HUFFCUTT_CONCURRENT_STUDY_SHARE = D("0.74")  # share of studies, p. 6 and p. 17. Not a sample-size share.

PAPER_OPERATIONAL = D("0.42")  # Table 2 overall current estimate; Table 3; Table 4
PAPER_OVERALL_OBSERVED = D("0.32")  # Table 2 overall structured row

# Worked examples used only to check the formulas, not as separate claims.
JOB_KNOWLEDGE_OBSERVED_R = D("0.31")
JOB_KNOWLEDGE_RYY = D("0.60")
JOB_KNOWLEDGE_PAPER = D("0.40")


def n_weighted_mean(pairs: list[tuple[int, Decimal]]) -> Decimal:
    numerator = sum(D(str(n)) * value for n, value in pairs)
    denominator = sum(D(str(n)) for n, _ in pairs)
    return numerator / denominator


def mcdaniel_reliability_corrected() -> Decimal:
    return correct_for_criterion_unreliability(MCDANIEL_OBSERVED_R, MCDANIEL_RYY)


def huffcutt_reliability_corrected() -> Decimal:
    """Sackett operational path for this row: ryy = .60, U not applied.

    Table 2 marks Huffcutt's U = 1.64 correction "No: assumed distribution
    with no empirical basis" and prints a current estimate of .45, which is
    the two-decimal reliability correction of the tabled observed r.
    """
    return correct_for_criterion_unreliability(HUFFCUTT_OBSERVED_R, HUFFCUTT_SACKETT_RYY)


def operational_validity() -> Decimal:
    """Sample-size-weighted mean of the two reliability-corrected estimates.

    This is the recomputation of the Table 2 / Table 3 value .42. Range
    restriction is not applied: the paper's own current-estimate column
    withholds the U values it marks as not credible.
    """
    return n_weighted_mean(
        [
            (MCDANIEL_N, mcdaniel_reliability_corrected()),
            (HUFFCUTT_N, huffcutt_reliability_corrected()),
        ]
    )


def observed_baseline() -> Decimal:
    """Trivial baseline: the N-weighted observed correlation, with no correction."""
    return n_weighted_mean(
        [
            (MCDANIEL_N, MCDANIEL_OBSERVED_R),
            (HUFFCUTT_N, HUFFCUTT_OBSERVED_R),
        ]
    )


def partial_predictive_blend(
    predictive_observed_r: Optional[Decimal],
    predictive_n: Optional[int],
    concurrent_observed_r: Optional[Decimal],
    concurrent_n: Optional[int],
) -> Optional[Decimal]:
    """Apply U = 1.63 only to Huffcutt's predictive studies.

    The open PDF does not report the predictive-versus-concurrent split of
    the observed correlation or of N. Those inputs are UNKNOWN. This function
    returns None unless every one of them is supplied. It never fills them in.
    """
    if (
        predictive_observed_r is None
        or predictive_n is None
        or concurrent_observed_r is None
        or concurrent_n is None
    ):
        return None
    predictive = correct_for_direct_range_restriction(
        correct_for_criterion_unreliability(predictive_observed_r, HUFFCUTT_SACKETT_RYY),
        HUFFCUTT_PREDICTIVE_U,
    )
    concurrent = correct_for_criterion_unreliability(concurrent_observed_r, HUFFCUTT_SACKETT_RYY)
    return n_weighted_mean([(predictive_n, predictive), (concurrent_n, concurrent)])


def u_from_U(U: Decimal) -> Decimal:
    """u is restricted SD / unrestricted SD. Sackett et al. set u = 1/U (p. 18)."""
    return D("1") / U


def build_report() -> dict[str, str]:
    ours = operational_validity()
    baseline = observed_baseline()
    mcdaniel_rel = mcdaniel_reliability_corrected()
    huffcutt_rel = huffcutt_reliability_corrected()
    mcdaniel_rr_from_paper_rel = correct_for_direct_range_restriction(
        MCDANIEL_PAPER_RELIABILITY_CORRECTED, MCDANIEL_U
    )
    huffcutt_rr_from_paper_rel = correct_for_direct_range_restriction(
        HUFFCUTT_PAPER_RELIABILITY_CORRECTED, HUFFCUTT_U
    )
    job_knowledge = correct_for_criterion_unreliability(JOB_KNOWLEDGE_OBSERVED_R, JOB_KNOWLEDGE_RYY)
    partial = partial_predictive_blend(None, None, None, None)

    def six(value: Decimal) -> str:
        return format(round_half_up(value, 6), "f")

    report = {
        "seed": str(SEED),
        "python": sys.version.split()[0],
        "pinned_python": PINNED_PYTHON,
        "pinned_pytest": PINNED_PYTEST,
        "paper_operational": format(PAPER_OPERATIONAL, "f"),
        "ours_exact": format(ours, "f"),
        "ours_six": six(ours),
        "ours_two_decimals": format(round_half_up(ours, 2), "f"),
        "delta_exact": format(ours - PAPER_OPERATIONAL, "f"),
        "delta_six": six(ours - PAPER_OPERATIONAL),
        "delta_two_decimals": format(round_half_up(ours, 2) - PAPER_OPERATIONAL, "f"),
        "baseline_exact": format(baseline, "f"),
        "baseline_six": six(baseline),
        "baseline_two_decimals": format(round_half_up(baseline, 2), "f"),
        "mcdaniel_reliability_ours": six(mcdaniel_rel),
        "mcdaniel_reliability_paper": format(MCDANIEL_PAPER_RELIABILITY_CORRECTED, "f"),
        "mcdaniel_reliability_delta": six(mcdaniel_rel - MCDANIEL_PAPER_RELIABILITY_CORRECTED),
        "huffcutt_reliability_ours": six(huffcutt_rel),
        "huffcutt_current_paper": format(HUFFCUTT_PAPER_CURRENT, "f"),
        "mcdaniel_rr_check": six(mcdaniel_rr_from_paper_rel),
        "mcdaniel_rr_paper": format(MCDANIEL_PAPER_RANGE_CORRECTED, "f"),
        "huffcutt_rr_check": six(huffcutt_rr_from_paper_rel),
        "huffcutt_rr_paper": format(HUFFCUTT_PAPER_RANGE_CORRECTED, "f"),
        "job_knowledge_check": six(job_knowledge),
        "job_knowledge_paper": format(JOB_KNOWLEDGE_PAPER, "f"),
        "mcdaniel_u": six(u_from_U(MCDANIEL_U)),
        "huffcutt_u": six(u_from_U(HUFFCUTT_U)),
        "huffcutt_predictive_u": six(u_from_U(HUFFCUTT_PREDICTIVE_U)),
        "partial_u": "UNKNOWN" if partial is None else format(partial, "f"),
        "headline_status": (
            "reproduced at two decimals"
            if round_half_up(ours, 2) == PAPER_OPERATIONAL
            else "did not reproduce"
        ),
        "mcdaniel_reliability_status": (
            "reproduced at two decimals"
            if round_half_up(mcdaniel_rel, 2) == MCDANIEL_PAPER_RELIABILITY_CORRECTED
            else "did not reproduce"
        ),
        "huffcutt_full_rr_status": (
            "reproduced at two decimals"
            if round_half_up(huffcutt_rr_from_paper_rel, 2) == HUFFCUTT_PAPER_RANGE_CORRECTED
            else "did not reproduce"
        ),
    }
    return report


def format_report(report: dict[str, str]) -> str:
    lines = [
        "Sackett et al. 2022 structured interviews",
        f"seed: {report['seed']}",
        f"python: {report['python']} (pinned CI line: {report['pinned_python']}; pytest {report['pinned_pytest']})",
        f"paper_operational (estimated/reported): {report['paper_operational']}",
        f"ours_exact (system-verified): {report['ours_exact']}",
        f"ours_six_decimals (system-verified): {report['ours_six']}",
        f"ours_two_decimals (system-verified): {report['ours_two_decimals']}",
        f"delta_exact (system-verified, ours minus paper): {report['delta_exact']}",
        f"delta_six_decimals (system-verified): {report['delta_six']}",
        f"delta_two_decimals (system-verified): {report['delta_two_decimals']}",
        f"baseline_observed_r (system-verified): {report['baseline_six']}",
        f"headline_status: {report['headline_status']}",
        f"mcdaniel_reliability_ours (system-verified): {report['mcdaniel_reliability_ours']}",
        f"mcdaniel_reliability_paper (estimated/reported): {report['mcdaniel_reliability_paper']}",
        f"mcdaniel_reliability_status: {report['mcdaniel_reliability_status']}",
        f"huffcutt_full_range_restriction_ours (system-verified): {report['huffcutt_rr_check']}",
        f"huffcutt_full_range_restriction_paper (estimated/reported): {report['huffcutt_rr_paper']}",
        f"huffcutt_full_range_restriction_status: {report['huffcutt_full_rr_status']}",
        f"mcdaniel_u (system-verified, 1/U): {report['mcdaniel_u']}",
        f"huffcutt_u (system-verified, 1/U): {report['huffcutt_u']}",
        f"huffcutt_predictive_u (system-verified, 1/U): {report['huffcutt_predictive_u']}",
        f"partial_predictive_U_blend: {report['partial_u']}",
        f"job_knowledge_formula_check (system-verified): {report['job_knowledge_check']}",
    ]
    return "\n".join(lines) + "\n"


def main() -> int:
    if sys.version_info < (3, 11):
        print("Python 3.11 or newer is required.", file=sys.stderr)
        return 1
    report = build_report()
    sys.stdout.write(format_report(report))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
