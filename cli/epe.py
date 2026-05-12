#!/usr/bin/env python3
"""
EPE Compiler — Executable Prompt Engineering Reference Implementation

Reads .epe files, validates PROGRAM format, and compiles to executable output.

Usage:
    python3 epe.py validate my-prompt.epe       # Validate PROGRAM format
    python3 epe.py compile my-prompt.epe        # Compile and show output plan
    python3 epe.py list                         # List all .epe files
"""

import os, sys, re, json, pathlib

PROGRAM_FIELDS = ["NAME", "VERSION", "PURPOSE", "INPUT", "LOGIC", "CONSTRAINT", "OUTPUT"]

def parse_epe(filepath):
    """Parse a .epe file and return the PROGRAM fields as a dict."""
    content = pathlib.Path(filepath).read_text(encoding="utf-8")

    # Extract PROGRAM block
    m = re.search(r'\[PROGRAM\]\s*\n(.*?)\n\s*\[END\]', content, re.DOTALL)
    if not m:
        raise ValueError("No valid [PROGRAM]...[END] block found")

    body = m.group(1)
    fields = {}
    for line in body.strip().split("\n"):
        line = line.strip()
        if not line or line.startswith("#") or line.startswith("//"):
            continue
        match = re.match(r'^([A-Z_]+):\s*(.*)', line)
        if match:
            key, val = match.group(1), match.group(2).strip()
            fields[key] = val

    return fields

def validate(filepath):
    """Validate an .epe file against the PROGRAM spec."""
    errors = []
    try:
        fields = parse_epe(filepath)
    except ValueError as e:
        return {"valid": False, "errors": [str(e)], "fields": {}}

    # Check required fields
    for field in PROGRAM_FIELDS:
        if field not in fields or not fields[field]:
            errors.append(f"Missing required field: {field}")

    # Check NAME
    if "NAME" in fields and len(fields["NAME"]) < 2:
        errors.append("NAME must be at least 2 characters")

    # Check CONSTRAINT count
    if "CONSTRAINT" in fields:
        count = len([c for c in fields["CONSTRAINT"].split("、") if c.strip()])
        if count < 2:
            errors.append(f"CONSTRAINT must have at least 2 rules (found {count})")

    # Check LOGIC steps
    if "LOGIC" in fields:
        steps = fields["LOGIC"].count("→") + 1
        if steps < 3:
            errors.append(f"LOGIC should have at least 3 steps (found {steps})")

    return {
        "valid": len(errors) == 0,
        "errors": errors,
        "fields": fields,
        "file": os.path.basename(filepath)
    }

def list_epe_files(directory="."):
    """List all .epe files in a directory."""
    return sorted(pathlib.Path(directory).glob("**/*.epe"))

def main():
    if len(sys.argv) < 2:
        print("Usage: epe.py <command> [file]")
        print("Commands:")
        print("  validate <file>   Validate an .epe file")
        print("  compile <file>    Compile and show execution plan")
        print("  list              List all .epe files in current dir")
        sys.exit(1)

    cmd = sys.argv[1]

    if cmd == "list":
        files = list_epe_files()
        if not files:
            print("No .epe files found.")
            return
        print(f"Found {len(files)} .epe file(s):")
        for f in files:
            result = validate(str(f))
            badge = "✅" if result["valid"] else "❌"
            print(f"  {badge}  {f}")
        return

    if cmd in ("validate", "compile"):
        if len(sys.argv) < 3:
            print("Please specify a .epe file")
            sys.exit(1)

        filepath = sys.argv[2]
        if not os.path.exists(filepath):
            print(f"File not found: {filepath}")
            sys.exit(1)

        result = validate(filepath)

        print(f"\n{'='*50}")
        print(f"File: {result['file']}")
        print(f"{'='*50}")

        if not result["valid"]:
            print(f"Status: ❌ INVALID")
            for err in result["errors"]:
                print(f"  - {err}")
            sys.exit(1)

        print(f"Status: ✅ VALID")
        print(f"\nFields:")
        for key in PROGRAM_FIELDS:
            val = result["fields"].get(key, "(missing)")
            print(f"  {key:12} → {val}")

        if cmd == "compile":
            print(f"\n{'='*50}")
            print(f"COMPILE PLAN")
            print(f"{'='*50}")
            purpose = result["fields"].get("PURPOSE", "")
            logic = result["fields"].get("LOGIC", "")
            output = result["fields"].get("OUTPUT", "")

            print(f"  Target:      {purpose}")
            print(f"  Steps:       {logic}")
            print(f"  Output:      {output}")

            steps = [s.strip() for s in logic.split("→") if s.strip()]
            print(f"\n  Execution Plan ({len(steps)} steps):")
            for i, step in enumerate(steps, 1):
                print(f"    [{i}] {step}")

            print(f"\n  Constraints to enforce:")
            for c in result["fields"].get("CONSTRAINT", "").split("、"):
                if c.strip():
                    print(f"    ⚠  {c.strip()}")

        return

    print(f"Unknown command: {cmd}")
    print("Use: validate, compile, or list")
    sys.exit(1)

if __name__ == "__main__":
    main()
