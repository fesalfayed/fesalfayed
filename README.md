
---

**[#1 on comma.ai's video compression leaderboard](https://comma.ai/leaderboard)** — `semantic-pose-HPAC_CPR1`, 0.172 on comma's own T4 evaluation. Runner-up 0.187; the three prize winners scored 0.193–0.195. [Submission](https://github.com/commaai/comma_video_compression_challenge/pull/130) &nbsp;·&nbsp; [reproduction](https://github.com/fesalfayed/comma-ai-semantic-pose-hpac-cpr1) — byte-exact archive from a clean clone, reproduced independently by another entrant.

**[gpt-oss-20b, tuned for tool use](https://huggingface.co/collections/fesalfayed/finetuned-hermes-function-calling-v1)** — one weight set exported to four runtimes: MLX, GGUF, 4-bit, 16-bit. 19.8k downloads.

**Merged into [`hermes-agent`](https://github.com/NousResearch/hermes-agent) (223k★), [`topcoat`](https://github.com/tokio-rs/topcoat) (4k★), and [`hermes-lcm`](https://github.com/stephenschoettler/hermes-lcm)** — four fixes for bugs that only surface in real runs:

- [signed-reasoning replay crash loop](https://github.com/NousResearch/hermes-agent/pull/35859) — orphan tool-use stripping was invalidating signed reasoning blocks
- [session-allowlist resolution](https://github.com/NousResearch/hermes-agent/pull/54083) — modern WhatsApp installs were silently dropping allowlisted senders
- [DAG context role invariant](https://github.com/stephenschoettler/hermes-lcm/pull/280) — context summaries could surface as provider-visible leading assistant messages
- [formatter panic on macro bodies](https://github.com/tokio-rs/topcoat/pull/273) — a `prettyplease` round trip dropped token adjacency, re-parsing `aria-label` as `aria - label`

One further crash [filed and root-caused](https://github.com/NousResearch/hermes-agent/issues/35975), since resolved upstream. Write-ups: [`oss-contributions`](https://github.com/fesalfayed/oss-contributions).

---

[fesalfayed.com](https://fesalfayed.com) &nbsp;·&nbsp; [huggingface.co/fesalfayed](https://huggingface.co/fesalfayed) &nbsp;·&nbsp; [hi@fesalfayed.com](mailto:hi@fesalfayed.com)
