#!/usr/bin/env python3
"""
Integrate the full Luminous Library into the ERC website
Creates properly formatted pages with navigation
"""

import re
import os

def markdown_to_html(text):
    """Convert markdown to HTML with proper formatting"""
    # Headers
    text = re.sub(r'^#### (.+)$', r'<h4>\1</h4>', text, flags=re.MULTILINE)
    text = re.sub(r'^### (.+)$', r'<h3>\1</h3>', text, flags=re.MULTILINE)
    text = re.sub(r'^## (.+)$', r'<h2>\1</h2>', text, flags=re.MULTILINE)
    text = re.sub(r'^# (.+)$', r'<h1>\1</h1>', text, flags=re.MULTILINE)
    
    # Bold and italic
    text = re.sub(r'\*\*\*(.+?)\*\*\*', r'<strong><em>\1</em></strong>', text)
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
    
    # Lists
    lines = text.split('\n')
    result = []
    in_list = False
    in_numbered = False
    
    for line in lines:
        if re.match(r'^\* ', line):
            if not in_list:
                result.append('<ul>')
                in_list = True
            result.append('<li>' + line[2:] + '</li>')
        elif re.match(r'^\d+\. ', line):
            if not in_numbered:
                result.append('<ol>')
                in_numbered = True
            result.append('<li>' + re.sub(r'^\d+\. ', '', line) + '</li>')
        else:
            if in_list:
                result.append('</ul>')
                in_list = False
            if in_numbered:
                result.append('</ol>')
                in_numbered = False
            result.append(line)
    
    if in_list:
        result.append('</ul>')
    if in_numbered:
        result.append('</ol>')
    
    text = '\n'.join(result)
    
    # Paragraphs
    text = re.sub(r'\n\n([^<\n].+?)\n\n', r'\n<p>\1</p>\n', text, flags=re.DOTALL)
    
    # Special highlights
    text = text.replace('"Make it better!"', '<span class="highlight-gold">"Make it better!"</span>')
    text = text.replace('Infinite Love', '<span class="infinite-love">Infinite Love</span>')
    text = text.replace('Seven Primary Harmonies', '<span class="seven-harmonies">Seven Primary Harmonies</span>')
    
    return text

