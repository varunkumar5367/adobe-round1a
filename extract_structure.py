import fitz
import json
import sys
from collections import Counter, defaultdict

def extract_text_spans(pdf_path):
    doc = fitz.open(pdf_path)
    spans = []
    for page_index, page in enumerate(doc):
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            if "lines" not in block:
                continue
            for line in block["lines"]:
                for span in line["spans"]:
                    text = span["text"].strip()
                    if text:
                        spans.append({
                            "text": text,
                            "font_size": span["size"],
                            "font_name": span["font"],
                            "page": page_index + 1
                        })
    return spans

def analyze_font_sizes(spans):
    sizes = [round(s["font_size"]) for s in spans]
    sorted_sizes = sorted(set(sizes), reverse=True)
    levels = ["Title", "H1", "H2", "H3"]
    hierarchy = {}
    for i, size in enumerate(sorted_sizes[:4]):
        hierarchy[size] = levels[i]
    return hierarchy

def classify_headings(spans, hierarchy):
    structured = []
    for span in spans:
        size = round(span["font_size"])
        level = hierarchy.get(size, "Body")
        structured.append({
            "text": span["text"],
            "level": level,
            "font_size": span["font_size"],
            "font_name": span["font_name"],
            "page": span["page"]
        })
    return structured

def group_hierarchy(structured):
    grouped = defaultdict(list)
    for item in structured:
        grouped[item["level"]].append({
            "text": item["text"],
            "page": item["page"]
        })
    return grouped

def extract_document_structure(pdf_path):
    spans = extract_text_spans(pdf_path)
    hierarchy = analyze_font_sizes(spans)
    structured = classify_headings(spans, hierarchy)
    grouped = group_hierarchy(structured)
    return {
        "font_hierarchy": hierarchy,
        "document_structure": grouped
    }

if __name__ == "__main__":
    pdf_path = sys.argv[1]
    result = extract_document_structure(pdf_path)
    print(json.dumps(result, indent=4))
