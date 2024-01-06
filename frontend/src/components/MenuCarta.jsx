import { useEffect, useState } from "react";
import { CardCarta } from "./CardCarta";

export const MenuCarta = ({pedidoId}) => {
    const [anuncioAbierto, setAnuncioAbierto] = useState(false);
    const [trio, setTrio] = useState([]);
    const [duo, setDuo] = useState([]);
    const [fritos, setFritos] = useState([]);
    const [solos, setSolos] = useState([]);
    const [sopas, setSopas] = useState([]);

    const abrirAnuncio = () => {
        setAnuncioAbierto(true);
    };

    const cerrarAnuncio = () => {
        setAnuncioAbierto(false);
    };

    const fetchData = async (url, setter) => {
        try {
            const response = await fetch(url);
            const data = await response.json();
            setter(data);
            console.log(data);
        } catch (error) {
            console.error(`Error al obtener datos de ${url}:`, error);

        }
    };

    useEffect(() => {
        fetchData('/trio_marino', setTrio);
        fetchData('/duo_marino', setDuo);
        fetchData('/fritos', setFritos);
        fetchData('/platos_solos', setSolos);
        fetchData('/sopas', setSopas);
    }, []);

    const cardData = [
        { title: "Trio Marino", data: trio },
        { title: "Duo Marino", data: duo },
        { title: "Platos Solos", data: solos },
        { title: "Fritos", data: fritos },
        { title: "Sopas", data: sopas },
    ];

    return (
        <div className="sm:px-[20%] flex flex-wrap items-center justify-center gap-10 my-20">
            {cardData.map((card, index) => (
                <CardCarta key={index} title={card.title} onAnuncio={abrirAnuncio} onCerrar={cerrarAnuncio} anuncioAbierto={anuncioAbierto} data={card.data} pedidoId={pedidoId}/>
            ))}
        </div>
    );
};
