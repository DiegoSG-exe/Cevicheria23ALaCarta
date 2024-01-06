import { useCallback, useEffect, useState } from "react";
import { IoMdCart } from "react-icons/io";
import { AnuncioCarrito } from "./AnuncioCarrito";

export const IconCarrito = ({ onAnuncio, onCerrar, pedidoId }) => {
  const [anuncioAbierto, setAnuncioAbierto] = useState(false);
  const [pedido, setPedido] = useState({ items: [] });
  const [loading, setLoading] = useState(true);

  const fetchData = async (url, setter) => {
    try {
      const response = await fetch(url);
      if (!response.ok) {
        throw new Error(`Error al obtener datos de ${url}: ${response.statusText}`);
      }
      const data = await response.json();
      setter(data);
      console.log(data);
    } catch (error) {
      console.error(`Error al obtener datos de ${url}:`, error.message);
    } finally {
      setLoading(false);
    }
  };

  const fetchPedido = useCallback(async () => {
    setLoading(true);
    try {
      if (pedidoId) {
        await fetchData(`/pedido/${pedidoId}`, setPedido);
      }
    } catch (error) {
      console.error("Error al obtener el pedido:", error.message);
    } finally {
      setLoading(false);
    }
  }, [pedidoId]);

  const abrirAnuncio = useCallback(() => {
    setAnuncioAbierto(true);
    onAnuncio();
  }, [onAnuncio]);

  const cerrarAnuncio = useCallback(() => {
    setAnuncioAbierto(false);
    onCerrar();
  }, [onCerrar]);

  useEffect(() => {
    const updateDataInterval = setInterval(() => {
      fetchPedido();
    }, 2000);

    return () => clearInterval(updateDataInterval);
  }, [fetchPedido]);

  return (
    <>
      <div className="fixed bottom-0 mb-4 sm:mb-[30px] ml-4 sm:ml-10 cursor-pointer" onClick={abrirAnuncio}>
        <IoMdCart className="text-[80px] text-[#708187]" />
        {pedido.items.length > 0 && (
          <span className="absolute top-0 right-0 w-8 h-8 bg-red-500 flex justify-center items-center text-white rounded-full">
            {pedido.items.length > 99 ? "+99" : pedido.items.length}
          </span>
        )}
      </div>
      {anuncioAbierto && (
        <AnuncioCarrito title="Pedido" action={cerrarAnuncio} logic={anuncioAbierto} data={pedido} />
      )}
    </>
  );
};
