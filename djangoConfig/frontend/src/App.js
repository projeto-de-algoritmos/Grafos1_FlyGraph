import "./App.css";
import React, { useState, useEffect } from "react";
import api from "./services/api";

function App() {
  const [flight, setFlights] = useState([]);
  const [totalPrice, setTotalPrice] = useState("");

  const getFligths = async (ido, idd) => {
    try {
      const _flight = await api.get(`get-data/?ido=${ido}&idd=${idd}`);
      setFlights(_flight.data.flights);
      setTotalPrice(_flight.data.total_price);
    } catch (error) {
      console.log(error.message);
    }
  };

  let i = 0;
  function soma() {
    i++;
  }

  useEffect(() => {
    getFligths(5, 9);
  }, []);

  return (
    <div className="App">
      {flight &&
        flight.map((data) => {
          soma();
          return (
            <div>
              <p>Vôo {i}</p>
              Origem: {data.origin.town}
              <br />
              Destino: {data.destination.town}
              <br />
              Preço: {data.price}
            </div>
          );
        })}
      <p> Preço total: {totalPrice}</p>
    </div>
  );
}

export default App;
