"""
Crop Management Module
Handles cropping operations
"""

from typing import Tuple, Dict

class CropManager:
    """Manages crop operations"""
    
    def __init__(self):
        self.crop_offset = 0.0
        self.is_enabled = True
        self.original_bounds = None
    
    def apply_crop(self, bounds: Tuple = None, offset: float = 0.0) -> Dict:
        """
        Apply crop to bounds
        
        Args:
            bounds: (x1, y1, x2, y2) coordinates
            offset: Offset in mm from edge
            
        Returns:
            Dict with crop info
        """
        try:
            if not self.is_enabled:
                print("[Crop] Crop is disabled")
                return {"status": "disabled"}
            
            self.crop_offset = offset
            self.original_bounds = bounds
            
            # Convert mm to points
            mm_to_pt = 2.834645669
            offset_pt = offset * mm_to_pt
            
            if bounds:
                x1, y1, x2, y2 = bounds
                cropped = (
                    x1 + offset_pt,
                    y1 + offset_pt,
                    x2 - offset_pt,
                    y2 - offset_pt
                )
            else:
                cropped = None
            
            print(f"[Crop] Applied with offset {offset}mm")
            return {
                "status": "success",
                "original": bounds,
                "cropped": cropped,
                "offset": offset
            }
        except Exception as e:
            print(f"[Crop] Error: {e}")
            return {"status": "error", "message": str(e)}
    
    def enable(self):
        """Enable cropping"""
        self.is_enabled = True
        print("[Crop] Enabled")
    
    def disable(self):
        """Disable cropping"""
        self.is_enabled = False
        print("[Crop] Disabled")
    
    def toggle(self) -> bool:
        """Toggle crop state"""
        self.is_enabled = not self.is_enabled
        print(f"[Crop] {'Enabled' if self.is_enabled else 'Disabled'}")
        return self.is_enabled
    
    def get_crop_marks(self, bounds: Tuple) -> Dict:
        """
        Generate crop marks
        
        Args:
            bounds: Document bounds
            
        Returns:
            Dict with crop mark positions
        """
        x1, y1, x2, y2 = bounds
        mark_length = 10  # points
        
        return {
            "top_left": [(x1, y2), (x1 + mark_length, y2), (x1, y2 - mark_length)],
            "top_right": [(x2, y2), (x2 - mark_length, y2), (x2, y2 - mark_length)],
            "bottom_left": [(x1, y1), (x1 + mark_length, y1), (x1, y1 + mark_length)],
            "bottom_right": [(x2, y1), (x2 - mark_length, y1), (x2, y1 + mark_length)]
        }