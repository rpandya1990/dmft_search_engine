(function e(t,n,r){function s(o,u){if(!n[o]){if(!t[o]){var a=typeof require=="function"&&require;if(!u&&a)return a(o,!0);if(i)return i(o,!0);var f=new Error("Cannot find module '"+o+"'");throw f.code="MODULE_NOT_FOUND",f}var l=n[o]={exports:{}};t[o][0].call(l.exports,function(e){var n=t[o][1][e];return s(n?n:e)},l,l.exports,e,t,n,r)}return n[o].exports}var i=typeof require=="function"&&require;for(var o=0;o<r.length;o++)s(r[o]);return s})({1:[function(require,module,exports){
var searchForm = require("./searchForm.js"); 
var cols = [
    { key: 'id', label: 'Id' },
    { key: 'userId', label: 'User' },    
    { key: 'title', label: 'Title' },
    { key: 'body', label: 'Body' }
];

var data = [
  {
"userId": 1,
"id": 1,
"title": "Hello tirl",
"body": "m rerum est autem sunt rem eveniet architecto"
  },
  {
    "userId": 1,
    "id": 2,
    "title": "qui est esse",
    "body": "est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla"
  }
];

var Table = React.createClass({displayName: "Table",

render: function() {
    var headerComponents = this.generateHeaders(),
        rowComponents = this.generateRows();

    return (
        React.createElement("div", {class: "table-responsive"}, 
            React.createElement("table", {class: "table"}, 
                React.createElement("thead", null, " ", headerComponents, " "), 
                React.createElement("tbody", null, " ", rowComponents, " ")
            )
        )
    );
},

generateHeaders: function() {
    var cols = this.props.cols;  // [{key, label}]

    // generate our header (th) cell components
    return cols.map(function(colData) {
        return React.createElement("th", {key: colData.key}, " ", colData.label, " ");
    });
},

generateRows: function() {
    var cols = this.props.cols,  // [{key, label}]
        data = this.props.data;

    return data.map(function(item) {
        // handle the column data within each row
        var cells = cols.map(function(colData) {

            // colData.key might be "firstName"
            return React.createElement("td", null, " ", item[colData.key], " ");
        });
        return React.createElement("tr", {key: item.id}, " ", cells, " ");
    });
}
});

ReactDOM.render(React.createElement(Table, {cols: cols, data: data}),  document.getElementById('search'));

},{"./searchForm.js":2}],2:[function(require,module,exports){
var cols = [
    { key: 'path', label: 'Path' },
    { key: 'last_modified', label: 'Last Modified' },    
    { key: 'files', label: 'Files' },
    { key: 'folders', label: 'Folders' },
    { key: 'description', label: 'Description' }
];

class SearchForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = {items: [], searchString: ''};
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
    this.resetSearch = this.resetSearch.bind(this);
  }

  handleChange(event) {
    this.setState({searchString: event.target.value});
  }

  handleSubmit(event) {
    // alert('A name was submitted: ' + this.state.searchString);
    event.preventDefault();
    // this.getMoviesFromApiAsync();
    this.getData();
  }

  resetSearch(event) {
    this.setState({items: [], searchString: ''});
    event.preventDefault();
  }

  getData() {
    if (this.state.searchString.length > 0) {
      var url = "http://localhost:5000/search/" + this.state.searchString;
      fetch(url)
        .then(response => response.json())
        .then(json => {
          this.setState({
            items: json.Data
          });
        });
    }
  }

  generateRows() {
        var cols = this.props.cols,  // [{key, label}]
            data = this.state.items;

        return data.map(function(item) {
            // handle the column data within each row
            var cells = cols.map(function(colData) {

                // colData.key might be "firstName"
                return React.createElement("td", {key: colData.key}, " ", item[colData.key], " ");
            });
            return React.createElement("tr", {key: item.path}, " ", cells, " ");
        });
    }

  generateHeaders() {
    var cols = this.props.cols;  // [{key, label}]

    // generate our header (th) cell components
    return cols.map(function(colData) {
        return React.createElement("th", {key: colData.key}, " ", colData.label, " ");
    });
  }

  render() {
    var headerComponents = this.generateHeaders(),
        rowComponents = this.generateRows();
    return (
      React.createElement("div", null, 
        React.createElement("form", {onSubmit: this.handleSubmit}, 
          React.createElement("input", {className: "resizedTextbox", type: "text", value: this.state.searchString, onChange: this.handleChange, placeholder: "Enter Material to search"}), 
          React.createElement("br", null), 
          React.createElement("br", null), 
          React.createElement("input", {className: "btn btn-primary", type: "submit", value: "Search"}), 
          React.createElement("button", {type: "button", className: "btn btn-primary", onClick: this.resetSearch}, "Reset")
        ), 
        React.createElement("br", null), 
        React.createElement("div", {className: "table-responsive"}, 
            React.createElement("table", {className: "table"}, 
                React.createElement("thead", null, " ", headerComponents, " "), 
                React.createElement("tbody", null, " ", rowComponents, " ")
            )
        )
      )
    );
  }
}

module.exports = SearchForm;

const main = document.getElementById('main');

ReactDOM.render(React.createElement(SearchForm, {cols: cols}), main);

},{}]},{},[1]);
