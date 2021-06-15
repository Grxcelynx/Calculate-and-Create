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
    Paint: "Gouache Paint",
    imgURL: "/static/img/gouache.jpeg",
    Ingridients:"Gouache paint is a mix of natural or synthetic pigments, water, and gum arabic that acts as a binding agent to hold the paint together.",
    Process: "Similar to watercolor paint, gouache takes about 10-30 minutes to dry depending on how diluted it is. If you choose to not dilute the paint, the drying process is fairly similar to acrylic paint. ",
    Factors:" Similarly again to watercolors, the more water you add to gouache the thinner and more translucent the pigment will be. As water is the mixing medium for gouache, you can reactivate it. ",
    Results:"For the best results using gouache, it’s recommended to use watercolor or drawing paper for the best opacity and smoothness. While you can use canvas, canvas is better suited for acrylic and oil paint.",
    paintId: "2"
  },

  {
    Paint: "Watercolor Paint",
    imgURL: "/static/img/watercolor.jpeg",
    Ingridients:"Watercolor paint consists of a pigment,  gum arabic as a binder to hold the pigment together,  additives like glycerin, ox gall, honey, and preservatives to alter the viscosity, hiding, durability or color of the pigment and vehicle mixture",
    Process: " Depending on how much water is used, watercolor paint can dry as fast as 5 minutes - 25 minutes per layer. ",
    Factors:"As water can evaporate at different rates depending on humidity and temperature, you must be mindful as to how much water you’re using when painting. The more water you add, the thinner and softer the color gets. To create a more opaque finish, less water and more layers. When applying more layers, be aware of how much water is being used for each layer as the water can reactivate the paint.",
    Results:"Watercolors produce such a unique result unlike any other paint type. Being able to create such a vibrant yet translucent effect. Many people use watercolors to create “old” or “vintage” looking pieces. Because water is the mixing medium, you can reactivate the paint to make adjustments post creation, but you won’t have as much control as you may with adjusting oils.",
    paintId: "3"
  },

  {
    Paint: "Oil Paint",
    imgURL: "/static/img/oil.jpeg",
    Ingridients:"Oil paint consists of high pigment particles that are combined into a drying oil, usually consisting of linseed oil. The hard-wearing properties, vibrant, and luminous colors make it one of the most desirable paint types for artistic canvas. As well as interior and exterior use most commonly used on exterior surfaces like wood and metal.",
    Process: " Because of the linseed oil, this creates a slow drying process that allows artists to have ample time for blending and adjustments. Depending on weather conditions and thickness of layers, oil paint can take anywhere from 12 hours to 14 days to dry. But this creates a window of time for touch ups or adjustments an artist may want to make after the initial creation of the piece. ",
    Factors:"Many artists enjoy using a paint thinner with oil paints as it can speed up the dry time. Paint thinner can always allow more variety in thickness and opacity. Because oil and water do not mix, a proper paint thinner consisting of Turpentine and odorless mineral spirits or specifically made oil paint thinner. You cannot use natural oils like vegetable or olive oil because your paint will never dry and settle properly.",
    Results:"You can achieve so many different results with oil. With it’s thick consistency, the variety of textures in the finished result can add a whole other level to your creation. The flexibility of this paint medium creates endless results. Because of the tucker consistency of the paint, any textures created are usually able to hold their shape throughout the drying process depending on the amount of paint thinner used or layers done.",
    paintId: "4"
  },

  {
    Paint: "Paint Thinner",
    imgURL: "/static/img/paintthinner.jpeg",
    Ingridients:"Paint thinner is a volatile solvent that is used to dilute or extend oil-based paints or cleanup after use. Common solvents used as paint thinner chemicals include mineral spirits, mineral and true turpentine, acetone, naphtha, toluene, methyl ethyl ketone (MEK), dimethylformamide (DMF), glycol ethers and xylene. The chemicals in paint thinner are strong and toxic and should only be used in well ventilated areas or outdoors. ",
    Process: "The drying process varies per brand and amount used in the oil paint selected. Alone, it can take about 20 minutes to dry, yet when mixed into oil paint it can speed up the drying process by hours or overnight.",
    Factors:"There are many different types of paint thinners that are speifically made for certain paint types and brands. Gouache and watercolor are going to be the safest to use as neither requires any other thinning medium than water.",
    Results:"While paint thinner can help speed up the process of your piece and create effects you desire, there are any side effects of paint thinner to be cautious of such as: slurred speech, inability to coordinate movements, dazed or dizzy appearance, delusions or hallucinations, impaired judgment,  severe headaches, rashes on mouth and nose, unconsciousness. Keeping all windows open, fan on, in your space when using a paint thinner is essential.",
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