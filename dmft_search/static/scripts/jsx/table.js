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

var Table = React.createClass({

render: function() {
    var headerComponents = this.generateHeaders(),
        rowComponents = this.generateRows();

    return (
        <div class="table-responsive">
            <table class="table">
                <thead> {headerComponents} </thead>
                <tbody> {rowComponents} </tbody>
            </table>
        </div>
    );
},

generateHeaders: function() {
    var cols = this.props.cols;  // [{key, label}]

    // generate our header (th) cell components
    return cols.map(function(colData) {
        return <th key={colData.key}> {colData.label} </th>;
    });
},

generateRows: function() {
    var cols = this.props.cols,  // [{key, label}]
        data = this.props.data;

    return data.map(function(item) {
        // handle the column data within each row
        var cells = cols.map(function(colData) {

            // colData.key might be "firstName"
            return <td> {item[colData.key]} </td>;
        });
        return <tr key={item.id}> {cells} </tr>;
    });
}
});

ReactDOM.render(<Table cols={cols} data={data}/>,  document.getElementById('search'));
