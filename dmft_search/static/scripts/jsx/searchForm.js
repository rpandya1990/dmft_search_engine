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
      <div>
        <form onSubmit={this.handleSubmit.bind(this)}>
          <input type="text" value={this.state.searchString} onChange={this.handleChange.bind(this)} />
          <input type="submit" value="Search" />
        </form>
      </div>
    );
  }
}


const main = document.getElementById('main');

ReactDOM.render(<SearchForm dataURL="https://facebook.github.io/react-native/movies.json"/>, main);
