import React, { useState } from "react";
import enterImage from "./img/enter_button.jpg";
import pageTurn from "./img/page-turn.png";
import axios from "axios";

const Home = () => {
  const [question, setQuestion] = useState();
  const [answer, setAnswer] = useState("");

  function handleQuestion(e) {
    setQuestion(e.target.value);
  }

  function handleClick() {
    axios
      .get("http://localhost:8000/api/question", {
        params: {
          question: question,
        },
      })
      .then((response) => {
        setAnswer(response.data.best_sentence);
      });
  }

  return (
    <div>
      {/* how do you change the <title> of the page?? */}

      {/* header */}
      <div className="siteHeader">Get a Little Wiser</div>

      {/* user selects their source of wisdom - either the Bible or Meditations */}
      <div className="wisdomHeader">Choose your source of wisdom</div>

      {/* carousel */}
      <div className="carousel">
        <img src={pageTurn} alt="" className="carouselItem" />
        <img src={pageTurn} alt="" className="carouselItem" />
        <img src={pageTurn} alt="" className="carouselItem" />
        <img src={pageTurn} alt="" className="carouselItem" />
        <img src={pageTurn} alt="" className="carouselItem" />
      </div>

      {/* option to upload a plain-text file*/}

      {/* user tells their problem based on their source of wisdom */}
      <div className="userProblem">
        <input
          type="text"
          placeholder="Tell us your problem..."
          onBlur={handleQuestion}
        />
        <button onClick={handleClick}>
          <img src={enterImage} alt="Image" className="enterButton" />
        </button>
      </div>
      <div className="userSolution mt-2">
        <textarea
          className="answerBox"
          type="textarea"
          placeholder="And your scripture will tell you the answer..."
          value={answer}
          readOnly
        />
      </div>

      <img src={pageTurn} alt="" className="pageTurn" />
    </div>
  );
};

export default Home;
