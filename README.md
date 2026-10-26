# Simple Notes Saver

A Flask web application that securely ingests technician notes, extracts a summary, and appends them to `notes.txt`.

## Summary Rule
For each saved note, a summary is generated and prepended:
- Extracts the **first complete sentence** (ending with `.`, `!`, or `?`) if it is 120 characters or fewer.
- Otherwise, truncates the note to 120 characters.

Notes are formatted in `notes.txt` as:
```text
Summary: <summary>
Note: <sanitized_note>
---