# Simple Notes Saver

A lightweight Flask web application that securely ingests technician notes, extracts a 20-word summary, and appends the formatted entry to a local `notes.txt` file.

- **Live Deployment URL:** https://simple-notes-saver-production.up.railway.app
- **Full Handover Document:** [HANDOVER.md](HANDOVER.md)

---

## Handover & Architecture Overview

### Purpose
Designed as an MVP tool for technicians to rapidly record field notes with auto-generated summary headers for structured log tracking.

### Live URL & Usage Steps
1. Visit the live app at: `https://simple-notes-saver-production.up.railway.app`
2. Enter your note into the text area.
3. Click **Save**.
4. The backend extracts the first 20 words as a summary header and saves the formatted entry.

### Storage Limitation (Ephemeral File System)
- **Local Storage Mechanism:** Notes are written to `notes.txt` formatted as:
  ```text
  Summary: <first 20 words>
  <sanitized_note>
  ---