#!/usr/bin/env python3
"""
SEO Image Creation Script for Windows
Creates missing SEO images from existing SVG files using online conversion.

Requirements:
- requests (install with: pip install requests)
- Pillow (install with: pip install Pillow)

Usage:
1. Install dependencies: pip install requests Pillow
2. Run: python create_seo_images.py
3. Or manually convert using online tools
"""

import os
import requests
from PIL import Image, ImageDraw, ImageFont
import io

def create_simple_favicon(size, filename, text="OP", bg_color="#000000", text_color="#00ff88"):
    """Create a simple favicon with initials."""
    try:
        # Create image with black background
        img = Image.new('RGB', (size, size), bg_color)
        draw = ImageDraw.Draw(img)
        
        # Try to use a default font, fallback to basic if not available
        try:
            # Try to use a system font
            font_size = size // 2
            font = ImageFont.truetype("arial.ttf", font_size)
        except:
            # Fallback to default font
            font = ImageFont.load_default()
        
        # Calculate text position to center it
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        
        x = (size - text_width) // 2
        y = (size - text_height) // 2
        
        # Draw text
        draw.text((x, y), text, fill=text_color, font=font)
        
        # Save image
        img.save(filename, 'PNG')
        print(f"✅ Created {filename} ({size}x{size})")
        return True
        
    except Exception as e:
        print(f"❌ Error creating {filename}: {e}")
        return False

def create_og_image(filename, title="Om Patel", subtitle="Backend Developer", bg_color="#000000", text_color="#ffffff", accent_color="#00ff88"):
    """Create a simple Open Graph image."""
    try:
        # Create 1200x630 image (Facebook/LinkedIn recommended size)
        width, height = 1200, 630
        img = Image.new('RGB', (width, height), bg_color)
        draw = ImageDraw.Draw(img)
        
        # Try to use a system font
        try:
            title_font = ImageFont.truetype("arial.ttf", 72)
            subtitle_font = ImageFont.truetype("arial.ttf", 48)
        except:
            # Fallback to default font
            title_font = ImageFont.load_default()
            subtitle_font = ImageFont.load_default()
        
        # Draw title
        bbox = draw.textbbox((0, 0), title, font=title_font)
        title_width = bbox[2] - bbox[0]
        title_height = bbox[3] - bbox[1]
        
        title_x = (width - title_width) // 2
        title_y = height // 3
        
        draw.text((title_x, title_y), title, fill=text_color, font=title_font)
        
        # Draw subtitle
        bbox = draw.textbbox((0, 0), subtitle, font=subtitle_font)
        subtitle_width = bbox[2] - bbox[0]
        subtitle_height = bbox[3] - bbox[1]
        
        subtitle_x = (width - subtitle_width) // 2
        subtitle_y = title_y + title_height + 30
        
        draw.text((subtitle_x, subtitle_y), subtitle, fill=accent_color, font=subtitle_font)
        
        # Add a simple accent line
        line_y = subtitle_y + subtitle_height + 40
        draw.line([(width//4, line_y), (3*width//4, line_y)], fill=accent_color, width=4)
        
        # Save image
        img.save(filename, 'JPEG', quality=95)
        print(f"✅ Created {filename} (1200x630)")
        return True
        
    except Exception as e:
        print(f"❌ Error creating {filename}: {e}")
        return False

def main():
    """Main function to create all missing SEO images."""
    print("🖼️  SEO Image Creation Script for Windows")
    print("=" * 50)
    
    # Check if Pillow is available
    try:
        from PIL import Image, ImageDraw, ImageFont
        print("✅ Pillow (PIL) is available")
    except ImportError:
        print("❌ Pillow not found! Install with: pip install Pillow")
        return
    
    # Create output directory if it doesn't exist
    img_dir = "myapp/static/img"
    os.makedirs(img_dir, exist_ok=True)
    
    print("\n🔄 Creating missing SEO images...")
    
    success_count = 0
    total_count = 0
    
    # List of images to create
    images_to_create = [
        {
            'type': 'favicon',
            'filename': f'{img_dir}/favicon-16x16.png',
            'size': 16,
            'description': 'Small favicon'
        },
        {
            'type': 'favicon', 
            'filename': f'{img_dir}/favicon-32x32.png',
            'size': 32,
            'description': 'Standard favicon'
        },
        {
            'type': 'apple',
            'filename': f'{img_dir}/apple-touch-icon.png',
            'size': 180,
            'description': 'iOS app icon'
        },
        {
            'type': 'android',
            'filename': f'{img_dir}/android-chrome-192x192.png',
            'size': 192,
            'description': 'Android icon (medium)'
        },
        {
            'type': 'android',
            'filename': f'{img_dir}/android-chrome-512x512.png',
            'size': 512,
            'description': 'Android icon (large)'
        },
        {
            'type': 'og',
            'filename': f'{img_dir}/og-image.jpg',
            'size': None,
            'description': 'Social media sharing image'
        }
    ]
    
    for img_info in images_to_create:
        total_count += 1
        filename = img_info['filename']
        size = img_info['size']
        description = img_info['description']
        
        # Check if file already exists
        if os.path.exists(filename):
            print(f"⚠️  {filename} already exists, skipping...")
            continue
        
        print(f"\n📝 Creating {description}...")
        
        success = False
        if img_info['type'] == 'favicon':
            success = create_simple_favicon(size, filename)
        elif img_info['type'] == 'apple':
            success = create_simple_favicon(size, filename, text="OP", bg_color="#000000", text_color="#00ff88")
        elif img_info['type'] == 'android':
            success = create_simple_favicon(size, filename, text="OP", bg_color="#000000", text_color="#00ff88")
        elif img_info['type'] == 'og':
            success = create_og_image(filename)
        
        if success:
            success_count += 1
    
    print("\n" + "=" * 50)
    print(f"🎉 Image creation complete: {success_count}/{total_count} successful")
    
    if success_count > 0:
        print("\n✅ Next steps:")
        print("1. Rebuild your static site: python manage.py distill-local")
        print("2. Deploy to Vercel: vercel --prod")
        print("3. Test social media sharing")
        print("4. Submit to Google Search Console")
    else:
        print("\n⚠️  No images were created. Check the errors above.")
        print("\n💡 Alternative: Use online SVG to PNG converters:")
        print("   - https://convertio.co/svg-png/")
        print("   - https://cloudconvert.com/svg-to-png")

if __name__ == "__main__":
    main()

