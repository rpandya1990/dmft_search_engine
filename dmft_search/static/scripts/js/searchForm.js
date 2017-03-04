(function e(t,n,r){function s(o,u){if(!n[o]){if(!t[o]){var a=typeof require=="function"&&require;if(!u&&a)return a(o,!0);if(i)return i(o,!0);var f=new Error("Cannot find module '"+o+"'");throw f.code="MODULE_NOT_FOUND",f}var l=n[o]={exports:{}};t[o][0].call(l.exports,function(e){var n=t[o][1][e];return s(n?n:e)},l,l.exports,e,t,n,r)}return n[o].exports}var i=typeof require=="function"&&require;for(var o=0;o<r.length;o++)s(r[o]);return s})({1:[function(require,module,exports){
class SearchForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = {items: [], searchString: ''};
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.setState({searchString: event.target.value});
  }

  getMoviesFromApiAsync() {
    fetch("https://facebook.github.io/react-native/movies.json")
      .then(response => response.json())
      .then(json => {
        console.log(json);
        this.setState({
          items: json.movies
        });
      });
  }

  handleSubmit(event) {
    // alert('A name was submitted: ' + this.state.searchString);
    // event.preventDefault();
    this.getMoviesFromApiAsync();
  }

  render() {
    return (
      React.createElement("div", null, 
        React.createElement("form", {onSubmit: this.handleSubmit.bind(this)}, 
          React.createElement("input", {type: "text", value: this.state.searchString, onChange: this.handleChange.bind(this)}), 
          React.createElement("input", {type: "submit", value: "Search"})
        )
      )
    );
  }
}


const main = document.getElementById('main');

ReactDOM.render(React.createElement(SearchForm, {dataURL: "https://facebook.github.io/react-native/movies.json"}), main);

},{}]},{},[1]);
