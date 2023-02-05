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
  const [book, setBook] = useState("Bible");
  const [images, setImages] = useState([
    {id: 1, src: holyBible, title: 'Bible',  opacity: 0.5},
    {id: 2, src: meditations, title: 'Meditations', style: {transform: "scale(0.91)", marginRight: "35px"}, opacity: 0.5},
    {id: 3, src: quran, title: 'Quran', opacity: 0.5}
  ]
  );

  // const generalImageStyles = height

  function handleQuestion(e) {
    setQuestion(e.target.value);
  }

  function handleClick() {
    axios
      .get("http://localhost:8000/api/question", {
        params: {
          question: question,
          book: book,
        },
      })
      .then(async (response) => {
        await new Promise((r) => setTimeout(r, 1000));
        setAnswer(response.data.best_sentence);
      });
  }

  function changeBook(chosenBook) {
    setBook(chosenBook);
  }

  const handleClickReq = (id, title) => {
    changeBook(title)
    const updatedImages = images.map(image => {
      if (image.id === id) {
        return {
          ...image,
          opacity: image.opacity === 1 ? 0.5 : 1
        };
      }
      else {
        return {
          ...image,
          opacity: image.opacity = 0.5
        }
      }
      return image;
    });
    setImages(updatedImages);
  };
  




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
              {images.map(image => (
                <img
                  key={image.id}
                  src={image.src}
                  style={{ opacity: image.opacity, ...image.style}}
                  className="carouselItem"
                  onClick={() => handleClickReq(image.id, image.title)}
                />
              ))}
          </div>
        </div>

        {/* option to upload a plain-text file*/}
        <button className="userReq">
          <img src={bookImage} alt="Enter" className="bookVector" />
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
          placeholder="And your text will show you the answer..."
          readOnly
          value={answer}
        />
      </div>

      <img src={pageTurn} alt="" className="pageTurn" />
      <img src={vineImage} alt="" className="vineDecorator" />
    </div>
  );
};

export default Home;
