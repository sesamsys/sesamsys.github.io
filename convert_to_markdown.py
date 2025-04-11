import os
import re
from bs4 import BeautifulSoup
import html2text
from datetime import datetime
import shutil
import urllib.parse
import pathlib

def clean_front_matter(front_matter):
    # Remove WordPress-specific fields
    fields_to_remove = [
        'wordpress_id',
        'wordpress_url',
        'author_login',
        'author_email',
        'author_url',
        'status',
        'published'
    ]
    
    lines = front_matter.split('\n')
    cleaned_lines = []
    for line in lines:
        if not any(field in line for field in fields_to_remove):
            cleaned_lines.append(line)
    
    return '\n'.join(cleaned_lines)

def convert_html_to_markdown(html_content):
    # Initialize html2text
    h = html2text.HTML2Text()
    h.ignore_links = False
    h.ignore_images = False
    h.body_width = 0  # Disable line wrapping
    
    # Convert HTML to Markdown
    markdown = h.handle(html_content)
    
    # Clean up any remaining HTML entities
    markdown = markdown.replace('&amp;', '&')
    
    return markdown.strip()

def process_post(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Split front matter and content
        front_matter_match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
        if not front_matter_match:
            print(f"Warning: No front matter found in {file_path}")
            return
        
        front_matter = front_matter_match.group(1)
        html_content = content[front_matter_match.end():]
        
        # Clean front matter
        cleaned_front_matter = clean_front_matter(front_matter)
        
        # Convert HTML content to Markdown
        markdown_content = convert_html_to_markdown(html_content)
        
        # Create new content with cleaned front matter and markdown
        new_content = f"---\n{cleaned_front_matter}\n---\n\n{markdown_content}\n"
        
        # Create new filename with .md extension
        new_file_path = str(file_path).replace('.html', '.md')
        
        # Write the new file
        with open(new_file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"Converted {file_path} to {new_file_path}")
    except Exception as e:
        print(f"Error processing {file_path}: {str(e)}")

def safe_copy(src, dst):
    """Safely copy a file, handling special characters in paths."""
    try:
        shutil.copy2(src, dst)
    except Exception as e:
        print(f"Warning: Could not copy {src} to {dst}: {str(e)}")

def main():
    posts_dir = '_posts'
    
    # Create backup of original files
    backup_dir = '_posts_backup'
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    
    # Process all HTML files
    for filename in os.listdir(posts_dir):
        if filename.endswith('.html'):
            src_path = os.path.join(posts_dir, filename)
            dst_path = os.path.join(backup_dir, filename)
            
            # First backup the file
            safe_copy(src_path, dst_path)
            
            # Then process it
            process_post(src_path)

if __name__ == '__main__':
    main() 