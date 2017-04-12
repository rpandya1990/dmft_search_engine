class SearchForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = {items: [], searchString: '', showBy: 'DATE', current: ''};
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
    this.handleSubmit();
  }

  handleSubmit(event) {
    event.preventDefault();
    this.setState({current: this.state.showBy});
    this.getData();
  }

  resetSearch(event) {
    this.setState({items: [], searchString: '', showBy: 'DATE', current: ''});
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
      return <td key={item}>
              <img src={item} className="img-thumbnail" width="100px" height="100px"/>
             </td>;
    });
    return <tr> {cells} </tr>;
  }

  generateResult() {
    var data = this.state.items;
    var rowComponents = this.generateRows();
    return data.map(function(item) {
      return  <div key={item.path}>
                <h3>{item.path}</h3>
                Hello, This is sample description
                <br />
                <br />
                <table>
                  {rowComponents}
                </table>
                <br />
                <br />
                <br />
                <br />
              </div>;
    })
  }

  render() {
    var resultComponents = <div><i><b>Showing Results by {this.state.current}: </b> <br /> <br /></i>{this.generateResult()}</div>;
    return (
      <div>
        <div>
          <form onSubmit={this.handleSubmit}>
            <input className="resizedTextbox" type="text" value={this.state.searchString} onChange={this.handleChange} placeholder="Enter Formula"/>
            <div style={{display: "inline-block"}}>
              <select className="selectpicker show-menu-arrow" defaultvalue={this.state.showBy} onChange={this.handleFilterChange}>
                <option value="DATE">Show Most Recent</option>
                <option value="RELEVANCE">Show Most Relevant</option>
              </select>
            </div>
            <br />
            <br />
            <input className="btn btn-primary" type="submit" value="Search" />
            <button type="button" className="btn btn-primary" onClick={this.resetSearch}>Reset</button>
          </form>
          <br />
          <br />
          <br />
        </div>
        <div>
          {resultComponents}
        </div>
      </div>
    );
  }
}

module.exports = SearchForm;

const main = document.getElementById('main');

ReactDOM.render(<SearchForm/>, main);
