import React from "react";
import enterImage from "./img/enter_button.jpg";
import pageTurn from "./img/page-turn.png"

const Home = () => {
  return (
  <div>
    {/* how do you change the <title> of the page?? */}

    {/* header */}
    <div className="siteHeader">Get a Little Wiser</div>

    {/* user selects their source of wisdom - either the Bible or Meditations */}
    <div className="wisdomHeader">Choose your source of wisdom</div>
    
    {/* carousel */}
    <div className="carousel">
      
    <img src={pageTurn} alt="" class="carouselItem"/>
    <img src={pageTurn} alt="" class="carouselItem"/>
    <img src={pageTurn} alt="" class="carouselItem"/>
    <img src={pageTurn} alt="" class="carouselItem"/>
    <img src={pageTurn} alt="" class="carouselItem"/>

    </div>

    {/* option to upload a plain-text file*/}      

    {/* user tells their problem based on their source of wisdom */}
    <div className="userProblem">
      <input type="text" placeholder="Tell us your problem..."/>
      <img src={enterImage}
      alt="Image" className="enterButton"/>
    </div>
    
    <img src={pageTurn} alt="" className="pageTurn"/>
  </div>
  );
};

export default Home;
