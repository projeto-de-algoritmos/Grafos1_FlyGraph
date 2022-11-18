import "./App.css";
import React, { useState, useEffect } from "react";
import api from "./services/api";

function App() {
  const [flight, setFlights] = useState([]);
  const [airport, setAirports] = useState([]);
  const [origin, setOrigin] = useState([]);
  const [destination, setDestination] = useState([]);

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

  const getAirports = async () => {
    try {
      const _airport = await api.get("/airports");
      setAirports(_airport.data);
    } catch (error) {
      console.log(error.message);
    }
  };

  let i = 0;
  let idd = 0;
  let ido = 0;
  function soma() {
    i++;
  }

  useEffect(() => {
    getFligths(origin, destination);
  }, []);

  useEffect(() => {
    getAirports();
  }, []);

  return (
    <div className="App">
      {flight &&
        flight.map((data) => {
          soma();
          return (
            <div>
              <p>Voo {i}</p>
              Origem: {data.origin.town}
              <br />
              Destino: {data.destination.town}
              <br />
              Preço: {data.price}
            </div>
          );
        })}
      <p> Preço total: {totalPrice}</p>

      <div className="Input">
        <select onChange={({ target: { value } }) => setOrigin(value)}>
          {airport &&
            airport.map((obj) => {
              ido++;
              return (
                <option value={ido}>
                  {" "}
                  {`${ido} = ${obj.state} - ${obj.town}`}
                </option>
              );
            })}
        </select>

        <select onChange={({ target: { value } }) => setDestination(value)}>
          {airport &&
            airport.map((obj) => {
              idd++;
              return (
                <option value={idd}>
                  {" "}
                  {`${idd} = ${obj.state} - ${obj.town}`}
                </option>
              );
            })}
        </select>
      </div>
      <button onClick={() => getFligths(origin, destination)}> Ok </button>
    </div>
  );
}

export default App;
