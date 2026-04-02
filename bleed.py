"""
Bleed Management Module
Handles bleed calculation and application
"""

from dataclasses import dataclass
from typing import Dict, Tuple

@dataclass
class BleedSettings:
    left: float = 2.0
    top: float = 2.0
    right: float = 2.0
    bottom: float = 2.0
    unit: str = "mm"

class BleedManager:
    """Manages bleed operations"""
    
    def __init__(self):
        self.current_bleed = BleedSettings()
        self.history = []
    
    def apply(self, bleed_dict: Dict) -> bool:
        """
        Apply bleed settings
        
        Args:
            bleed_dict: Dictionary with bleed values
            
        Returns:
            bool: Success status
        """
        try:
            self.current_bleed = BleedSettings(
                left=bleed_dict.get("bleed_left", 2.0),
                top=bleed_dict.get("bleed_top", 2.0),
                right=bleed_dict.get("bleed_right", 2.0),
                bottom=bleed_dict.get("bleed_bottom", 2.0),
                unit=bleed_dict.get("unit", "mm")
            )
            self.history.append(self.current_bleed)
            print(f"[Bleed] Applied: L={self.current_bleed.left}, T={self.current_bleed.top}, "
                  f"R={self.current_bleed.right}, B={self.current_bleed.bottom} {self.current_bleed.unit}")
            return True
        except Exception as e:
            print(f"[Bleed] Error: {e}")
            return False
    
    def apply_to_selection(self, selection_bounds: Tuple) -> Dict:
        """
        Apply bleed to selection bounds
        
        Args:
            selection_bounds: (x1, y1, x2, y2)
            
        Returns:
            Dict with new bounds
        """
        x1, y1, x2, y2 = selection_bounds
        
        # Convert mm to points (1mm = 2.834645669 points)
        mm_to_pt = 2.834645669
        
        bleed_left_pt = self.current_bleed.left * mm_to_pt
        bleed_top_pt = self.current_bleed.top * mm_to_pt
        bleed_right_pt = self.current_bleed.right * mm_to_pt
        bleed_bottom_pt = self.current_bleed.bottom * mm_to_pt
        
        return {
            "original": (x1, y1, x2, y2),
            "with_bleed": (
                x1 - bleed_left_pt,
                y1 - bleed_top_pt,
                x2 + bleed_right_pt,
                y2 + bleed_bottom_pt
            ),
            "bleed_areas": {
                "left": (x1 - bleed_left_pt, y1, x1, y2),
                "top": (x1, y2, x2, y2 + bleed_top_pt),
                "right": (x2, y1, x2 + bleed_right_pt, y2),
                "bottom": (x1, y1 - bleed_bottom_pt, x2, y1)
            }
        }
    
    def get_current(self) -> BleedSettings:
        """Get current bleed settings"""
        return self.current_bleed
    
    def reset(self):
        """Reset to default"""
        self.current_bleed = BleedSettings()
        print("[Bleed] Reset to defaults")
    
    def undo(self) -> bool:
        """Undo last bleed application"""
        if len(self.history) > 1:
            self.history.pop()
            self.current_bleed = self.history[-1]
            print("[Bleed] Undo successful")
            return True
        return False