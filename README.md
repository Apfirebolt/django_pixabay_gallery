# Django Project Template

The clean, fast and right way to start a new Django `4.2` powered website.

## Getting Started

Setup project environment with [virtualenv](https://virtualenv.pypa.io) and [pip](https://pip.pypa.io).

```bash
$ virtualenv project-env
$ source project-env/bin/activate
$ pip install -r https://raw.githubusercontent.com/juanifioren/django-project-template/master/requirements.txt

# You may want to change the name `projectname`.
$ django-admin startproject --template https://github.com/juanifioren/django-project-template/archive/master.zip projectname

$ cd projectname/
$ cp settings_custom.py.edit settings_custom.py
$ python manage.py migrate
$ python manage.py runserver
```

## Tailwind CSS installation through CLI

`
curl -sLO https://github.com/tailwindlabs/tailwindcss/releases/latest/download/tailwindcss-macos-x64
chmod +x tailwindcss-macos-x64
mv tailwindcss-macos-x64 tailwindcss
`

`
chmod +x tailwindcss
`

`
./tailwindcss -i ./static/css/input.css -o ./static/css/output.css --minify
`
## Features

* Basic Django scaffolding (commands, templatetags, statics, media files, etc).
* Split settings in two files. `settings_custom.py` for specific environment settings (localhost, production, etc). `projectname/settings.py` for core settings.
* Simple logging setup ready for production envs.

## Contributing

I love contributions, so please feel free to fix bugs, improve things, provide documentation. Just send a pull request.