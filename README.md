# djazz-cli

`djazz-cli` is a Django command-line tool that extends and enhances Django's built-in management commands. It provides a simpler, more intuitive interface through the `dj` command.

## Features

- Simplified project creation with template support
- Enhanced app creation with better defaults
- Shorter, more intuitive command syntax
- Helpful next-step guidance after commands
- Default templates with common configurations

## Installation

Install using pip:

```bash
pip install djazz-cli
```

## Usage

### Creating a New Project

```bash
# Basic project creation (in current directory)
dj startproject myproject

# Create project with a specific template
dj startproject myproject -t custom_template
# or
dj startproject myproject --template custom_template

# Create project in a specific directory
dj startproject myproject -t custom_template -p /path/to/directory
# or
dj startproject myproject --template custom_template --path /path/to/directory
```

### Creating a New App

```bash
# Basic app creation
dj startapp myapp

# Create app with a specific template
dj startapp myapp -t custom_template
# or
dj startapp myapp --template custom_template

# Create app in a specific directory
dj startapp myapp -t custom_template -p /path/to/directory
# or
dj startapp myapp --template custom_template --path /path/to/directory
```

### Listing Available Templates

```bash
# List all templates
dj list-templates

# List only project templates
dj list-templates project

# List only app templates
dj list-templates app
```

## Templates

### Project Templates
- `default`: Enhanced version of Django's default project template

### App Templates
- `default`: Extended app template with additional files (urls.py, etc.)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Development

### Setting Up Development Environment

```bash
# Clone the repository
git clone https://github.com/djazzcc/cli.git
cd cli

# Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate  # On Unix/macOS
# or
.\.venv\Scripts\activate  # On Windows

# Install development dependencies
uv pip install -e .
```

### Local Testing

```bash
# Create a sandbox test environment
mkdir -p sandbox/test1
cd sandbox/test1

# Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate  # On Unix/macOS
# or
.\.venv\Scripts\activate  # On Windows

# Install the package in editable mode (from project root)
cd ../..  # Go back to project root
uv pip install -e .

# Verify installation
uv pip list | grep djazz-cli

# Test the CLI
cd sandbox/test1
dj startproject myproject
```

### Project Structure
```
cli/
├── djazz_cli/
│   ├── __init__.py
│   ├── main.py
│   └── templates/
│       ├── app_templates/
│       │   └── default/
│       └── project_templates/
│           └── default/
├── sandbox/          # For local testing (git ignored)
├── pyproject.toml
├── README.md
└── .gitignore
```

### Building the Package

```bash
# Build both wheel and sdist
uv build

# The built packages will be in the dist/ directory
ls dist/
```

