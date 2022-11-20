import React from "react";

function BoardingPass(props) {
  return (
    <div class="ticket inverse">
      <header>
        <div class="company-name">{props.nameOrigin || "Airport Name"}</div>
        <div class="gate">
          <div>PASSO</div>
          <div>{props.step || 0}</div>
        </div>
      </header>
      <section class="airports">
        <div class="airport">
          <div class="airport-name">{props.nameOrigin || "Origin"}</div>
          <div class="airport-code">{props.oaciOrigin || "OACI"}</div>
          <div class="dep-arr-label">({props.stateOrigin || "STATE"})</div>
          <div class="time">Embarque</div>
        </div>
        <div class="airport">
          <div class="airport-name">
            {props.nameDestination || "Destination"}
          </div>
          <div class="airport-code">{props.oaciDestination || "OACI"}</div>
          <div class="dep-arr-label">({props.stateDestination || "STATE"})</div>
          <div class="time">Desembarque</div>
        </div>
      </section>
      <section class="place">
        <div class="place-block">
          <div class="place-label">PREÇO</div>
          <div class="place-value">R$ {props.price || 0}</div>
        </div>
        <div class="place-block">
          <div class="place-label">ASSENTOS LIVRES</div>
          <div class="place-value">{props.seats || 0} Assento(s)</div>
        </div>
        <div class="qr">
          <img src="http://www.classtools.net/QR/pics/qr.png" />
        </div>
      </section>
    </div>
  );
}

export default BoardingPass;
