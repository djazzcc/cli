# cli
`djazz-cli` provides some extention to the django management commands and provides a `dj` command line utility.


`djazz-cli` provides one `dj` command line tool. which is an extention and sometimes replacement for some of the `django-admin` cli. 

## Motivation 

The `django-admin` cli is a powerful tool for managing django projects. But it has some limitations, for example the default app template dose not have the `urls.py` file. And we might want to have a better way to create the project and app based on the tempaltes. The django-admin cli provides a way to use the templates, which receives a --template option. This cli provides an easier, shorter and more intuitive way to create the project and app based on the templates. 

## Usage 

```bash
dj startproject <project_name> [project_template_name] [path]
```

This command will create a new django project with the name `<project_name>` and the template `<project_template_name>`. If the template name is not provided, the default template will be used. 
A notable difference between the `django-admin startproject` and the `dj startproject` is that the `dj startproject` command will create the project in the current directory by default, unless a path is provided. 

