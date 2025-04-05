
# john-doe-genai-python-basics-2025-04-06.mp4


import os
from datetime import datetime, timedelta

def batch_rename_files(directory):
    # Set the author name
    author = "john-doe"
    
    # Set the future date (current date + 3 years)
    future_date = (datetime.now() + timedelta(days=3*365)).strftime("%Y-%m-%d")
    
    # Iterate through files in directory
    for filename in os.listdir(directory):
        # Skip if it's not a file
        if not os.path.isfile(os.path.join(directory, filename)):
            continue
            
        # Skip if it's this script itself
        if filename == os.path.basename(__file__):
            continue
            
        # Get file extension
        name, ext = os.path.splitext(filename)
        
        # Create new filename
        new_filename = f"{author}-{name}-{future_date}{ext}"
        
        # Rename the file
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
        print(f"Renamed: {filename} -> {new_filename}")

# from ChatGPT
def rename_mp4_files(directory, username="john-doe", date_str=None):
    """
    Renames all .mp4 files in the given directory to the format:
    username-originalname-date.mp4

    Parameters:
    - directory (str): Path to the folder
    - username (str): Name to prefix (default: 'john-doe')
    - date_str (str): Date in YYYY-MM-DD format (default: today)
    """
    if date_str is None:
        date_str = datetime.today().strftime('%Y-%m-%d')

    for filename in os.listdir(directory):
        if filename.endswith('.mp4'):
            base_name = os.path.splitext(filename)[0]
            new_name = f"{username}-{base_name}-{date_str}.mp4"
            src = os.path.join(directory, filename)
            dst = os.path.join(directory, new_name)
            os.rename(src, dst)
            print(f"Renamed: {filename} → {new_name}")




