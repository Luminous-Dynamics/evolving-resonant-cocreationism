#!/usr/bin/env python3
"""
Fix color contrast issues on dark purple backgrounds for ERC website.
Addresses readability problems with dark text on dark backgrounds.
"""

import os
import re

def fix_color_in_file(filepath):
    """Fix problematic colors in a single file."""
    with open(filepath, 'r') as f:
        content = f.read()
    
    original_content = content
    
    # Fix light blue (#87CEEB) - change to bright gold for better contrast
    content = content.replace('#87CEEB', '#FFD700')
    content = content.replace('color: #87CEEB', 'color: #FFD700')
    
    # Fix grey (#666) - change to light grey for dark backgrounds
    # Only in files with dark backgrounds
    if 'background: linear-gradient(135deg, #1a0033' in content or 'background: linear-gradient(135deg, #2d1b69' in content:
        content = content.replace('color: #666', 'color: #d0d0d0')
    
    # Fix cosmic blue (#1A237E) on dark backgrounds - change to bright cyan
    if 'background: linear-gradient(135deg, #1a0033' in content or 'background: linear-gradient(135deg, #2d1b69' in content:
        content = content.replace('color: var(--cosmic-blue)', 'color: #00FFFF')
        content = content.replace('color: #1A237E', 'color: #00FFFF')
    
    # Fix deep purple text (#4A148C) on dark backgrounds - change to light purple
    if 'background: linear-gradient(135deg, #1a0033' in content or 'background: linear-gradient(135deg, #2d1b69' in content:
        content = content.replace('color: var(--deep-purple)', 'color: #DDA0DD')
        content = content.replace('color: #4A148C', 'color: #DDA0DD')
    
    # Fix dark purple text (#8B4789) - change to lighter shade
    content = content.replace('color: #8B4789', 'color: #FF69B4')
    
    # Add specific fixes for library.html's unique CSS
    if 'library.html' in filepath:
        # Fix the harmonies list item colors
        content = re.sub(
            r'\.harmony-(\d+) \{\s*color: #87CEEB;',
            r'.harmony-\1 { color: #FFD700;',
            content
        )
        # Fix border colors to match
        content = content.replace('border-left: 3px solid #87CEEB', 'border-left: 3px solid #FFD700')
    
    # Write back only if changes were made
    if content != original_content:
        with open(filepath, 'w') as f:
            f.write(content)
        return True
    return False

def main():
    """Fix color contrast issues across all HTML and CSS files."""
    
    # List of files with dark purple backgrounds that need fixing
    dark_bg_files = [
        'appendix-dissonance.html',
        'appendix-lexicon.html', 
        'appendix-partnership.html',
        'appendix-resonance-circle.html',
        'appendix-shadow-work.html',
        'appendix-shield.html',
        'lexicon.html',
        'library-full.html',
        'library.html',
        'treasury.html'
    ]
    
    fixed_count = 0
    
    # Fix HTML files
    for filename in dark_bg_files:
        filepath = f'/srv/luminous-dynamics/evolving-resonant-cocreationism/{filename}'
        if os.path.exists(filepath):
            if fix_color_in_file(filepath):
                print(f"✅ Fixed colors in {filename}")
                fixed_count += 1
    
    # Also check and fix CSS files
    css_files = [
        '/srv/luminous-dynamics/evolving-resonant-cocreationism/css/main.css',
        '/srv/luminous-dynamics/evolving-resonant-cocreationism/css/library.css',
        '/srv/luminous-dynamics/evolving-resonant-cocreationism/css/harmonies.css'
    ]
    
    for filepath in css_files:
        if os.path.exists(filepath):
            # For CSS files, we need to be more careful
            with open(filepath, 'r') as f:
                content = f.read()
            
            original_content = content
            
            # Don't change the color definitions in :root, but add comments
            if ':root' in content:
                # Add a comment about contrast considerations
                if '/* Contrast note:' not in content:
                    content = content.replace(
                        '--cosmic-blue: #1A237E;',
                        '--cosmic-blue: #1A237E; /* Note: Use carefully on dark backgrounds */'
                    )
            
            if content != original_content:
                with open(filepath, 'w') as f:
                    f.write(content)
                print(f"✅ Updated {os.path.basename(filepath)}")
                fixed_count += 1
    
    print(f"\n🎨 Color contrast fixes complete! Modified {fixed_count} files.")
    print("\nChanges made:")
    print("- Light blue (#87CEEB) → Gold (#FFD700) for better visibility")
    print("- Grey (#666) → Light grey (#d0d0d0) on dark backgrounds")
    print("- Cosmic blue (#1A237E) → Bright cyan (#00FFFF) on dark backgrounds")
    print("- Deep purple (#4A148C) → Light purple (#DDA0DD) on dark backgrounds")

if __name__ == "__main__":
    main()