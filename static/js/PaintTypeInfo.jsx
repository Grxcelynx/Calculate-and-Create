const paintTypeInfoData = [
  {
    Paint: "Acrylic Paint",
    About: "Acrylic paint is a fast-drying paint made of pigment suspended in acrylic polymer emulsion and plasticizers, silicon oils, defoamers, stabilizers, or metal soaps.[2] Most acrylic paints are water-based, but become water-resistant when dry. Depending on how much the paint is diluted with water, or modified with acrylic gels, mediums, or pastes, the finished acrylic painting can resemble a watercolor, a gouache, or an oil painting, or have its own unique characteristics not attainable with other media",
    imgURL: "/static/img/acrylic.jpeg",
    paintId: "1"
  },

  {
    Paint: "Oil Paint",
    About: "",
    imgURL: "/static/img/oil.jpeg",
    paintId: "2"
  },

  {
    Paint: "Gouache Paint",
    About: "",
    imgURL: "/static/img/gouache.jpeg",
    paintId: "3"
  },

  {
    Paint: "Watercolor Paint",
    About: "",
    imgURL: "/static/img/watercolor.jpeg",
    paintId: "4"
  },

  {
    Paint: "Paint Thinner",
    About: "",
    imgURL: "/static/img/paintthinner.jpeg",
    paintId: "5"
  },


];

function PaintTypeInfo(props) {
  return (
    <div className="info">
      <h3>{props.Paint} </h3> 
      <img src={props.imgURL}/>
      <h4>About: </h4>
      <p>{props.About}</p>
    </div>
  );
}

function PaintTypeInfoContainer(props) {
  const paintInfo = [];

  for (const paintType of paintTypeInfoData) {
    paintInfo.push(
      <PaintTypeInfo
      Paint={paintType.Paint}
      About={paintType.About}
      imgURL={paintType.imgURL}
      key={paintType.paintId}
      />
    );
  }

  return <React.Fragment>{paintInfo}</React.Fragment>
}

ReactDOM.render(<PaintTypeInfoContainer/>, document.getElementById("paint-info"));