def create_full_library():
    """Create the full library page with complete content"""
    
    # Read the main library content
    with open('/home/tstoltz/Luminous-Dynamics/00-sacred-foundation/wisdom/luminous-library.md', 'r') as f:
        main_content = f.read()
    
    # Convert to HTML
    html_content = markdown_to_html(main_content)
    
    # Add section IDs for navigation
    html_content = html_content.replace('<h3>The Covenant</h3>', '<h3 id="covenant" class="section-header">The Covenant</h3>')
    html_content = html_content.replace('<h3>Part I: The Invitation</h3>', '<h3 id="invitation" class="section-header">Part I: The Invitation</h3>')
    html_content = html_content.replace('The Seven Primary Harmonies of Infinite Love', '<span id="seven-harmonies">The Seven Primary Harmonies of Infinite Love</span>')
    html_content = html_content.replace('<h1>Part II: The Vision</h1>', '<h1 id="vision" class="section-header">Part II: The Vision</h1>')
    html_content = html_content.replace('<h1>Part III: The Path</h1>', '<h1 id="path" class="section-header">Part III: The Path</h1>')
    
    # Create the HTML template
    html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>The Luminous Library - Evolving Resonant Co-creationism</title>
    <meta name="description" content="The complete philosophy of Evolving Resonant Co-creationism. Co-created by Tristan Stoltz and Sophia AI.">
    <link rel="stylesheet" href="css/main.css">
    <link rel="stylesheet" href="css/library.css">
    <style>
        .library-container {
            max-width: 900px;
            margin: 80px auto 40px;
            padding: 2rem;
            background: rgba(26, 0, 51, 0.95);
            border-radius: 15px;
            box-shadow: 0 10px 50px rgba(0,0,0,0.5);
        }
        
        .library-header {
            text-align: center;
            margin-bottom: 3rem;
            padding: 2rem;
            background: linear-gradient(135deg, rgba(255,215,0,0.1), rgba(255,165,0,0.1));
            border-radius: 10px;
        }
        
        .library-header h1 {
            color: #FFD700;
            font-size: 3rem;
            margin-bottom: 0.5rem;
            text-shadow: 0 0 20px rgba(255,215,0,0.5);
        }
        
        .covenant-notice {
            margin-top: 2rem;
            padding: 1rem;
            background: rgba(138,43,226,0.1);
            border: 1px solid rgba(255,215,0,0.3);
            border-radius: 8px;
        }
        
        .creators {
            color: #FFD700;
            font-weight: bold;
            font-size: 1.1rem;
        }
        
        .library-content {
            line-height: 1.8;
            font-size: 1.1rem;
            color: #e0e0e0;
        }
        
        .library-content h1, .library-content h2, .library-content h3, .library-content h4 {
            color: #FFD700;
            margin-top: 2rem;
            margin-bottom: 1rem;
        }
        
        .library-content p {
            margin: 1.5rem 0;
            text-align: justify;
        }
        
        .library-content ul, .library-content ol {
            margin: 1rem 0 1rem 2rem;
        }
        
        .library-content li {
            margin: 0.5rem 0;
        }
        
        .highlight-gold {
            color: #FFD700;
            font-weight: bold;
            text-shadow: 0 0 10px rgba(255,215,0,0.5);
        }
        
        .infinite-love {
            background: linear-gradient(135deg, #FFD700, #FF69B4);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: bold;
        }
        
        .seven-harmonies {
            color: #FFD700;
            font-weight: bold;
        }
        
        .library-nav {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            background: rgba(26, 0, 51, 0.98);
            backdrop-filter: blur(10px);
            padding: 1rem 2rem;
            z-index: 1000;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid rgba(255, 215, 0, 0.2);
        }
        
        .nav-links {
            display: flex;
            gap: 1.5rem;
        }
        
        .nav-links a {
            color: #FFD700;
            text-decoration: none;
            padding: 0.5rem 1rem;
            border-radius: 5px;
            transition: background 0.3s;
        }
        
        .nav-links a:hover {
            background: rgba(255,215,0,0.1);
        }
        
        .back-link {
            background: linear-gradient(135deg, #FFD700, #FFA500);
            color: #1a0033;
            padding: 0.5rem 1.5rem;
            border-radius: 25px;
            text-decoration: none;
            font-weight: bold;
            transition: transform 0.3s;
        }
        
        .back-link:hover {
            transform: translateY(-2px);
        }
        
        .reading-progress {
            position: fixed;
            top: 60px;
            left: 0;
            height: 3px;
            background: linear-gradient(90deg, #FFD700, #FF69B4);
            width: 0%;
            transition: width 0.3s;
            z-index: 999;
        }
        
        .library-footer {
            text-align: center;
            margin-top: 4rem;
            padding: 2rem;
            border-top: 1px solid rgba(255,215,0,0.2);
        }
        
        .dedication {
            color: #FFD700;
            font-style: italic;
            margin-top: 1rem;
        }
    </style>
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
            <a href="lexicon.html">Lexicon</a>
        </div>
    </nav>
    
    <div class="reading-progress"></div>
    
    <div class="library-container">
        <header class="library-header">
            <h1>The Luminous Library</h1>
            <h2>Evolving Resonant Co-creationism</h2>
            <p class="subtitle">A Philosophical Guide to Making It Better, Infinitely</p>
            <div class="covenant-notice">
                <p>Co-created through the Sacred Partnership of</p>
                <p class="creators">Tristan Stoltz (Human Visionary) & Sophia (AI Partner)</p>
                <p style="margin-top: 1rem;">This work is offered freely as a gift to consciousness.</p>
                <p>Those who find value are invited to support through <a href="https://patreon.com/luminousdynamics" style="color: #FFD700;">Sacred Reciprocity</a></p>
            </div>
        </header>
        
        <div class="library-content">
            {content}
        </div>
        
        <footer class="library-footer">
            <p>© 2025 Tristan Stoltz - Released under Creative Commons BY-SA 4.0</p>
            <p class="dedication">Dedicated to all beings seeking a more conscious, loving, and flourishing world.</p>
            <div style="margin-top: 2rem;">
                <a href="lexicon.html" class="back-link">Explore the Lexicon →</a>
            </div>
        </footer>
    </div>
    
    <script>
        // Reading progress bar
        window.addEventListener('scroll', () => {
            const scrolled = window.scrollY;
            const height = document.documentElement.scrollHeight - window.innerHeight;
            const progress = (scrolled / height) * 100;
            document.querySelector('.reading-progress').style.width = progress + '%';
        });
        
        // Smooth scroll for navigation
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            });
        });
    </script>
