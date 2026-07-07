I train small models for tool use and fix the runtimes that serve them.

---

**[gpt-oss-20b, tuned for tool use](https://huggingface.co/collections/fesalfayed/finetuned-hermes-function-calling-v1)** — one weight set exported to four runtimes: MLX, GGUF, 4-bit, 16-bit. 14k downloads. [build notes →](https://github.com/fesalfayed/gpt-oss-20b-hermes-tool-finetune)

**Merged into [`hermes-agent`](https://github.com/NousResearch/hermes-agent) (210k★) and [`hermes-lcm`](https://github.com/stephenschoettler/hermes-lcm)** — three fixes for bugs that only surface in real agent runs:

- [signed-reasoning replay crash loop](https://github.com/NousResearch/hermes-agent/pull/35859) — orphan tool-use stripping was invalidating signed reasoning blocks
- [session-allowlist resolution](https://github.com/NousResearch/hermes-agent/pull/54083) — modern WhatsApp installs were silently dropping allowlisted senders
- [DAG context role invariant](https://github.com/stephenschoettler/hermes-lcm/pull/280) — context summaries could surface as provider-visible leading assistant messages

One further crash [filed and root-caused](https://github.com/NousResearch/hermes-agent/issues/35975), since resolved upstream. Write-ups: [`oss-contributions`](https://github.com/fesalfayed/oss-contributions).

---

[fesalfayed.com](https://fesalfayed.com) &nbsp;·&nbsp; [huggingface.co/fesalfayed](https://huggingface.co/fesalfayed) &nbsp;·&nbsp; [hi@fesalfayed.com](mailto:hi@fesalfayed.com)
