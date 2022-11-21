import "./css/App.css";
import "./css/boardingpass.css"
import "./css/dropdown.css"
import "./css/index.css"
import React, { useState, useEffect } from "react";
import api from "./services/api";
import BoardingPass from "./components/BoardingPass";
require('bootstrap');

function App() {
  const [flight, setFlights] = useState([]);
  const [airport, setAirports] = useState([]);
  const [origin, setOrigin] = useState([]);
  const [destination, setDestination] = useState([]);
  const [checkedGraph, setCheckedGraph] = useState([]);

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

  const getCheckGraph = async () => {
    try {
      const _checkedGraph = await api.get("/check-graph");
      setCheckedGraph(_checkedGraph.data);
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
      <br />

      <div className="Integridade">
        <h2 class="white"> CHECAR INTEGRIDADE DO GRAFO</h2>
        <button type="button" class="btn btn-outline-info" onClick={() => getCheckGraph()}> CHECAR</button>
        {checkedGraph ? (
          <div class="white">
            <p>
              Não há caminho entre {checkedGraph.origin} e{" "}
              {checkedGraph.destination}
            </p>
            <p>
              {" "}
              Fortemente conectado:{" "}
              {checkedGraph.stronglyConnected ? "True" : "False"}
            </p>
            <p> Grafo: {checkedGraph.Grafo}</p>
          </div>
        ) : (
          <h1> ahhhhhhhhhhh</h1>
        )}
      </div>

      <div className="Input">
        <select class="custom-select" aria-label="origem" onChange={({ target: { value } }) => setOrigin(value)}>
          <option selected>SELECIONE A ORIGEM</option>
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

        <select class="custom-select" onChange={({ target: { value } }) => setDestination(value)}>
        <option selected>SELECIONE O DESTINO</option>
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

      <button type="button" class="btn btn-outline-success" onClick={() => getFligths(origin, destination)}> VER MENOR ROTA VOANDO </button>

      <p> PREÇO TOTAL DA VIAGEM: R${Math.round(totalPrice)}</p>

      {flight &&
        flight.map((data) => {
          soma();
          return (
            <section>
              <BoardingPass
                nameOrigin={data.origin.name}
                nameDestination={data.destination.name}
                step={i}
                oaciOrigin={data.origin.oaci}
                oaciDestination={data.destination.oaci}
                stateOrigin={data.origin.state}
                stateDestination={data.destination.state}
                destinationOrigin={data.destination.state}
                price={data.price}
                seats={data.seats}
                img={"https://api.qrserver.com/v1/create-qr-code/?size=1000x1000&data=https://pt.wikipedia.org/wiki/Special:Search?search=aeroporto+"+data.origin.name.toLowerCase()}
              />
            </section>
          );
        })}
    </div>
  );
}

export default App;
