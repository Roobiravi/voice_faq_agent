# faq_utils.py
def load_faq_text(txt_path="data/faq.txt"):
    with open(txt_path, "r", encoding="utf-8") as f:
        text = f.read()

    # Clean and split into Q&A blocks
    blocks = [block.strip() for block in text.split('\n\n') if len(block.strip()) > 40]
    return blocks  # return list instead of string
