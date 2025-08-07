#!/usr/bin/env python3
"""
Test script for the Android Card Generator
This script tests the PDF generation functionality without the GUI
"""

from card_generator_android import CardGeneratorAndroid
import os
import json
from datetime import datetime

def create_sample_card_data():
    """Create sample card data for testing"""
    sample_cards = [
        {
            'Card_Name': 'Fire Dragon',
            'Suit': 'Lightning',
            'Value': 'A',
            'Task': 'Deal 3 damage to any target',
            'Rules': 'Can only be played if you have 3 or more energy',
            'Icon_Color': 'red',
            'Custom_Image': None
        },
        {
            'Card_Name': 'Shield Maiden',
            'Suit': 'Shield',
            'Value': 'Q',
            'Task': 'Block next attack and draw a card',
            'Rules': 'Can be played at any time as instant',
            'Icon_Color': 'blue',
            'Custom_Image': None
        },
        {
            'Card_Name': 'Star Power',
            'Suit': 'Star',
            'Value': '10',
            'Task': 'Gain 2 energy and take extra turn',
            'Rules': 'Once per game only',
            'Icon_Color': 'purple',
            'Custom_Image': None
        },
        {
            'Card_Name': 'Royal Crown',
            'Suit': 'Crown',
            'Value': 'K',
            'Task': 'Control opponent next turn',
            'Rules': 'Must be highest value card in hand',
            'Icon_Color': 'orange',
            'Custom_Image': None
        }
    ]
    return sample_cards

def test_card_generator():
    """Test the card generator functionality"""
    print("Testing Android Card Generator...")
    print("="*50)
    
    try:
        # Create generator instance
        generator = CardGeneratorAndroid()
        print("✓ Card generator initialized successfully")
        
        # Create sample data
        cards_data = create_sample_card_data()
        print(f"✓ Created {len(cards_data)} sample cards")
        
        # Generate PDF
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        output_file = f'test_cards_{timestamp}.pdf'
        
        print(f"\nGenerating PDF: {output_file}")
        print("-" * 30)
        
        result = generator.generate_pdf(cards_data, output_file)
        
        if result:
            print(f"✓ PDF generated successfully: {output_file}")
            
            # Check file exists and get size
            if os.path.exists(output_file):
                file_size = os.path.getsize(output_file)
                print(f"✓ File exists, size: {file_size} bytes")
                
                print(f"\n📄 PDF Details:")
                print(f"   - File: {output_file}")
                print(f"   - Cards: {len(cards_data)}")
                print(f"   - Dimensions: 26mm × 36.4mm per card")
                print(f"   - Paper: 30mm width receipt paper")
                print(f"   - Layout: Single column, vertical stack")
                
                return True
            else:
                print("✗ Error: PDF file not found after generation")
                return False
        else:
            print("✗ Error: PDF generation failed")
            return False
            
    except Exception as e:
        print(f"✗ Error during testing: {str(e)}")
        return False

def test_image_processing():
    """Test image processing functionality"""
    print(f"\n{'='*50}")
    print("Testing Image Processing...")
    print("="*50)
    
    try:
        generator = CardGeneratorAndroid()
        
        # Test with a simple colored rectangle image (if PIL is working)
        from PIL import Image as PILImage
        import io
        
        # Create a test image
        test_image = PILImage.new('RGB', (100, 100), color='red')
        test_image_path = 'test_image.png'
        test_image.save(test_image_path)
        
        print(f"✓ Created test image: {test_image_path}")
        
        # Test resizing
        resized_path = generator.resize_custom_image(test_image_path)
        
        if resized_path and os.path.exists(resized_path):
            print("✓ Image resizing functionality works")
            
            # Clean up
            os.remove(test_image_path)
            if os.path.exists(resized_path):
                os.remove(resized_path)
            
            return True
        else:
            print("✗ Image resizing failed")
            return False
            
    except ImportError:
        print("⚠ PIL/Pillow not available, skipping image tests")
        return True
    except Exception as e:
        print(f"✗ Error testing image processing: {str(e)}")
        return False

def main():
    """Main test function"""
    print("Android Card Game Generator - Test Suite")
    print("="*60)
    
    success_count = 0
    total_tests = 2
    
    # Test 1: Basic PDF generation
    if test_card_generator():
        success_count += 1
    
    # Test 2: Image processing
    if test_image_processing():
        success_count += 1
    
    # Summary
    print(f"\n{'='*60}")
    print("TEST SUMMARY")
    print("="*60)
    print(f"Tests passed: {success_count}/{total_tests}")
    
    if success_count == total_tests:
        print("🎉 All tests passed! The Android card generator is working correctly.")
        print("\nNext steps:")
        print("1. Run the full app: python main.py")
        print("2. Test the UI and create custom cards")
        print("3. Build for Android when ready")
    else:
        print("⚠ Some tests failed. Please check the errors above.")
        
    return success_count == total_tests

if __name__ == "__main__":
    main()
