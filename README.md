# LLM-as-a-Judge Evaluator

## Overview
This project provides a robust benchmarking framework utilizing LLM-as-a-judge workflows. It evaluates model responses using structured rubric-based scoring methodologies, achieving high correlation with human annotators.

## Key Features
- **LLM-as-a-Judge:** Automates evaluation of model outputs using Azure OpenAI models.
- **Rubric-Based Scoring:** Implements structured scoring criteria for consistent evaluation.
- **Efficiency:** Reduces manual evaluation time by ~65% while processing thousands of responses.
- **Documentation:** Standardized benchmark methodology for cross-functional teams.

## Installation

```bash
pip install -r requirements.txt
```

## Usage

To run an evaluation:

```bash
python src/evaluator.py --input_file data/responses.json --output_file results/evaluation.json
```

## Architecture
- `src/evaluator.py`: Core logic for the evaluation loop.
- `src/rubric.py`: Defines the criteria and scoring logic.
- `src/azure_client.py`: Interface for Azure OpenAI.
