import random

TEMPLATES = [
    "The {item} arrived with unexpected issues.",
    "Unfortunately, the {item} didn't meet expectations.",
    "I noticed some problems with the {item} after using it.",
    "The {item} seems defective or not functioning properly.",
    "There were quality concerns with the {item} upon arrival."
]

FILLERS = {
    "casual": ["just", "honestly", "kinda", "felt like", "sort of"],
    "assertive": ["clearly", "obviously", "without a doubt", "undeniably"],
    "passive": ["maybe", "I think", "not sure but", "possibly"]
}

def mutate_excuse(item_type, tone="casual"):
    template = random.choice(TEMPLATES)
    filler = random.choice(FILLERS.get(tone, [""]))
    excuse = template.replace("{item}", item_type)
    if filler:
        excuse = f"{filler.capitalize()}, {excuse}"
    return excuse

# Example usage
if __name__ == "__main__":
    print("🎭 Excuse:", mutate_excuse("supplement", "casual"))
