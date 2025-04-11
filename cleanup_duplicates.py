import os
import shutil
from pathlib import Path

def cleanup_duplicates():
    posts_dir = Path('_posts')
    backup_dir = Path('_posts_html_backup')
    
    # Create backup directory if it doesn't exist
    backup_dir.mkdir(exist_ok=True)
    
    # Get all files in _posts directory
    files = list(posts_dir.glob('*'))
    
    # Group files by their base name (without extension)
    file_groups = {}
    for file in files:
        base_name = file.stem
        if base_name not in file_groups:
            file_groups[base_name] = []
        file_groups[base_name].append(file)
    
    # Process each group
    for base_name, group in file_groups.items():
        if len(group) > 1:  # If we have duplicates
            # Find .md and .html files
            md_file = next((f for f in group if f.suffix == '.md'), None)
            html_files = [f for f in group if f.suffix == '.html']
            
            if md_file and html_files:
                print(f"Processing {base_name}:")
                print(f"  Keeping: {md_file.name}")
                
                # Move HTML files to backup
                for html_file in html_files:
                    backup_path = backup_dir / html_file.name
                    print(f"  Moving to backup: {html_file.name}")
                    shutil.move(str(html_file), str(backup_path))

if __name__ == '__main__':
    cleanup_duplicates() 