import tkinter as tk
from tkinter import ttk
import webbrowser

def add_url():
    url = url_entry.get()
    if url:
        with open("youtube_urls.txt", "a") as file:
            file.write(url + "\n")
        url_entry.delete(0, tk.END)
        refresh_library()

def view_urls():
    url_listbox.delete(0, tk.END)
    with open("youtube_urls.txt", "r") as file:
        urls = file.readlines()
        for i, url in enumerate(urls, start=1):
            url_listbox.insert(tk.END, f"Website {i}:  {url.strip()}")

def delete_url():
    selected_index = url_listbox.curselection()
    if selected_index:
        index = selected_index[0]
        url_listbox.delete(index)
        with open("youtube_urls.txt", "r") as file:
            urls = file.readlines()
        with open("youtube_urls.txt", "w") as file:
            for i, url in enumerate(urls):
                if i != index:
                    file.write(url)
        refresh_library()

def on_url_click(event):
    selected_url = url_listbox.get(url_listbox.curselection())
    if selected_url:
        url = selected_url.split(": ", 1)[1]
        webbrowser.open(url)

def refresh_library():
    view_urls()
    num_urls_label.config(text=f"Total Bookmarks: {url_listbox.size()}")

# Create the GUI
root = tk.Tk()
root.title("Website Bookmark Storage")

url_frame = ttk.Frame(root)
url_label = ttk.Label(url_frame, text="Enter Website URL:")
url_label.pack(side=tk.LEFT, padx=5)
url_entry = ttk.Entry(url_frame, width=int(60 * 1.25))  # Increased the width of the entry field by 25%
url_entry.pack(side=tk.LEFT, padx=5)
add_button = ttk.Button(url_frame, text="Add", command=add_url)
add_button.pack(side=tk.LEFT, padx=5)
url_frame.pack()

view_frame = ttk.Frame(root)
view_button = ttk.Button(view_frame, text="View Bookmarks", command=view_urls)
view_button.pack(side=tk.LEFT, padx=5)
delete_button = ttk.Button(view_frame, text="Delete Selected Bookmark", command=delete_url)
delete_button.pack(side=tk.LEFT, padx=5)
view_frame.pack()

url_listbox = tk.Listbox(root, width=70)
url_listbox.pack(pady=10)
url_listbox.bind("<Double-Button-1>", on_url_click)  # Make the URLs clickable

num_urls_label = ttk.Label(root, text="Total Bookmarks: 0")
num_urls_label.pack(pady=5)

# Initial view
refresh_library()

root.mainloop()
