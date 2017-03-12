var cols = [
    { key: 'path', label: 'Path' },
    { key: 'last_Modified', label: 'Last Modified' },    
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
                return <td key={colData.key}> {item[colData.key]} </td>;
            });
            return <tr key={item.path}> {cells} </tr>;
        });
    }

  generateHeaders() {
    var cols = this.props.cols;  // [{key, label}]

    // generate our header (th) cell components
    return cols.map(function(colData) {
        return <th key={colData.key}> {colData.label} </th>;
    });
  }

  render() {
    var headerComponents = this.generateHeaders(),
        rowComponents = this.generateRows();
    return (
      <div>
        <form onSubmit={this.handleSubmit}>
          <input className="resizedTextbox" type="text" value={this.state.searchString} onChange={this.handleChange} placeholder="Enter Material to search"/>
          <br />
          <br />
          <input className="btn btn-primary" type="submit" value="Search" />
          <button type="button" className="btn btn-primary" onClick={this.resetSearch}>Reset</button>
        </form>
        <br />
        <div className="table-responsive">
            <table className="table">
                <thead> {headerComponents} </thead>
                <tbody> {rowComponents} </tbody>
            </table>
        </div>
      </div>
    );
  }
}

module.exports = SearchForm;

const main = document.getElementById('main');

ReactDOM.render(<SearchForm cols={cols}/>, main);
