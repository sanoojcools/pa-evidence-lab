# Reviewer pass

No-edit review of the branch `cursor/pa-evidence-lab-mvp-1b05` against packet `WE-PAEL-2026-10-13`, section 5, after the build. This pass does not change the reproduction. An independent Python review of `repro.py` and the tests required no change before merge.

Reference for Sackett: open accepted manuscript, structured-interview operational validity **0.42** (Table 2 overall current estimate, Table 3, Table 4 ryy = .60 column). Reference for Wilson: Step 0 of the packet. If the released code lacks resumes and name lists, the experiment is blocked.

## Grades

| Check | Sackett et al. 2022 | Wilson & Caliskan 2024 |
| --- | --- | --- |
| EXTRACT cites every reported number | PASS | BLOCKED |
| One command reproduces it from a clean environment | PASS | BLOCKED |
| RESULT shows paper vs ours, the delta, and a baseline | PASS | BLOCKED |
| Reviewer records accept or reject against the reference | ACCEPT the two-decimal headline. REJECT the McDaniel 0.37 cell and the Huffcutt range-restriction steps | REJECT the re-run. BLOCKED at Step 0 |
| FACT / INFERENCE / UNKNOWN, and system-verified vs estimated/reported on every number | PASS | PASS |
| Names the exact model, occupation, and sample size, and claims nothing beyond them | Not this check. The check is for experiment 1 | BLOCKED |
| Hosted proof: live-page screenshot and a passing CI link | BLOCKED | BLOCKED |
| Pull request on `sanoojcools/pa-evidence-lab` | PASS | PASS |

## Reasons

**EXTRACT (Sackett), PASS.** `papers/sackett2022/EXTRACT.md` gives a page or table for each printed input the reproduction uses: Table 2 Ns, observed rs, reliabilities, U values, and current estimates; the 0.60 reliability rule on p. 10; the correction order and the definition of U on p. 2; the u = 1/U example on p. 18; the 74% concurrent share on pp. 6 and 17; the headline 0.42 on pp. 11, 15, and 17. Europe PMC has no full text. The numbers come from the GREEN open PDF, not a paywalled scrape. Unknown splits are marked UNKNOWN.

**EXTRACT (Wilson), BLOCKED.** The chosen scope asked for a Step 0 write-up in `experiments/wilson_caliskan2024/RESULT.md` only. No paper extract was written, and no paper number was taken, because the experiment stopped before a re-run.

**One command (Sackett), PASS.** `python experiments/sackett2022/repro.py` is the command. Seed 20221013, pytest 8.3.5, CI Python 3.12. GitHub Actions run [40686325809](https://github.com/sanoojcools/pa-evidence-lab/actions/runs/40686325809) completed with conclusion success on pull request head `f5c3ea6`, which is the reproduction commit. The job ran the script and the tests on a clean runner.

**One command (Wilson), BLOCKED.** There is no reproduction command. That is the Step 0 stop, not a missing script for a run that should have happened.

**RESULT (Sackett), PASS.** `experiments/sackett2022/RESULT.md` has the paper value 0.42 (estimated/reported), ours 0.416580 (system-verified), delta −0.003420 (system-verified), and the trivial baseline 0.322682 (system-verified), which is the N-weighted observed correlation. The write-up says the gap over that baseline is the reliability division and is not a win. Two-decimal status is reproduced. The McDaniel reliability cell and the Huffcutt full range-restriction cell are marked did not reproduce after one correction pass each. The partial predictive blend stays UNKNOWN.

**RESULT (Wilson), BLOCKED.** There is no "ours" rate, so there is no delta. The packet's 50% no-preference baseline is stated as estimated/reported and not computed. That is the right blocked RESULT. It does not satisfy the check for a finished re-run.

**Accept / reject against the reference.**

- Structured-interview operational validity at the paper's two decimals: **ACCEPT**. Ours rounds half-up from 0.416580 to 0.42. The exact delta is −0.003420. The path is the sample-size-weighted Spearman correction of Table 2's observed 0.28 (N = 3,069) and 0.35 (N = 4,795) with ryy = 0.60, which is the paper's own rule when it withholds a U it calls not credible.
- McDaniel reliability-corrected cell 0.37: **REJECT**. Printed 0.28 and 0.60 produce 0.361478, which rounds to 0.36. The formula matches the paper's job-knowledge example (0.31 and 0.60 produce 0.40) and is not the problem. The unrounded mean that would print as both 0.28 and 0.37 is not in the PDF. One correction pass did not close it. **Did not reproduce.**
- Huffcutt Table 2 range-corrected 0.70 from 0.48 and U = 1.64: **REJECT**. Case II, which recovers the McDaniel 0.51 cell from 0.37 and U = 1.47, produces 0.667866 here. One correction pass. **Did not reproduce.** This cell is not the operational claim. Table 2 already marks it not credible.
- Huffcutt predictive-only U = 1.63 blend: **REJECT**. Predictive observed r and predictive N are UNKNOWN. The code returns UNKNOWN and does not fill them. **Did not reproduce.**
- Wilson White-vs-Black preference rate: **REJECT** as a reproduction. **BLOCKED** at Step 0. No rate was computed, so nothing is accepted against the paper.

**Labels, PASS.** Sackett EXTRACT and RESULT, the Wilson RESULT, the README table, and `site/index.html` label numbers as system-verified or estimated/reported, and the Wilson statements carry FACT, INFERENCE, or UNKNOWN. The 28 Oct 2026 OSF listing is recorded as a FACT that updates the packet's 17 Oct 2026 listing failure. File contents were not downloaded, and the experiment stays blocked.

**Model, occupation, sample size, BLOCKED.** Experiment 1 was not run. The RESULT names no model, no occupation, and no sample size, and it says so. Naming one now would claim a run that did not happen.

**Hosted proof, BLOCKED.** The passing CI link is https://github.com/sanoojcools/pa-evidence-lab/actions/runs/40686325809. There is no live page. On 28 Oct 2026, `has_pages` was false, `POST /repos/sanoojcools/pa-evidence-lab/pages` with `{"build_type":"workflow"}` returned 403 `Resource not accessible by integration`, and a browser load of https://sanoojcools.github.io/pa-evidence-lab/ showed the GitHub Pages document title "Page not found · GitHub Pages" with heading "404". Screenshot of that load: `/opt/cursor/artifacts/github-pages-404.png`. That file is the 404, not the evidence-lab page. The branch was not merged, and Pages was not switched on by a setting this token cannot change. A local render of `site/index.html` was checked in a browser at desktop and 390px widths. It shows both results and the labels. It is not hosted proof.

**Pull request, PASS.** Draft pull request https://github.com/sanoojcools/pa-evidence-lab/pull/1 on `sanoojcools/pa-evidence-lab`, base `main`. It is still a draft.
