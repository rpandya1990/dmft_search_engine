(function e(t,n,r){function s(o,u){if(!n[o]){if(!t[o]){var a=typeof require=="function"&&require;if(!u&&a)return a(o,!0);if(i)return i(o,!0);var f=new Error("Cannot find module '"+o+"'");throw f.code="MODULE_NOT_FOUND",f}var l=n[o]={exports:{}};t[o][0].call(l.exports,function(e){var n=t[o][1][e];return s(n?n:e)},l,l.exports,e,t,n,r)}return n[o].exports}var i=typeof require=="function"&&require;for(var o=0;o<r.length;o++)s(r[o]);return s})({1:[function(require,module,exports){
class SearchForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = {items: [], searchString: '', showBy: 'DATE', 'current': ''};
    this.handleChange = this.handleChange.bind(this);
    this.handleFilterChange = this.handleFilterChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
    this.resetSearch = this.resetSearch.bind(this);
  }

  handleChange(event) {
    this.setState({searchString: event.target.value});
  }

  handleFilterChange(event) {
    event.preventDefault();
    this.setState({showBy: event.target.value});
  }

  handleSubmit(event) {
    event.preventDefault();
    this.setState({current: this.state.showBy});
    this.getData();
  }

  resetSearch(event) {
    this.setState({items: [], searchString: ''});
    event.preventDefault();
  }

  getData() {
    if (this.state.searchString.length > 0) {
      var url = "http://localhost:5000/search/" + this.state.searchString + "/" + this.state.showBy;
      console.log(url);
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
    var data = ["https://www.oneblowdrybar.com/wp-content/uploads/2013/05/placeholder2.png",
        "http://ccmmp.ph.qmul.ac.uk/sites/default/files/styles/newsimage/public/newsimages/Perovskite.png?itok=eYV75gwZ",
        "http://news.rice.edu/files/2013/11/1111_ARO-BB.jpg"];
    
    var cells = data.map(function(item) {
      return React.createElement("td", {key: item}, 
              React.createElement("img", {src: item, className: "img-thumbnail", width: "100px", height: "100px"})
             );
    });
    return React.createElement("tr", null, " ", cells, " ");
  }

  generateResult() {
    var data = this.state.items;
    var rowComponents = this.generateRows();
    return data.map(function(item) {
      return  React.createElement("div", {key: item.path}, 
                React.createElement("h3", null, item.path), 
                "Hello, This is sample description", 
                React.createElement("br", null), 
                React.createElement("br", null), 
                React.createElement("table", null, 
                  rowComponents
                ), 
                React.createElement("br", null), 
                React.createElement("br", null), 
                React.createElement("br", null), 
                React.createElement("br", null)
              );
    })
  }

  render() {
    var resultComponents = React.createElement("div", null, React.createElement("i", null, React.createElement("b", null, "Showing Results by ", this.state.current, ": "), " ", React.createElement("br", null), " ", React.createElement("br", null)), this.generateResult());
    return (
      React.createElement("div", null, 
        React.createElement("div", null, 
          React.createElement("form", {onSubmit: this.handleSubmit}, 
            React.createElement("input", {className: "resizedTextbox", type: "text", value: this.state.searchString, onChange: this.handleChange, placeholder: "Enter Formula"}), 
            React.createElement("div", {style: {display: "inline-block"}}, 
              React.createElement("select", {className: "selectpicker show-menu-arrow", defaultvalue: this.state.showBy, onChange: this.handleFilterChange}, 
                React.createElement("option", {value: "DATE"}, "Show Most Recent"), 
                React.createElement("option", {value: "RELEVANCE"}, "Show Most Relevant")
              )
            ), 
            React.createElement("br", null), 
            React.createElement("br", null), 
            React.createElement("input", {className: "btn btn-primary", type: "submit", value: "Search"}), 
            React.createElement("button", {type: "button", className: "btn btn-primary", onClick: this.resetSearch}, "Reset")
          ), 
          React.createElement("br", null), 
          React.createElement("br", null), 
          React.createElement("br", null)
        ), 
        React.createElement("div", null, 
          resultComponents
        )
      )
    );
  }
}

module.exports = SearchForm;

const main = document.getElementById('main');

ReactDOM.render(React.createElement(SearchForm, null), main);

},{}]},{},[1]);
