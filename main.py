"""
CorelDRAW Bleed & Crop Professional Plugin
Main entry point for plugin initialization
Kompatibel: CorelDraw 2024
"""

import os
import sys
import json
from pathlib import Path

# Add src to path
PLUGIN_DIR = Path(__file__).parent.parent
sys.path.insert(0, str(PLUGIN_DIR / "src"))

from ui.panel import BleedCropPanel
from features.bleed import BleedManager
from features.crop import CropManager
from features.safe_area import SafeAreaManager
from features.export_pdf import PDFExporter
from utils.config import Config

class CorelDrawPlugin:
    def __init__(self):
        self.config = Config()
        self.bleed_manager = BleedManager()
        self.crop_manager = CropManager()
        self.safe_area_manager = SafeAreaManager()
        self.pdf_exporter = PDFExporter()
        self.panel = None
        self.initialize()
    
    def initialize(self):
        """Initialize plugin"""
        print("[CorelDRAW Plugin] Initializing Bleed & Crop Plugin...")
        try:
            self.panel = BleedCropPanel(self)
            self.setup_toolbar()
            print("[CorelDRAW Plugin] ✓ Plugin loaded successfully!")
            return True
        except Exception as e:
            print(f"[CorelDRAW Plugin] ✗ Error: {e}")
            return False
    
    def setup_toolbar(self):
        """Setup toolbar button"""
        try:
            # CorelDraw toolbar integration
            toolbar_config = {
                "name": "Bleed & Crop Tools",
                "buttons": [
                    {
                        "id": "bleed_tool",
                        "label": "Bleed Settings",
                        "icon": "bleed.png",
                        "callback": self.show_panel
                    },
                    {
                        "id": "crop_tool",
                        "label": "Crop to Artboard",
                        "icon": "crop.png",
                        "callback": self.crop_manager.apply_crop
                    },
                    {
                        "id": "export_pdf",
                        "label": "Export PDF",
                        "icon": "export.png",
                        "callback": self.pdf_exporter.export
                    }
                ]
            }
            print("[Toolbar] Buttons configured successfully")
        except Exception as e:
            print(f"[Toolbar] Error: {e}")
    
    def show_panel(self):
        """Show main panel"""
        if self.panel:
            self.panel.show()
    
    def apply_bleed(self, bleed_values):
        """Apply bleed settings"""
        return self.bleed_manager.apply(bleed_values)
    
    def apply_crop(self):
        """Apply crop"""
        return self.crop_manager.apply_crop()
    
    def apply_safe_area(self, safe_value):
        """Apply safe area"""
        return self.safe_area_manager.apply(safe_value)
    
    def export_pdf(self, filepath, settings):
        """Export to PDF"""
        return self.pdf_exporter.export(filepath, settings)

# Global plugin instance
plugin_instance = None

def load_plugin():
    """Load plugin in CorelDraw"""
    global plugin_instance
    plugin_instance = CorelDrawPlugin()
    return plugin_instance

if __name__ == "__main__":
    load_plugin()