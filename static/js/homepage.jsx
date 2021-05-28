function Homepage(props) {
    return (
      <React.Fragment>
        <h1>Calculate and Create</h1>
        <h2>Time to Calculate and Create your dry time!</h2>
        <a href="/render_form">Calculate My Creation!</a>
        <a href="/paint_info">Learn more about the paint you're selecting!</a>
      </React.Fragment>
      );
  }
    
  ReactDOM.render(<Homepage />, document.getElementById('app'));