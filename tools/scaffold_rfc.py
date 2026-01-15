#!/usr/bin/env python3
import os
import datetime
import re
import sys

def slugify(text):
    """Simple slugify function to create safe filenames."""
    text = text.lower()
    text = re.sub(r'[^a-z0-9]+', '-', text)
    return text.strip('-')

def scaffold_rfc():
    print("Welcome to the RFC Scaffolder.")
    print("--------------------------------")
    
    title = input("Enter RFC Title (e.g., 'Adopt Rust for Payment Service'): ").strip()
    if not title:
        print("Error: Title is required.")
        sys.exit(1)
        
    author = input("Enter Author Name: ").strip()
    
    # Generate Metadata
    date_str = datetime.date.today().strftime("%Y-%m-%d")
    slug = slugify(title)
    filename = f"{date_str}-{slug}.md"
    target_path = os.path.join("rfcs", filename)
    template_path = os.path.join("templates", "technology-rfc.md")
    
    # Check if template exists
    if not os.path.exists(template_path):
        print(f"Error: Template not found at {template_path}")
        sys.exit(1)
        
    # Read Template
    with open(template_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Replace Placeholders (Basic substitution)
    # Note: The template currently has placeholders like [Name], [YYYY-MM-DD].
    # We will do a robust replacement suitable for the 'Standard' template we created.
    
    content = content.replace("[Name]", author)
    content = content.replace("[YYYY-MM-DD]", date_str)
    content = content.replace("Status: [Draft | Under Review | Approved | Rejected]", "Status: Draft")
    
    # Write to new file
    with open(target_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"\nSuccess! New RFC created at:")
    print(f"  -> {target_path}")
    print("\nYou can now open this file and begin drafting.")

if __name__ == "__main__":
    scaffold_rfc()
