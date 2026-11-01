# MDnight

Clean up your Obsidian notes overnight with LLMs, for free.

## Project Goal

The goal is to build a CLI which runs overnight that can keep the notes in an Obsidian vault clean, no matter how messy the notetaker is during the day.

## MVP

A working CLI, which can work overnight starting from one command. It should only process new and changed files, and read and write directly from the Obsidian vault. 

## Plans

- Customizable instruction prompt
- Only processing changes since last run
- Support for non-Markdown formats
- Throttling inference to reduce heat
- Confidence levels and warnings for certain changes
- Linking between files

## Tech Stack

- Obsidian: the notetaking aspect, has tons of plugins including gitÎ
- Markdown: well known syntax, versatile enough. Note storage format of Obsidian
- llama.cpp server: local inference, very customizable
- OpenAI-style API: llama servers use this, also makes it easier to swap in other models for testing since they’re just gonna be making the same API calls with a different endpoint.
- Bash: probably needed at some point, since I’m using a decent number of command line tools and interacting with files
- Local models: (no need for the speed of MoEs, but streaming weights from SSD is probably too slow)
	- Qwen3.8 27B (Q3/4): probably best model runnable locally, a bit slow but that doesn’t matter. Easy to switch to Qwen4 when that comes out.
	- Qwen3.5 9B/Gemma 4 12B (Q4/6): models with smaller footprints, worth testing in case performance is not significantly worse.
	- I lowkey kinda wanna experiment with streaming a larger MoE from SSD since speed doesn’t matter and the kinda knowledge task that this is could really benefit from a larger model with more knowledge, but that’s really unnecessary and an inference thing anyways.
- Python: easy to write scripts, lots of libraries, I know the language, performance doesn’t matter.
	- Typer: should be good for building simple CLIs
	- OpenAI: more easily make API calls, since I’m using llama serve
	- Requests: might be needed? I think oai handles it though.
- Git: can be used to track new/changed files between runs of the program
- JSON: probably just some JSON log in addition to track progress in case of interruption