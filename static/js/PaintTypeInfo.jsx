const paintTypeInfoData = [
  {
    Paint: "Acrylic Paint",
    imgURL: "/static/img/acrylic.jpeg",
    Ingridients:"Acrylic paint is a fast-drying paint made of pigment suspended in acrylic polymer emulsion and plasticizers, silicon oils, defoamers, stabilizers, or metal soaps.",
    Process: "While Acrylic paint has an average drying time is 20-30 minutes, climate change, especially humidity, can alter the drying process.",
    Factors:"Typically artists use water as a mixing medium for Acrylic paint as most acrylic paints are water-based, but become water-resistant when dry.",
    Results:"Depending on how much the paint is diluted with water, or other mediums, the finished acrylic painting can resemble a watercolor, a gouache, or an oil painting, or have its own unique characteristics not attainable with other media. Although it is not as thick as oil paint, when building color in acrylic, the final texture can be a lot smoother.",
    paintId: "1"
  },

  {
    Paint: "Oil Paint",
    imgURL: "/static/img/oil.jpeg",
    Ingridients:"",
    Process: "",
    Factors:"",
    Results:"",
    paintId: "2"
  },

  {
    Paint: "Gouache Paint",
    imgURL: "/static/img/gouache.jpeg",
    Ingridients:"",
    Process: "",
    Factors:"",
    Results:"",
    paintId: "3"
  },

  {
    Paint: "Watercolor Paint",
    imgURL: "/static/img/watercolor.jpeg",
    Ingridients:"",
    Process: "",
    Factors:"",
    Results:"",
    paintId: "4"
  },

  {
    Paint: "Paint Thinner",
    imgURL: "/static/img/paintthinner.jpeg",
    Ingridients:"",
    Process: "",
    Factors:"",
    Results:"",
    paintId: "5"
  },


];

function PaintTypeInfo(props) {
  return (
    <div className="info">
      <h3>{props.Paint} </h3> 
      <img src={props.imgURL}/>
      <h4>About: </h4>
      <a>What it's made of:</a>
      <p>{props.Ingridients}</p>
      <a>Drying Process:</a>
      <p>{props.Process}</p>
      <a>Medium Factors:</a>
      <p>{props.Factors}</p>
      <a>Results:</a>
      <p>{props.Results}</p>
    </div>
  );
}

function PaintTypeInfoContainer(props) {
  const paintInfo = [];

  for (const paintType of paintTypeInfoData) {
    paintInfo.push(
      <PaintTypeInfo
      Paint={paintType.Paint}
      imgURL={paintType.imgURL}
      Ingridients={paintType.Ingridients}
      Process={paintType.Process}
      Factors={paintType.Factors}
      Results={paintType.Results}
      key={paintType.paintId}
      />
    );
  }

  return <React.Fragment>{paintInfo}</React.Fragment>
}

ReactDOM.render(<PaintTypeInfoContainer/>, document.getElementById("paint-info"));