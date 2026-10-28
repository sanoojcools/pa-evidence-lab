# People Analytics Evidence Lab

This repository recomputes published people-analytics numbers and says, for each one, whether we computed it or took it from a paper.

**Beat the trivial baseline before claiming a win.** A corrected correlation that is larger than the raw correlation only because it was divided by the square root of a reliability is the correction itself. Matching a published headline is a computation check. It is not a claim that a selection procedure beat a harder baseline.

**Every number is labeled.**

- **system-verified** means this repository computed it.
- **estimated/reported** means it is taken from a paper, a README, or the approved packet, and was not recomputed.

Approval: `WE-PAEL-2026-10-13-APPROVED`. Scope chosen by Sanuj: Sackett et al. (2022) in full, and Wilson and Caliskan (2024) as a blocked Step 0 write-up. Bertrand and Mullainathan (2004) and the attrition model are out of scope.

## Roles

| Role | What they do here |
| --- | --- |
| Reader | Start with this file and the results table. Open `site/index.html` for the same two write-ups on one page. |
| Builder | Run `python experiments/sackett2022/repro.py` from a clean checkout. Inputs, formula, and the UNKNOWN list are in `papers/sackett2022/EXTRACT.md`. |
| Reviewer | Grade the packet's acceptance checks in `REVIEW.md`. The grade is separate from the build. |
| Interface | `site/` is the static page. `.github/workflows/pages.yml` is the GitHub Actions Pages deploy. `.github/workflows/ci.yml` runs the Sackett reproduction and the tests. |

## One command

```bash
python experiments/sackett2022/repro.py
```

Pinned seed `20221013`. CI Python `3.12`. Test pin `pytest==8.3.5` in `experiments/sackett2022/requirements.txt`. The reproduction uses the standard library only. The calculation does not draw random numbers. The seed is set so the packet's pin is visible in the output.

```bash
python -m pip install -r experiments/sackett2022/requirements.txt
python -m pytest experiments/sackett2022 experiments/wilson_caliskan2024 -q
```

## Results

| Experiment | Quantity | Number | Label |
| --- | --- | --- | --- |
| Sackett et al. 2022, structured interviews | Paper operational validity | 0.42 | estimated/reported |
| Sackett et al. 2022, structured interviews | Recomputed operational validity | 0.416580 (0.42 at two decimals) | system-verified |
| Sackett et al. 2022, structured interviews | Delta, ours minus 0.42 | -0.003420 | system-verified |
| Sackett et al. 2022, structured interviews | Trivial baseline, N-weighted observed r | 0.322682 | system-verified |
| Sackett et al. 2022, structured interviews | McDaniel reliability cell, recomputed | 0.361478 | system-verified |
| Sackett et al. 2022, structured interviews | McDaniel reliability cell, paper | 0.37 | estimated/reported. did not reproduce |
| Sackett et al. 2022, structured interviews | Two-decimal headline status | reproduced at two decimals | system-verified comparison |
| Wilson & Caliskan 2024 | Status | BLOCKED at Step 0 | no system-verified rate |
| Wilson & Caliskan 2024 | Packet target preference rate | about 85% | estimated/reported from the packet. Not checked against the paper here. Not computed |
| Wilson & Caliskan 2024 | Packet no-preference baseline | 50% | estimated/reported from the packet. Not computed |

Detail: `experiments/sackett2022/RESULT.md` and `experiments/wilson_caliskan2024/RESULT.md`.

## Hosting

The static page is `site/index.html`. The deploy workflow is `.github/workflows/pages.yml`. On 28 Oct 2026 this repository had `has_pages` false, `https://sanoojcools.github.io/pa-evidence-lab/` returned HTTP 404, and `POST /repos/sanoojcools/pa-evidence-lab/pages` with `{"build_type":"workflow"}` returned **403 Resource not accessible by integration**. Enabling Pages is a repository setting this token cannot change. The workflow is not run from the draft pull request, and this branch is not merged to get around that.
