"""Tests for the Sackett et al. (2022) structured-interview recomputation."""

from __future__ import annotations

import subprocess
import sys
from decimal import Decimal
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = Path(__file__).resolve().parent / "repro.py"
sys.path.insert(0, str(SCRIPT.parent))

import repro  # noqa: E402


def test_pinned_seed_and_versions():
    assert repro.SEED == 20221013
    assert repro.PINNED_PYTEST == "8.3.5"
    assert repro.PINNED_PYTHON == "3.12"


def test_job_knowledge_formula_matches_paper_example():
    got = repro.correct_for_criterion_unreliability(
        repro.JOB_KNOWLEDGE_OBSERVED_R, repro.JOB_KNOWLEDGE_RYY
    )
    assert repro.round_half_up(got, 2) == repro.JOB_KNOWLEDGE_PAPER


def test_case_ii_matches_mcdaniel_table_range_correction():
    got = repro.correct_for_direct_range_restriction(
        repro.MCDANIEL_PAPER_RELIABILITY_CORRECTED, repro.MCDANIEL_U
    )
    assert repro.round_half_up(got, 2) == repro.MCDANIEL_PAPER_RANGE_CORRECTED


def test_headline_matches_paper_at_two_decimals():
    ours = repro.operational_validity()
    assert repro.round_half_up(ours, 2) == Decimal("0.42")
    assert ours < Decimal("0.42")
    assert ours > Decimal("0.41")


def test_mcdaniel_reliability_intermediate_did_not_reproduce():
    got = repro.mcdaniel_reliability_corrected()
    assert repro.round_half_up(got, 2) == Decimal("0.36")
    assert repro.round_half_up(got, 2) != repro.MCDANIEL_PAPER_RELIABILITY_CORRECTED


def test_huffcutt_full_range_restriction_did_not_reproduce():
    got = repro.correct_for_direct_range_restriction(
        repro.HUFFCUTT_PAPER_RELIABILITY_CORRECTED, repro.HUFFCUTT_U
    )
    assert repro.round_half_up(got, 2) != repro.HUFFCUTT_PAPER_RANGE_CORRECTED


def test_unknown_predictive_split_is_not_guessed():
    assert repro.partial_predictive_blend(None, None, None, None) is None


def test_observed_baseline_rounds_to_table_overall():
    assert repro.round_half_up(repro.observed_baseline(), 2) == Decimal("0.32")


def test_command_prints_labeled_headline():
    completed = subprocess.run(
        [sys.executable, str(SCRIPT)],
        check=True,
        capture_output=True,
        text=True,
        cwd=ROOT,
    )
    text = completed.stdout
    assert "paper_operational (estimated/reported): 0.42" in text
    assert "ours_six_decimals (system-verified): 0.416580" in text
    assert "delta_six_decimals (system-verified): -0.003420" in text
    assert "baseline_observed_r (system-verified): 0.322682" in text
    assert "headline_status: reproduced at two decimals" in text
    assert "mcdaniel_reliability_status: did not reproduce" in text
    assert "partial_predictive_U_blend: UNKNOWN" in text
    assert "mcdaniel_u (system-verified, 1/U): 0.680272" in text
    assert "seed: 20221013" in text


def test_result_md_matches_the_command():
    text = (SCRIPT.parent / "RESULT.md").read_text(encoding="utf-8")
    for snippet in (
        "0.416580",
        "0.42",
        "-0.003420",
        "0.322682",
        "system-verified",
        "estimated/reported",
        "did not reproduce",
        "UNKNOWN",
        "0.361478",
    ):
        assert snippet in text


def test_site_shows_both_results():
    html = (ROOT / "site" / "index.html").read_text(encoding="utf-8")
    assert "0.416580" in html
    assert "BLOCKED" in html
    assert "system-verified" in html
    assert "estimated/reported" in html


def test_requirements_pin_matches_module():
    pinned = (SCRIPT.parent / "requirements.txt").read_text(encoding="utf-8")
    assert f"pytest=={repro.PINNED_PYTEST}" in pinned

