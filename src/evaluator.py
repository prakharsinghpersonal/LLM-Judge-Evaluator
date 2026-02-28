import argparse
import json
import logging
import sys
from tqdm import tqdm
import pandas as pd

from azure_client import AzureClient
from rubric import Rubric

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    datefmt="%m/%d/%Y %H:%M:%S",
    handlers=[logging.StreamHandler(sys.stdout)],
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

class Judge:
    def __init__(self):
        self.client = AzureClient()
        self.rubric = Rubric()

    def evaluate_batch(self, responses: List[str]) -> List[Dict]:
        results = []
        prompt_template = self.rubric.get_prompt_template()

        for response in tqdm(responses, desc="Evaluating"):
            prompt = prompt_template.format(response=response)
            evaluation = self.client.get_completion(prompt)
            results.append({
                "response": response,
                "evaluation": evaluation
            })
        return results

def main():
    parser = argparse.ArgumentParser(description="LLM-as-a-Judge Evaluator")
    parser.add_argument("--input_file", type=str, default="data/responses.json", help="Path to input JSON file")
    parser.add_argument("--output_file", type=str, default="results/evaluation.json", help="Path to output JSON file")
    args = parser.parse_args()

    logger.info("Starting Evaluation Pipeline...")
    
    # Mock data for demonstration if file doesn't exist
    if not os.path.exists(args.input_file):
        logger.warning(f"Input file {args.input_file} not found. Using mock data.")
        responses = [
            "Photosynthesis is the process used by plants to convert light energy into chemical energy.",
            "To reverse a string in Python, you can use the slicing method: text[::-1]",
            "Newton's second law states that Force = mass x acceleration."
        ]
    else:
        with open(args.input_file, 'r') as f:
            data = json.load(f)
            responses = [item['response'] for item in data]

    judge = Judge()
    results = judge.evaluate_batch(responses)

    # Save results
    os.makedirs(os.path.dirname(args.output_file), exist_ok=True)
    with open(args.output_file, 'w') as f:
        json.dump(results, f, indent=4)
    
    logger.info(f"Evaluation complete. Results saved to {args.output_file}")

if __name__ == "__main__":
    import os
    from typing import List, Dict
    main()
