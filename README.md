# Getting Started with the Canvas API

{ToDo}

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for use with your own API tokens and Canvas domains.

### Prerequisites

1. **Install [Python 3.7 or greater](https://www.python.org/downloads/)**.
2. **Install [Git](https://git-scm.com/downloads)**.

### Installation and execution

1. Clone this repo. `git clone https://github.com/ubccapico/getting-started-with-the-canvas-api-with-python.git`
1. Then cd into the repo. `cd getting-started-with-the-canvas-api-with-python`
1. Run the installation script. `pip install -r requirements.txt` (If you see `bash: pip: command not found`, try using `pip3 install -r requirements.txt`)
1. Generate Canvas API token and copy it to clipboard.
1. Rename the `sample.env` file to `.env`, and add your API token to `CANVAS_API_TOKEN={ADD TOKEN HERE}`.
1. Run the script. `python main.py` (If you see `bash: python: command not found`, try using `python3 main.py`). This should log your Canvas info.

### What to do from here

Write your own code and run it! Be mindful that the API is running on the production Canvas instance - if you want to run against the Beta or Test instance, change the URL in `main.py` to `https://ubc.test.instructure.com` or `http://ubc.beta.instructure.com` and regenerate your token(s) from the Beta/Test site.

## Authors

* **Justin Lee**
https://github.com/justin0022 | justin.lee@ubc.ca
* **Andrew Gardener**
https://github.com/andrew-gardener | andrew.gardener@ubc.ca

## License

This project is licensed under the GPL 3 License.
