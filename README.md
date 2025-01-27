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
dj startproject myproject template_name

# Create project in a specific directory
dj startproject myproject template_name path/to/directory
```

### Creating a New App

```bash
# Basic app creation
dj startapp myapp

# Create app with a specific template
dj startapp myapp template_name

# Create app in a specific directory
dj startapp myapp template_name path/to/directory
```

## Motivation

The `django-admin` CLI is a powerful tool for managing Django projects, but it has some limitations:

1. The default app template lacks common files like `urls.py`
2. Project creation always creates a nested directory structure
3. Template usage requires verbose command-line options

`djazz-cli` addresses these issues by:
- Providing better default templates
- Simplifying the command interface
- Creating projects in the current directory by default
- Making template usage more straightforward

## Templates

### Project Templates
- `default`: Enhanced version of Django's default project template

### App Templates
- `default`: Extended app template with additional files (urls.py, etc.)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

