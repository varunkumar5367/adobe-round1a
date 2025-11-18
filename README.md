Connecting the Dots Challenge - Round 1A Submission

This project extracts a structured outline (Title, H1, H2, H3) from PDF documents using a lightweight, heuristic-based Python approach.

My Approach

The solution uses no machine learning models and relies entirely on PDF style properties to infer structure. This ensures the system is fast, explainable, and lightweight.

🔹 1. Text Extraction

Using PyMuPDF, the script iterates through each page and extracts text spans along with detailed metadata:

Text

Font size

Font name

Page number

These attributes form the basis for all structural analysis.

🔹 2. Style Analysis

All extracted font sizes are collected, and the unique values are:

Sorted from largest to smallest

Used to determine the visual hierarchy of the document

This helps identify headings even when the document varies stylistically.

🔹 3. Heuristic Classification

Heading levels are assigned based on:

Font Size Priority → Largest = Title → Next = H1 → Next = H2 → Next = H3

Font Weight (Bold detection) → Bold text is more likely to be a heading

Text Patterns → Ensures headers aren't misclassified body text

This avoids the flaws of relying on a single attribute.

🔹 4. Structured JSON Output

The script assembles a clean, hierarchical JSON containing:

Heading Level

Extracted Text

Page Number

This makes integration with other systems straightforward.

Models or Libraries Used
✔ PyMuPDF (fitz)

Chosen for its speed and precision in extracting:

Text

Fonts

Font sizes

Page positions

✔ Python Standard Libraries

json → To generate structured output

os → File path handling

🔸 No ML models or heavy dependencies are used.
🔸 Entire solution runs fast on CPU and works on all operating systems.

How to Build and Run the Solution (Python Only)
Installation

Install dependencies:

pip install -r requirements.txt

Run the Script

Provide any PDF as input:

python extract_structure.py input.pdf


The output will print the full structured JSON in the console.
