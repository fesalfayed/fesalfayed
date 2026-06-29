<div align="center">

<img src="./attention.svg" alt="a self-attention matrix as a self-portrait — the diagonal is the self attending to the self" width="660">

<br/>

# Fesal Fayed

#### Data & ML Engineer · Agentic Systems · Tool-Use Fine-Tuning · Applied ML

</div>

<br/>

<table>
<tr>
<td valign="top" width="58%">

I build agentic infrastructure and ship the models that run on it — fine-tuning
for tool use, fixing where agent systems break in production-shaped edge cases,
and writing the workflow glue that lets agents affect the real world without
taking the wheel from the human.

My contributed fixes have landed in the Hermes agent ecosystem; my fine-tuned
`gpt-oss-20b` tool-use models ship in four runtimes and are downloaded across
the Hugging Face community.

</td>
<td valign="top" width="42%">

### At a Glance

```text
role      Data & ML Engineer
focus     agent infra · fine-tuning
          adapter correctness · context
shipped   gpt-oss-20b tool-use finetune
          MLX · GGUF · 4-bit · 16-bit
adoption  9k+ Hugging Face downloads
oss       merged fixes in repos
          totaling 205k+ stars
based     Miami · B.S. DS & AI, FIU
```

</td>
</tr>
</table>

<br/>

<table>
<tr>
<td valign="top">

### Proof of work

