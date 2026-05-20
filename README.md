# fesal

data science and ai at fiu

i build agents and i fine-tune models

---

## what i actually shipped

**hermes function-calling fine-tunes** — gpt-oss-20b tuned for tool use, released in four formats so it runs wherever

collection: https://huggingface.co/collections/fesalfayed/finetuned-hermes-function-calling-v1

| model | format | downloads |
| :--- | :--- | ---: |
| [gpt-oss-20b-hermes_agent-tool-finetune_mlx](https://huggingface.co/fesalfayed/gpt-oss-20b-hermes_agent-tool-finetune_mlx) | mlx | 1,120 |
| [gpt-oss-20b-hermes_agent-tool-finetune_gguf](https://huggingface.co/fesalfayed/gpt-oss-20b-hermes_agent-tool-finetune_gguf) | gguf | 1,006 |
| [gpt-oss-20b-hermes_agent-tool-finetune_4bit](https://huggingface.co/fesalfayed/gpt-oss-20b-hermes_agent-tool-finetune_4bit) | 4-bit | 191 |
| [gpt-oss-20b-hermes_agent-tool-finetune_16bit](https://huggingface.co/fesalfayed/gpt-oss-20b-hermes_agent-tool-finetune_16bit) | 16-bit | 89 |

2,400+ downloads + eval coming soon

---

## what i'm in the middle of

a multi-agent setup running on hermes. orchestration frameworks, building local infra for agentic workflows. collecting datasets & fine-tuning. and local LLM hosting + evals for personal use-cases.

a quantified-self pipeline that pulls ultrahuman and siloed ios/apple into one store. the actual goal is predicting mood from biometrics and digital context -> ML model for correlation (coming soon)

llm post-training. quantization. mlx and gguf and 4-bit. getting open models small enough to live on a mac mini

---

## stack

llms — pytorch, dspy, vllm, llama.cpp, mlx, lm-eval-harness, w&b

agents — hermes, mcp, discord, notion workers sdk

day to day — python, typescript, bash, docker, tailscale

---

## links

huggingface https://huggingface.co/fesalfayed

fiu, b.s. data science and ai

miami
