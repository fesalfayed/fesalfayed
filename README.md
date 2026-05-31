<div align="center">

<img src="./attention.svg" alt="a self-attention matrix as a self-portrait — the diagonal is the self attending to the self" width="660">

</div>

<br/>

# Fesal Fayed

> I build agents and fine-tune the models that run them.
> `agents type, humans steer`

<br/>

Most of my work lives in the space between a messy source and a signal you
can act on. I tune transformers for tool use, wire them into systems that do
real work, and keep a human — me — holding the wheel. The picture above is a
decoder's attention seeded from my name; the rest of this page is what it adds
up to.

<br/>

### Fine-tuning

`gpt-oss-20b` tuned for function-calling, shipped in four formats so it runs
wherever you are — Apple Silicon, llama.cpp, Colab, vLLM.

| model | format | runs on |
| :--- | :--- | :--- |
| [`finetune_mlx`](https://huggingface.co/fesalfayed/gpt-oss-20b-hermes_agent-tool-finetune_mlx)   | mlx    | Apple Silicon |
| [`finetune_gguf`](https://huggingface.co/fesalfayed/gpt-oss-20b-hermes_agent-tool-finetune_gguf) | gguf   | llama.cpp · Ollama · LM Studio |
| [`finetune_4bit`](https://huggingface.co/fesalfayed/gpt-oss-20b-hermes_agent-tool-finetune_4bit) | 4-bit  | Colab |
| [`finetune_16bit`](https://huggingface.co/fesalfayed/gpt-oss-20b-hermes_agent-tool-finetune_16bit) | 16-bit | vLLM |

> ~4,000 downloads across formats &middot; evals in progress
> [the collection &rarr;](https://huggingface.co/collections/fesalfayed/finetuned-hermes-function-calling-v1)

<br/>

### Systems

A multi-profile agentic harness — orchestrator, builders, an analyst —
running on [Hermes](https://huggingface.co/fesalfayed), wired through Discord,
kanban, and Notion. Local by default, cloud when a job earns it. Alongside it,
a quantified-self pipeline that folds biometrics, context, and training into
one store and asks the machine which habits actually move tomorrow.

<br/>

### How I work

```
fix the root, not the symptom        local default, cloud on demand
agents type, humans steer            one project, one repo, one job
```

<br/>

<div align="center">

[hi@fesalfayed.com](mailto:hi@fesalfayed.com) &nbsp;·&nbsp; [huggingface.co/fesalfayed](https://huggingface.co/fesalfayed) &nbsp;·&nbsp; [fesalfayed.com](https://fesalfayed.com)

<sub>Data &amp; ML Engineer &middot; Miami &middot; B.S. Data Science &amp; AI, FIU</sub>

</div>
