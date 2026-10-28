# RESULT: Sackett et al. (2022), structured interviews

**Claim.** The operational validity of structured employment interviews, after Sackett et al.'s revision, is 0.42.

**Conditions.** Two published meta-analytic means, combined by sample size. McDaniel et al. (1994) structured interviews, N = 3,069, K = 36, observed r = 0.28. Huffcutt et al. (2014) structured interviews, N = 4,795, K = 69, observed r = 0.35 (Table 2). Criterion reliability 0.60 (open PDF p. 10). The U ratios printed for these rows (1.47 and 1.64) are not applied, because Table 2 marks both range-restriction corrections not credible and the current-estimate cells are the reliability-corrected values. No applicant-level data. No other predictor. The script is `experiments/sackett2022/repro.py` (seed 20221013, pytest 8.3.5, CI Python 3.12).

## Headline

| Quantity | Value | Label |
| --- | --- | --- |
| Paper operational validity | 0.42 | estimated/reported. Table 2 overall current estimate (p. 11), Table 3 (p. 15), Table 4 ryy = .60 column (p. 17) |
| Ours, exact | 0.41658046582890619130740710836409900731016010222519 | system-verified |
| Ours, six decimals | 0.416580 | system-verified |
| Ours, two decimals (half up) | 0.42 | system-verified |
| Delta, ours minus 0.42, six decimals | -0.003420 | system-verified |
| Delta at two decimals | 0.00 | system-verified |
| Status at the paper's two-decimal precision | reproduced at two decimals | system-verified comparison |

The exact value sits 0.003420 below 0.42. Both round to 0.42. That match is the reliability correction of the two tabled observed correlations, weighted by N.

## Trivial baseline

| Quantity | Value | Label |
| --- | --- | --- |
| N-weighted observed r, six decimals | 0.322682 | system-verified |
| Same baseline at two decimals | 0.32 | system-verified. Matches the Table 2 overall observed r, which is estimated/reported as 0.32 |
| Zero correlation | 0 | the no-relationship baseline. Not a paper result |

The corrected 0.416580 is larger than 0.322682 because each correlation is divided by √0.60. That gap is the arithmetic of the reliability correction. It is not a new finding, and it is not a range-restriction result: U is not in the headline. Beating this baseline is required before any stronger claim, and this recomputation does not make one. The result is a check that the published 0.42 is the N-weighted reliability correction of the printed observed correlations.

## Components

| Piece | Ours | Paper | Delta (six decimals) | Status |
| --- | --- | --- | --- | --- |
| McDaniel, 0.28 / √0.60 | 0.361478 system-verified | 0.37 estimated/reported (Table 2 reliability-corrected and current estimate) | -0.008522 | did not reproduce |
| Huffcutt, 0.35 / √0.60 | 0.451848 system-verified | 0.45 estimated/reported (Table 2 current estimate) | +0.001848 | reproduced at two decimals |
| N-weighted mean of those two | 0.416580 system-verified | 0.42 estimated/reported | -0.003420 | reproduced at two decimals |

One correction pass on the McDaniel gap: the rest of the paper's reliability examples use r / √ryy (job knowledge, 0.31 with 0.60, equals 0.40; our check is 0.400208). Applying that same division to the printed 0.28 and 0.60 yields 0.36, not the printed 0.37. The reliability that would make 0.28 land on 0.37 is (0.28 / 0.37)² = 0.573, and that reliability is not printed. It is UNKNOWN. It was not substituted. After that pass the intermediate gap is still unexplained, so the McDaniel reliability cell **did not reproduce**. The headline still rounds to 0.42 because the 0.01 cell gap is diluted by the larger Huffcutt sample.

## Range restriction

| Check | Ours | Paper | Status |
| --- | --- | --- | --- |
| u = 1/U for the McDaniel row, U = 1.47 | 0.680272 system-verified | u is not printed as a decimal. estimated/reported U is 1.47 | INFERENCE from the p. 18 definition u = 1/U. Not applied to the headline |
| Case II on the printed McDaniel reliability-corrected 0.37 with U = 1.47 | 0.505232 system-verified | 0.51 estimated/reported (Table 2) | reproduced at two decimals. This is the correction Sackett et al. reject for the operational estimate |
| Case II on the printed Huffcutt reliability-corrected 0.48 with U = 1.64 | 0.667866 system-verified | 0.70 estimated/reported (Table 2) | did not reproduce |
| U = 1.63 applied only to Huffcutt predictive studies | UNKNOWN | 0.45 estimated/reported as the blend (p. 17) | did not reproduce |

One correction pass on the Huffcutt 0.70 cell: Case II, which recovers the McDaniel 0.51 cell, does not recover 0.70 from the printed 0.48 and 1.64. The PDF does not give another U or another reliability for that cell. The gap is unexplained. That 0.70 is the correction Table 2 already marks not credible. It is not the operational 0.42.

One correction pass on the p. 17 blend: predictive observed r, concurrent observed r, and the N in each subset are UNKNOWN (74% is a share of studies, not a printed N). The blend function returns UNKNOWN and does not fill those inputs. A common-r illustration, which the script does not adopt, moves a reliability-corrected 0.45 up, away from a result of 0.45. The partial-U step **did not reproduce**.

## Unverified

- Standard deviations, the 80% credibility interval, and the Black–White d on the Table 3 row (0.19, 0.18, 0.23). Estimated/reported. Not recomputed.
- Table 4's Case IV move from 0.42 to 0.45. The indirect-range-restriction inputs for that cell are UNKNOWN.
- The prose observed r of 0.36 on p. 17. Estimated/reported, and not the Table 2 input. A sensitivity that replaces 0.35 with 0.36 still rounds the headline to 0.42. It is not the primary result.
- Anything about unstructured interviews beyond the inputs left unused here.
