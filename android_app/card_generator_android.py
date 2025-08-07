from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch, mm
from reportlab.lib.colors import black, red, blue, green
from reportlab.graphics.shapes import Drawing, Rect, Circle, Polygon
from reportlab.graphics import renderPDF
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.utils import ImageReader
from PIL import Image as PILImage
import os
import sys

class CardGeneratorAndroid:
    def __init__(self):
        # Updated dimensions for 26mm card width
        self.card_width = 26 * mm  # 26mm card width as requested
        self.card_height = 36.4 * mm  # Maintaining 2.5:3.5 aspect ratio (26 * 3.5/2.5)
        self.print_width = 30 * mm  # 30mm print paper width
        self.margin = 2 * mm  # Smaller margins for 26mm card on 30mm paper
        
    def resize_custom_image(self, image_path, target_size=(20*mm, 20*mm)):
        """Resize uploaded image to 20mm x 20mm"""
        try:
            with PILImage.open(image_path) as img:
                # Convert to RGB if needed
                if img.mode != 'RGB':
                    img = img.convert('RGB')
                
                # Resize to target size (maintaining aspect ratio with crop)
                img_resized = img.resize((int(target_size[0]), int(target_size[1])), PILImage.Resampling.LANCZOS)
                
                # Save temporary resized image
                temp_path = 'temp_resized_image.png'
                img_resized.save(temp_path, 'PNG')
                return temp_path
        except Exception as e:
            print(f"Error resizing image: {e}")
            return None
    
    def draw_suit_icon(self, canvas, x, y, suit, color, size=4):
        """Draw suit icon on the card - scaled for mobile cards"""
        canvas.saveState()
        
        if color == 'red':
            canvas.setFillColor(colors.red)
        elif color == 'blue':
            canvas.setFillColor(colors.blue)
        elif color == 'green':
            canvas.setFillColor(colors.green)
        elif color == 'purple':
            canvas.setFillColor(colors.purple)
        elif color == 'orange':
            canvas.setFillColor(colors.orange)
        else:
            canvas.setFillColor(colors.black)
        
        if suit.lower() == 'diamond':
            # Draw diamond shape
            path = canvas.beginPath()
            path.moveTo(x + size/2, y)
            path.lineTo(x, y + size/2)
            path.lineTo(x + size/2, y + size)
            path.lineTo(x + size, y + size/2)
            path.close()
            canvas.drawPath(path, fill=1)
            
        elif suit.lower() == 'heart':
            # Draw heart shape
            canvas.circle(x + size/3, y + 2*size/3, size/4, fill=1)
            canvas.circle(x + 2*size/3, y + 2*size/3, size/4, fill=1)
            path = canvas.beginPath()
            path.moveTo(x + size/6, y + size/2)
            path.lineTo(x + 5*size/6, y + size/2)
            path.lineTo(x + size/2, y)
            path.close()
            canvas.drawPath(path, fill=1)
            
        elif suit.lower() == 'spade':
            # Draw spade shape
            canvas.circle(x + size/2, y + 2*size/3, size/3, fill=1)
            canvas.rect(x + 2*size/5, y, size/5, size/2, fill=1)
            
        elif suit.lower() == 'club':
            # Draw club shape
            canvas.circle(x + size/2, y + 2*size/3, size/6, fill=1)
            canvas.circle(x + size/3, y + size/2, size/6, fill=1)
            canvas.circle(x + 2*size/3, y + size/2, size/6, fill=1)
            canvas.rect(x + 2*size/5, y, size/5, size/2, fill=1)
            
        elif suit.lower() == 'star':
            # Draw star shape
            star_points = []
            for i in range(10):
                angle = i * 36 * 3.14159 / 180
                if i % 2 == 0:
                    radius = size/2
                else:
                    radius = size/4
                px = x + size/2 + radius * cos(angle - 3.14159/2)
                py = y + size/2 + radius * sin(angle - 3.14159/2)
                star_points.extend([px, py])
            
            path = canvas.beginPath()
            path.moveTo(star_points[0], star_points[1])
            for i in range(2, len(star_points), 2):
                path.lineTo(star_points[i], star_points[i+1])
            path.close()
            canvas.drawPath(path, fill=1)
            
        elif suit.lower() == 'crown':
            # Draw crown shape
            canvas.rect(x, y, size, size/3, fill=1)
            for i in range(3):
                canvas.rect(x + i*size/3, y + size/3, size/6, size/2, fill=1)
                
        elif suit.lower() == 'shield':
            # Draw shield shape
            path = canvas.beginPath()
            path.moveTo(x + size/2, y)
            path.lineTo(x, y + size/3)
            path.lineTo(x, y + 2*size/3)
            path.lineTo(x + size/2, y + size)
            path.lineTo(x + size, y + 2*size/3)
            path.lineTo(x + size, y + size/3)
            path.close()
            canvas.drawPath(path, fill=1)
            
        elif suit.lower() == 'lightning':
            # Draw lightning bolt
            path = canvas.beginPath()
            path.moveTo(x + size/3, y)
            path.lineTo(x, y + size/2)
            path.lineTo(x + size/3, y + size/2)
            path.lineTo(x, y + size)
            path.lineTo(x + 2*size/3, y + size/2)
            path.lineTo(x + size/3, y + size/2)
            path.close()
            canvas.drawPath(path, fill=1)
        
        canvas.restoreState()
    
    def draw_card(self, canvas, x, y, card_data):
        """Draw a single card optimized for 26mm width"""
        # Draw card border
        canvas.setStrokeColor(colors.black)
        canvas.setLineWidth(0.5)
        canvas.roundRect(x, y, self.card_width, self.card_height, 2)
        
        # Fill card background
        canvas.setFillColor(colors.white)
        canvas.roundRect(x, y, self.card_width, self.card_height, 2, fill=1)
        canvas.setFillColor(colors.black)
        
        # Draw card name at top
        canvas.setFont("Helvetica-Bold", 7)
        canvas.drawCentredString(x + self.card_width/2, y + self.card_height - 7*mm, 
                                card_data['Card_Name'])
        
        # Draw suit and value in corners
        canvas.setFont("Helvetica-Bold", 6)
        if card_data['Icon_Color'] == 'red':
            canvas.setFillColor(colors.red)
        elif card_data['Icon_Color'] == 'blue':
            canvas.setFillColor(colors.blue)
        elif card_data['Icon_Color'] == 'green':
            canvas.setFillColor(colors.green)
        elif card_data['Icon_Color'] == 'purple':
            canvas.setFillColor(colors.purple)
        elif card_data['Icon_Color'] == 'orange':
            canvas.setFillColor(colors.orange)
        else:
            canvas.setFillColor(colors.black)
        
        # Top-left corner
        canvas.drawString(x + 1*mm, y + self.card_height - 9*mm, str(card_data['Value']))
        
        # Bottom-right corner (upside down)
        canvas.saveState()
        canvas.translate(x + self.card_width - 1*mm, y + 4*mm)
        canvas.rotate(180)
        canvas.drawString(0, 0, str(card_data['Value']))
        canvas.restoreState()
        
        # Draw custom image if provided
        if card_data.get('Custom_Image') and os.path.exists(card_data['Custom_Image']):
            try:
                # Resize and draw custom image
                resized_image_path = self.resize_custom_image(card_data['Custom_Image'])
                if resized_image_path and os.path.exists(resized_image_path):
                    # Draw image in center-top area
                    image_size = 8*mm
                    img_x = x + (self.card_width - image_size) / 2
                    img_y = y + self.card_height - 18*mm
                    
                    canvas.drawImage(resized_image_path, img_x, img_y, 
                                   width=image_size, height=image_size)
                    
                    # Clean up temp file
                    os.remove(resized_image_path)
            except Exception as e:
                print(f"Error drawing custom image: {e}")
        else:
            # Draw suit icons if no custom image
            icon_size = 3*mm
            self.draw_suit_icon(canvas, x + 1*mm, y + self.card_height - 14*mm, 
                               card_data['Suit'], card_data['Icon_Color'], size=icon_size)
            
            # Draw suit icon in bottom-right (upside down)
            canvas.saveState()
            canvas.translate(x + self.card_width - 4*mm, y + 7*mm)
            canvas.rotate(180)
            self.draw_suit_icon(canvas, 0, 0, card_data['Suit'], 
                               card_data['Icon_Color'], size=icon_size)
            canvas.restoreState()
            
            # Draw central suit icon (larger)
            central_icon_size = 5*mm
            self.draw_suit_icon(canvas, x + self.card_width/2 - central_icon_size/2, 
                               y + self.card_height/2 + 3*mm, 
                               card_data['Suit'], card_data['Icon_Color'], size=central_icon_size)
        
        # Draw task section
        canvas.setFillColor(colors.black)
        canvas.setFont("Helvetica-Bold", 5)
        canvas.drawString(x + 1*mm, y + self.card_height/2 - 1*mm, "Task:")
        
        canvas.setFont("Helvetica", 4)
        # Wrap text for task
        task_lines = self.wrap_text(card_data['Task'], 15)
        for i, line in enumerate(task_lines[:2]):  # Limit to 2 lines
            canvas.drawString(x + 1*mm, y + self.card_height/2 - 4*mm - (i * 4*mm), line)
        
        # Draw rules section
        canvas.setFont("Helvetica-Bold", 5)
        canvas.drawString(x + 1*mm, y + 10*mm, "Rules:")
        
        canvas.setFont("Helvetica", 4)
        # Wrap text for rules
        rules_lines = self.wrap_text(card_data['Rules'], 15)
        for i, line in enumerate(rules_lines[:2]):  # Limit to 2 lines
            canvas.drawString(x + 1*mm, y + 7*mm - (i * 4*mm), line)
    
    def wrap_text(self, text, max_chars):
        """Wrap text to fit within card width"""
        words = text.split()
        lines = []
        current_line = ""
        
        for word in words:
            if len(current_line + word + " ") <= max_chars:
                current_line += word + " "
            else:
                if current_line:
                    lines.append(current_line.strip())
                current_line = word + " "
        
        if current_line:
            lines.append(current_line.strip())
        
        return lines
    
    def generate_pdf(self, cards_data, output_file="android_cards.pdf"):
        """Generate PDF file optimized for Android app and 26mm cards"""
        try:
            # Custom page size for 30mm receipt paper
            paper_width = 30 * mm
            cards_needed = len(cards_data)
            card_height_with_margin = self.card_height + self.margin
            paper_height = (cards_needed * card_height_with_margin) + self.margin
            
            # Set minimum height
            min_height = 100 * mm
            if paper_height < min_height:
                paper_height = min_height
            
            custom_page_size = (paper_width, paper_height)
            c = canvas.Canvas(output_file, pagesize=custom_page_size)
            page_width, page_height = custom_page_size
            
            print(f"Generating PDF...")
            print(f"Paper dimensions: {page_width/mm:.1f}mm x {page_height/mm:.1f}mm")
            print(f"Card dimensions: {self.card_width/mm:.1f}mm x {self.card_height/mm:.1f}mm")
            print(f"Total cards: {len(cards_data)}")
            
            # Calculate horizontal centering
            x_center = (page_width - self.card_width) / 2
            
            for index, card_data in enumerate(cards_data):
                # Calculate vertical position (from top to bottom)
                y_position = page_height - self.margin - (index + 1) * (self.card_height + self.margin)
                
                # Draw the card centered horizontally
                self.draw_card(c, x_center, y_position, card_data)
                
                print(f"Card {index + 1}: {card_data['Card_Name']} - Done")
            
            c.save()
            print(f"PDF generated successfully: {output_file}")
            return True
            
        except Exception as e:
            print(f"Error generating PDF: {e}")
            return False

# Helper function for trigonometry (missing import)
def cos(angle):
    import math
    return math.cos(angle)

def sin(angle):
    import math
    return math.sin(angle)
