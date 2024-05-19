import config from "./assets/config.json";
import axios from "axios";
const linkToApi = config["api-link"] + "api/";
import { useState } from "react";

export default function Submit() {
  const [inputValue, setInputValue] = useState("");

  const handleChange = (event) => {
    setInputValue(event.target.value);
  };

  function player() {
    axios
      .post(linkToApi + "play/", {
        com: "start",
      })
      .then((response) => {
        console.log("String sent successfully: " + response);
      })
      .catch((error) => {
        console.error("Error sending string:", error.message);
      });
  }

  function submitted() {
    let l = inputValue;
    console.log(l);
    axios
      .post(linkToApi + "download/", {
        link: l,
      })
      .then((response) => {
        console.log("String sent successfully: " + response);
      })
      .catch((error) => {
        console.error("Error sending string:", error.message);
      });
  }
  return (
    <div>
      <input
        type="text"
        id="link"
        placeholder="Insert Youtube Link"
        value={inputValue}
        onChange={handleChange}
      />
      <button
        id="submit"
        type="button"
        className="btn btn-primary"
        onClick={submitted}
      >
        Submit
      </button>
      <p id="status"></p>
      <button id="startstop" className="btn btn-dark" onClick={player}>
        Start
      </button>
    </div>
  );
}
