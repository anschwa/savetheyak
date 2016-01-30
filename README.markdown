# SaveTheYak

[SaveTheYak](https://anschwa.github.io/savetheyak)

A yak friendly redesign of [KillTheYak](http://killtheyak.com), a wonderful website created by [Steven Loria](http://stevenloria.com/)

> You see, yak shaving is what you are doing when you're doing some stupid, fiddly little task that bears no obvious relationship to what you're supposed to be working on, but yet a chain of twelve causal relations links what you're doing to the original meta-task.

<cite>- Jeremy H. Brown</cite>

Save The Yak is a website with guides that will reduce the time you spend yak shaving.

## Contribute content

If you are interested in contributing content, see the [killtheyak-pages][] repo.

## Hacking

Save The Yak is a small Flask app that uses [Flask-FlatPages](https://github.com/SimonSapin/Flask-FlatPages) and [Frozen-Flask](https://github.com/SimonSapin/Frozen-Flask) to build the static content. The app itself lives in the [savetheyak/ directory](https://github.com/anschwa/savetheyak/tree/master/savetheyak). Feel free to use, modify, or just browse around.

### Setting up

Clone the repo

```
$ git clone https://github.com/anschwa/savetheyak.git --recursive
```

The `--recursive` option clones the `killtheyak-pages` submodule.

Install the necessary Python packages (requires Python 2.7 or 3.4.n with pip):

```
# After activating your virtualenv
$ pip install -r requirements.txt
```

### Building the site

To run the local development server

```
$ python manage.py runserver
```

You can browse to `http://localhost:5000/` to view the site.

To build the static version of the site:

```
$ python manage.py build
```

This will build the static site to the `build/` directory.

### Deployment

To deploy to GitHub Pages:

```
$ python manage.py deploy
```

This will build the site, commit to the `master` branch, and push to GitHub.

## License

Copyrights to the guides are owned by their original authors and are licensed under the [Creative Commons Attribution-Share-Alike license][CC-SA].  The website is licensed under the [MIT License][].

[SaveTheYak](https://anschwa.github.io/savetheyak)
[KillTheYak]: http://killtheyak.com
[killtheyak-pages]: https://github.com/killtheyak/killtheyak-pages
[MIT License]: https://github.com/anschwa/savetheyak/blob/master/LICENSE
[CC-SA]: https://creativecommons.org/licenses/by-sa/3.0/legalcode
