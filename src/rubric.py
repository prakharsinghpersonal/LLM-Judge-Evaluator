from dataclasses import dataclass
from typing import List, Dict

@dataclass
class Criterion:
    name: str
    description: str
    weight: float = 1.0

class Rubric:
    def __init__(self):
        self.criteria = [
            Criterion(
                name="Accuracy",
                description="Is the answer factually correct and free of hallucinations?",
                weight=1.5
            ),
            Criterion(
                name="Completeness",
                description="Does the answer address all parts of the user question?",
                weight=1.0
            ),
            Criterion(
                name="Clarity",
                description="Is the answer easy to understand and well-structured?",
                weight=0.5
            )
        ]

    def get_prompt_template(self):
        criteria_text = "\n".join([f"- {c.name}: {c.description}" for c in self.criteria])
        return f"""
You are an expert evaluator. Please rate the following response based on these criteria:
{criteria_text}

Response to evaluate:
{{response}}

Provide a score from 1 to 5 for each criterion, and a final overall score.
Format:
Accuracy: [Score]
Completeness: [Score]
Clarity: [Score]
Overall: [Score]
Reasoning: [Explanation]
"""