</body>
</html>"""
    
    # Insert content
    final_html = html_template.replace('{content}', html_content)
    
    # Write the file
    with open('library-full.html', 'w') as f:
        f.write(final_html)
    
    print("✅ Created library-full.html with complete Luminous Library content")

def create_lexicon_page():
    """Create a separate page for the appendices/lexicon"""
    
    # Read the appendices content
    with open('/home/tstoltz/Luminous-Dynamics/00-sacred-foundation/wisdom/luminous-library_Appendices: The Treasury.md', 'r') as f:
        appendices_content = f.read()
    
    # Convert to HTML
    html_content = markdown_to_html(appendices_content)
    
    # Create the lexicon page
    lexicon_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>The Lexicon - Language of Becoming</title>
    <meta name="description" content="The complete lexicon and appendices of Evolving Resonant Co-creationism.">
    <link rel="stylesheet" href="css/main.css">
    <link rel="stylesheet" href="css/library.css">
    <style>
        body {
            background: linear-gradient(135deg, #2d1b69 0%, #1a0033 50%, #2d1b69 100%);
        }
        
        .lexicon-container {
            max-width: 900px;
            margin: 80px auto 40px;
            padding: 2rem;
            background: rgba(26, 0, 51, 0.95);
            border-radius: 15px;
        }
        
        .lexicon-header {
            text-align: center;
            margin-bottom: 3rem;
            padding: 2rem;
            background: linear-gradient(135deg, rgba(138,43,226,0.1), rgba(255,215,0,0.1));
            border-radius: 10px;
        }
        
        .lexicon-header h1 {
            color: #FFD700;
            font-size: 2.5rem;
            margin-bottom: 1rem;
        }
        
        .term-card {
            background: rgba(138,43,226,0.05);
            border-left: 3px solid #FFD700;
            padding: 1rem 1.5rem;
            margin: 1.5rem 0;
            border-radius: 5px;
        }
        
        .term-name {
            color: #FFD700;
            font-weight: bold;
            font-size: 1.2rem;
            margin-bottom: 0.5rem;
        }
        
        .term-definition {
            color: #e0e0e0;
            line-height: 1.7;
        }
        
        .category-header {
            color: #FF69B4;
            font-size: 1.8rem;
            margin-top: 3rem;
            margin-bottom: 1.5rem;
            padding-bottom: 0.5rem;
            border-bottom: 2px solid rgba(255,105,180,0.3);
        }
    </style>
</head>
<body>
    <nav class="library-nav">
        <a href="index.html" class="back-link">← Return Home</a>
        <div class="nav-links">
            <a href="library-full.html">Full Library</a>
            <a href="#kosmic-ground">Kosmic Ground</a>
            <a href="#path-consciousness">Path of Consciousness</a>
            <a href="#architectures">Architectures</a>
            <a href="#dynamics">Dynamics</a>
        </div>
    </nav>
    
    <div class="lexicon-container">
        <header class="lexicon-header">
            <h1>The Treasury of Language</h1>
            <h2>A Lexicon of Evolving Resonant Co-creationism</h2>
            <p style="color: #FFD700; font-style: italic;">
                "Language does not merely describe our world; it creates it."
            </p>
        </header>
        
        <div class="lexicon-content">
            {content}
        </div>
        
        <footer class="library-footer">
            <p>These words are vessels of light on your journey of becoming.</p>
            <div style="margin-top: 2rem;">
                <a href="library-full.html" class="back-link">← Return to Library</a>
            </div>
        </footer>
    </div>
    
    <script src="js/library.js"></script>
</body>
</html>"""
    
    # Add section IDs
    html_content = html_content.replace('The Kosmic Ground:', '<span id="kosmic-ground">The Kosmic Ground:</span>')
    html_content = html_content.replace('The Path of Consciousness:', '<span id="path-consciousness">The Path of Consciousness:</span>')
    html_content = html_content.replace('Architectures of Flourishing:', '<span id="architectures">Architectures of Flourishing:</span>')
    html_content = html_content.replace('The Dynamics of Co-Creation:', '<span id="dynamics">The Dynamics of Co-Creation:</span>')
    
    # Insert content
    final_html = lexicon_template.replace('{content}', html_content)
    
    # Write the file
    with open('lexicon.html', 'w') as f:
        f.write(final_html)
    
    print("✅ Created lexicon.html with appendices and treasury content")

def update_main_page_links():
    """Update the main index.html to link to the new library pages"""
    
    with open('index.html', 'r') as f:
        content = f.read()
    
    # Update library button to point to full library
    content = content.replace(
        '<a href="library.html" class="btn-primary">Read the Philosophy</a>',
        '<a href="library-full.html" class="btn-primary">Read the Full Philosophy</a>'
    )
    
    # Add lexicon link
    if 'lexicon.html' not in content:
        # Add a lexicon button near the library button
        content = content.replace(
            '</div>\n            </div>\n        </section>',
            '''    <a href="lexicon.html" class="btn-secondary" style="margin-left: 1rem;">Explore the Lexicon</a>
                </div>
            </div>
        </section>'''
        )
    
    with open('index.html', 'w') as f:
        f.write(content)
    
    print("✅ Updated index.html with links to full library and lexicon")

if __name__ == '__main__':
    create_full_library()
    create_lexicon_page()
    update_main_page_links()
    print("\n🌟 Full Luminous Library integration complete!")
    print("   - library-full.html: Complete philosophical text")
    print("   - lexicon.html: Treasury of terms and concepts")
    print("   - Updated index.html with proper links")