| signal | evidence |
| :--- | :--- |
| **Model shipping** | Fine-tuned `gpt-oss-20b` for Hermes-style tool use; released MLX, GGUF, 4-bit, and 16-bit artifacts |
| **Adoption** | 9k+ Hugging Face downloads across formats |
| **OSS reach** | Merged fixes into repositories totaling **205k+ stars** ([`hermes-agent`](https://github.com/NousResearch/hermes-agent) · [`hermes-lcm`](https://github.com/stephenschoettler/hermes-lcm)) |
| **OSS** | Two `NousResearch/hermes-agent` fixes accepted by Teknium: [Anthropic signed-thinking replay](https://github.com/NousResearch/hermes-agent/commit/64628ea89b1d5624f47b402edd54b13afd335123) and [WhatsApp LID alias resolution](https://github.com/NousResearch/hermes-agent/commit/263ffec1b03114ec98671919943fb61de7ebf1bf) |
| **Systems** | Discord ↔ Notion worker sync, multi-profile agent harness, local-first automation |
| **Applied DS** | Amazon image-quality + product-rank (BSR) modeling case study |

</td>
</tr>
</table>

<br/>

<table>
<tr>
<td valign="top">

### Fine-tuning

`gpt-oss-20b` tuned for Hermes-style function calling, shipped in four formats —
Apple Silicon, llama.cpp/Ollama, Colab, and vLLM.

| model | format | runs on |
| :--- | :--- | :--- |
| [`finetune_mlx`](https://huggingface.co/fesalfayed/gpt-oss-20b-hermes_agent-tool-finetune_mlx) | MLX | Apple Silicon |
| [`finetune_gguf`](https://huggingface.co/fesalfayed/gpt-oss-20b-hermes_agent-tool-finetune_gguf) | GGUF | llama.cpp · Ollama · LM Studio |
| [`finetune_4bit`](https://huggingface.co/fesalfayed/gpt-oss-20b-hermes_agent-tool-finetune_4bit) | 4-bit | Colab · low-VRAM experiments |
| [`finetune_16bit`](https://huggingface.co/fesalfayed/gpt-oss-20b-hermes_agent-tool-finetune_16bit) | 16-bit | vLLM · full precision |

> 9k+ downloads across formats · MLX, GGUF, 4-bit, and 16-bit exports  
> [the collection →](https://huggingface.co/collections/fesalfayed/finetuned-hermes-function-calling-v1) · [repo notes →](https://github.com/fesalfayed/gpt-oss-20b-hermes-tool-finetune)

</td>
</tr>
</table>

<br/>

<table>
<tr>
<td valign="top">

### Open source

Merged fixes into the Hermes agent ecosystem — repositories totaling **205k+ stars**.
My contributions target where agent systems fail in production-shaped edge cases:
provider adapters, signed reasoning blocks, tool-use replay, and context assembly.

| project | contribution |
| :--- | :--- |
| [`NousResearch/hermes-agent`](https://github.com/NousResearch/hermes-agent/pull/35859) | Authored the fix for Anthropic extended-thinking crash loops when orphan tool-use stripping invalidated signed reasoning blocks; Teknium salvaged/cherry-picked it to `main` with authorship preserved ([commit `64628ea`](https://github.com/NousResearch/hermes-agent/commit/64628ea89b1d5624f47b402edd54b13afd335123), closes [#35847](https://github.com/NousResearch/hermes-agent/issues/35847)) |
| [`NousResearch/hermes-agent`](https://github.com/NousResearch/hermes-agent/pull/54083) | Authored the WhatsApp LID alias session-path fix so modern `platforms/whatsapp/session` installs stop silently dropping allowlisted senders; Teknium accepted it with authorship preserved ([commit `263ffec`](https://github.com/NousResearch/hermes-agent/commit/263ffec1b03114ec98671919943fb61de7ebf1bf), closes [#36664](https://github.com/NousResearch/hermes-agent/issues/36664)) |
| [`NousResearch/hermes-agent`](https://github.com/NousResearch/hermes-agent/issues/35975) | Filed and root-caused a separate interleaved-thinking signature crash loop; maintainers confirmed the order-preserving channel on `main` solved it without demoting reasoning |
| [`NousResearch/hermes-agent`](https://github.com/NousResearch/hermes-agent/pull/52276) | Maintains an adapter-level backstop PR for leading-assistant transcripts after compaction, complementing the built-in compressor fix path for [#52160](https://github.com/NousResearch/hermes-agent/issues/52160) / [#52167](https://github.com/NousResearch/hermes-agent/pull/52167) |
| [`stephenschoettler/hermes-lcm`](https://github.com/stephenschoettler/hermes-lcm/pull/280) | Merged role-invariant fix so DAG context summaries cannot become provider-visible leading assistant messages |

> More detail: [`oss-contributions`](https://github.com/fesalfayed/oss-contributions).

</td>
</tr>
</table>

<br/>

<table>
<tr>
<td valign="top" width="60%">

### Selected work

| work | what it shows |
| :--- | :--- |
| [`gpt-oss-20b-hermes-tool-finetune`](https://github.com/fesalfayed/gpt-oss-20b-hermes-tool-finetune) | End-to-end tool-use fine-tuning notes, export matrix, local inference packaging |
| [`hermes-Notion-Worker-sync`](https://github.com/fesalfayed/hermes-Notion-Worker-sync) | Production-shaped Discord ↔ Notion worker sync on `@notionhq/workers` |
| [`amazon-image-quality-bsr-analysis`](https://github.com/fesalfayed/amazon-image-quality-bsr-analysis) | Applied DS: image-quality metrics, pricing/review enrichment, BSR modeling |
| [`fesalfayed.com`](https://github.com/fesalfayed/fesalfayed-com) | Personal site and public identity surface |

</td>
<td valign="top" width="40%">

### Principles

```
build the infra first
glue siloed sources
humans design, agents scaffold
see the elephant, not the tail
```

</td>
</tr>
</table>

<br/>

<div align="center">

[hi@fesalfayed.com](mailto:hi@fesalfayed.com) &nbsp;·&nbsp; [huggingface.co/fesalfayed](https://huggingface.co/fesalfayed) &nbsp;·&nbsp; [fesalfayed.com](https://fesalfayed.com)

<sub>Data &amp; ML Engineer &middot; Miami &middot; B.S. Data Science &amp; AI, FIU</sub>

</div>
