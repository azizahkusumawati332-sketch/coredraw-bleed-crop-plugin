"""
Professional UI Panel for Bleed & Crop settings
Displays interface matching the design requirements
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import json
from pathlib import Path

class BleedCropPanel:
    def __init__(self, plugin):
        self.plugin = plugin
        self.window = None
        self.presets = self.load_presets()
        self.current_preset = "default"
        
    def load_presets(self):
        """Load preset settings from JSON"""
        preset_file = Path(__file__).parent.parent / "presets" / "presets.json"
        try:
            with open(preset_file, 'r') as f:
                return json.load(f)
        except:
            return {
                "default": {
                    "bleed_left": 2.00,
                    "bleed_top": 2.00,
                    "bleed_right": 2.00,
                    "bleed_bottom": 2.00,
                    "crop_enabled": True,
                    "safe_area": 5.00
                }
            }
    
    def show(self):
        """Display the panel"""
        if self.window is not None:
            self.window.lift()
            return
        
        self.window = tk.Tk()
        self.window.title("Bleed & Crop Studio Pro")
        self.window.geometry("650x750")
        self.window.resizable(False, False)
        
        # Apply dark theme
        self.window.configure(bg="#f5f5f5")
        
        self.create_widgets()
        self.window.mainloop()
    
    def create_widgets(self):
        """Create UI components"""
        
        # Header
        header = tk.Frame(self.window, bg="#2c3e50", height=60)
        header.pack(fill=tk.X)
        
        title = tk.Label(header, text="BLEED & CROP STUDIO", 
                        font=("Segoe UI", 14, "bold"), 
                        fg="white", bg="#2c3e50")
        title.pack(pady=10)
        
        # Main content
        content = ttk.Notebook(self.window)
        content.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Tab 1: Bleed Settings
        self.create_bleed_tab(content)
        
        # Tab 2: Crop Settings
        self.create_crop_tab(content)
        
        # Tab 3: Safe Area
        self.create_safe_area_tab(content)
        
        # Tab 4: Export
        self.create_export_tab(content)
        
        # Bottom buttons
        self.create_bottom_buttons()
    
    def create_bleed_tab(self, notebook):
        """Create Bleed settings tab"""
        frame = ttk.Frame(notebook, padding=15)
        notebook.add(frame, text="BLEED")
        
        # Method selection
        method_frame = ttk.LabelFrame(frame, text="Bleed Method", padding=10)
        method_frame.pack(fill=tk.X, pady=10)
        
        self.bleed_method = tk.StringVar(value="individual")
        
        rb1 = ttk.Radiobutton(method_frame, text="From all sides of the design",
                             variable=self.bleed_method, value="individual")
        rb1.pack(anchor=tk.W, pady=5)
        
        rb2 = ttk.Radiobutton(method_frame, text="Inside and outside layout",
                             variable=self.bleed_method, value="combined")
        rb2.pack(anchor=tk.W, pady=5)
        
        # Individual settings
        self.individual_frame = ttk.LabelFrame(frame, text="Individual Sides", padding=10)
        self.individual_frame.pack(fill=tk.X, pady=10)
        
        # Left and Top
        row1 = tk.Frame(self.individual_frame, bg="white")
        row1.pack(fill=tk.X, pady=5)
        
        tk.Label(row1, text="Left", font=("Segoe UI", 10), bg="white").pack(side=tk.LEFT, padx=5)
        self.bleed_left = ttk.Spinbox(row1, from_=0, to=50, width=10, 
                                      format="%.2f", increment=0.5)
        self.bleed_left.set(2.00)
        self.bleed_left.pack(side=tk.LEFT, padx=5)
        
        tk.Label(row1, text="mm", font=("Segoe UI", 9), bg="white").pack(side=tk.LEFT, padx=2)
        
        tk.Label(row1, text="Top", font=("Segoe UI", 10), bg="white").pack(side=tk.LEFT, padx=15)
        self.bleed_top = ttk.Spinbox(row1, from_=0, to=50, width=10,
                                     format="%.2f", increment=0.5)
        self.bleed_top.set(2.00)
        self.bleed_top.pack(side=tk.LEFT, padx=5)
        
        tk.Label(row1, text="mm", font=("Segoe UI", 9), bg="white").pack(side=tk.LEFT, padx=2)
        
        # Right and Bottom
        row2 = tk.Frame(self.individual_frame, bg="white")
        row2.pack(fill=tk.X, pady=5)
        
        tk.Label(row2, text="Right", font=("Segoe UI", 10), bg="white").pack(side=tk.LEFT, padx=5)
        self.bleed_right = ttk.Spinbox(row2, from_=0, to=50, width=10,
                                       format="%.2f", increment=0.5)
        self.bleed_right.set(2.00)
        self.bleed_right.pack(side=tk.LEFT, padx=5)
        
        tk.Label(row2, text="mm", font=("Segoe UI", 9), bg="white").pack(side=tk.LEFT, padx=2)
        
        tk.Label(row2, text="Bottom", font=("Segoe UI", 10), bg="white").pack(side=tk.LEFT, padx=10)
        self.bleed_bottom = ttk.Spinbox(row2, from_=0, to=50, width=10,
                                        format="%.2f", increment=0.5)
        self.bleed_bottom.set(2.00)
        self.bleed_bottom.pack(side=tk.LEFT, padx=5)
        
        tk.Label(row2, text="mm", font=("Segoe UI", 9), bg="white").pack(side=tk.LEFT, padx=2)
        
        # Combined settings (hidden by default)
        self.combined_frame = ttk.LabelFrame(frame, text="Combined Bleed", padding=10)
        
        row3 = tk.Frame(self.combined_frame, bg="white")
        row3.pack(fill=tk.X, pady=5)
        
        tk.Label(row3, text="Inner", font=("Segoe UI", 10), bg="white").pack(side=tk.LEFT, padx=5)
        self.bleed_inner = ttk.Spinbox(row3, from_=0, to=50, width=10,
                                       format="%.2f", increment=0.5)
        self.bleed_inner.set(2.00)
        self.bleed_inner.pack(side=tk.LEFT, padx=5)
        
        tk.Label(row3, text="mm", font=("Segoe UI", 9), bg="white").pack(side=tk.LEFT, padx=2)
        
        tk.Label(row3, text="Outer", font=("Segoe UI", 10), bg="white").pack(side=tk.LEFT, padx=15)
        self.bleed_outer = ttk.Spinbox(row3, from_=0, to=50, width=10,
                                       format="%.2f", increment=0.5)
        self.bleed_outer.set(2.00)
        self.bleed_outer.pack(side=tk.LEFT, padx=5)
        
        tk.Label(row3, text="mm", font=("Segoe UI", 9), bg="white").pack(side=tk.LEFT, padx=2)
        
        # Preset selector
        preset_frame = ttk.LabelFrame(frame, text="Presets", padding=10)
        preset_frame.pack(fill=tk.X, pady=10)
        
        self.preset_var = tk.StringVar(value="default")
        preset_combo = ttk.Combobox(preset_frame, textvariable=self.preset_var,
                                    values=list(self.presets.keys()), state="readonly")
        preset_combo.pack(fill=tk.X)
        preset_combo.bind("<<ComboboxSelected>>", self.on_preset_selected)
    
    def create_crop_tab(self, notebook):
        """Create Crop settings tab"""
        frame = ttk.Frame(notebook, padding=15)
        notebook.add(frame, text="CROP")
        
        # Crop options
        crop_frame = ttk.LabelFrame(frame, text="Crop Settings", padding=10)
        crop_frame.pack(fill=tk.X, pady=10)
        
        self.crop_enabled = tk.BooleanVar(value=True)
        ttk.Checkbutton(crop_frame, text="Enable auto crop to artboard",
                       variable=self.crop_enabled).pack(anchor=tk.W, pady=5)
        
        # Crop offset
        offset_frame = tk.Frame(crop_frame, bg="white")
        offset_frame.pack(fill=tk.X, pady=10)
        
        tk.Label(offset_frame, text="Crop Offset:", font=("Segoe UI", 10), bg="white").pack(side=tk.LEFT)
        self.crop_offset = ttk.Spinbox(offset_frame, from_=0, to=20, width=10,
                                       format="%.2f", increment=0.5)
        self.crop_offset.set(0.00)
        self.crop_offset.pack(side=tk.LEFT, padx=5)
        tk.Label(offset_frame, text="mm", font=("Segoe UI", 9), bg="white").pack(side=tk.LEFT)
        
        # Info
        info = tk.Label(frame, text="Crop will remove unwanted content outside\nthe defined bleed area automatically.",
                       font=("Segoe UI", 9), fg="#555", bg="white", justify=tk.LEFT,
                       padx=10, pady=10)
        info.pack(fill=tk.X)
        
        # Preview button
        ttk.Button(frame, text="Preview Crop Area", 
                  command=self.preview_crop).pack(pady=10)
    
    def create_safe_area_tab(self, notebook):
        """Create Safe Area settings tab"""
        frame = ttk.Frame(notebook, padding=15)
        notebook.add(frame, text="SAFE AREA")
        
        # Safe area settings
        safe_frame = ttk.LabelFrame(frame, text="Safe Area Configuration", padding=10)
        safe_frame.pack(fill=tk.X, pady=10)
        
        tk.Label(safe_frame, text="Safe Area Distance from Edge:",
                font=("Segoe UI", 10)).pack(anchor=tk.W, pady=10)
        
        row = tk.Frame(safe_frame, bg="white")
        row.pack(fill=tk.X, pady=5)
        
        self.safe_area = ttk.Spinbox(row, from_=0, to=50, width=15,
                                     format="%.2f", increment=0.5)
        self.safe_area.set(5.00)
        self.safe_area.pack(side=tk.LEFT, padx=5)
        
        tk.Label(row, text="mm", font=("Segoe UI", 9), bg="white").pack(side=tk.LEFT)
        
        # Info
        info = tk.Label(frame, 
                       text="Safe area protects critical content from being cut off.\n" +
                            "Content outside this area may be trimmed during printing.",
                       font=("Segoe UI", 9), fg="#555", justify=tk.LEFT, padx=10, pady=10)
        info.pack(fill=tk.X)
        
        # Visualization
        ttk.Button(frame, text="Show Safe Area Guides",
                  command=self.show_safe_guides).pack(pady=10)
    
    def create_export_tab(self, notebook):
        """Create Export settings tab"""
        frame = ttk.Frame(notebook, padding=15)
        notebook.add(frame, text="EXPORT")
        
        # PDF Export settings
        pdf_frame = ttk.LabelFrame(frame, text="PDF Export Options", padding=10)
        pdf_frame.pack(fill=tk.X, pady=10)
        
        # Quality
        tk.Label(pdf_frame, text="Quality:", font=("Segoe UI", 10)).pack(anchor=tk.W, pady=5)
        self.pdf_quality = ttk.Combobox(pdf_frame,
                                        values=["Screen (72 dpi)", "Medium (150 dpi)", "High (300 dpi)", "Print (600 dpi)"],
                                        state="readonly")
        self.pdf_quality.set("Print (600 dpi)")
        self.pdf_quality.pack(fill=tk.X)
        
        # Include settings
        tk.Label(pdf_frame, text="Include:", font=("Segoe UI", 10)).pack(anchor=tk.W, pady=(10, 5))
        
        self.include_bleed = tk.BooleanVar(value=True)
        ttk.Checkbutton(pdf_frame, text="Include bleed marks",
                       variable=self.include_bleed).pack(anchor=tk.W)
        
        self.include_crop = tk.BooleanVar(value=True)
        ttk.Checkbutton(pdf_frame, text="Include crop marks",
                       variable=self.include_crop).pack(anchor=tk.W)
        
        self.include_safe = tk.BooleanVar(value=False)
        ttk.Checkbutton(pdf_frame, text="Include safe area guides",
                       variable=self.include_safe).pack(anchor=tk.W)
        
        # Color space
        tk.Label(pdf_frame, text="Color Space:", font=("Segoe UI", 10)).pack(anchor=tk.W, pady=(10, 5))
        self.color_space = ttk.Combobox(pdf_frame,
                                       values=["RGB", "CMYK", "Grayscale"],
                                       state="readonly")
        self.color_space.set("CMYK")
        self.color_space.pack(fill=tk.X)
        
        # Export button
        ttk.Button(frame, text="Export to PDF",
                  command=self.export_pdf).pack(pady=20)
    
    def create_bottom_buttons(self):
        """Create bottom action buttons"""
        button_frame = tk.Frame(self.window, bg="#f5f5f5")
        button_frame.pack(fill=tk.X, padx=10, pady=10)
        
        ttk.Button(button_frame, text="Apply Settings",
                  command=self.apply_settings).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(button_frame, text="Reset to Defaults",
                  command=self.reset_defaults).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(button_frame, text="Save Preset",
                  command=self.save_preset).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(button_frame, text="Close",
                  command=self.close).pack(side=tk.RIGHT, padx=5)
    
    def on_preset_selected(self, event=None):
        """Handle preset selection"""
        preset_name = self.preset_var.get()
        if preset_name in self.presets:
            preset = self.presets[preset_name]
            self.bleed_left.delete(0, tk.END)
            self.bleed_left.insert(0, str(preset.get("bleed_left", 2.00)))
            self.bleed_top.delete(0, tk.END)
            self.bleed_top.insert(0, str(preset.get("bleed_top", 2.00)))
            self.bleed_right.delete(0, tk.END)
            self.bleed_right.insert(0, str(preset.get("bleed_right", 2.00)))
            self.bleed_bottom.delete(0, tk.END)
            self.bleed_bottom.insert(0, str(preset.get("bleed_bottom", 2.00)))
    
    def apply_settings(self):
        """Apply current settings"""
        try:
            settings = {
                "bleed_left": float(self.bleed_left.get()),
                "bleed_top": float(self.bleed_top.get()),
                "bleed_right": float(self.bleed_right.get()),
                "bleed_bottom": float(self.bleed_bottom.get()),
                "crop_enabled": self.crop_enabled.get(),
                "safe_area": float(self.safe_area.get())
            }
            self.plugin.apply_bleed(settings)
            messagebox.showinfo("Success", "Settings applied successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to apply settings: {e}")
    
    def preview_crop(self):
        """Preview crop area"""
        messagebox.showinfo("Preview", "Crop area preview will be displayed")
    
    def show_safe_guides(self):
        """Show safe area guides"""
        messagebox.showinfo("Safe Area", "Safe area guides displayed on artboard")
    
    def export_pdf(self):
        """Export to PDF"""
        filepath = filedialog.asksaveasfilename(defaultextension=".pdf",
                                               filetypes=[("PDF files", "*.pdf")])
        if filepath:
            try:
                settings = {
                    "quality": self.pdf_quality.get(),
                    "include_bleed": self.include_bleed.get(),
                    "include_crop": self.include_crop.get(),
                    "include_safe": self.include_safe.get(),
                    "color_space": self.color_space.get()
                }
                self.plugin.export_pdf(filepath, settings)
                messagebox.showinfo("Success", f"PDF exported to {filepath}")
            except Exception as e:
                messagebox.showerror("Error", f"Export failed: {e}")
    
    def save_preset(self):
        """Save current settings as preset"""
        preset_name = tk.simpledialog.askstring("Save Preset", "Enter preset name:")
        if preset_name:
            self.presets[preset_name] = {
                "bleed_left": float(self.bleed_left.get()),
                "bleed_top": float(self.bleed_top.get()),
                "bleed_right": float(self.bleed_right.get()),
                "bleed_bottom": float(self.bleed_bottom.get()),
                "crop_enabled": self.crop_enabled.get(),
                "safe_area": float(self.safe_area.get())
            }
            messagebox.showinfo("Success", f"Preset '{preset_name}' saved!")
    
    def reset_defaults(self):
        """Reset to default values"""
        self.bleed_left.set(2.00)
        self.bleed_top.set(2.00)
        self.bleed_right.set(2.00)
        self.bleed_bottom.set(2.00)
        self.safe_area.set(5.00)
        messagebox.showinfo("Reset", "Settings reset to defaults")
    
    def close(self):
        """Close the panel"""
        if self.window:
            self.window.destroy()
            self.window = None