"""
allow you to create isolated and independent environments for different Python projects.
Virtual environments help manage dependencies and avoid conflicts between project requirements.

Why Use Virtual Environments?

In Python, different projects may require different versions of libraries or dependencies.
Using a virtual environment allows you to keep each project isolated,
so changes made to one project's dependencies do not affect other projects.
"""

# Creating a Virtual Environment
"""
Python 3 comes with the venv module, which allows you to create virtual environments.

Example 1: Creating a Virtual Environment Open your command line or terminal, navigate to your project's directory, and run the following command:

`python -m venv myenv`

This will create a new virtual environment named `myenv` in your project directory.
"""

# Activating the Virtual Environment

"""
After creating a virtual environment, you need to activate it to start using it.

On Windows: `myenv\Scripts\activate`

On macOS/Linux: `source myenv/bin/activate`

When the virtual environment is activated, 
you'll see the environment's name in your command prompt.
"""

# Installing Libraries in the Virtual Environment

"""
Example 2: Installing a Library in the Virtual Environment

`pip install library_name`

"""

# Deactivating the Virtual Environment
"""
To deactivate the virtual environment and return to the system's Python environment, use the deactivate command.

Example 3: Deactivating the Virtual Environment

`deactivate`

"""
