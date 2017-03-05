(function e(t,n,r){function s(o,u){if(!n[o]){if(!t[o]){var a=typeof require=="function"&&require;if(!u&&a)return a(o,!0);if(i)return i(o,!0);var f=new Error("Cannot find module '"+o+"'");throw f.code="MODULE_NOT_FOUND",f}var l=n[o]={exports:{}};t[o][0].call(l.exports,function(e){var n=t[o][1][e];return s(n?n:e)},l,l.exports,e,t,n,r)}return n[o].exports}var i=typeof require=="function"&&require;for(var o=0;o<r.length;o++)s(r[o]);return s})({1:[function(require,module,exports){
var cols = [
    { key: 'id', label: 'Id' },
    { key: 'owner', label: 'Owner' },    
    { key: 'path', label: 'Path' },
    { key: 'description', label: 'Description' }
];

class SearchForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = {items: [], searchString: ''};
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.setState({searchString: event.target.value});
    console.log(this.state.items);
  }

  handleSubmit(event) {
    // alert('A name was submitted: ' + this.state.searchString);
    // event.preventDefault();
    // this.getMoviesFromApiAsync();
    console.log(this.state.searchString);
    this.getData();
  }

  getData() {
    fetch("http://localhost:5000/search")
      .then(response => response.json())
      .then(json => {
        console.log("Inside request: ");
        console.log(json.Data);
        this.setState({
          items: json.Data
        });
        console.log("after copy to state");
        console.log(this.state.items);
      });
  }

  generateRows() {
        var cols = this.props.cols,  // [{key, label}]
            data = this.state.items;
        console.log("Inside functions");
        console.log(data);
            // console.log(data);

        return data.map(function(item) {
            // handle the column data within each row
            var cells = cols.map(function(colData) {

                // colData.key might be "firstName"
                return React.createElement("td", {key: colData.key}, " ", item[colData.key], " ");
            });
            return React.createElement("tr", {key: item.id}, " ", cells, " ");
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
        React.createElement("form", {onSubmit: this.handleSubmit.bind(this)}, 
          React.createElement("input", {type: "text", value: this.state.searchString, onChange: this.handleChange.bind(this)}), 
          React.createElement("input", {type: "submit", value: "Search"})
        ), 
        React.createElement("br", null), 
        React.createElement("div", {class: "table-responsive"}, 
            React.createElement("table", {class: "table"}, 
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

ReactDOM.render(React.createElement(SearchForm, {cols: cols, dataURL: "https://facebook.github.io/react-native/movies.json"}), main);

},{}]},{},[1]);
