import "./css/App.css";
import "./css/boardingpass.css";
import "./css/dropdown.css";
import "./css/index.css";
import React, { useState, useEffect } from "react";
import api from "./services/api";
import BoardingPass from "./components/BoardingPass";
require("bootstrap");

function App() {
  const [flight, setFlights] = useState([]);
  const [airport, setAirports] = useState([]);
  const [origin, setOrigin] = useState([]);
  const [destination, setDestination] = useState([]);
  const [checkedGraph, setCheckedGraph] = useState([]);
  const [consumed, setConsumed] = useState(false);
  const [noPath, setNoPath] = useState(false);
  const [totalPrice, setTotalPrice] = useState("");

  const getFlights = async (ido, idd) => {
    try {
      const _flight = await api.get(`get-data/?ido=${ido}&idd=${idd}`);
      setFlights(_flight.data.flights);
      setTotalPrice(_flight.data.total_price);
      setNoPath(false);
    } catch (error) {
      setNoPath(true);
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
      setConsumed(true);
    } catch (error) {
      console.log(error.message);
    }
  };

  const plotGraph = async () => {
      await api.get(`plot/`);
  }

  const plotPath = async (ido, idd) => {
    try{
      await api.get(`plot-path/?ido=${ido}&idd=${idd}`)
    }
    catch(error){
      console.log(error.message);
      if(ido === idd)
        alert('Você não pode usar um aeroporto de destino igual ao de origem.')
    }
  }

  let i = 0;
  let idd = 0;
  let ido = 0;
  function soma() {
    i++;
  }

  useEffect(() => {
    getAirports();
  }, []);

  return (
    <div className="App">
      <br />

      <div className="Integridade">
        <h2 class="white"> Checar integridade do Grafo</h2>
        <button
          type="button"
          class="btn btn-outline-info"
          onClick={() => getCheckGraph()}
        >
          {" "}
          CHECAR
        </button>
        {consumed ? (
          checkedGraph.stronglyConnected ? (
            <p style={{ color: "#ffffff" }}>
              {" "}
              Fortemente conectado:{" "}
              <span style={{ color: "#17a2b8" }}> Sim </span>{" "}
            </p>
          ) : (
            <div class="white">
              <p>
                Não há caminho entre{" "}
                <span style={{ color: "#17a2b8" }}>
                  {" "}
                  {checkedGraph.origin}{" "}
                </span>{" "}
                e{" "}
                <span style={{ color: "#17a2b8" }}>
                  {" "}
                  {checkedGraph.destination}{" "}
                </span>
              </p>
              <p>
                {" "}
                Fortemente conectado:{" "}
                <span style={{ color: "#17a2b8" }}> Não </span>
              </p>
              <p>
                {" "}
                Grafo:{" "}
                <span style={{ color: "#17a2b8" }}>
                  {" "}
                  {checkedGraph.Grafo}{" "}
                </span>{" "}
              </p>
            </div>
          )
        ) : null}
      </div>

      <div className="Input">
        <select
          class="align-select custom-select"
          aria-label="origem"
          onChange={({ target: { value } }) => setOrigin(value)}
        >
          <option selected>SELECIONE A ORIGEM</option>
          {airport &&
            airport.map((obj) => {
              ido++;
              return (
                <option value={ido}>
                  {" "}
                  {`${ido} - ${obj.state} - ${obj.name}`}
                </option>
              );
            })}
        </select>

        <select
          class="align-select custom-select"
          onChange={({ target: { value } }) => setDestination(value)}
        >
          <option selected>SELECIONE O DESTINO</option>
          {airport &&
            airport.map((obj) => {
              idd++;
              return (
                <option value={idd}>
                  {" "}
                  {`${idd} - ${obj.state} - ${obj.name}`}
                </option>
              );
            })}
        </select>
      </div>

      <div>
        <button
          type="button"
          class="btn btn-outline-secondary"
          onClick={() => plotGraph()}
        >
          {" "}
          PLOTAR GRAFO COMPLETO{" "}
        </button>

        <button
          type="button"
          class="btn btn-outline-primary"
          onClick={() => plotPath(origin, destination)}
        >
          {" "}
          PLOTAR ÁRVORE RESPOSTA{" "}
        </button>
      </div>
      <p style={{ color: "#b8b8b8" }}>(Não rodar no Docker para usar a biblioteca matplotlib.pyplot)</p>


      <button
        type="button"
        class="btn btn-outline-success"
        onClick={() => getFlights(origin, destination)}
      >
        {" "}
        VER MENOR ROTA VOANDO{" "}
      </button>

      {noPath ? (
        <p className="semCaminho"> Não existe caminho possível </p>
      ) : (
        flight &&
        flight.map((data) => {
          soma();
          return (
            <section>
              {i !== 1 ? null : (
                <p className="preco">
                  <span>
                    {" "}
                    PREÇO TOTAL DA VIAGEM: R$ {Number(totalPrice).toFixed(
                      2
                    )}{" "}
                  </span>
                </p>
              )}
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
                img={
                  "https://api.qrserver.com/v1/create-qr-code/?size=1000x1000&data=https://pt.wikipedia.org/wiki/Special:Search?search=aeroporto+" +
                  data.origin.name.toLowerCase()
                }
              />
            </section>
          );
        })
      )}
    </div>
  );
}

export default App;
