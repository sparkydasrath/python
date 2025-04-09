import csv
from typing import List, Dict, Any


def parse_csv(file_path: str) -> List[Dict[str, Any]]:
    """
    Parse a CSV file and return its contents as a list of dictionaries.
    
    Args:
        file_path (str): Path to the CSV file
        
    Returns:
        List[Dict[str, Any]]: List of dictionaries where each dictionary represents a row                              with column headers as keys
    """
    try:
        with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
            # Create a CSV reader object
            csv_reader = csv.DictReader(csvfile)
            
            # Convert the CSV reader to a list of dictionaries
            data = [row for row in csv_reader]
            
            return data
            
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file_path} was not found")
    except Exception as e:
        raise Exception(f"An error occurred while parsing the CSV file: {str(e)}")


def append_to_csv(file_path: str, row_data: Dict[str, Any]) -> None:
    """
    Append a new row to an existing CSV file.
    
    Args:
        file_path (str): Path to the CSV file
        row_data (Dict[str, Any]): Dictionary containing the data to append, where keys 
        match the CSV headers
    """
    try:
        with open(file_path, 'a', newline='', encoding='utf-8') as csvfile:
            # Get the fieldnames from the existing file
            with open(file_path, 'r', newline='', encoding='utf-8') as readfile:
                headers = csv.DictReader(readfile).fieldnames
            
            # Create a CSV writer object
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            
            # Write the new row
            writer.writerow(row_data)
            
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file_path} was not found")
    except Exception as e:
        raise Exception(f"An error occurred while appending to the CSV file: {str(e)}")




