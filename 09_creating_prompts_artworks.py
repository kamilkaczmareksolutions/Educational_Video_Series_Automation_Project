# ===============================
# User Configuration Section
# ===============================

# Variables for the illustration prompts
variables = [
    "Observation", "Overview", "Fundamentals", "Sensory", "Details", "Differentiation", 
    "Importance", "Methodology", "Perception", "Data", "Analysis", "Uniqueness", "Sight", 
    "Touch", "Smell", "Hearing", "Taste", "Color", "Texture", "Chemistry", "Techniques", 
    "Attention", "Presence", "Tools", "Journaling", "Senses", "Features", "Contrast", 
    "Patterns", "Discovery"
]

# Color for the prompts
color = "LIGHT YELLOW"  # Replace with desired color

# Output file path
output_file_path = "illustration_prompts.txt"

# =================================
# End of User Configuration Section
# =================================

def create_prompts(color, variables):
    prompt_structure = """Create a minimalistic illustration that clearly and distinctively represents OBJECT. 
    The illustration should focus on making OBJECT immediately recognizable, with a central and prominent display. 
    Use smooth lines and gentle shading to convey a friendly and approachable feel. 
    Include organic and fluid patterns and shapes around OBJECT, ensuring they complement without overshadowing it. 
    The background should be a solid, COLOR hue, with a soft gradient. 
    Importantly, no text or lettering should be included in the illustration - the focus is entirely on the visual portrayal of OBJECT."""
    
    prompts = []
    for object_keyword in variables:
        prompt = prompt_structure.replace("OBJECT", object_keyword).replace("COLOR", color)
        prompts.append(prompt)
    return prompts

# Generate prompts
prompts = create_prompts(color, variables)

# Save the prompts to a file
with open(output_file_path, 'w') as file:
    for i, prompt in enumerate(prompts, 1):
        file.write(f"Prompt {i}:\n{prompt}\n\n")

print(f"Prompts saved to {output_file_path}")
