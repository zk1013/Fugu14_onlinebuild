#!/usr/bin/env python3
import sys
cdhash = sys.argv[1]
print(f"CDHash of jailbreakd: {cdhash}")

print("Patching arm/iOS/Fugu14App/Fugu14App/closures.swift...")

with open("./arm/iOS/Fugu14App/Fugu14App/closures.swift", "r") as f:
    closure_swift = f.read()

lines = []
for line in closure_swift.split("\n"):
    if line.startswith('        try simpleSetenv("JAILBREAKD_CDHASH", '):
        lines.append (f'        try simpleSetenv("JAILBREAKD_CDHASH", "{cdhash}")')
    else:
        lines.append(line)

with open("./arm/iOS/Fugu14App/Fugu14App/closures.swift", "w") as f:
    f.write("\n".join(lines))

print("Patched")