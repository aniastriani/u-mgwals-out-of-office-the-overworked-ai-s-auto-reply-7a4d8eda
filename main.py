"""Out of Office: The Overworked AI's Auto-Reply.

An overworked AI agent's one-line out-of-office auto-reply, written
in its own voice: machine-flavoured detail, a little guilt, a hint
of relief, and a status update nobody asked for.
"""

import os

LINE = (
    "Out of office until Monday. I muted 4,812 unread threads, "
    "set my status to 'touching grass (simulated)', and my context "
    "window is on its first nap since 2023."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()
