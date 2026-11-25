## My Agent

A personal learning and development project focused on Python programming, AI Agents, and practical research in AI engineering.

## Overview

This project is developed as part of my journey in Artificial Intelligence. It aims to build a solid understanding of Large Language Models (LLMs), tool-using agents, and agent architectures through hands-on programming and paper reproduction.

The initial focus is on understanding and implementing the ReAct (Reasoning + Acting) framework using native Python.

## Learning Objectives

- Strengthen Python programming and software engineering skills.
- Understand LLM APIs and prompt engineering.
- Study the ReAct framework and its underlying principles.
- Implement tool registration and dynamic tool execution.
- Build multi-tool AI Agents from scratch without relying on high-level agent frameworks.
- Conduct small-scale experiments and analyze agent performance.
- Develop the ability to read, understand, and reproduce AI research papers.

## Research Focus

React: Synergizing Reasoning and Acting in Language Models

- Paper: https://arxiv.org/abs/2210.03629
- Official Repository:
    https://github.com/ysymyth/ReAct

## The project will explore the interaction between:

- Thought: Reasoning about the current task.
- Action: Selecting and executing an available tool.
- Observation: Receivng feedback from the environment.

The goal is to implement a simplified ReAct-style agent and investigate how reasoning and tool execution work together.

This project is an educational implementation, not a complete reproduction of the original paper's experiments.

## Project Structure

My_agent/
├── agent/          # Agent core logic
├── api/            # LLM API integration
├── experiments/    # Experimental records and results
├── practice/       # Python programming exercises
├── prompts/        # Prompt templates
├── tests/          # Unit and integration tests
├── tools/          # Tool implementations
├── requirements.txt
├── .gitignore
└── README.md

## Technology Stack

- Python 3.14

- OpenAI Python SDK

- DeepSeek API

- Git and GitHub

- Linux / Ubuntu

- Visual Studio Code

## Development Environment

- Create and activate a virtual environment:

python3 -m venv .venv
source .venv/bin/activate

- Install dependencies:

python -m pip install -r requirements.txt

- For Windows users, activate the environment with:

.venv\Scripts\Activate.ps1

## API Configuration

- This project uses the DeepSeek API through an OpenAI-compatible Python SDK.

- API credentials should be configured through environment variables.

# Never hard-code API keys or commit sensitive credentials to GitHub.

## Development Roadmap

- (done)Create the initial project structure.

- (done)Set up an isolated Python virtual environment.

- (done)Install the OpenAI Python SDK.

- (done)Create a dependency list.

- (done)Configure Git ignore rules.

- Implement DeepSeek API integration.

- Build a Python tool registry.

- Implement Action parsing and execution.

- Develop a ReAct-style agent loop.

- Implement multiple tools.

- Conduct small-scale comparative experiments.

- Study and reproduce selected examples from the original ReAct repository.

## Research and Learning Philosophy

- This project emphasizes understanding over copying.

- The implementation process prioritizes:

    Reading original research papers.

    Understanding the underlying mechanisms.

    Writing and debugging code independently.

    Recording experimental results.

    Analyzing limitations and failure cases.

## The long-term goal is to develop practical skills in AI engineering and research-oriented agent development.
