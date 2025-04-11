import os
import re
import html
from pathlib import Path

def fix_html_entities(text):
    """Fix HTML entities in text."""
    # Common HTML entities that might need fixing
    entities = {
        '&amp;': '&',
        '&lt;': '<',
        '&gt;': '>',
        '&quot;': '"',
        '&#39;': "'",
        '&apos;': "'"
    }
    
    # Replace each entity with its proper character
    for entity, char in entities.items():
        text = text.replace(entity, char)
    
    # Use html module to decode any remaining entities
    return html.unescape(text)

def process_file(file_path):
    """Process a single HTML file and fix tags."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all tag sections
    # This pattern looks for tags in various formats
    tag_patterns = [
        r'<li>([^<]+)</li>',  # Basic list items
        r'<a[^>]*>([^<]+)</a>',  # Links
        r'<span[^>]*>([^<]+)</span>'  # Spans
    ]
    
    modified = False
    for pattern in tag_patterns:
        def replace_tag(match):
            nonlocal modified
            tag = match.group(1)
            fixed_tag = fix_html_entities(tag)
            if fixed_tag != tag:
                modified = True
                return match.group(0).replace(tag, fixed_tag)
            return match.group(0)
        
        content = re.sub(pattern, replace_tag, content)
    
    if modified:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed tags in {file_path}")
        return True
    return False

def main():
    """Main function to process all HTML files."""
    # Get the root directory (current directory)
    root_dir = Path('.')
    
    # Find all HTML files
    html_files = list(root_dir.rglob('*.html'))
    
    total_files = len(html_files)
    modified_files = 0
    
    print(f"Found {total_files} HTML files to process")
    
    for file_path in html_files:
        if process_file(file_path):
            modified_files += 1
    
    print(f"\nProcessing complete!")
    print(f"Modified {modified_files} out of {total_files} files")

if __name__ == '__main__':
    main() 