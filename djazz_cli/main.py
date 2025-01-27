# djazz_cli/main.py
# 2025-01-27
# Azat (@azataiot)

import os
import sys
from pathlib import Path
import shutil
import tempfile

import typer
from django.core import management
from typing import Optional

app = typer.Typer(
    name="dj",
    help="Django CLI tool that extends django-admin functionality",
    add_completion=True,
)

# ------------
# startproject
# dj startproject <project_name> [project_template_name] [path] which is the same as django-admin startproject <project_name> [project_template_name] [path]
# ------------

@app.command()
def startproject(
    project_name: str,
    template: str = typer.Option("default", "--template", "-t", help="Template to use"),
    path: Path | None = typer.Option(None, "--path", "-p", help="Path where project should be created"),
):
    """
    Create a new Django project with an optional template.
    
    Args:
        project_name: Name of the project
        template: Template to use (default: "default")
        path: Path where project should be created (default: current directory)
    """
    if path is None:
        path = Path.cwd()
    
    typer.echo(f"Creating project {project_name}")
    
    # Prepare arguments for django-admin startproject
    argv = ["django-admin", "startproject", project_name]
    
    # Create a temporary directory for the template
    with tempfile.TemporaryDirectory() as temp_dir:
        template_path = Path(__file__).parent / "templates" / "project_templates" / template
        if not template_path.exists():
            typer.echo(typer.style(
                f"Error: Template '{template}' not found.",
                fg=typer.colors.RED
            ))
            typer.echo("\nAvailable project templates:")
            list_templates("project")
            sys.exit(1)
        
        # Copy template to temp directory, excluding description files
        temp_template = Path(temp_dir) / "template"
        shutil.copytree(template_path, temp_template, ignore=lambda x, y: {'description.txt', 'README.md'})
        
        # Use the cleaned template
        argv.extend(["--template", str(temp_template)])
        
        if path:
            argv.append(str(path))
        
        try:
            # Set the current working directory
            os.chdir(str(path))
            
            # Execute django-admin startproject
            management.execute_from_command_line(argv)
            
            typer.echo(typer.style(
                f"✨ Successfully created project {project_name}!",
                fg=typer.colors.GREEN,
                bold=True
            ))
            
            # Show next steps based on path
            typer.echo("\nNext steps:")
            if path != Path.cwd():
                typer.echo(f"  cd {project_name}")
            typer.echo("  python manage.py migrate")
            typer.echo("  python manage.py runserver")
            
        except Exception as e:
            typer.echo(typer.style(
                f"Error creating project: {e!s}",
                fg=typer.colors.RED,
                bold=True
            ))
            sys.exit(1)

# ------------
# startapp
# dj startapp <app_name> [app_template_name] [path]
# ------------

@app.command()
def startapp(
    app_name: str,
    template: str = typer.Option("default", "--template", "-t", help="Template to use"),
    path: Path | None = typer.Option(None, "--path", "-p", help="Path where app should be created"),
):
    """
    Create a new Django app with an optional template.
    
    Args:
        app_name: Name of the app
        template: Template to use (default: "default")
        path: Path where app should be created (default: current directory)
    """
    if path is None:
        path = Path.cwd()
    
    typer.echo(f"Creating app {app_name}")
    
    # Create a temporary directory for the template
    with tempfile.TemporaryDirectory() as temp_dir:
        # Prepare arguments for django-admin startapp
        argv = ["django-admin", "startapp", app_name]
        
        template_path = Path(__file__).parent / "templates" / "app_templates" / template
        if not template_path.exists():
            typer.echo(typer.style(
                f"Error: Template '{template}' not found.",
                fg=typer.colors.RED
            ))
            typer.echo("\nAvailable app templates:")
            list_templates("app")
            sys.exit(1)
        
        # Copy template to temp directory, excluding description files
        temp_template = Path(temp_dir) / "template"
        shutil.copytree(template_path, temp_template, ignore=lambda x, y: {'description.txt', 'README.md'})
        
        # Use the cleaned template
        argv.extend(["--template", str(temp_template)])
        
        # Create app directory
        app_dir = path / app_name
        if not app_dir.exists():
            app_dir.mkdir(parents=True)
        
        # Add path if provided
        argv.append(str(app_dir))
        
        try:
            # Execute django-admin startapp
            management.execute_from_command_line(argv)
            
            typer.echo(typer.style(
                f"✨ Successfully created app {app_name}!",
                fg=typer.colors.GREEN,
                bold=True
            ))
            
            # Show next steps
            typer.echo("\nNext steps:")
            typer.echo("1. Add your app to INSTALLED_APPS in settings.py:")
            typer.echo(f"   INSTALLED_APPS += ['{app_name}']")
            typer.echo(f"2. Create your models in {app_name}/models.py")
            typer.echo(f"3. Create your views in {app_name}/views.py")
            typer.echo("4. Run migrations:")
            typer.echo("   python manage.py makemigrations")
            typer.echo("   python manage.py migrate")
            
        except Exception as e:
            typer.echo(typer.style(
                f"Error creating app: {e!s}",
                fg=typer.colors.RED,
                bold=True
            ))
            sys.exit(1)

# ------------
# list-templates
# dj list-templates [project|app]
# ------------

@app.command()
def list_templates(
    template_type: str = typer.Argument(
        None,
        help="Type of templates to list: 'project' or 'app'",
    )
):
    """
    List available templates for projects or apps.
    
    If template_type is not provided, lists both project and app templates.
    """
    templates_dir = Path(__file__).parent / "templates"
    
    def list_template_dir(template_type: str):
        template_dir = templates_dir / f"{template_type}_templates"
        if not template_dir.exists():
            typer.echo(f"No {template_type} templates directory found.")
            return
        
        templates = [d.name for d in template_dir.iterdir() if d.is_dir()]
        if templates:
            typer.echo(typer.style(f"\n{template_type.title()} Templates:", bold=True))
            for template in sorted(templates):
                typer.echo(f"  • {template}")
        else:
            typer.echo(f"No {template_type} templates available.")
    
    if template_type:
        if template_type.lower() not in ['project', 'app']:
            typer.echo(typer.style(
                "Error: Template type must be either 'project' or 'app'",
                fg=typer.colors.RED
            ))
            raise typer.Exit(1)
        list_template_dir(template_type.lower())
    else:
        # List both project and app templates
        list_template_dir("project")
        list_template_dir("app")
