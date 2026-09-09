# Recurrent Memory Lab — DataForge 2026 / Pathway Track

## Live Demo

- **Public URL**: `https://naveen-637.github.io/dataforge-2026-pathway/`
  *(Active once GitHub Pages is enabled under Repository Settings → Pages → Branch: `main` / `root`)*
- **Local Preview**: Open `index.html` directly in any standard modern web browser (no local server or build step required).

## One-sentence claim

**Adding demonstrations can be absorbed into a fixed-size recurrent state, but overlapping evidence can interfere and cause retrieval errors.**

This is the single falsifiable claim taught by the artifact.

## Intended learner

Advanced undergraduate / early graduate data-science or ML learner who knows vectors, matrices, and the basic idea of attention, but has not studied recurrent memory in depth.

## Prerequisites

- Matrix multiplication and dot products.
- High-level familiarity with Transformer attention.
- No prior knowledge of BDH required.

## Learning objectives

After 2–4 minutes, a learner should be able to:

1. Explain why a recurrent memory can keep a **fixed state shape** while the number of seen demonstrations grows.
2. Describe a write as an update of state rather than an append to a token-by-token buffer.
3. Predict why similar keys create **interference / crosstalk**.
4. Distinguish the teaching toy from official BDH/BDH-CQ behavior.
5. State the BDH-CQ connection: inference-time inputs update recurrent memory, and the query is solved through iterative latent computation without verbalizing intermediate reasoning.

## What is live, precomputed, synthetic, or official?

- **Live:** every demo write, matrix update, query, probability calculation, and visualization is computed in the browser from JavaScript.
- **Synthetic:** the key/value pairs and 5×5 teaching substrate are synthetic.
- **Toy:** the update `M_t = lambda M_(t-1) + alpha k_t v_t^T` is an independent educational simplification of recurrent associative memory. It is **not** the official BDH equation or checkpoint.
- **Official / sourced:** claims about BDH and BDH-CQ are limited to published primary sources and are clearly marked as such.
- **No external API:** the demo runs as a static file and needs no sign-in, model key, GPU, or paid service.

## Architecture of the artifact

`index.html` contains the complete frontend and toy computation. There is no backend. The learner interacts with three concept variables:

- **Learning rate alpha** changes the strength of writes.
- **Decay lambda** changes how much previous state is retained.
- **Key similarity** changes how much different keys share representational features and therefore how strongly they interfere.

The query produces both the model estimate and the known ground-truth value.

## Teaching flow

1. The page opens with a populated preset and a correct query, so the learner sees the substrate behaving before clicking anything.
2. The learner can add demonstrations while the state remains 5×5.
3. The learner sees `q^T M` scores and ground truth side by side.
4. The learner raises similarity or adds a conflicting demonstration and observes a failure.
5. The BDH module explicitly labels the mapping as conceptual rather than an official implementation.

## BDH / BDH-CQ connection

### BDH
The original Dragon Hatchling paper describes a scale-free, locally interacting architecture and states that its working memory during inference relies on synaptic plasticity with Hebbian learning. The paper also emphasizes sparse, positive activations and interpretability of state. This makes a state-update teaching substrate a natural conceptual bridge, but the toy matrix update here should not be mistaken for BDH's complete dynamics.

### BDH-CQ
The BDH-CQ report describes a reasoning model that combines in-context learning with recurrent latent reasoning. Inputs presented at inference time continuously update recurrent memory; the query is then solved with iterative computation in high-dimensional latent space rather than by verbalizing intermediate reasoning. This directly motivates the demo's learner journey: **write demonstrations → evolve state → query the evolved state**.

## Why this concept / why not the Rime track?

For a one-hour, zero-budget build, the Pathway track is the lower-risk option because the judged artifact can be entirely static, live, and free to host. The Rime track requires verifiable Rime integration, a current model/voice configuration, a working voice product, and a recorded stress-case demo. A Pathway artifact can demonstrate the concept without depending on an external API key or realtime audio transport.

## Three+ recent primary papers supporting the concept

1. **Engdahl et al. (2026), “BDH-CQ: In-Context Learning with Recurrent Latent Reasoning.”** arXiv:2608.09888. Primary source for the BDH-CQ connection.
2. **Behrouz, Zhong & Mirrokni (2025), “Titans: Learning to Memorize at Test Time.”** NeurIPS 2025 / arXiv:2501.00663. Primary source on learned recurrent/neural memory for long context and test-time memorization.
3. **De et al. (2024), “Griffin: Mixing Gated Linear Recurrences with Local Attention for Efficient Language Models.”** arXiv:2402.19427. Primary source on gated linear recurrences and fixed-size state.
4. **Botev et al. (2024), “RecurrentGemma: Moving Past Transformers for Efficient Open Language Models.”** arXiv:2404.07839. Primary source for an open model using the Griffin recurrent architecture.
5. **Kosowski et al. (2025), “The Dragon Hatchling: The Missing Link between the Transformer and Models of the Brain.”** arXiv:2509.26507. Primary source for BDH's synaptic working memory formulation.

## Known limitations / common misconceptions

- Fixed-size state does **not** mean perfect recall: finite capacity and interference remain.
- Recurrent memory is not the same as a growing Transformer KV cache.
- The toy update is not a faithful reimplementation of BDH or BDH-CQ.
- A toy associative memory does not establish benchmark-level reasoning ability.
- The BDH-CQ benchmark result is a published result, not something reproduced by this toy.

## Reproduction

### Local
Open `index.html` in any modern browser. No install is needed.

### Free public hosting
Use GitHub Pages:

1. Create a public GitHub repository.
2. Upload `index.html` and this README.
3. Repository Settings → Pages → Deploy from branch → `main` / root.
4. Open the generated `https://<username>.github.io/<repo>/` URL in an incognito window.

Alternative: drag the folder into any static hosting service that supports free public HTML hosting.

## Submission package checklist

- [x] Interactive explorable artifact: [`index.html`](./index.html)
- [x] Meaningful learner controls (learning rate, decay, key similarity, stress test).
- [x] Live calculation with ground truth beside estimate.
- [x] BDH/BDH-CQ module integrated into the learning journey.
- [x] Limitation / failure case (finite capacity & interference).
- [x] Source list with recent primary papers: [`SOURCES.md`](./SOURCES.md)
- [x] AI / license disclosure: [`AI_DISCLOSURE.md`](./AI_DISCLOSURE.md)
- [x] One-page concept summary: [`one_page_concept_summary.pdf`](./one_page_concept_summary.pdf)
- [x] Extended blog report: [`blog.pdf`](./blog.pdf)
- [x] Quick judge walkthrough: [`QUICKSTART.md`](./QUICKSTART.md)

## Provenance and license

- Original code in [`index.html`](./index.html): [MIT License](./LICENSE).
- No third-party code or external graphics are bundled.
- Scientific claims cite the primary sources listed in [`SOURCES.md`](./SOURCES.md).
- AI assistance is disclosed in [`AI_DISCLOSURE.md`](./AI_DISCLOSURE.md).
