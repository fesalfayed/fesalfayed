<div align="center">

<img src="./attention.svg" alt="a self-attention matrix as a self-portrait — the diagonal is the self attending to the self" width="640">

# Fesal Fayed

#### Data &amp; ML Engineer<br/><sub>agentic systems · tool-use fine-tuning · applied ML</sub>

</div>

I build agents and fine-tune models. Mostly in the Hermes ecosystem: the model itself, the provider adapters it runs on, the context engine behind it.

My `gpt-oss-20b` tool-use finetune ships in four runtimes with 9k+ downloads. Two of my fixes are merged into `hermes-agent`, one into `hermes-lcm`.

```text
role       Data & ML Engineer
focus      agent infra · fine-tuning · adapter correctness · context
shipped    gpt-oss-20b tool-use finetune — MLX · GGUF · 4-bit · 16-bit
adoption   9k+ Hugging Face downloads
oss        merged fixes in repos totaling 205k+ stars
based      Miami · B.S. Data Science & AI, FIU
```

---

## Fine-tuning

`gpt-oss-20b`, tuned for Hermes-style function calling. Same weights, four runtimes:

| model | format | runs on |
| :--- | :--- | :--- |
| [`finetune_mlx`](https://huggingface.co/fesalfayed/gpt-oss-20b-hermes_agent-tool-finetune_mlx) | MLX | Apple Silicon |
| [`finetune_gguf`](https://huggingface.co/fesalfayed/gpt-oss-20b-hermes_agent-tool-finetune_gguf) | GGUF | llama.cpp · Ollama · LM Studio |
| [`finetune_4bit`](https://huggingface.co/fesalfayed/gpt-oss-20b-hermes_agent-tool-finetune_4bit) | 4-bit | Colab · low-VRAM |
| [`finetune_16bit`](https://huggingface.co/fesalfayed/gpt-oss-20b-hermes_agent-tool-finetune_16bit) | 16-bit | vLLM · full precision |

[the collection →](https://huggingface.co/collections/fesalfayed/finetuned-hermes-function-calling-v1) &nbsp;·&nbsp; [repo notes →](https://github.com/fesalfayed/gpt-oss-20b-hermes-tool-finetune)

---

## Open source

Five fixes merged across `hermes-agent` and `hermes-lcm` (205k+ stars combined). These bugs only surface in real agent runs: signed-reasoning replay, tool-use stripping, context assembly.

- **[`hermes-agent`](https://github.com/NousResearch/hermes-agent/pull/35859) — Anthropic extended-thinking crash loop**  
  Authored the fix for crashes when orphan tool-use stripping invalidated signed reasoning blocks. Teknium cherry-picked it to `main` with authorship preserved. [`64628ea`](https://github.com/NousResearch/hermes-agent/commit/64628ea89b1d5624f47b402edd54b13afd335123) · closes [#35847](https://github.com/NousResearch/hermes-agent/issues/35847)

- **[`hermes-agent`](https://github.com/NousResearch/hermes-agent/pull/54083) — WhatsApp LID alias resolution**  
  Authored the session-path fix so modern `platforms/whatsapp/session` installs stop silently dropping allowlisted senders. Accepted with authorship preserved. [`263ffec`](https://github.com/NousResearch/hermes-agent/commit/263ffec1b03114ec98671919943fb61de7ebf1bf) · closes [#36664](https://github.com/NousResearch/hermes-agent/issues/36664)

- **[`hermes-agent`](https://github.com/NousResearch/hermes-agent/issues/35975) — interleaved-thinking signature crash loop**  
  Filed and root-caused; maintainers confirmed the order-preserving channel on `main` solved it without demoting reasoning.

- **[`hermes-agent`](https://github.com/NousResearch/hermes-agent/pull/52276) — leading-assistant transcript backstop**  
  Maintains an adapter-level backstop PR for post-compaction transcripts, complementing the built-in compressor fix for [#52160](https://github.com/NousResearch/hermes-agent/issues/52160) / [#52167](https://github.com/NousResearch/hermes-agent/pull/52167).

- **[`hermes-lcm`](https://github.com/stephenschoettler/hermes-lcm/pull/280) — DAG context role invariant**  
  Merged fix so DAG context summaries cannot become provider-visible leading assistant messages.

More detail: [`oss-contributions`](https://github.com/fesalfayed/oss-contributions).

---

## Selected work

- **[`gpt-oss-20b-hermes-tool-finetune`](https://github.com/fesalfayed/gpt-oss-20b-hermes-tool-finetune)** — end-to-end tool-use fine-tuning notes, export matrix, local inference packaging
- **[`hermes-Notion-Worker-sync`](https://github.com/fesalfayed/hermes-Notion-Worker-sync)** — Discord ↔ Notion worker sync on `@notionhq/workers`
- **[`amazon-image-quality-bsr-analysis`](https://github.com/fesalfayed/amazon-image-quality-bsr-analysis)** — applied DS: image-quality metrics, pricing/review enrichment, BSR modeling
- **[`fesalfayed.com`](https://github.com/fesalfayed/fesalfayed-com)** — my site, a tmux session in the browser

---

## Principles

```text
fix the root, not the symptom      ·   local default, cloud on demand
agents type, humans steer          ·   one project, one repo, one job
```

<div align="center">

[hi@fesalfayed.com](mailto:hi@fesalfayed.com) &nbsp;·&nbsp; [huggingface.co/fesalfayed](https://huggingface.co/fesalfayed) &nbsp;·&nbsp; [fesalfayed.com](https://fesalfayed.com)

<sub>Data &amp; ML Engineer &middot; Miami &middot; B.S. Data Science &amp; AI, FIU</sub>

</div>
