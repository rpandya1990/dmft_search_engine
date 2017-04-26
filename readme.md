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


### Todos

 - Error handling in case of invalid keywords
 - 2 element compounds search
 - Tokenization to filter inverted indices
