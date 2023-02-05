import React, { useState } from "react";
import enterImage from "./img/enter_button.jpg";
import pageTurn from "./img/page-turn.png";
import axios from "axios";
import bookImage from "./img/book-vector.png";
import vineImage from "./img/green_vine.png";
import holyBible from "./img/holyBiblecover.png";
import meditations from "./img/meditationsBook.png";
import quran from "./img/quran.png";

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
      <div className="selectionSection">
        <div className="carousel_parent">
          <div className="carousel">
            <img src={holyBible} alt="" className="carouselItem" />
            <img
              src={meditations}
              alt=""
              className="carouselItem meditations"
            />
            <img src={quran} alt="" className="carouselItem" />
            <img src={enterImage} alt="" className="carouselItem" />
            <img src={enterImage} alt="" className="carouselItem" />
            <img src={enterImage} alt="" className="carouselItem" />
            <img src={enterImage} alt="" className="carouselItem" />
            <img src={enterImage} alt="" className="carouselItem" />
          </div>
        </div>

        {/* option to upload a plain-text file*/}
        <button className="userReq">
          <img src={bookImage} alt="" className="bookVector" />
          <br></br>
          Upload your own
        </button>
      </div>

      {/* user tells their problem based on their source of wisdom */}
      <div className="userProblem">
        <input
          type="text"
          placeholder="Tell us your problem..."
          onBlur={handleQuestion}
        />
        <img
          onClick={handleClick}
          src={enterImage}
          alt="Image"
          className="enterButton"
        />
      </div>
      <div className="userSolution mt-2">
        <textarea
          className="answerBox"
          type="textarea"
          placeholder="And your scripture will tell you the answer..."
          readOnly
          value={answer}
        />
      </div>

      {/* user tells their problem based on their source of wisdom */}
      <div className="userProblem">
        <input
          type="text"
          onBlur={handleQuestion}
          placeholder="Tell us your problem..."
        />
        <img
          src={enterImage}
          onClick={handleClick}
          alt="Image"
          className="enterButton"
        />
      </div>

      <img src={pageTurn} alt="" className="pageTurn" />
      <img src={vineImage} alt="" className="vineDecorator" />
    </div>
  );
};

export default Home;
