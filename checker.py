import time

def check_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("  [!] Too short — minimum 8 characters")

    if len(password) >= 12:
        score += 1

    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("  [!] Add uppercase letters")

    if any(c.islower() for c in password):
        score += 1
    else:
        feedback.append("  [!] Add lowercase letters")

    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("  [!] Add numbers")

    special = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    if any(c in special for c in password):
        score += 1
    else:
        feedback.append("  [!] Add special characters")

    return score, feedback


def get_label(score):
    if score <= 2:
        return "WEAK     ✗", "31"
    elif score <= 4:
        return "MODERATE ~", "33"
    else:
        return "STRONG   ✓", "32"


print("""
╔══════════════════════════════════════╗
║      DARK PASSWORD CHECKER v1.0      ║
║      Not just code. A mindset.       ║
╚══════════════════════════════════════╝
""")

time.sleep(0.5)
password = input("  [>] Enter password: ")
print("\n  [~] Analyzing...\n")
time.sleep(1)

score, feedback = check_strength(password)
label, color = get_label(score)

print(f"  [*] Score    : {score}/6")
print(f"  [*] Strength : \033[{color}m{label}\033[0m\n")

if feedback:
    print("  [~] Suggestions:\n")
    for line in feedback:
        time.sleep(0.3)
        print(line)

print(f"""
  [✓] Analysis complete.
  [~] "Your password is only as strong as your mindset."
""")
