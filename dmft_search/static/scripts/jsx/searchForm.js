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
                return <td key={colData.key}> {item[colData.key]} </td>;
            });
            return <tr key={item.id}> {cells} </tr>;
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
        <form onSubmit={this.handleSubmit.bind(this)}>
          <input type="text" value={this.state.searchString} onChange={this.handleChange.bind(this)} />
          <input type="submit" value="Search" />
        </form>
        <br />
        <div class="table-responsive">
            <table class="table">
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

ReactDOM.render(<SearchForm cols={cols} dataURL="https://facebook.github.io/react-native/movies.json"/>, main);
