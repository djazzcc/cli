# djazz_cli/main.py
# 2025-01-27
# Azat (@azataiot)

import os
import sys
from pathlib import Path

import typer
from django.core import management

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
    template_name: str | None = None,
    path: Path | None = None,
):
    """
    Create a new Django project with an optional template.
    
    If path is not provided, creates the project in the current directory.
    """
    if path is None:
        path = Path.cwd()

    typer.echo(f"Creating project {project_name}")

    # Prepare arguments for django-admin startproject
    argv = ["django-admin", "startproject", project_name]

    # Add template if provided
    if template_name:
        template_path = str(Path(__file__).parent / "templates" / "project_templates" / template_name)
        typer.echo(f"Using template: {template_name}")
        argv.extend(["--template", template_path])
    else:
        # Use default template
        template_path = str(Path(__file__).parent / "templates" / "project_templates" / "default")
        argv.extend(["--template", template_path])

    # Add path if provided
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
    template_name: str | None = None,
    path: Path | None = None,
):
    """
    Create a new Django app with an optional template.
    
    If path is not provided, creates the app in the current directory.
    """
    if path is None:
        path = Path.cwd()

    typer.echo(f"Creating app {app_name}")

    # Prepare arguments for django-admin startapp
    argv = ["django-admin", "startapp", app_name]

    # Add template if provided
    if template_name:
        template_path = str(Path(__file__).parent / "templates" / "app_templates" / template_name)
        typer.echo(f"Using template: {template_name}")
        argv.extend(["--template", template_path])
    else:
        # Use default template
        template_path = str(Path(__file__).parent / "templates" / "app_templates" / "default")
        argv.extend(["--template", template_path])

    # Add path if provided
    if path:
        argv.append(str(path))

    try:
        # Set the current working directory
        os.chdir(str(path))

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
