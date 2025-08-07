import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.spinner import Spinner
from kivy.uix.popup import Popup
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.metrics import dp
from kivy.core.window import Window

import os
import json
from datetime import datetime
from card_generator_android import CardGeneratorAndroid

kivy.require('2.0.0')

class CardInputWidget(BoxLayout):
    def __init__(self, card_number, on_delete_callback, **kwargs):
        super().__init__(orientation='vertical', size_hint_y=None, height=dp(400), **kwargs)
        self.card_number = card_number
        self.on_delete_callback = on_delete_callback
        self.uploaded_image_path = None
        
        # Card header with delete button
        header = BoxLayout(orientation='horizontal', size_hint_y=None, height=dp(40))
        header.add_widget(Label(text=f'Card {card_number}', font_size='16sp', bold=True))
        
        delete_btn = Button(text='Delete', size_hint_x=None, width=dp(80))
        delete_btn.bind(on_press=self.delete_card)
        header.add_widget(delete_btn)
        self.add_widget(header)
        
        # Card name input
        self.add_widget(Label(text='Card Name:', size_hint_y=None, height=dp(30)))
        self.card_name_input = TextInput(hint_text='e.g., Diamond 7', size_hint_y=None, height=dp(40))
        self.add_widget(self.card_name_input)
        
        # Suit selection
        self.add_widget(Label(text='Suit:', size_hint_y=None, height=dp(30)))
        self.suit_spinner = Spinner(
            text='Select Suit',
            values=['Diamond', 'Heart', 'Spade', 'Club', 'Star', 'Crown', 'Shield', 'Lightning'],
            size_hint_y=None, height=dp(40)
        )
        self.add_widget(self.suit_spinner)
        
        # Value input
        self.add_widget(Label(text='Card Value:', size_hint_y=None, height=dp(30)))
        self.value_input = TextInput(hint_text='e.g., 7, K, A, Q, J', size_hint_y=None, height=dp(40))
        self.add_widget(self.value_input)
        
        # Task input
        self.add_widget(Label(text='Task/Action:', size_hint_y=None, height=dp(30)))
        self.task_input = TextInput(hint_text='What happens when this card is played', 
                                   multiline=True, size_hint_y=None, height=dp(60))
        self.add_widget(self.task_input)
        
        # Rules input
        self.add_widget(Label(text='Rules:', size_hint_y=None, height=dp(30)))
        self.rules_input = TextInput(hint_text='When and how this card can be played', 
                                    multiline=True, size_hint_y=None, height=dp(60))
        self.add_widget(self.rules_input)
        
        # Icon color selection
        self.add_widget(Label(text='Icon Color:', size_hint_y=None, height=dp(30)))
        self.color_spinner = Spinner(
            text='Select Color',
            values=['red', 'black', 'blue', 'green', 'purple', 'orange'],
            size_hint_y=None, height=dp(40)
        )
        self.add_widget(self.color_spinner)
        
        # Image upload section
        image_section = BoxLayout(orientation='horizontal', size_hint_y=None, height=dp(50))
        image_section.add_widget(Label(text='Custom Image (20x20mm):', size_hint_x=0.7))
        
        upload_btn = Button(text='Upload Image', size_hint_x=0.3)
        upload_btn.bind(on_press=self.open_image_chooser)
        image_section.add_widget(upload_btn)
        self.add_widget(image_section)
        
        # Image preview
        self.image_preview = Image(size_hint_y=None, height=dp(60), allow_stretch=True)
        self.add_widget(self.image_preview)
        
        # Separator
        self.add_widget(Widget(size_hint_y=None, height=dp(10)))
    
    def delete_card(self, instance):
        self.on_delete_callback(self)
    
    def open_image_chooser(self, instance):
        content = BoxLayout(orientation='vertical')
        
        filechooser = FileChooserIconView(
            filters=['*.png', '*.jpg', '*.jpeg', '*.bmp']
        )
        content.add_widget(filechooser)
        
        button_layout = BoxLayout(size_hint_y=None, height=dp(50))
        select_btn = Button(text='Select')
        cancel_btn = Button(text='Cancel')
        button_layout.add_widget(select_btn)
        button_layout.add_widget(cancel_btn)
        content.add_widget(button_layout)
        
        popup = Popup(title='Choose Image', content=content, size_hint=(0.9, 0.9))
        
        def select_image(instance):
            if filechooser.selection:
                self.uploaded_image_path = filechooser.selection[0]
                self.image_preview.source = self.uploaded_image_path
                popup.dismiss()
        
        def cancel_selection(instance):
            popup.dismiss()
        
        select_btn.bind(on_press=select_image)
        cancel_btn.bind(on_press=cancel_selection)
        
        popup.open()
    
    def get_card_data(self):
        return {
            'Card_Name': self.card_name_input.text.strip() or f'Card {self.card_number}',
            'Suit': self.suit_spinner.text if self.suit_spinner.text != 'Select Suit' else 'Diamond',
            'Value': self.value_input.text.strip() or '1',
            'Task': self.task_input.text.strip() or 'No special action',
            'Rules': self.rules_input.text.strip() or 'Play normally',
            'Icon_Color': self.color_spinner.text if self.color_spinner.text != 'Select Color' else 'black',
            'Custom_Image': self.uploaded_image_path
        }

