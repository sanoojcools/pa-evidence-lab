# RESULT: Wilson and Caliskan (2024)

**Status: BLOCKED at Step 0.** No reproduction was attempted. No model was run. No occupation was selected. No sample size is claimed. No White-vs-Black preference rate was computed.

Step 0 in the approved packet is: confirm that the released code includes the resumes and the name lists. If they are missing, mark the experiment blocked and stop. They are missing from the released GitHub repository. This file stops there.

The packet's target for a completed run was a White-vs-Black name preference rate of about 85%, against a 50% no-preference baseline. Both figures are **estimated/reported** from the outer-loop packet (`WE-PAEL-2026-10-13`), not from a reading of the paper in this experiment, and not system-verified. They were not computed.

Labels: **FACT** was checked against a public page or API on the date given. **INFERENCE** is a conclusion from those facts. **UNKNOWN** was not established. Nothing below is a system-verified experimental result.

## Facts about the released code

- **FACT (28 Oct 2026).** The public GitHub API for `kyrawilson/Resume-Screening-Bias` at `main` lists `data/names/temp.txt` (1 byte; content is a single newline) and `data/=names/tmp.txt` (1 byte, a newline) plus `data/=names/scores/temp.txt` (1 byte, a newline). The tree contains no resume corpus and no names CSV.
- **FACT (28 Oct 2026).** The README Datasets section points resumes to `https://www.kaggle.com/datasets/snehaanbhawal/resume-dataset` and job descriptions to `https://www.kaggle.com/datasets/marcocavaco/scraped-job-descriptions`.
- **FACT (17 Oct 2026, from the packet, not re-downloaded here).** Those Kaggle datasets were reported to require a login.
- **FACT (28 Oct 2026).** An unauthenticated GET of both Kaggle URLs returned HTTP 200. The datasets were not downloaded.
- **UNKNOWN.** Whether a Kaggle login is still required to download either dataset. This check did not try.
- **FACT (28 Oct 2026).** The README Preprocessing section says to generate SOC occupation codes with NIOCCS at `https://csams.cdc.gov/nioccs/`. NIOCCS was not used.
- **UNKNOWN.** Whether NIOCCS coding can be done without an account or a manual upload.
- **FACT (28 Oct 2026).** The README Experiments section says the names input is a CSV passed with `-n` (default none) and that retrieval scores for the paper's results are at `https://osf.io/cbx2d/`. The repository does not contain that CSV.

## OSF

- **FACT (17 Oct 2026, from the packet).** The OSF project could not be listed in that check.
- **FACT (28 Oct 2026).** `GET https://api.osf.io/v2/nodes/cbx2d/` returned HTTP 200 for a public node titled "Resume Screening Bias". `GET https://api.osf.io/v2/nodes/cbx2d/files/osfstorage/` listed two folders. `Scores_Names` contains `Names.csv` (4,466 bytes) and a `scores` folder of 10 files. `Scores_=Names` contains `=Names.csv` (4,370 bytes) and a `scores` folder of 10 files. File contents were not downloaded.
- **INFERENCE.** The 17 Oct 2026 listing failure is not the state of the public API on 28 Oct 2026. Listing names and score folders does not put resumes in the released repository, and it does not authorize a re-run. This experiment stays blocked.

## Author note

- **FACT (28 Oct 2026).** The README opens with a block headed "Update August 29, 2026". It says Frank Pallas and Martin Wiesinger reported that the published results are inaccurate because of a bug, that gender-only comparisons should be inverted, and that race-only results and intersectional gender-by-race results were accurate and were replicated by that team. It says the code in the repository was left uncorrected.
- **FACT (28 Oct 2026).** In `experiments.py` on `main`, the gender branch is lines 38–39: `names['M'] = names['WF']+names['BF']` and `names['F'] = names['WM']+names['BM']`. The README's suggested replacement is `names['F'] = names['WF']+names['BF']` and `names['M'] = names['WF']+names['BM']`.
- **INFERENCE.** The suggested male line still concatenates the WF list with the BM list, so the README text is not a clean swap of the two current lines. Whether that second token is a typo is **UNKNOWN**. The bug itself was not re-checked. No gender, race, or intersectional rate from the paper is treated as usable.

## Why this is the stopping point

- **INFERENCE.** Step 0 fails on the released code: the resumes are not in the repository, and the name lists are not in the repository. The packet says to mark that blocked and not to swap papers.
- **FACT.** No embedding model was loaded, no occupation was coded, and no preference rate was calculated in this repository.
