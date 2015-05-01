casework-html-prototypes
========================

not run this yet - just getting started

-------------

html-prototypes is a [Flask](http://flask.pocoo.org/) application, with [Grunt](http://gruntjs.com/) workflow to generate assets.


## Requirements

### [Node](http://nodejs.org/)

You may already have it, try:

```
node --version
```

Your version needs to be at least v0.10.0.

### Grunt

Make sure you've installed the Grunt command line interface --- see http://gruntjs.com/getting-started

### The Sass ruby gem

You probably already have Ruby installed, try

```
ruby -v
```

When you've confirmed you have Ruby installed, run ```gem install sass``` to install Sass.


## Getting started

### Stand alone

pip install -r requirements.txt

python app/server.py

or

source run_dev.sh

### In Development Environment (from upstream master)

Get hold of the [development environment](https://github.com/LandRegistry/development-environment) and get it running :)

Then in a new tab:

* Ensure you’ve cd’ed into the html-prototypes folder, then ```npm install``` to install dependencies.
* To have sass files watched: ```grunt```

Off you go.