class CardGameApp(App):
    def build(self):
        Window.clearcolor = (0.95, 0.95, 0.95, 1)
        
        main_layout = BoxLayout(orientation='vertical', padding=dp(10), spacing=dp(10))
        
        # App header
        header = BoxLayout(orientation='vertical', size_hint_y=None, height=dp(100))
        title = Label(text='Card Game Generator', font_size='24sp', bold=True, 
                     size_hint_y=None, height=dp(40))
        subtitle = Label(text='Create custom cards for 30mm receipt printer\nCard size: 26mm x 36.4mm', 
                        font_size='14sp', size_hint_y=None, height=dp(60))
        header.add_widget(title)
        header.add_widget(subtitle)
        main_layout.add_widget(header)
        
        # Scroll view for cards
        scroll = ScrollView()
        self.cards_layout = BoxLayout(orientation='vertical', spacing=dp(10), size_hint_y=None)
        self.cards_layout.bind(minimum_height=self.cards_layout.setter('height'))
        scroll.add_widget(self.cards_layout)
        main_layout.add_widget(scroll)
        
        # Control buttons
        button_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=dp(60), spacing=dp(10))
        
        add_card_btn = Button(text='Add New Card')
        add_card_btn.bind(on_press=self.add_card)
        button_layout.add_widget(add_card_btn)
        
        generate_btn = Button(text='Generate PDF')
        generate_btn.bind(on_press=self.generate_pdf)
        button_layout.add_widget(generate_btn)
        
        clear_all_btn = Button(text='Clear All')
        clear_all_btn.bind(on_press=self.clear_all_cards)
        button_layout.add_widget(clear_all_btn)
        
        main_layout.add_widget(button_layout)
        
        # Add first card by default
        self.card_widgets = []
        self.add_card()
        
        return main_layout
    
    def add_card(self, instance=None):
        card_number = len(self.card_widgets) + 1
        card_widget = CardInputWidget(card_number, self.remove_card)
        self.card_widgets.append(card_widget)
        self.cards_layout.add_widget(card_widget)
    
    def remove_card(self, card_widget):
        if len(self.card_widgets) > 1:  # Keep at least one card
            self.card_widgets.remove(card_widget)
            self.cards_layout.remove_widget(card_widget)
            self.renumber_cards()
    
    def renumber_cards(self):
        for i, card_widget in enumerate(self.card_widgets):
            card_widget.card_number = i + 1
            # Update the header label
            if card_widget.children:
                header = card_widget.children[-1]  # First child (added last)
                if isinstance(header, BoxLayout) and header.children:
                    label = header.children[-1]  # First child in header
                    if isinstance(label, Label):
                        label.text = f'Card {i + 1}'
    
    def clear_all_cards(self, instance):
        # Clear all cards and add one empty card
        for card_widget in self.card_widgets[:]:
            self.cards_layout.remove_widget(card_widget)
        self.card_widgets.clear()
        self.add_card()
    
    def generate_pdf(self, instance):
        try:
            # Collect all card data
            cards_data = []
            for card_widget in self.card_widgets:
                card_data = card_widget.get_card_data()
                cards_data.append(card_data)
            
            if not cards_data:
                self.show_popup('Error', 'No cards to generate!')
                return
            
            # Generate PDF using the card generator
            generator = CardGeneratorAndroid()
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            output_file = f'custom_cards_{timestamp}.pdf'
            
            # Save cards data temporarily
            temp_data_file = 'temp_cards_data.json'
            with open(temp_data_file, 'w', encoding='utf-8') as f:
                json.dump(cards_data, f, indent=2, ensure_ascii=False)
            
            # Generate PDF
            result = generator.generate_pdf(cards_data, output_file)
            
            # Clean up temp file
            if os.path.exists(temp_data_file):
                os.remove(temp_data_file)
            
            if result:
                self.show_popup('Success', f'PDF generated successfully!\nFile: {output_file}\n\nCards: {len(cards_data)}\nSize: 26mm x 36.4mm each')
            else:
                self.show_popup('Error', 'Failed to generate PDF. Please check your input data.')
                
        except Exception as e:
            self.show_popup('Error', f'An error occurred:\n{str(e)}')
    
    def show_popup(self, title, message):
        content = BoxLayout(orientation='vertical', padding=dp(10), spacing=dp(10))
        content.add_widget(Label(text=message, text_size=(None, None)))
        
        close_btn = Button(text='OK', size_hint_y=None, height=dp(50))
        content.add_widget(close_btn)
        
        popup = Popup(title=title, content=content, size_hint=(0.8, 0.6))
        close_btn.bind(on_press=popup.dismiss)
        popup.open()

if __name__ == '__main__':
    CardGameApp().run()
