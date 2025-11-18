# PDF Document Structure Extraction (Lightweight Python Project)

## Project Summary
- Developed a heuristic-based solution to identify document structure without relying on complex ML models.
- Implemented core logic using **PyMuPDF**, extracting text spans with properties like **font size**, **font name**, and **page number**.
- Performed style analysis to detect unique font sizes and classify text hierarchy into **Title**, **H1**, **H2**, and **H3**.
- Outputs clean JSON representation of the document’s structure.

## Installation
```
pip install -r requirements.txt
```

## Usage
```
python extract_structure.py input.pdf
```
