# DMFT Search Engine
![Logo](https://raw.githubusercontent.com/rpandya1990/dmft_search_engine/master/Images/Logo.JPG)

Search Engine to query files/folders based on chemical compounds.

  - Keyword based on chemical formula
  - Front end using React.js
  - Python-Flask server driving the backend
---
### Installation


Requires [Node.js](https://nodejs.org/), [NPM](https://docs.npmjs.com/cli/install) and [bower](https://bower.io/) to run.

Install the dependencies and devDependencies and start the server.

```sh
$ pip install -r requirements.txt
$ npm install
$ bower install    or bower install --allow-root```    when running with root user
```
---
### Run
* Watch for changes and jsx to js transformation
    ```sh
    $ gulp
    ```
* Run Flask server
    ```sh
    $ sh run.sh
    ```
### Deploy
- Follow the instructions above to install dependencies and configure python virtual environment(should be installed in ```/opt```)
- Copy the application directory under ```/var/www/```
- Under the project directory, create ```dmft_search.wsgi``` and paste following contents:
    ```
    #!/usr/bin/python
    activate_this = '/opt/dmft/bin/activate_this.py' # Path to venv
    execfile(activate_this, dict(__file__=activate_this))
    import sys
    import logging
    logging.basicConfig(stream=sys.stderr)
    sys.path.insert(0,"/var/www/dmft_search_engine/dmft_search")
    
    from app import app as application
    ```
- Configure the virtual apache host
    - Go to ```/etc/apache2/sites-available```, create ```dmft_search.conf``` and paste following contents:
        ```
        <VirtualHost *:80>
                        ServerName      search_engine.com
                        WSGIScriptAlias / /var/www/dmft_search_engine/dmft_search.wsgi
                        <Directory /var/www/dmft_search_engine/dmft_search/>
                                Order allow,deny
                                Allow from all
                        </Directory>
                        Alias /static /var/www/dmft_search_engine/dmft_search/static
                        <Directory /var/www/dmft_search_engine/dmft_search/static/>
                                Order allow,deny
                                Allow from all
                        </Directory>
                        ErrorLog ${APACHE_LOG_DIR}/error.log
                        LogLevel warn
                        CustomLog ${APACHE_LOG_DIR}/access.log combined
        </VirtualHost>
        ```
    - Replace the server name with the actual domain name
    - Enable the site: ```sudo a2ensite dmft_search.conf```
    - Restart apache: ```service apache2 reload```
- Go to application root in ```\var\www\``` and run ```$ gulp```



### Todos

 - Error handling in case of invalid keywords
 - Classifier implementation to further reduce candidates in filesystem dump
