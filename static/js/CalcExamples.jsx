const exampleData = [
    {
        PaintUsed: "Acrylic",
        CanvasSelected: "Medium: 16x20 - 24x48",
        WeatherCondition: "Temperate",
        DryTime: "40 Minutes",
        exampleId: "1"
    },

    {
        PaintUsed: "Watercolor",
        CanvasSelected: "Small: 5x7 - 11x14",
        WeatherCondition: "Humid",
        DryTime: "37 Minutes",
        exampleId: "2"

    },

    {
        PaintUsed: "Oil",
        CanvasSelected: "Large: 48x48 & Up",
        WeatherCondition: "Temperate",
        DryTime: "24-48 Hours",
        exampleId: "3"
    },

    {
        PaintUsed: "Gouache",
        CanvasSelected: "Medium: 16x20 - 24x48",
        WeatherCondition: "Cold",
        DryTime: "50 Minutes",
        exampleId: "4"
    },

    {
        PaintUsed: "Acrylic",
        CanvasSelected: "Medium: 16x20 - 24x48",
        WeatherCondition: "Cold",
        DryTime: "55 Minutes",
        exampleId: "5"
    },
    
    {
        PaintUsed: "Oil W/ Paint Thinner",
        CanvasSelected: "Medium: 16x20 - 24x48",
        WeatherCondition: "Temperate",
        DryTime: "12-13 Hours",
        exampleId: "6"
    } 
];

function CalcExamples(props) {
    return (
      <div className="examples">
        <h5>Paint Used: </h5>
        <p>{props.PaintUsed}</p>
        <h5>Canvas Selected:</h5>
        <p>{props.CanvasSelected}</p>
        <h5>Weather Condition:</h5>
        <p>{props.WeatherCondition}</p>
        <h5>Total Dry Time:</h5>
        <p>{props.DryTime}</p>
      </div>
    );
  }
  
  function ExampleContainer(props) {
    const exampleInfo = [];
  
    for (const example of exampleData) {
      exampleInfo.push(
        <CalcExamples
        PaintUsed={example.PaintUsed}
        CanvasSelected={example.CanvasSelected}
        WeatherCondition={example.WeatherCondition}
        key={example.exampleId}
        />
      );
    }
  
    return <React.Fragment>{exampleInfo}</React.Fragment>
  }
  
  ReactDOM.render(<ExampleContainer/>, document.getElementById("example-info"));