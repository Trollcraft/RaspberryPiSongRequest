import "./App.css";
import "./api.jsx";
import Submit from "./api.jsx";
import axios from "axios";
import { useState, useEffect } from "react";
const linkToApi = config["api-link"] + "api/";
import config from "./assets/config.json";

function App() {
  const [songs, setSongs] = useState([]);

  useEffect(() => {
    axios.get(linkToApi + "showPlaylist/").then((response) => {
      console.log(response.data.query);
      console.log("Fetch playlist: " + response.status);
      setSongs(response.data.query);
    });
  }, []);

  return (
    <div>
      <div id="submit">
        <Submit></Submit>
      </div>
      <div id="playlistPart">
        <h2>Playlist</h2>
        <ol className="list-group">
          {songs.map((song, index) => (
            <li className="list-group-item" key={index}>
              {index + 1}. {song}
            </li>
          ))}
        </ol>
      </div>
    </div>
  );
}
export default App;
