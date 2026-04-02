"""
Safe Area Management Module
Manages content protection zones
"""

from typing import Tuple, Dict

class SafeAreaManager:
    """Manages safe area settings"""
    
    def __init__(self):
        self.safe_distance = 5.0  # mm
        self.safe_area_enabled = True
        self.current_bounds = None
    
    def apply(self, safe_distance: float) -> bool:
        """
        Apply safe area distance
        
        Args:
            safe_distance: Distance in mm from edge
            
        Returns:
            bool: Success status
        """
        try:
            self.safe_distance = safe_distance
            print(f"[Safe Area] Applied: {safe_distance}mm from edge")
            return True
        except Exception as e:
            print(f"[Safe Area] Error: {e}")
            return False
    
    def calculate_safe_zone(self, bounds: Tuple) -> Dict:
        """
        Calculate safe zone within bounds
        
        Args:
            bounds: (x1, y1, x2, y2)
            
        Returns:
            Dict with safe area coordinates
        """
        x1, y1, x2, y2 = bounds
        
        # Convert mm to points
        mm_to_pt = 2.834645669
        safe_pt = self.safe_distance * mm_to_pt
        
        safe_bounds = (
            x1 + safe_pt,
            y1 + safe_pt,
            x2 - safe_pt,
            y2 - safe_pt
        )
        
        return {
            "full_bounds": bounds,
            "safe_bounds": safe_bounds,
            "danger_zones": {
                "left": (x1, y1, x1 + safe_pt, y2),
                "right": (x2 - safe_pt, y1, x2, y2),
                "top": (x1, y2 - safe_pt, x2, y2),
                "bottom": (x1, y1, x2, y1 + safe_pt)
            }
        }
    
    def get_guide_lines(self, bounds: Tuple) -> Dict:
        """
        Generate guide lines for safe area
        
        Args:
            bounds: Document bounds
            
        Returns:
            Dict with guide line positions
        """
        x1, y1, x2, y2 = bounds
        mm_to_pt = 2.834645669
        safe_pt = self.safe_distance * mm_to_pt
        
        return {
            "vertical": [x1 + safe_pt, x2 - safe_pt],
            "horizontal": [y1 + safe_pt, y2 - safe_pt]
        }
    
    def enable(self):
        """Enable safe area"""
        self.safe_area_enabled = True
        print("[Safe Area] Enabled")
    
    def disable(self):
        """Disable safe area"""
        self.safe_area_enabled = False
        print("[Safe Area] Disabled")
    
    def check_content_in_danger_zone(self, bounds: Tuple, content_bounds: Tuple) -> bool:
        """
        Check if content is in danger zone
        
        Args:
            bounds: Full document bounds
            content_bounds: Content bounds
            
        Returns:
            bool: True if content is in danger zone
        """
        safe_zone = self.calculate_safe_zone(bounds)
        safe_x1, safe_y1, safe_x2, safe_y2 = safe_zone["safe_bounds"]
        c_x1, c_y1, c_x2, c_y2 = content_bounds
        
        # Check if any corner of content is outside safe zone
        return (c_x1 < safe_x1 or c_x2 > safe_x2 or 
                c_y1 < safe_y1 or c_y2 > safe_y2)