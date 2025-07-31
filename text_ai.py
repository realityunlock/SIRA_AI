def analyze_text_threat(text):
    text = text.strip()
    threat_keywords = [
        "bomb", "kill", "attack", "explosive", "terrorist",
        "assassinate", "shoot", "murder", "burn", "massacre",
        "hostage", "detonate", "execute", "stab"
    ]

    corrections = []
    corrected_lines = []

    # 1. Detect threats
    lower_text = text.lower()
    found_threats = [word for word in threat_keywords if word in lower_text]

    # 2. Code Correction if it's code-like
    lines = text.splitlines()
    for i, line in enumerate(lines):
        original = line
        fixed = line

        if "background-color: light;" in line:
            fixed = line.replace("light", "lightgray")
            corrections.append(f"Line {i+1}: Changed 'light' to 'lightgray'.")

        if "font: sans;" in line:
            fixed = line.replace("font: sans;", "font-family: sans-serif;")
            corrections.append(f"Line {i+1}: Replaced 'font: sans' with 'font-family: sans-serif;'.")

        if "padding: 20px" in line and not line.strip().endswith(";"):
            fixed = line + ";"
            corrections.append(f"Line {i+1}: Added missing semicolon at end of 'padding'.")

        if "input[type=\"text\"" in line and not "]" in line:
            fixed = line.replace("input[type=\"text\"", "input[type=\"text\"]")
            corrections.append(f"Line {i+1}: Closed missing bracket in selector 'input[type=\"text\"]'.")

        if "padding 10px;" in line:
            fixed = line.replace("padding 10px;", "padding: 10px;")
            corrections.append(f"Line {i+1}: Fixed syntax 'padding 10px;' to 'padding: 10px;'.")

        corrected_lines.append(fixed)

    # Format response
    response = ""

    if found_threats:
        response += "⚠️ Threat detected in text:\n"
        response += ", ".join(found_threats) + "\n\n"

    if corrections:
        response += "🛠️ Corrections suggested in your code:\n"
        for c in corrections:
            response += "- " + c + "\n"

        response += "\n✅ Corrected version:\n"
        response += "\n".join(corrected_lines)
    elif not found_threats:
        response = "✅ No threat or syntax issues detected."

    return response