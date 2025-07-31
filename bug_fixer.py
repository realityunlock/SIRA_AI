# modules/bug_fixer.py

import traceback

class CodeDebugger:
    def __init__(self):
        pass

    def analyze_code(self, code):
        try:
            # Try to run the code
            exec(code, {})
            return "✅ No error found in the code."
        except Exception as e:
            # If an error happens, return the full error message
            return f"❌ Error found:\n{traceback.format_exc()}"