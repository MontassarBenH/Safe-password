import random
import string
import xml.etree.ElementTree as ET
import tkinter as tk

def generate_password(length):
    # Define possible characters for the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password using the specified length and characters
    password = ''.join(random.choices(characters, k=length))

    return password

def save_password():
    # Get the website and length inputs from the user
    website = website_entry.get()
    length = int(length_entry.get())

    # Generate a password and save it to the XML file
    password = generate_password(length)
    password_element = ET.Element("password")
    password_element.set("website", website)
    password_element.text = password
    try:
        tree = ET.parse("passwords.xml")
        root = tree.getroot()
    except:
        root = ET.Element("passwords")
    root.append(password_element)
    tree = ET.ElementTree(root)
    tree.write("passwords.xml")

    # Update the output label to show the generated password
    output_label.config(text=f"Generated password for {website}: {password}")

# Create the GUI
root = tk.Tk()
root.title("Password Generator")

website_label = tk.Label(root, text="Website:")
website_label.grid(row=0, column=0)

website_entry = tk.Entry(root)
website_entry.grid(row=0, column=1)

length_label = tk.Label(root, text="Length:")
length_label.grid(row=1, column=0)

length_entry = tk.Entry(root)
length_entry.grid(row=1, column=1)

generate_button = tk.Button(root, text="Generate Password", command=save_password)
generate_button.grid(row=2, column=0, columnspan=2)

output_label = tk.Label(root, text="")
output_label.grid(row=3, column=0, columnspan=2)

root.mainloop()
