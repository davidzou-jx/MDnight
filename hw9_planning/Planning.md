# Planning

## The Problem

Sometimes for classes, I take notes in Obsidian, which stores everything in locally plaintext with markdown syntax plus some extended features like LaTeX and HTML. However my class notes are often very messy, with lots of shorthands and messy formatting and organization.

## The Idea

LLMs in a harness such as Codex or Claude Code work really well for organizing the notes, but I don’t really want to burn tokens on something so relatively unimportant, and with the overhead of a full harness. So I want to build a CLI which does the fixing with a local model and better review mechanisms, and make it run overnight so speed is unnecessary. Will probably be a CLI in mostly python, plus git (for note diffs), and llama.cpp with Qwen3.8 27B or Gemma 4 (something <30B params at under Q4 so it runs on my 24GB computer).

## Eisenhower Matrix

|               | Urgent                                                                                                                                                                 | Not Urgent                                                                                                                                                                                                                                      |
| ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Important     | - A working CLI<br>- One command to start entire process (including server)<br>- Processing only new/changed files<br>- Directly reading and writing in the notes file | - Customizable instruction prompt<br>- Only processing changes since last run<br>- Support for non-Markdown formats<br>- Throttling inference to reduce heat<br>- Confidence levels and warnings for certain changes<br>- Linking between files |
| Not important | - Model selection: huggingface<br>- Local inference: llama.cpp<br>- Reviewing changes: git diff<br>- Notetaking and viewing: Obsidian<br>- CLI parsing: typer          | - Detecting hardware and suggesting model<br>- GUI<br>- Easier setup for the llama server<br>- Running MoE with SSD streaming<br>- Fan controller<br>- Non-markdown handling<br>- Model choice in the CLI                                       |
|               |                                                                                                                                                                        |                                                                                                                                                                                                                                                 |

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

## Build Plan

1. Based on git of the Obsidian Vault, parse a list of files that have been changed since the last run.
2. Extract the text into some python structure (prob just a dictionary)
3. Create some mechanism for storing different models with configurations
4. Implement starting the llama server from python
5. Figure out and implement how to start a new session with fresh context for each note file
6. Make a function for processing a single file
7. Implement the structure for editing all files
8. Output the edited files to the vault and commit.
9. Write the prompt for the calls
10. Make the CLI

## System Diagram

![[Planning 2026-10-30 14.54.44.excalidraw]]
