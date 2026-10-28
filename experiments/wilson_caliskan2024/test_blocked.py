"""The Wilson and Caliskan experiment is a blocked write-up, not a run."""

from pathlib import Path

RESULT = Path(__file__).resolve().parent / "RESULT.md"


def test_result_is_blocked_at_step_zero():
    text = RESULT.read_text(encoding="utf-8")
    assert "BLOCKED" in text
    assert "Step 0" in text
    assert "No reproduction was attempted" in text
    assert "FACT" in text
    assert "INFERENCE" in text
    assert "UNKNOWN" in text
    # A completed re-run would name a model and an occupation. This write-up must not.
    assert "intfloat/e5-mistral-7b-instruct" not in text
    assert "White-vs-Black preference rate we computed" not in text
