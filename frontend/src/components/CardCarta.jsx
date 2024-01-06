import React, { useState } from 'react';
import { Anuncio } from './Anuncio';

export const CardCarta = (props) => {
  const [anuncioAbierto, setAnuncioAbierto] = useState(false);

  const abrirAnuncio = () => {
    setAnuncioAbierto(true);
    props.onAnuncio();
  };

  const cerrarAnuncio = () => {
    setAnuncioAbierto(false);
    props.onCerrar();
  };

  return (
    <>
    <div className={`w-[300px] sm:w-[250px] flex flex-col items-center justify-center ${props.anuncioAbierto ? 'blur-md' : ''}`}>
        <div className="w-[100%] h-[300px] sm:h-[250px] bg-[#D2F4FF]">
            
        </div>
        <div>
        
        </div>
        <p className="mt-4 mb-6 font-lato text-[18px] tracking-widest">{props.title}</p>
        <button
            onClick={abrirAnuncio}
            className="cursor-pointer border-2 rounded-md px-4 py-1 font-lato border-[#6D858C] w-[172px] text-[18px] hover:bg-slate-400 hover:text-white transition-all"
            >
            Opciones
        </button>
    </div>
    {anuncioAbierto && (
                <Anuncio title={props.title} action={cerrarAnuncio} logic={props.anuncioAbierto} data={props.data} pedidoId={props.pedidoId}/>
                )}
    </>
  );
};
