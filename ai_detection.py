import os, re

def ai_score(text):
    ai_patterns = ['def ', 'return ', 'print(', 'class ', 'import ']
    long_lines = len([l for l in text.split('\n') if len(l) > 100])
    camel_case = len(re.findall(r'[a-z]+[A-Z][a-z]+', text))
    comments = len(re.findall(r'#', text))
    complexity = (long_lines + camel_case) / (comments + 1)
    return round(min(complexity * 10, 100), 2)

base_path = './'
scores = []
for root, _, files in os.walk(base_path):
    for f in files:
        if f.endswith('.py'):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf8') as file:
                text = file.read()
            score = ai_score(text)
            scores.append(score)
            print(f"{f}: {score}% AI-likeness")

print(f"\nOverall estimated AI-like pattern: {sum(scores)/len(scores):.2f}%")
