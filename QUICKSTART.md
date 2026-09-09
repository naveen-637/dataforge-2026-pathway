# 60-minute execution plan

## 0-5 min — Create the repo
Create a public GitHub repository named `recurrent-memory-lab-dataforge`. Upload this folder unchanged.

## 5-12 min — Publish the artifact
GitHub → Settings → Pages → Deploy from branch → `main` / root. Open the public URL in an incognito window.

## 12-22 min — Run the judge path
Use exactly this flow:

1. Page loads with the clean preset.
2. Query B → `triangle` (correct).
3. Increase **Key similarity** to about 0.70.
4. Click **Stress test: add a conflicting demo**.
5. Query B again.
6. Point to the 5×5 matrix and say: “The sequence grew; the state shape did not. The error comes from overlapping writes, not from a growing memory buffer.”

## 22-30 min — Verify controls
Try the decay slider and learning-rate slider. Confirm the matrix changes. Reload the page to confirm there are no console errors.

## 30-40 min — Finish the repo
Keep these files in the repo:

- `index.html`
- `README.md`
- `SOURCES.md`
- `AI_DISCLOSURE.md`
- `LICENSE`
- `one_page_concept_summary.pdf`
- `blog.pdf`

Do not add generated build folders or temporary renders.

## 40-50 min — Read the defense facts
Memorize only these facts:

- BDH paper: working memory during inference relies on synaptic plasticity with Hebbian learning.
- BDH-CQ paper: inference-time inputs continuously update recurrent memory; the query is solved by iterative latent computation without verbalizing intermediate reasoning.
- Toy equation is not official BDH; it is an independent teaching substrate.
- Main limitation: fixed-size state creates a capacity/interference trade-off.

## 50-60 min — Final submission check
Open the public URL without signing in. Open both PDFs. Confirm README says what is live/toy/official. Paste the artifact URL, repository URL, and PDF files into the submission form. Keep the public repo stable until judging.
