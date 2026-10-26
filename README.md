# Simple Notes Saver

A Flask web application that securely ingests technician notes, extracts a 20-word summary, and appends the entry to a local `notes.txt` file.

## Summary Rule & Storage Format
- **Summary Extraction:** Automatically extracts the **first 20 words** from the note. Notes with fewer than 20 words are saved in full as the summary.
- **Format in `notes.txt`:**
  ```text
  Summary: <first 20 words>
  <sanitized_note>
  ---