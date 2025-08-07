# Card Game Generator - Android App

A mobile Android application for creating custom playing cards optimized for 30mm POS receipt printers.

## Features

### 📱 **User-Friendly Interface**
- **Add/Remove Cards**: Dynamic card management with easy add/delete functionality
- **Scrollable Interface**: Handle multiple cards with smooth scrolling
- **Input Fields**: Complete card customization with text inputs
- **Visual Feedback**: Real-time image preview and validation

### 🎨 **Card Customization**
- **Card Name**: Custom card names (e.g., "Diamond 7", "Power Card")
- **Suit Selection**: Choose from 8 different suits:
  - Traditional: Diamond, Heart, Spade, Club
  - Modern: Star, Crown, Shield, Lightning
- **Card Value**: Any value (numbers, letters, symbols)
- **Task/Action**: Define what happens when the card is played
- **Rules**: Specify when and how the card can be used
- **Icon Colors**: 6 color options (red, black, blue, green, purple, orange)

### 🖼️ **Image Upload**
- **Custom Images**: Upload 20mm x 20mm custom images
- **Auto-Resize**: Automatically resizes images to fit card layout
- **Image Preview**: See your uploaded image before generating PDF
- **Supported Formats**: PNG, JPG, JPEG, BMP

### 📄 **PDF Generation**
- **Optimized for Receipt Printers**: Perfect for 30mm width POS printers
- **Card Dimensions**: 26mm × 36.4mm (maintains proper aspect ratio)
- **Vertical Layout**: Single column, vertically stacked cards
- **Professional Quality**: High-resolution PDF output

## Technical Specifications

### **Card Specifications**
- **Card Width**: 26mm (increased from 22mm for better readability)
- **Card Height**: 36.4mm (maintains 2.5:3.5 aspect ratio)
- **Paper Width**: 30mm (POS receipt printer standard)
- **Margins**: 2mm on each side
- **Layout**: Single column, vertically stacked

### **Image Handling**
- **Target Size**: 20mm × 20mm (as requested)
- **Display Size**: 8mm × 8mm on card (scaled for visibility)
- **Position**: Center-top area of each card
- **Auto-Processing**: Automatic resize and format conversion

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- Android development environment (for building APK)

### 1. Install Dependencies
```bash
cd android_app
python setup_android.py
```

### 2. Test Locally (Desktop)
```bash
python main.py
```

### 3. Build for Android (Linux/WSL)
```bash
python setup_android.py --build
```

## Usage Guide

### **Creating Cards**

1. **Start the App**: Launch the Card Game Generator
2. **Add Cards**: Use "Add New Card" button to create multiple cards
3. **Fill Information**:
   - Enter card name
   - Select suit from dropdown
   - Add card value
   - Write task/action description
   - Add rules for card usage
   - Choose icon color
4. **Upload Images** (Optional):
   - Tap "Upload Image"
   - Select image file
   - See preview immediately
5. **Generate PDF**: Tap "Generate PDF" when ready

### **Managing Cards**

- **Delete Cards**: Use "Delete" button on each card (minimum 1 card required)
- **Clear All**: "Clear All" button removes all cards and starts fresh
- **Scroll**: Scroll through multiple cards easily

### **PDF Output**

- **File Naming**: Automatic timestamped filenames (e.g., `custom_cards_20250107_143022.pdf`)
- **Location**: Saved in app directory
- **Format**: Ready for 30mm receipt printer
- **Quality**: Professional print quality

## File Structure

```
android_app/
├── main.py                    # Main Android app with Kivy UI
├── card_generator_android.py  # PDF generation engine
├── buildozer.spec            # Android build configuration
├── requirements.txt          # Python dependencies
├── setup_android.py         # Setup and build script
└── README.md               # This documentation
```

## Building for Android

### **Option 1: Linux/WSL (Recommended)**
```bash
# Install Buildozer
pip install buildozer

# Initialize (first time only)
buildozer init

# Build debug APK
buildozer android debug

# Install on connected device
buildozer android deploy
```

### **Option 2: Online Build Services**
- Use services like GitHub Actions with Linux runners
- Upload your code to cloud-based Android build systems
- Use Docker containers with Linux environment

### **Option 3: Alternative Frameworks**
Consider using:
- **BeeWare** (Python to native apps)
- **Flask + WebView** (Web-based mobile app)
- **React Native** with Python backend

## API Reference

### **CardGeneratorAndroid Class**

```python
class CardGeneratorAndroid:
    def __init__(self):
        # Initialize with 26mm card dimensions
        
    def generate_pdf(self, cards_data, output_file):
        # Generate PDF from card data
        # Returns: True if successful, False otherwise
        
    def resize_custom_image(self, image_path, target_size):
        # Resize uploaded images to target size
        # Returns: Path to resized image
        
    def draw_card(self, canvas, x, y, card_data):
        # Draw individual card on PDF canvas
```

### **Card Data Format**

```python
card_data = {
    'Card_Name': 'Diamond 7',
    'Suit': 'Diamond',
    'Value': '7',
    'Task': 'Draw 2 cards from deck',
    'Rules': 'Must match suit or number',
    'Icon_Color': 'red',
    'Custom_Image': '/path/to/image.png'  # Optional
}
```

## Troubleshooting

### **Common Issues**

1. **App won't start**: Check Python version and dependencies
2. **Image upload fails**: Verify image format and size
3. **PDF generation error**: Check write permissions and disk space
4. **Android build fails**: Ensure Linux environment or use WSL

### **Performance Tips**

- Keep image files under 5MB for faster processing
- Limit to 20-30 cards per PDF for optimal performance
- Use PNG format for best image quality

## Customization

### **Adding New Suits**
Edit `main.py` line ~47:
```python
values=['Diamond', 'Heart', 'Spade', 'Club', 'Star', 'Crown', 'Shield', 'Lightning', 'YourNewSuit']
```

### **Adding New Colors**
Edit `main.py` line ~63:
```python
values=['red', 'black', 'blue', 'green', 'purple', 'orange', 'YourNewColor']
```

### **Changing Card Dimensions**
Edit `card_generator_android.py` lines 16-17:
```python
self.card_width = 26 * mm    # Change width
self.card_height = 36.4 * mm # Change height (maintain ratio)
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the MIT License.

---

**Created for POS Receipt Printer Optimization**
*Perfect for 30mm width thermal printers and card game enthusiasts!*
