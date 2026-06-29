<div align="center">

<img src="./attention.svg" alt="a self-attention matrix as a self-portrait; the diagonal is the self attending to the self" width="660">

# Fesal Fayed

#### Data and ML Engineer · Agentic Systems Builder · B.S. Data Science and AI @ FIU

[![Website](https://img.shields.io/badge/Website-fesalfayed.com-111111?style=for-the-badge)](https://fesalfayed.com)
[![Hugging Face](https://img.shields.io/badge/Hugging%20Face-fesalfayed-ffcc4d?style=for-the-badge)](https://huggingface.co/fesalfayed)
[![Email](https://img.shields.io/badge/Email-hi%40fesalfayed.com-444444?style=for-the-badge)](mailto:hi@fesalfayed.com)

</div>

---

<div align="center">

### I build local-first agentic infrastructure, fine-tune tool-use models, and turn messy real-world workflows into systems that can be verified.

</div>

<table>
<tr>
<td width="60%" valign="top">

## Who I Am

I'm **Fesal Fayed** - a Data and ML engineer studying **Data Science and Artificial Intelligence at Florida International University**.

My work sits at the seam between applied ML, agentic systems, and operational infrastructure: tool-use fine-tuning, provider adapter correctness, context management, Discord and Notion automation, and local-first workflows where agents assist without taking control away from the human.

I care most about systems that survive contact with reality: grounded data pipelines, reversible patches, provenance, verification loops, and small automation surfaces that compound into durable leverage.

</td>
<td width="40%" valign="top">

## At a Glance

```yaml
name:        Fesal Fayed
location:    Miami, FL
school:      Florida International University
program:     B.S. Data Science and AI
focus:       Agentic systems, ML, automation
shipping:    Tool-use fine-tunes and OSS fixes
platforms:   GitHub, Hugging Face, Cloudflare
principle:   Build the infra first
```

</td>
</tr>
</table>

---

## Current Work

<table>
<tr>
<td width="50%" valign="top">

### Building

- **Agentic OS** - a local-first multi-profile agent harness around Discord, Notion, memory, scheduled jobs, and verification-oriented workflows.
- **Tool-use fine-tuning** - `gpt-oss-20b` tuned for Hermes-style function calling and exported for MLX, GGUF, 4-bit, and 16-bit runtimes.
- **Vertical intelligence systems** - data pipelines and report infrastructure for high-margin local operators.
- **Quantified self infrastructure** - biometric and context pipelines aimed at behavior-to-outcome modeling.

</td>
<td width="50%" valign="top">

### Exploring

- Provider adapter invariants for long-context, tool-use, and signed-reasoning edge cases.
- Latent context memory, compaction, and retrieval systems for agents that work across long projects.
- Practical data-product loops: scrape, normalize, model, inspect, render, and verify.
- Local-first automation that keeps credentials, memory, and user control scoped by profile.

</td>
</tr>
</table>

---

## Proof Points

| area | grounded evidence |
| :--- | :--- |
| **Model shipping** | Fine-tuned `gpt-oss-20b` for Hermes-style tool use and released MLX, GGUF, 4-bit, and 16-bit artifacts |
| **Adoption** | 9.4k+ Hugging Face downloads across the released model formats |
| **OSS** | Authored two accepted `NousResearch/hermes-agent` fixes with authorship preserved by Teknium |
| **OSS** | Merged [`hermes-lcm` PR #280](https://github.com/stephenschoettler/hermes-lcm/pull/280), fixing provider-visible summary role invariants |
| **Systems** | Built Discord to Notion worker sync, multi-profile agent orchestration, memory-backed workflows, and Cloudflare-hosted personal surfaces |
| **Applied ML** | Amazon image-quality and product-rank modeling case study |

---

## Fine-Tuning

`gpt-oss-20b` tuned for Hermes-style function calling and shipped in formats that cover local Apple Silicon, llama.cpp/Ollama, Colab-class experiments, and full-precision serving.

| model | format | runs on |
| :--- | :--- | :--- |
| [`finetune_mlx`](https://huggingface.co/fesalfayed/gpt-oss-20b-hermes_agent-tool-finetune_mlx) | MLX | Apple Silicon |
| [`finetune_gguf`](https://huggingface.co/fesalfayed/gpt-oss-20b-hermes_agent-tool-finetune_gguf) | GGUF | llama.cpp, Ollama, LM Studio |
| [`finetune_4bit`](https://huggingface.co/fesalfayed/gpt-oss-20b-hermes_agent-tool-finetune_4bit) | 4-bit | Colab and low-VRAM experiments |
| [`finetune_16bit`](https://huggingface.co/fesalfayed/gpt-oss-20b-hermes_agent-tool-finetune_16bit) | 16-bit | vLLM and full-precision serving |

> 9,459 downloads across formats as of the latest profile refresh.  
> [Hugging Face collection](https://huggingface.co/collections/fesalfayed/finetuned-hermes-function-calling-v1) · [training notes](https://github.com/fesalfayed/gpt-oss-20b-hermes-tool-finetune)

---

## Open Source Contributions

My contributions focus on where agent systems break in production-shaped edge cases: provider adapters, signed reasoning blocks, tool-use replay, session identity, and context assembly.

| project | contribution |
| :--- | :--- |
| [`NousResearch/hermes-agent`](https://github.com/NousResearch/hermes-agent/pull/35859) | Authored the fix for Anthropic extended-thinking crash loops when orphan tool-use stripping invalidated signed reasoning blocks; Teknium cherry-picked it to `main` with authorship preserved ([commit `64628ea`](https://github.com/NousResearch/hermes-agent/commit/64628ea89b1d5624f47b402edd54b13afd335123), closes [#35847](https://github.com/NousResearch/hermes-agent/issues/35847)) |
| [`NousResearch/hermes-agent`](https://github.com/NousResearch/hermes-agent/pull/54083) | Authored the WhatsApp LID alias session-path fix so modern `platforms/whatsapp/session` installs stop silently dropping allowlisted senders; accepted with authorship preserved ([commit `263ffec`](https://github.com/NousResearch/hermes-agent/commit/263ffec1b03114ec98671919943fb61de7ebf1bf), closes [#36664](https://github.com/NousResearch/hermes-agent/issues/36664)) |
| [`NousResearch/hermes-agent`](https://github.com/NousResearch/hermes-agent/issues/35975) | Filed and root-caused an interleaved-thinking signature crash loop; maintainers confirmed the order-preserving channel on `main` solved it without demoting reasoning |
| [`NousResearch/hermes-agent`](https://github.com/NousResearch/hermes-agent/pull/52276) | Maintains an adapter-level backstop PR for leading-assistant transcripts after compaction, complementing the built-in compressor fix path for [#52160](https://github.com/NousResearch/hermes-agent/issues/52160) / [#52167](https://github.com/NousResearch/hermes-agent/pull/52167) |
| [`stephenschoettler/hermes-lcm`](https://github.com/stephenschoettler/hermes-lcm/pull/280) | Merged role-invariant fix so DAG context summaries cannot become provider-visible leading assistant messages |

> More detail: [`oss-contributions`](https://github.com/fesalfayed/oss-contributions)

---

## Selected Work

| work | what it shows |
| :--- | :--- |
| [`gpt-oss-20b-hermes-tool-finetune`](https://github.com/fesalfayed/gpt-oss-20b-hermes-tool-finetune) | End-to-end tool-use fine-tuning notes, export matrix, and local inference packaging |
| [`hermes-Notion-Worker-sync`](https://github.com/fesalfayed/hermes-Notion-Worker-sync) | Production-shaped Discord to Notion sync on `@notionhq/workers` |
| [`amazon-image-quality-bsr-analysis`](https://github.com/fesalfayed/amazon-image-quality-bsr-analysis) | Applied DS: image-quality metrics, pricing and review enrichment, and BSR modeling |
| [`fesalfayed.com`](https://github.com/fesalfayed/fesalfayed-com) | Personal site and public identity surface |

---

## Operating Principles

```text
build the infra first                    keep the human in control
verify before claiming                   reversible patches over big swings
glue siloed sources                      see the elephant, not the tail
```

---

<div align="center">

[hi@fesalfayed.com](mailto:hi@fesalfayed.com) &middot; [huggingface.co/fesalfayed](https://huggingface.co/fesalfayed) &middot; [fesalfayed.com](https://fesalfayed.com)

<sub>Data and ML Engineer &middot; Miami &middot; B.S. Data Science and AI, FIU</sub>

</div>
