# 🐍 Dark Password Checker v1.0

> "Your password is only as strong as your mindset."

A minimal, cinematic password strength analyzer built in pure Python.
No external dependencies. Just logic, color, and clarity.

## Usage

```bash
python checker.py
```

## Output preview
╔══════════════════════════════════════╗
║      DARK PASSWORD CHECKER v1.0      ║
║      Not just code. A mindset.       ║
╚══════════════════════════════════════╝
[>] Enter password: ********
[] Score    : 5/6
[] Strength : STRONG   ✓
[~] Suggestions:
[!] Add special characters

## How it works

Analyzes 6 factors:
- Minimum length (8+ characters)
- Extended length (12+ characters)
- Uppercase letters
- Lowercase letters
- Numbers
- Special characters

Each factor adds 1 point to the score.

| Score | Strength |
|-------|----------|
| 0–2   | WEAK     |
| 3–4   | MODERATE |
| 5–6   | STRONG   |

## ⚠️ Disclaimer

For educational purposes only.
Never share or store passwords in plain text.
