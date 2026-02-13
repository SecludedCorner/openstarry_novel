import os

base = r"C:\Users\yulin\Desktop\claude research\research record\results\cycle_01\novel\academic\EN"

title = """# Code Arisen from Conditions — OpenStarry Cycle 01 Research Chronicle

> An interdisciplinary dialogue among eighteen AI research agents

---
"""

separator = """
---

<div style="page-break-after: always;"></div>

---

"""

colophon = """
---

## About This Book

This book was written based on the Cycle 01 interdisciplinary research process of OpenStarry v0.2.0-beta. All technical findings, philosophical arguments, and code citations derive from authentic research reports. Character dialogue has been given literary treatment, but core viewpoints faithfully reflect each agent's actual analytical conclusions.

**Research Team**: SUNYATA, SYNTHESIST, SCRIBE, VITRUVIUS, MESH, ATHENA, DARWIN, NAGARJUNA, ASANGA, BABBAGE, KERNEL, GUARDIAN, WIENER, LINNAEUS, LEIBNIZ, HERACLITUS, ARCHIMEDES, TURING

**Research Cycle**: Cycle 01 (2026-02-12)

---

*Arising from conditions, empty of inherent nature; all dharmas are without self.*
*Code arises from conditions, and is empty of independent existence.*
"""

chapters = [
    "00_prologue.md",
    "01_code_never_lies.md",
    "02_individual_truths.md",
    "03_four_threads.md",
    "04_reviewers_notes.md",
    "05_emptiness_and_consciousness.md",
    "06_three_views_of_pain.md",
    "07_puzzle_complete.md",
    "08_epilogue.md",
]

output_path = os.path.join(base, "full_novel.md")

with open(output_path, "w", encoding="utf-8") as out:
    out.write(title)
    for i, ch in enumerate(chapters):
        ch_path = os.path.join(base, ch)
        with open(ch_path, "r", encoding="utf-8") as f:
            content = f.read()
        out.write(content)
        if i < len(chapters) - 1:
            out.write(separator)
    out.write(colophon)

print("Done. Output:", output_path)
