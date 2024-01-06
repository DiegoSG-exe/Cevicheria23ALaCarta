import { useState } from "react";

export const Anuncio = ({ pedidoId, title, data, action }) => {
    
    const [cerrando, setCerrando] = useState(false);

    const cerrarAnuncio = () => {
        setCerrando(true);
    };

    const animationEnd = () => {
        if (cerrando) {
            action();
        }
    };

    const handleSubmit = async (e, id, precio ) => {
        e.preventDefault();
        try {
            const response = await fetch(`/items_pedido`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    cantidad : 1,
                    sub_total: precio,
                    plato_id: id,
                    pedido_id: pedidoId,
                }),
            });
            if (!response.ok) {
                throw new Error(`Error al agregar plato: ${response.statusText}`);
            }
            const data = await response.json();
            console.log(data);
        } catch (error) {
            console.error(`Error al agregar plato: ${error.message}`);
        }
    };

    return (
        <div className={`fixed inset-0 flex items-center justify-center z-50 ${cerrando ? 'animate-slideOut' : 'animate-slideIn'}`} onAnimationEnd={animationEnd}>
            <div className="w-[80vw] sm:w-[454px] bg-[#6D858C] relative">
                <div className="h-[53px] flex justify-center items-center bg-[#586C73]">
                    <h1 className="font-lato text-[18px] text-center text-[#D2F4FF] tracking-widest">{title}</h1>
                    <span onClick={cerrarAnuncio} className="absolute right-0 top-0 cursor-pointer">
                        <p className="text-2xl font-lato px-2 py-2 text-[#D2F4FF]">X</p>
                    </span>
                </div>
                <div className="px-[20px] py-[20px] text-white">
                    {!data ? (
                        <p>Loading...</p>
                    ) : (
                        <div>
                            <ul>
                                {data.map(({ id, nombre, ingredientes, precio }) => (
                                    <li key={id} className="my-4">
                                        <div className="flex justify-between items-center">
                                            <div className="flex flex-col">
                                                <div className="w-[100%]">
                                                    <strong className="text-right">{nombre}</strong>
                                                </div>
                                                {ingredientes && ingredientes.length > 0 && (
                                                    <ul className="list-disc pl-10 my-4">
                                                        {ingredientes.map((ingrediente, index) => (
                                                            <li key={index}>{ingrediente}</li>
                                                        ))}
                                                    </ul>
                                                )}
                                            </div>
                                            <div className="flex flex-col justify-center items-center">
                                                <p>S/ {precio.toFixed(2)}</p>
                                                <button type="button" onClick={(e) => handleSubmit(e, id, precio )} className="w-[133px] h-[40px] border-2 rounded-lg mt-4 hover:bg-slate-500">
                                                    Agregar
                                                </button>
                                            </div>
                                        </div>
                                    </li>
                                ))}
                            </ul>
                        </div>
                    )}
                </div>
            </div>
        </div>
    );
};
