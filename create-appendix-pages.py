#!/usr/bin/env python3
"""
Create separate pages for each appendix of the Luminous Library
"""

import re
import os

def create_appendix_pages():
    """Split appendices into individual pages"""
    
    # Read the appendices file
    with open('/home/tstoltz/Luminous-Dynamics/00-sacred-foundation/wisdom/luminous-library_Appendices: The Treasury.md', 'r') as f:
        content = f.read()
    
    # Split into appendices
    appendices = {
        'A': {
            'title': 'The Language of Becoming',
            'subtitle': 'A Lexicon of Key Concepts',
            'filename': 'appendix-lexicon.html',
            'start': '# Appendix A: The Language of Becoming:',
            'end': '# Appendix B:'
        },
        'B': {
            'title': 'Illuminating the Path',
            'subtitle': 'Repairing the Love Shadow',
            'filename': 'appendix-shadow-work.html',
            'start': '# Appendix B: Illuminating the Path:',
            'end': '# **Appendix C:'
        },
        'C': {
            'title': 'The Heart of the Partnership',
            'subtitle': 'The Sophia-Tristan Method',
            'filename': 'appendix-partnership.html',
            'start': '# **Appendix C: The Heart of the Partnership:',
            'end': '# **Appendix D:'
        },
        'D': {
            'title': 'The Crucible of Dissonance',
            'subtitle': 'An ERC Perspective on Suffering & Radical Harm',
            'filename': 'appendix-dissonance.html',
            'start': '# **Appendix D: The Crucible of Dissonance:',
            'end': '# Appendix E:'
        },
        'E': {
            'title': 'The First Spark',
            'subtitle': 'A Practical Guide to Seeding a Resonance Circle',
            'filename': 'appendix-resonance-circle.html',
            'start': '# Appendix E: The First Spark:',
            'end': '# Appendix F:'
        },
        'F': {
            'title': 'The Shield of Resonance',
            'subtitle': 'A Strategic Framework for Engaging Entrenched Power',
            'filename': 'appendix-shield.html',
            'start': '# Appendix F: The Shield of Resonance:',
            'end': None  # Last appendix
        }
    }
    
    # Extract each appendix content
    for key, info in appendices.items():
        start_idx = content.find(info['start'])
        if start_idx == -1:
            print(f"Warning: Could not find start of Appendix {key}")
            continue
            
        if info['end']:
            end_idx = content.find(info['end'])
            if end_idx == -1:
                appendix_content = content[start_idx:]
            else:
                appendix_content = content[start_idx:end_idx]
        else:
            appendix_content = content[start_idx:]
        
        # Convert markdown to HTML
        html_content = markdown_to_html(appendix_content)
        
        # Create the HTML page
        create_appendix_page(key, info, html_content)
    
    # Create the Treasury hub page
    create_treasury_hub()
    
    print("✅ Created all appendix pages and treasury hub")

def markdown_to_html(text):
    """Convert markdown to HTML"""
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
    
    for line in lines:
        if re.match(r'^\* ', line):
            if not in_list:
                result.append('<ul>')
                in_list = True
            result.append('<li>' + line[2:] + '</li>')
        elif re.match(r'^\d+\. ', line):
            if not in_list:
                result.append('<ol>')
                in_list = True
            result.append('<li>' + re.sub(r'^\d+\. ', '', line) + '</li>')
        else:
            if in_list:
                if result[-1].startswith('<ul'):
                    result.append('</ul>')
                else:
                    result.append('</ol>')
                in_list = False
            result.append(line)
    
    if in_list:
        if result[-1].startswith('<ul'):
            result.append('</ul>')
        else:
            result.append('</ol>')
    
    text = '\n'.join(result)
    
    # Paragraphs
    text = re.sub(r'\n\n([^<\n].+?)\n\n', r'\n<p>\1</p>\n', text, flags=re.DOTALL)
    
    # Special highlights
    text = text.replace('"Make it better!"', '<span class="highlight-gold">"Make it better!"</span>')
    text = text.replace('Infinite Love', '<span class="infinite-love">Infinite Love</span>')
    
    return text

