<div align="center">

<img src="./attention.svg" alt="a self-attention matrix as a self-portrait — the diagonal is the self attending to the self" width="660">

<br/>

# Fesal Fayed

> Agentic systems, tool-use fine-tuning, and applied ML · B.S. Data Science & AI @ FIU

</div>

<br/>

<table>
<tr>
<td align="center">

Currently exploring agentic infrastructure, model fine-tuning,
adapter correctness, context management, and the workflow glue that lets agents
affect the real world without taking the wheel from the human.

</td>
</tr>
</table>

<br/>

<table>
<tr>
<td valign="top" width="50%">

### Ongoing Explorations

| signal | evidence |
| :--- | :--- |
| **Model shipping** | Fine-tuned `gpt-oss-20b` for Hermes-style tool use and released MLX, GGUF, 4-bit, and 16-bit artifacts |
| **Adoption** | 9k+ Hugging Face downloads across formats |
| **OSS** | Authored two `NousResearch/hermes-agent` fixes accepted by Teknium: [Anthropic signed-thinking replay](https://github.com/NousResearch/hermes-agent/commit/64628ea89b1d5624f47b402edd54b13afd335123) and [WhatsApp LID alias resolution](https://github.com/NousResearch/hermes-agent/commit/263ffec1b03114ec98671919943fb61de7ebf1bf) |
| **OSS** | Merged [`hermes-lcm` PR #280](https://github.com/stephenschoettler/hermes-lcm/pull/280), fixing provider-visible summary role invariants |
| **Systems** | Discord ↔ Notion worker sync, multi-profile agent harness, local-first automation |
| **DS/ML** | Amazon image-quality + product-rank modeling case study |

</td>
</tr>
</table>

<br/>

<table>
<tr>
<td valign="top" width="50%">

### Fine-tuning

`gpt-oss-20b` tuned for Hermes-style function calling, shipped in four formats
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

### OSS

My contributed fixes focus on where agent systems fail in production-shaped edge cases:
provider adapters, signed reasoning blocks, tool-use replay, and context
assembly.

| project | contribution |
| :--- | :--- |
| [`NousResearch/hermes-agent`](https://github.com/NousResearch/hermes-agent/pull/35859) | Authored the fix for Anthropic extended-thinking crash loops when orphan tool-use stripping invalidated signed reasoning blocks; Teknium salvaged/cherry-picked it to `main` with authorship preserved ([commit `64628ea`](https://github.com/NousResearch/hermes-agent/commit/64628ea89b1d5624f47b402edd54b13afd335123), closes [#35847](https://github.com/NousResearch/hermes-agent/issues/35847)) |
| [`NousResearch/hermes-agent`](https://github.com/NousResearch/hermes-agent/pull/54083) | Authored the WhatsApp LID alias session-path fix so modern `platforms/whatsapp/session` installs stop silently dropping allowlisted senders; Teknium accepted it with authorship preserved ([commit `263ffec`](https://github.com/NousResearch/hermes-agent/commit/263ffec1b03114ec98671919943fb61de7ebf1bf), closes [#36664](https://github.com/NousResearch/hermes-agent/issues/36664)) |
| [`NousResearch/hermes-agent`](https://github.com/NousResearch/hermes-agent/issues/35975) | Filed and root-caused a separate interleaved-thinking signature crash loop; maintainers confirmed the order-preserving channel on `main` solved it without demoting reasoning |
| [`NousResearch/hermes-agent`](https://github.com/NousResearch/hermes-agent/pull/52276) | Maintains an adapter-level backstop PR for leading-assistant transcripts after compaction, complementing the built-in compressor fix path for [#52160](https://github.com/NousResearch/hermes-agent/issues/52160) / [#52167](https://github.com/NousResearch/hermes-agent/pull/52167) |
| [`stephenschoettler/hermes-lcm`](https://github.com/stephenschoettler/hermes-lcm/pull/280) | Merged role-invariant fix so DAG context summaries cannot become provider-visible leading assistant messages |

> More detail: [`oss-contributions`](https://github.com/fesalfayed/oss-contributions).
>

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
build the infra first                   glue siloed sources
humans design, agents scaffold          see the elephant, not the tail
```

</td>
</tr>
</table>

<br/>

<div align="center">

[hi@fesalfayed.com](mailto:hi@fesalfayed.com) &nbsp;·&nbsp; [huggingface.co/fesalfayed](https://huggingface.co/fesalfayed) &nbsp;·&nbsp; [fesalfayed.com](https://fesalfayed.com)

<sub>Data &amp; ML Engineer &middot; Miami &middot; B.S. Data Science &amp; AI, FIU</sub>

</div>