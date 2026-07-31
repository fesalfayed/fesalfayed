I build machine-learning systems under hard constraints and publish what the measurements said.

## Video compression

Rank #1 of 64 on the [comma.ai video compression leaderboard](https://comma.ai/leaderboard), score 0.172 on comma's [official T4 evaluation](https://github.com/commaai/comma_video_compression_challenge/pull/130#issuecomment-5028795671) over 600 samples.

| Rank | Entry | Score (lower is better) |
|---:|---|---:|
| 1 | `semantic-pose-HPAC_CPR1` (mine) | 0.172 |
| 2 | `rhnerv_latent_polish` | 0.187 |
| 8 | `hnerv_ft_microcodec` (prize winner) | 0.193 |
| 9 | `hnerv_lc_ac` (prize winner) | 0.195 |
| 10 | `hnerv_lc_v2_scale095_rplus1` (prize winner) | 0.195 |

This extends jas0xf's [merged PR #86](https://github.com/commaai/comma_video_compression_challenge/pull/86), which established the semantic-token and HPAC codec family in this challenge. I trained three components for it: a width-96 semantic renderer, a learned low-rank pose basis rendered per frame by one einsum rather than by a network, and an integer HPAC entropy model whose arithmetic-coded token stream is 116,980 bytes of the 191,052-byte archive. What is original in that lineage is exactness: HPAC inference on a bounded integer lattice with cross-device symbol verification, a standalone pose carrier in place of PR #86's NeRV slave renderer, and a deterministic repack gated on the archive hash. The archive [rebuilds byte-exact from a clean clone](https://github.com/fesalfayed/comma-ai-semantic-pose-hpac-cpr1), and another entrant [reproduced it](https://github.com/commaai/comma_video_compression_challenge/pull/130#issuecomment-5016978941) on their own RTX 5070 at 0.171. Prizes went to entries that landed earlier, so this holds the top score and no prize.

## Open source

Five fixes landed on `main` across three external repositories.

| Repo | Stars | Fix | Landed as |
|---|---:|---|---|
| `tokio-rs/topcoat` | 4,030 | formatter panic on nested macros | [PR #273](https://github.com/tokio-rs/topcoat/pull/273) |
| `stephenschoettler/hermes-lcm` | 929 | HTTP 400 from a leading assistant turn | [PR #280](https://github.com/stephenschoettler/hermes-lcm/pull/280) |
| `NousResearch/hermes-agent` | 223,369 | signed-reasoning replay crash loop | [commit 64628ea](https://github.com/NousResearch/hermes-agent/commit/64628ea89b) |
| `NousResearch/hermes-agent` | 223,369 | WhatsApp senders dropped by alias resolver | [commit 263ffec](https://github.com/NousResearch/hermes-agent/commit/263ffec1b0) |
| `NousResearch/hermes-agent` | 223,369 | HTTP 400 after a second compaction | [commit e71c113](https://github.com/NousResearch/hermes-agent/commit/e71c1137e8) |

The hermes-agent commits landed through maintainer cherry-picks from my closed pull requests, with git authorship preserved. I filed the topcoat panic as [#272](https://github.com/tokio-rs/topcoat/issues/272); the fix merged 57 minutes after I opened the pull request.

## Models

19,786 all-time downloads of one gpt-oss-20b tool-use finetune, exported to GGUF, MLX, 4-bit, and 16-bit ([Hugging Face](https://huggingface.co/fesalfayed)).

## Contact

[fesalfayed.com](https://fesalfayed.com) · [hi@fesalfayed.com](mailto:hi@fesalfayed.com)
