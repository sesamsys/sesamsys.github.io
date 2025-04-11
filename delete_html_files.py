import os
from pathlib import Path

def delete_html_files():
    posts_dir = Path('_posts')
    
    # Get all HTML files in _posts directory
    html_files = list(posts_dir.glob('*.html'))
    
    # Delete each HTML file
    for html_file in html_files:
        print(f"Deleting: {html_file.name}")
        html_file.unlink()

if __name__ == '__main__':
    delete_html_files() 