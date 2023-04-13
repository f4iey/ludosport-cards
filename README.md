# Ludosport Cards

This project allows to create a web page containing customizable *cards* to describe ludosport movements.
It uses Python and Jinja2 templates.

## Install

~~### Docker~~
~~You can pull the Docker image directly form this repository:~~
~~```sh~~
~~docker pull ghcr.io/f4iey/ludosport-cards:latest~~
~~```~~
~~It comes with every needed dependencies installed.~~

### From source

#### Prerequisites
First, you need Python to be installed on ytou system and be sure to get `Jinja2` library
```sh
pip install jinja2
```
Then, you can proceed cloning the repository
```sh
git clone https://github.com/f4iey/ludosport-cards.git
```

## Configuration
To generate the web page template, you will need to create at least one JSON config file in the same directory as `cards.py`
The configuration file has to look like this:
```json
{
    "name": "Move name",
    "media": "Thumbnail",
    "form": "[1-6]",
    "croce": "[first-second]",
    "ligatura": "[first-second]",
    "dir": "direction",
    "way": "trajectory",
    "moveType": "blocage",
    "touch": "touch type (e.g toco/taglio/splinta...)",
    "zone": "saber hit zone (debole/medio/forte...)",
    "target": "Body part to target",
    "desc": "Additionnal info"
}
```
If you are new to JSON files, you can also use `vijson.py` to edit your configuration in a more interactive way

## Generate template
Once your config files are present, the only thing needed is to run
```sh
python cards.py
```
It will automatically pick every JSON files in the current directory and generate a HTML file called `index.html`
