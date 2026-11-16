#!/usr/bin/env python3
"""Audit Set-Cookie headers for common browser security attributes."""
import argparse
import json
import sys
from pathlib import Path


def audit(lines):
    findings = []
    for number, raw in enumerate(lines, 1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if line.lower().startswith("set-cookie:"):
            line = line.split(":", 1)[1].strip()
        parts = [part.strip() for part in line.split(";")]
        if not parts or "=" not in parts[0]:
            findings.append((number, "error", "malformed cookie pair"))
            continue
        name = parts[0].split("=", 1)[0].strip()
        attrs = {}
        for item in parts[1:]:
            if not item:
                continue
            key, sep, value = item.partition("=")
            attrs[key.strip().lower()] = value.strip() if sep else None
        for key in ("secure", "httponly", "samesite"):
            if key not in attrs:
                findings.append((number, "warning", f"{name}: missing {key}"))
        same_site = (attrs.get("samesite") or "").lower()
        if same_site == "none" and "secure" not in attrs:
            findings.append((number, "error", f"{name}: SameSite=None requires Secure"))
        if name.startswith("__Secure-") and "secure" not in attrs:
            findings.append((number, "error", f"{name}: __Secure- cookies require Secure"))
        if name.startswith("__Host-"):
            if "secure" not in attrs:
                findings.append((number, "error", f"{name}: __Host- cookies require Secure"))
            if attrs.get("path") != "/":
                findings.append((number, "error", f"{name}: __Host- cookies require Path=/"))
            if "domain" in attrs:
                findings.append((number, "error", f"{name}: __Host- cookies must not set Domain"))
    return findings


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", nargs="?", type=Path, help="text file with Set-Cookie headers; stdin if omitted")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    try:
        lines = args.file.read_text(encoding="utf-8").splitlines() if args.file else sys.stdin.read().splitlines()
    except OSError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    findings = audit(lines)
    if args.json:
        print(json.dumps([{"line": n, "severity": s, "message": m} for n, s, m in findings], indent=2))
    elif not findings:
        print("No cookie flag issues found.")
    else:
        for number, severity, message in findings:
            print(f"line {number}: {severity}: {message}")
    return 1 if any(s == "error" for _, s, _ in findings) else 0


if __name__ == "__main__":
    raise SystemExit(main())
