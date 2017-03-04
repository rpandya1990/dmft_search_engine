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

  handleSubmit(event) {
    // alert('A name was submitted: ' + this.state.searchString);
    // event.preventDefault();

  }

  render() {
    return (
      <div>
        <form onSubmit={this.handleSubmit}>
          <input type="text" value={this.state.searchString} onChange={this.handleChange} />
          <input type="submit" value="Search" />
          <ul>
            { this.state.items.map(function(item){ return <p>{item.name} </p> }) }
          </ul>
        </form>
      </div>
    );
  }
}


const main = document.getElementById('main');

ReactDOM.render(<SearchForm dataURL="http://walden.dev/wp-json/wp/v2/posts"/>, main);
