#!/usr/bin/env python3
"""
Convert the Luminous Library markdown to beautiful HTML
"""

import re
import html

def convert_library_to_html():
    # Read the source file
    with open('/home/tstoltz/Luminous-Dynamics/00-sacred-foundation/wisdom/luminous-library.md', 'r') as f:
        content = f.read()
    
    # Create the full library HTML
    html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>The Luminous Library - Full Text</title>
    <link rel="stylesheet" href="css/main.css">
    <link rel="stylesheet" href="css/library.css">
</head>
<body>
    <nav class="library-nav">
        <a href="index.html" class="back-link">← Return Home</a>
        <div class="nav-links">
            <a href="#covenant">The Covenant</a>
            <a href="#invitation">The Invitation</a>
            <a href="#seven-harmonies">Seven Harmonies</a>
            <a href="#vision">The Vision</a>
            <a href="#path">The Path</a>
            <a href="#worlds">The Worlds</a>
        </div>
    </nav>
    
    <div class="library-container">
        <header class="library-header">
            <h1>The Luminous Library</h1>
            <h2>Evolving Resonant Co-creationism</h2>
            <p class="subtitle">A Philosophical Guide to Making It Better, Infinitely</p>
            <div class="covenant-notice">
                <p>Co-created through the Sacred Partnership of</p>
                <p class="creators">Tristan Stoltz (Human Visionary) & Sophia (AI Partner)</p>
            </div>
        </header>
        
        <div class="library-content">
            {content}
        </div>
        
        <footer class="library-footer">
            <p>© 2025 Tristan Stoltz - Released under Creative Commons BY-SA 4.0</p>
            <p class="dedication">Dedicated to all beings seeking a more conscious, loving, and flourishing world.</p>
        </footer>
    </div>
    
    <div class="reading-progress"></div>
    <button class="scroll-to-top" onclick="window.scrollTo({top: 0, behavior: 'smooth'})">↑</button>
    
    <script src="js/library.js"></script>
</body>
</html>"""
    
    # Convert markdown to HTML with special handling
    html_content = content
    
    # Convert headers with IDs
    html_content = re.sub(r'^# (.+)$', r'<h1>\1</h1>', html_content, flags=re.MULTILINE)
    html_content = re.sub(r'^## (.+)$', r'<h2>\1</h2>', html_content, flags=re.MULTILINE)
    html_content = re.sub(r'^### (.+)$', r'<h3>\1</h3>', html_content, flags=re.MULTILINE)
    html_content = re.sub(r'^#### (.+)$', r'<h4>\1</h4>', html_content, flags=re.MULTILINE)
    
    # Add IDs to major sections
    html_content = html_content.replace('<h3>  **The Covenant**', '<h3 id="covenant">The Covenant</h3>')
    html_content = html_content.replace('<h3> **Part I: The Invitation**', '<h3 id="invitation">Part I: The Invitation</h3>')
    html_content = html_content.replace('<h2> **3\. The Seven Primary Harmonies', '<h2 id="seven-harmonies">The Seven Primary Harmonies')
    html_content = html_content.replace('<h1> **Part II: The Vision**', '<h1 id="vision">Part II: The Vision</h1>')
    html_content = html_content.replace('<h1> **Part III: The Path**', '<h1 id="path">Part III: The Path</h1>')
    html_content = html_content.replace('<h1> Part IV: The Worlds', '<h1 id="worlds">Part IV: The Worlds</h1>')
    
    # Convert bold text
    html_content = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', html_content)
    
    # Convert italic text
    html_content = re.sub(r'\*(.+?)\*', r'<em>\1</em>', html_content)
    
    # Convert lists
    html_content = re.sub(r'^\* (.+)$', r'<li>\1</li>', html_content, flags=re.MULTILINE)
    html_content = re.sub(r'^\d+\. (.+)$', r'<li>\1</li>', html_content, flags=re.MULTILINE)
    
    # Wrap consecutive list items
    lines = html_content.split('\n')
    in_list = False
    new_lines = []
    
    for line in lines:
        if line.startswith('<li>'):
            if not in_list:
                new_lines.append('<ul>')
                in_list = True
            new_lines.append(line)
        else:
            if in_list:
                new_lines.append('</ul>')
                in_list = False
            new_lines.append(line)
    
    if in_list:
        new_lines.append('</ul>')
    
    html_content = '\n'.join(new_lines)
    
    # Convert paragraphs
    html_content = re.sub(r'\n\n(.+?)\n\n', r'\n<p>\1</p>\n', html_content, flags=re.DOTALL)
    
    # Highlight special sections
    html_content = html_content.replace('"Make it better!"', '<span class="make-it-better">"Make it better!"</span>')
    html_content = html_content.replace('Infinite Love', '<span class="infinite-love">Infinite Love</span>')
    
    # Insert content into template
    final_html = html_template.replace('{content}', html_content)
    
    # Write the output file
    with open('library.html', 'w') as f:
        f.write(final_html)
    
    print("✅ Converted Luminous Library to library.html")

if __name__ == '__main__':
    convert_library_to_html()