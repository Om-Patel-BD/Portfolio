#!/usr/bin/env python3
"""
Image Conversion Script for SEO Images
Converts SVG files to PNG format for web use.

Requirements:
- cairosvg (install with: pip install cairosvg)
- Or use online SVG to PNG converters

Usage:
1. Install cairosvg: pip install cairosvg
2. Run: python convert_images.py
3. Or manually convert using online tools
"""

import os
import sys

def check_dependencies():
    """Check if required dependencies are installed."""
    try:
        import cairosvg
        return True
    except ImportError:
        return False

def convert_svg_to_png(svg_path, png_path, width=None, height=None):
    """Convert SVG to PNG using cairosvg."""
    try:
        import cairosvg
        
        # Read SVG content
        with open(svg_path, 'r', encoding='utf-8') as f:
            svg_content = f.read()
        
        # Convert to PNG
        if width and height:
            cairosvg.svg2png(bytestring=svg_content, write_to=png_path, 
                           output_width=width, output_height=height)
        else:
            cairosvg.svg2png(bytestring=svg_content, write_to=png_path)
        
        print(f"✅ Converted {svg_path} to {png_path}")
        return True
        
    except Exception as e:
        print(f"❌ Error converting {svg_path}: {e}")
        return False

def main():
    """Main conversion function."""
    print("🖼️  SEO Image Conversion Script")
    print("=" * 40)
    
    # Check if cairosvg is available
    if not check_dependencies():
        print("❌ cairosvg not found!")
        print("\n📋 Manual Conversion Required:")
        print("1. Use online SVG to PNG converters:")
        print("   - https://convertio.co/svg-png/")
        print("   - https://cloudconvert.com/svg-to-png")
        print("   - https://www.aconvert.com/image/svg-to-png/")
        print("\n2. Or install cairosvg: pip install cairosvg")
        return
    
    # Define conversion tasks
    conversions = [
        {
            'svg': 'myapp/static/img/og-image.svg',
            'png': 'myapp/static/img/og-image.jpg',
            'width': 1200,
            'height': 630
        },
        {
            'svg': 'myapp/static/img/favicon-16x16.svg',
            'png': 'myapp/static/img/favicon-16x16.png',
            'width': 16,
            'height': 16
        },
        {
            'svg': 'myapp/static/img/favicon-32x32.svg',
            'png': 'myapp/static/img/favicon-32x32.png',
            'width': 32,
            'height': 32
        },
        {
            'svg': 'myapp/static/img/apple-touch-icon.svg',
            'png': 'myapp/static/img/apple-touch-icon.png',
            'width': 180,
            'height': 180
        },
        {
            'svg': 'myapp/static/img/android-chrome-192x192.svg',
            'png': 'myapp/static/img/android-chrome-192x192.png',
            'width': 192,
            'height': 192
        },
        {
            'svg': 'myapp/static/img/android-chrome-512x512.svg',
            'png': 'myapp/static/img/android-chrome-512x512.png',
            'width': 512,
            'height': 512
        }
    ]
    
    print("🔄 Starting conversions...")
    
    success_count = 0
    total_count = len(conversions)
    
    for conv in conversions:
        svg_path = conv['svg']
        png_path = conv['png']
        
        # Check if SVG exists
        if not os.path.exists(svg_path):
            print(f"⚠️  SVG file not found: {svg_path}")
            continue
        
        # Create output directory if it doesn't exist
        os.makedirs(os.path.dirname(png_path), exist_ok=True)
        
        # Convert SVG to PNG
        if convert_svg_to_png(svg_path, png_path, conv['width'], conv['height']):
            success_count += 1
    
    print("\n" + "=" * 40)
    print(f"🎉 Conversion complete: {success_count}/{total_count} successful")
    
    if success_count == total_count:
        print("✅ All images converted successfully!")
        print("\n📋 Next steps:")
        print("1. Deploy your project to Vercel")
        print("2. Test social media sharing")
        print("3. Verify favicons in different browsers")
        print("4. Submit sitemap to Google Search Console")
    else:
        print("⚠️  Some conversions failed. Check the errors above.")

if __name__ == "__main__":
    main()







