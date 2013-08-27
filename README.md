# status2xively

Small script that pushes the RZL status to Xively. It also takes care of the bank balance and the member count.


## Requirements
* Python
* Webserver with PHP
* Some old version of python-eeml


## Installation
1. Clone repo
2. Copy `htdocs` folder content to some place where it's made accessible on the web.
3. Make sure, `data.json`is writeable by your webserver.
4. Modify path to `data.json` inside `status2xively.py`.
5. Enter Xively API key in `config.py`, which is created by copying `config.py.sample`.
6. Edit your crontab to include the following line: `*/1 * * * * /<path to the status2xively folder>/status2xively.py >> /<path to the status2xively folder>/update.log`
7. Test some values for the bank balance and member count.
8. Protect the webfrontend using .htaccess, and some other fancy auth stuff.
