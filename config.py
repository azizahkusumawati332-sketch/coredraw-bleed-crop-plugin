"""
Configuration Management
Handles plugin configuration and settings
"""

import json
from pathlib import Path
from typing import Dict, Any

class Config:
    """Configuration manager for the plugin"""
    
    def __init__(self):
        self.config_dir = Path.home() / ".coredraw-bleed-crop"
        self.config_file = self.config_dir / "config.json"
        self.config_dir.mkdir(exist_ok=True)
        self.settings = self.load_config()
    
    def load_config(self) -> Dict:
        """Load configuration from file"""
        if self.config_file.exists():
            try:
                with open(self.config_file, 'r') as f:
                    return json.load(f)
            except:
                return self.get_defaults()
        return self.get_defaults()
    
    def save_config(self):
        """Save configuration to file"""
        try:
            with open(self.config_file, 'w') as f:
                json.dump(self.settings, f, indent=4)
            print(f"[Config] Saved to {self.config_file}")
        except Exception as e:
            print(f"[Config] Save error: {e}")
    
    def get_defaults(self) -> Dict:
        """Get default configuration"""
        return {
            "version": "1.0.0",
            "plugin_name": "Bleed & Crop Studio Pro",
            "coredraw_version": "2024",
            "default_bleed": {
                "left": 2.0,
                "top": 2.0,
                "right": 2.0,
                "bottom": 2.0,
                "unit": "mm"
            },
            "default_safe_area": 5.0,
            "default_export_quality": "Print (600 dpi)",
            "default_color_space": "CMYK",
            "auto_save_presets": True,
            "show_guides": True,
            "theme": "light"
        }
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get configuration value"""
        return self.settings.get(key, default)
    
    def set(self, key: str, value: Any):
        """Set configuration value"""
        self.settings[key] = value
        self.save_config()
    
    def get_bleed_defaults(self) -> Dict:
        """Get default bleed values"""
        return self.settings.get("default_bleed", {
            "left": 2.0,
            "top": 2.0,
            "right": 2.0,
            "bottom": 2.0
        })