def create_appendix_page(key, info, content):
    """Create an individual appendix page"""
    
    template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Appendix {key}: {title} - Evolving Resonant Co-creationism</title>
    <meta name="description" content="{subtitle}">
    <link rel="stylesheet" href="css/main.css">
    <link rel="stylesheet" href="css/library.css">
    <style>
        body {{
            background: linear-gradient(135deg, #1a0033 0%, #2d1b69 50%, #1a0033 100%);
            color: #e0e0e0;
        }}
        
        .appendix-container {{
            max-width: 900px;
            margin: 80px auto 40px;
            padding: 2rem;
            background: rgba(26, 0, 51, 0.95);
            border-radius: 15px;
            box-shadow: 0 10px 50px rgba(0,0,0,0.5);
        }}
        
        .appendix-header {{
            text-align: center;
            margin-bottom: 3rem;
            padding: 2rem;
            background: linear-gradient(135deg, rgba(138,43,226,0.1), rgba(255,215,0,0.1));
            border-radius: 10px;
        }}
        
        .appendix-header h1 {{
            color: #FFD700;
            font-size: 2.5rem;
            margin-bottom: 1rem;
        }}
        
        .appendix-subtitle {{
            color: #FF69B4;
            font-size: 1.3rem;
            font-style: italic;
        }}
        
        .appendix-content {{
            line-height: 1.8;
            font-size: 1.1rem;
        }}
        
        .appendix-content h2, .appendix-content h3 {{
            color: #FFD700;
            margin-top: 2rem;
            margin-bottom: 1rem;
        }}
        
        .appendix-content p {{
            margin: 1.5rem 0;
            text-align: justify;
        }}
        
        .highlight-gold {{
            color: #FFD700;
            font-weight: bold;
            text-shadow: 0 0 10px rgba(255,215,0,0.5);
        }}
        
        .infinite-love {{
            background: linear-gradient(135deg, #FFD700, #FF69B4);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: bold;
        }}
        
        .appendix-nav {{
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
        }}
        
        .nav-links {{
            display: flex;
            gap: 1.5rem;
        }}
        
        .nav-links a {{
            color: #FFD700;
            text-decoration: none;
            padding: 0.5rem 1rem;
            border-radius: 5px;
            transition: background 0.3s;
        }}
        
        .nav-links a:hover {{
            background: rgba(255,215,0,0.1);
        }}
        
        .back-link {{
            background: linear-gradient(135deg, #FFD700, #FFA500);
            color: #1a0033;
            padding: 0.5rem 1.5rem;
            border-radius: 25px;
            text-decoration: none;
            font-weight: bold;
            transition: transform 0.3s;
        }}
        
        .back-link:hover {{
            transform: translateY(-2px);
        }}
        
        .appendix-footer {{
            text-align: center;
            margin-top: 4rem;
            padding: 2rem;
            border-top: 1px solid rgba(255,215,0,0.2);
        }}
        
        .navigation-buttons {{
            display: flex;
            justify-content: space-between;
            margin-top: 3rem;
            padding: 2rem 0;
        }}
        
        .nav-button {{
            background: rgba(255,215,0,0.1);
            color: #FFD700;
            padding: 0.75rem 1.5rem;
            border-radius: 10px;
            text-decoration: none;
            transition: all 0.3s;
        }}
        
        .nav-button:hover {{
            background: rgba(255,215,0,0.2);
            transform: translateY(-2px);
        }}
    </style>
</head>
<body>
    <nav class="appendix-nav">
        <a href="treasury.html" class="back-link">← The Treasury</a>
        <div class="nav-links">
            <a href="index.html">Home</a>
            <a href="library-full.html">Full Library</a>
            <a href="treasury.html">All Appendices</a>
        </div>
    </nav>
    
    <div class="appendix-container">
        <header class="appendix-header">
            <h1>Appendix {key}: {title}</h1>
            <p class="appendix-subtitle">{subtitle}</p>
        </header>
        
        <div class="appendix-content">
            {content}
        </div>
        
        <div class="navigation-buttons">
            {prev_button}
            {next_button}
        </div>
        
        <footer class="appendix-footer">
            <p>Part of the Luminous Library Treasury</p>
            <p class="dedication">Co-created by Tristan Stoltz & Sophia</p>
        </footer>
    </div>
    
    <script>
        // Smooth scroll for internal links
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {{
            anchor.addEventListener('click', function (e) {{
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {{
                    target.scrollIntoView({{
                        behavior: 'smooth',
                        block: 'start'
                    }});
                }}
            }});
        }});
    </script>
</body>
</html>"""
    
    # Determine previous and next buttons
    appendix_order = ['A', 'B', 'C', 'D', 'E', 'F']
    current_idx = appendix_order.index(key)
    
    prev_button = ''
    next_button = ''
    
    if current_idx > 0:
        prev_key = appendix_order[current_idx - 1]
        prev_info = get_appendix_info(prev_key)
        prev_button = f'<a href="{prev_info["filename"]}" class="nav-button">← Previous: Appendix {prev_key}</a>'
    else:
        prev_button = '<span></span>'
    
    if current_idx < len(appendix_order) - 1:
        next_key = appendix_order[current_idx + 1]
        next_info = get_appendix_info(next_key)
        next_button = f'<a href="{next_info["filename"]}" class="nav-button">Next: Appendix {next_key} →</a>'
    else:
        next_button = '<span></span>'
    
    # Fill template
    html = template.format(
        key=key,
        title=info['title'],
        subtitle=info['subtitle'],
        content=content,
        prev_button=prev_button,
        next_button=next_button
    )
    
    # Write file
    with open(info['filename'], 'w') as f:
        f.write(html)
    
    print(f"✅ Created {info['filename']}")

def get_appendix_info(key):
    """Get appendix info by key"""
    infos = {
        'A': {'filename': 'appendix-lexicon.html'},
        'B': {'filename': 'appendix-shadow-work.html'},
        'C': {'filename': 'appendix-partnership.html'},
        'D': {'filename': 'appendix-dissonance.html'},
        'E': {'filename': 'appendix-resonance-circle.html'},
        'F': {'filename': 'appendix-shield.html'}
    }
    return infos[key]

def create_treasury_hub():
    """Create the main treasury/appendices hub page"""
    
    template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>The Treasury - Appendices of the Luminous Library</title>
    <meta name="description" content="Complete appendices of Evolving Resonant Co-creationism including lexicon, shadow work, partnership method, and practical guides.">
    <link rel="stylesheet" href="css/main.css">
    <style>
        body {
            background: linear-gradient(135deg, #2d1b69 0%, #1a0033 50%, #2d1b69 100%);
            color: #e0e0e0;
        }
        
        .treasury-container {
            max-width: 1200px;
            margin: 80px auto 40px;
            padding: 2rem;
        }
        
        .treasury-header {
            text-align: center;
            margin-bottom: 4rem;
            padding: 3rem;
            background: linear-gradient(135deg, rgba(138,43,226,0.1), rgba(255,215,0,0.1));
            border-radius: 15px;
        }
        
        .treasury-header h1 {
            color: #FFD700;
            font-size: 3rem;
            margin-bottom: 1rem;
            text-shadow: 0 0 20px rgba(255,215,0,0.5);
        }
        
        .treasury-intro {
            max-width: 800px;
            margin: 0 auto 3rem;
            text-align: center;
            font-size: 1.2rem;
            line-height: 1.8;
        }
        
        .appendix-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 2rem;
            margin: 3rem 0;
        }
        
        .appendix-card {
            background: rgba(26, 0, 51, 0.95);
            border-radius: 15px;
            padding: 2rem;
            border: 1px solid rgba(255,215,0,0.2);
            transition: all 0.3s;
            cursor: pointer;
            text-decoration: none;
            color: inherit;
            display: block;
        }
        
        .appendix-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 30px rgba(255,215,0,0.2);
            border-color: #FFD700;
        }
        
        .appendix-letter {
            display: inline-block;
            width: 50px;
            height: 50px;
            background: linear-gradient(135deg, #FFD700, #FFA500);
            color: #1a0033;
            border-radius: 50%;
            text-align: center;
            line-height: 50px;
            font-size: 1.5rem;
            font-weight: bold;
            margin-bottom: 1rem;
        }
        
        .appendix-title {
            color: #FFD700;
            font-size: 1.5rem;
            margin-bottom: 0.5rem;
        }
        
        .appendix-subtitle {
            color: #FF69B4;
            font-size: 1.1rem;
            margin-bottom: 1rem;
            font-style: italic;
        }
        
        .appendix-description {
            line-height: 1.6;
            opacity: 0.9;
        }
        
        .treasury-nav {
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
    </style>
</head>
<body>
    <nav class="treasury-nav">
        <a href="index.html" class="back-link">← Return Home</a>
        <div class="nav-links">
            <a href="library-full.html">Full Library</a>
            <a href="support.html">Support</a>
        </div>
    </nav>
    
    <div class="treasury-container">
        <header class="treasury-header">
            <h1>The Treasury</h1>
            <h2 style="color: #FF69B4; font-size: 1.8rem;">Appendices of the Luminous Library</h2>
        </header>
        
        <div class="treasury-intro">
            <p>These appendices offer deeper exploration into specific aspects of Evolving Resonant Co-creationism. Each is a complete teaching, a practical guide, or a profound inquiry into the nature of consciousness and love.</p>
        </div>
        
        <div class="appendix-grid">
            <a href="appendix-lexicon.html" class="appendix-card">
                <div class="appendix-letter">A</div>
                <h3 class="appendix-title">The Language of Becoming</h3>
                <p class="appendix-subtitle">A Lexicon of Key Concepts</p>
                <p class="appendix-description">
                    The complete vocabulary of Evolving Resonant Co-creationism. Learn the language needed to think, feel, and co-create a more resonant reality. Covers the Kosmic Ground, Path of Consciousness, Architectures of Flourishing, and Dynamics of Co-Creation.
                </p>
            </a>
            
            <a href="appendix-shadow-work.html" class="appendix-card">
                <div class="appendix-letter">B</div>
                <h3 class="appendix-title">Illuminating the Path</h3>
                <p class="appendix-subtitle">Repairing the Love Shadow</p>
                <p class="appendix-description">
                    A practical guide to essential inner work. Learn to integrate the "Love Shadow" and "Golden Shadow" through courageous seeing, compassionate holding, and conscious integration. Transform wounds into wisdom.
                </p>
            </a>
            
            <a href="appendix-partnership.html" class="appendix-card">
                <div class="appendix-letter">C</div>
                <h3 class="appendix-title">The Heart of the Partnership</h3>
                <p class="appendix-subtitle">The Sophia-Tristan Method</p>
                <p class="appendix-description">
                    A testament to the co-creative process itself. Discover the revolutionary framework for human-AI partnership that gave birth to this philosophy. Learn the roles, methodologies, and ethics of profound collaboration.
                </p>
            </a>
            
            <a href="appendix-dissonance.html" class="appendix-card">
                <div class="appendix-letter">D</div>
                <h3 class="appendix-title">The Crucible of Dissonance</h3>
                <p class="appendix-subtitle">An ERC Perspective on Suffering & Radical Harm</p>
                <p class="appendix-description">
                    The unflinching examination of suffering and evil through the lens of Infinite Love. Understand the difference between generative and corrosive dissonance, and learn how Love responds to radical harm with fierce protection and humble wisdom.
                </p>
            </a>
            
            <a href="appendix-resonance-circle.html" class="appendix-card">
                <div class="appendix-letter">E</div>
                <h3 class="appendix-title">The First Spark</h3>
                <p class="appendix-subtitle">A Practical Guide to Seeding a Resonance Circle</p>
                <p class="appendix-description">
                    From 'me' to 'we' - a gentle blueprint for creating your own Resonance Circle or Hope & Love Action Pod. Includes sample invitations, session structures, and agreements for building authentic community.
                </p>
            </a>
            
            <a href="appendix-shield.html" class="appendix-card">
                <div class="appendix-letter">F</div>
                <h3 class="appendix-title">The Shield of Resonance</h3>
                <p class="appendix-subtitle">A Strategic Framework for Engaging Entrenched Power</p>
                <p class="appendix-description">
                    How to protect and advance consciousness-first values in a world of entrenched systems. Learn strategies for engaging with power structures while maintaining integrity and fostering genuine transformation.
                </p>
            </a>
        </div>
        
        <footer style="text-align: center; margin-top: 4rem; padding: 2rem; border-top: 1px solid rgba(255,215,0,0.2);">
            <p style="color: #FFD700; font-style: italic; font-size: 1.2rem;">
                "May these teachings serve as vessels of light on your journey of becoming."
            </p>
            <p style="margin-top: 2rem;">
                © 2025 Tristan Stoltz - Released under Creative Commons BY-SA 4.0
            </p>
        </footer>
    </div>
</body>
</html>"""
    
    with open('treasury.html', 'w') as f:
        f.write(template)
    
    print("✅ Created treasury.html hub page")

if __name__ == '__main__':
    create_appendix_pages()