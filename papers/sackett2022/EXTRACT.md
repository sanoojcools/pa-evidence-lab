# Extract: Sackett, Zhang, Berry, and Lievens (2022)

Structured-interview operational validity only. Other predictors appear here only when a row is a worked check of the correction formula.

## Source

- **Paper.** Sackett, P. R., Zhang, C., Berry, C. M., & Lievens, F. (2022). Revisiting meta-analytic estimates of validity in personnel selection: Addressing systematic overcorrection for restriction of range. *Journal of Applied Psychology, 107*(11), 2040–2068. https://doi.org/10.1037/apl0000994
- **Europe PMC.** PMID [34968080](https://europepmc.org/article/med/34968080). The Europe PMC core record, read 28 Oct 2026, has `isOpenAccess` N, `inPMC` N, and `hasPDF` N. The only full-text link is the publisher DOI, marked subscription required. No number below is taken from a paywalled page.
- **Open manuscript used for every number.** Semantic Scholar records a GREEN open-access PDF for this DOI, license CC BY-NC-ND, landing page `https://ink.library.smu.edu.sg/lkcsb_research/6894` (accepted version). The PDF retrieved for this extract is `https://pdfs.semanticscholar.org/915a/a40e852d5975086111dcd359967400cc5150.pdf` (29 pages). Page numbers below are the numbers printed on that PDF. The PDF was not copied into this repository.

Labels: **FACT** is printed in that PDF. **INFERENCE** is a conclusion this extract draws. **UNKNOWN** is an input the PDF does not give. Nothing here is guessed.

## Claim this experiment recomputes

**FACT.** Table 3 (p. 15) lists employment interviews, structured, with a current validity estimate (ρ) of **0.42**. The same 0.42 is the Table 2 overall "current estimate" for structured interviews (p. 11) and the Table 4 current estimate corrected with ryy = .60 (p. 17).

**FACT.** The prior Schmidt and Hunter (1998) estimate on that Table 3 row is **0.51**. Table 3 also prints SD of ρ **0.19**, lower 80% credibility value **0.18**, and Black–White d **0.23**. Those three quantities are context. This experiment does not recompute them.

## Method, as printed

**FACT (p. 2).** U is the ratio of unrestricted predictor SD to restricted predictor SD. The mean observed validity is corrected with that U. When a criterion-unreliability correction is also made, it is applied to the mean observed validity first. The reliability-corrected mean is then corrected for range restriction. Computational details are attributed to Hunter and Schmidt (2004). The PDF does not print the algebra.

**INFERENCE.** The criterion step is the Spearman correction, observed r divided by the square root of criterion reliability. The range-restriction step is the direct (Thorndike Case II) formula

ρ = (U × r) / √(1 + r² × (U² − 1)),

with r already reliability-corrected. Two printed rows support that reading: job-knowledge tests, observed **0.31** with reliability **0.60**, rise to **0.40** (p. 18), and the McDaniel reliability-corrected **0.37** with U = **1.47** rises to the tabled range-corrected **0.51** (Table 2, p. 11). Both checks are computed in `experiments/sackett2022/repro.py`.

**FACT (p. 10).** Where a meta-analysis used an external reliability value, Sackett et al. use **0.60** rather than **0.52**. They call 0.60 the more conservative choice and still show a 0.52 sensitivity in Table 4.

**FACT (p. 18).** They also use lowercase u for the restricted-to-unrestricted SD ratio. In the assessment-center discussion, u = **0.90** corresponds to U = **1.1**. So u = 1/U. Table 2 prints U, not u.

## Structured-interview inputs (Table 2, p. 11)

Table 2 columns used here: K, N, mean observed rxy, ryy used by the source meta-analysis, validity corrected for ryy, U, range-restriction-corrected validity, whether that range-restriction correction is credible, and the current operational estimate.

### McDaniel et al. (1994), structured

| Input | Value | Label | Where |
| --- | --- | --- | --- |
| K | 36 | FACT, estimated/reported | Table 2, p. 11 |
| N | 3,069 | FACT, estimated/reported | Table 2, p. 11 |
| Mean observed r | 0.28 | FACT, estimated/reported | Table 2, p. 11; repeated in the interview section, p. 17 |
| Criterion reliability used by the source | 0.6 | FACT, estimated/reported | Table 2, p. 11. Read as 0.60, the value defined on p. 10 |
| Validity corrected for that reliability | 0.37 | FACT, estimated/reported | Table 2, p. 11 |
| U | 1.47 | FACT, estimated/reported | Table 2, p. 11. p. 17 says this mean came from 14 of 245 studies |
| u = 1/U | 1/1.47 | INFERENCE from the p. 18 definition of u | Not printed as a decimal |
| Range-restriction-corrected validity | 0.51 | FACT, estimated/reported | Table 2, p. 11 |
| Is that U correction credible? | No. It applies an empirical u to concurrent studies | FACT | Table 2, p. 11 |
| Current operational estimate | 0.37 | FACT, estimated/reported | Table 2, p. 11. p. 17 says they keep the reliability-corrected value because the predictive/concurrent mix is unknown |

**UNKNOWN.** The proportion of these 3,069 people, or of the 36 studies, that are predictive rather than concurrent. p. 17 says McDaniel et al. did not report it, which is why Sackett et al. do not apply U = 1.47.

### Huffcutt et al. (2014), structured

| Input | Value | Label | Where |
| --- | --- | --- | --- |
| K | 69 | FACT, estimated/reported | Table 2, p. 11 |
| N | 4,795 | FACT, estimated/reported | Table 2, p. 11 |
| Mean observed r | 0.35 | FACT, estimated/reported | Table 2, p. 11 |
| Conflicting prose observed r | 0.36 | FACT, estimated/reported | Interview section, p. 17. Not used in the recomputation. The table is the input grid |
| Criterion reliability used by Huffcutt et al. | 0.52 | FACT, estimated/reported | Table 2, p. 11. p. 17 attributes 0.52 to Rothstein et al. (1990) |
| Validity corrected for ryy = 0.52 | 0.48 | FACT, estimated/reported | Table 2, p. 11 |
| U in Table 2 | 1.64 | FACT, estimated/reported | Table 2, p. 11. Basis printed as an assumed selection ratio of 5% for concurrent studies and 50% for predictive studies |
| Is that U correction credible? | No. Assumed distribution with no empirical basis | FACT | Table 2, p. 11 |
| Current operational estimate | 0.45 | FACT, estimated/reported | Table 2, p. 11 |
| Share of studies that are concurrent | 74% | FACT, estimated/reported | p. 6 (in the list of concurrent shares) and p. 17 |
| U Sackett et al. say they apply to predictive studies only | 1.63 | FACT, estimated/reported | p. 17, attributed to Salgado and Moscoso (2002) |
| Predictive-study observed r | UNKNOWN | The PDF does not print it | |
| Predictive-study N, as distinct from 74% of studies | UNKNOWN | The PDF does not print it | |
| Concurrent-study observed r and N | UNKNOWN | The PDF does not print them | |

p. 17 also says a recorrection of the prose observed r with reliability 0.60 produces **0.46** for structured interviews, and that an N-weighted blend of predictive and concurrent studies is **0.45**. The predictive and concurrent correlations that would make that blend are UNKNOWN, so the blend is not filled in.

### Overall structured row (Table 2, p. 11)

| Quantity | Value | Label |
| --- | --- | --- |
| Mean observed r | 0.32 | FACT, estimated/reported |
| Reliability-corrected | 0.44 | FACT, estimated/reported |
| Range-restriction-corrected | 0.63 | FACT, estimated/reported |
| Current operational estimate | 0.42 | FACT, estimated/reported |

p. 18 says the 0.42 (and the unstructured 0.19) is the sample-size-weighted mean of the McDaniel and Huffcutt current estimates.

## What the operational 0.42 does with U

**INFERENCE, tied to printed cells.** Table 2's current estimate withholds both printed U values: McDaniel stays at the reliability-corrected 0.37, and Huffcutt's current estimate is 0.45 rather than the range-corrected 0.70. The recomputation therefore corrects each tabled observed r with ryy = 0.60 and does not apply U, then takes the sample-size-weighted mean. Applying U = 1.63 only to predictive studies would require the UNKNOWN split above.

Table 4 (p. 17) is a sensitivity, not the headline. For structured interviews it prints 0.42 (ryy = .60), 0.45 (that estimate also corrected for range restriction), 0.45 (ryy = .52), and 0.48 (the .52 estimate also corrected for range restriction). Note b says Case IV indirect range restriction was applied. The Case IV inputs that would turn 0.42 into 0.45 are not printed on the structured-interview row. Those inputs are UNKNOWN. This experiment recomputes the 0.42 column, not the 0.45 sensitivity.

## Assumptions carried into the recomputation

1. **FACT.** Sample-size weights are the Table 2 N values, 3,069 and 4,795. K is printed and is not the weight.
2. **FACT.** Criterion reliability for the operational path is 0.60 (p. 10), including the Huffcutt row whose source used 0.52.
3. **INFERENCE.** U is not applied on the operational path, because Table 2 marks those corrections not credible and the current-estimate cells match a reliability-only reading.
4. **UNKNOWN, left unknown.** Predictive versus concurrent observed correlations and Ns inside Huffcutt et al. (2014). Unrounded study-level means that might sit behind the printed 0.28 and 0.37.
