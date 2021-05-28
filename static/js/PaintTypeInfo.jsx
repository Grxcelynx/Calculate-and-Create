const paintTypeInfoData = [
  {
    Paint: "Acrylic",
    About: "",
    imgURL: "/static/img/acrylic.jpeg",
    paintId: "1"
  },

  {
    Paint: "Oil",
    About: "",
    imgURL: "/static/img/oil.jpeg",
    paintId: "2"
  },

  {
    Paint: "Gouache",
    About: "",
    imgURL: "/static/img/gouache.jpeg",
    paintId: "3"
  },

  {
    Paint: "Watercolor",
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
      <h2>Paint: {props.Paint}</h2>
      <img src={props.imgURL}/>
      <h2>About: {props.About}</h2>
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