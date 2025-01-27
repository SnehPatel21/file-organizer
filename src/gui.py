"""GUI interface for File Organizer."""

import threading
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

from .organizer import FileOrganizer


class FileOrganizerGUI:
    """GUI class for File Organizer."""

    def __init__(self, root):
        """Initialize GUI."""
        self.root = root
        self.root.title("File Organizer")
        self.root.geometry("600x400")

        # Configure style
        self.style = ttk.Style()
        self.style.theme_use("clam")

        self.setup_ui()

    def setup_ui(self):
        """Set up the user interface."""
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Source Directory Selection
        ttk.Label(main_frame, text="Select Directory:").grid(
            row=0, column=0, sticky=tk.W, pady=5
        )

        self.dir_entry = ttk.Entry(main_frame, width=50)
        self.dir_entry.grid(row=1, column=0, padx=5)

        browse_btn = ttk.Button(
            main_frame, text="Browse", command=self.browse_directory
        )
        browse_btn.grid(row=1, column=1, padx=5)

        # Progress Bar
        self.progress = ttk.Progressbar(main_frame, length=400, mode="indeterminate")
        self.progress.grid(row=2, column=0, columnspan=2, pady=20)

        # Status Text
        self.status_text = tk.Text(main_frame, height=10, width=50)
        self.status_text.grid(row=3, column=0, columnspan=2, pady=5)
        self.status_text.config(state=tk.DISABLED)

        # Organize Button
        self.organize_btn = ttk.Button(
            main_frame, text="Organize Files", command=self.start_organizing
        )
        self.organize_btn.grid(row=4, column=0, columnspan=2, pady=10)

    def browse_directory(self):
        directory = filedialog.askdirectory()
        if directory:
            self.dir_entry.delete(0, tk.END)
            self.dir_entry.insert(0, directory)

    def update_status(self, message):
        self.status_text.config(state=tk.NORMAL)
        self.status_text.insert(tk.END, message + "\n")
        self.status_text.see(tk.END)
        self.status_text.config(state=tk.DISABLED)

    def start_organizing(self):
        directory = self.dir_entry.get()
        if not directory:
            messagebox.showerror("Error", "Please select a directory first!")
            return

        # Disable buttons during organization
        self.organize_btn.config(state=tk.DISABLED)
        self.progress.start()
        self.update_status("Starting organization...")

        # Run organization in separate thread
        thread = threading.Thread(target=self.organize_files, args=(directory,))
        thread.daemon = True
        thread.start()

    def organize_files(self, directory):
        try:
            organizer = FileOrganizer(directory)
            summary = organizer.organize()

            # Update GUI with results
            self.root.after(0, self.organization_complete, summary)

        except Exception as e:
            self.root.after(0, self.show_error, str(e))

    def organization_complete(self, summary):
        self.progress.stop()
        self.organize_btn.config(state=tk.NORMAL)

        # Show summary
        self.update_status("\nOrganization Complete!")
        self.update_status("\nSummary:")
        for category, files in summary.items():
            if files:
                self.update_status(f"\n{category}:")
                for file in files:
                    self.update_status(f"  - {file}")

        messagebox.showinfo("Success", "Files have been organized successfully!")

    def show_error(self, error_message):
        self.progress.stop()
        self.organize_btn.config(state=tk.NORMAL)
        messagebox.showerror("Error", f"An error occurred: {error_message}")


def main():
    """Launch the GUI application."""
    root = tk.Tk()
    # Store app in root to prevent garbage collection
    root.app = FileOrganizerGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
