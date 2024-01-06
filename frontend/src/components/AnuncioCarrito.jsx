import React, { useEffect, useState } from "react";

export const AnuncioCarrito = ({ data, title, action }) => {
  const [cerrando, setCerrando] = useState(false);
  const [carrito, setCarrito] = useState(data);

  const [pedido, setPedido] = useState({ items: [] });

  const pedidoId = data.id;


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
    }
  }

  const fetchPedido = async () => {
    try {
      console.log("Fetching pedido for pedidoId:", pedidoId);
      if (pedidoId) {
        await fetchData(`/pedido/${pedidoId}`, setPedido);
      }
    } catch (error) {
      console.error("Error al obtener el pedido:", error.message);
    }
  }

  useEffect(() => {
    const updateDataInterval = setInterval(() => {
      fetchPedido();
    }, 1000);

    return () => clearInterval(updateDataInterval);
  }, [fetchPedido]);



  useEffect(() => {
    if (pedido) {
      setCarrito(pedido);
    }
  }, [pedido]);

  const cerrarAnuncio = () => {
    setCerrando(true);
  };

  const animationEnd = () => {
    if (cerrando) {
      action();
    }
  };

  const actualizarCantidad = async (index, nuevaCantidad) => {
    const nuevoCarrito = carrito.items.map((item, i) =>
      i === index
        ? {
            ...item,
            cantidad: nuevaCantidad,
            sub_total: nuevaCantidad * item.plato.precio,
          }
        : item
    );
  
    try {
      // Wait for the database update to complete
      await actualizarBaseDeDatos(nuevoCarrito);
      console.log(nuevoCarrito);
  
      // Update the state after the database update is successful
      setCarrito((prevCarrito) => ({ ...prevCarrito, items: nuevoCarrito }));
    } catch (error) {
      // Handle errors from the database update
      console.error("Error updating database:", error);
    }
  };

  const incrementarCantidad = (index) => {
    console.log(pedido);
    console.log(pedidoId)
    actualizarCantidad(index, carrito.items[index].cantidad + 1);
  };

  const decrementarCantidad = (index) => {
    if (carrito.items[index].cantidad > 1) {
      actualizarCantidad(index, carrito.items[index].cantidad - 1);
    }
  };

  const calcularTotal = () => {
    return carrito.items.reduce((total, item) => total + item.sub_total, 0);
  };

  const actualizarBaseDeDatos = async (nuevoCarrito) => {
    try {
      const response = await fetch(`/items_pedido/upload`, {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ items: nuevoCarrito }),
      });
  
      if (!response.ok) {
        throw new Error("Error al actualizar la base de datos");
      }
    } catch (error) {
      console.error("Error en la solicitud:", error);
      throw error;
    }
  };

  if (!pedido) {
    return <p>Loading...</p>;
  }

  return (
    <>
      <div className={`fixed inset-0 flex items-center justify-center z-50 ${cerrando ? 'animate-slideOut' : 'animate-slideIn'}`} onAnimationEnd={animationEnd}>
        <div className="w-[80vw] sm:w-[454px] bg-[#6D858C] relative ">
          <div className="h-[53px] flex justify-center items-center bg-[#586C73]">
            <h1 className="font-lato text-[18px] text-center text-[#D2F4FF] tracking-widest">{title}</h1>
            <span onClick={cerrarAnuncio} className="absolute right-2 top-2 border-2 rounded-full hover:bg-[#6D858C]">
              <p className="text-sm font-lato px-[10px] py-1 text-[#D2F4FF] cursor-pointer ">X</p>
            </span>
          </div>
          <div className="px-[20px] py-[20px] text-white">
            {!pedido ? (
              <p>Loading...</p>
            ) : (
              <div>
                <ul>
                  {carrito.items.map(({ id, cantidad, plato, sub_total }, index) => (
                    <li key={id} className="my-4">
                      <div className="flex justify-between items-center border-2 p-4 rounded-lg ">
                        <div className="flex flex-col">
                          <div className="w-[100%]">
                            <strong className="text-right">⮞ {plato.nombre}</strong>
                          </div>
                          {plato.ingredientes && plato.ingredientes.length > 0 && (
                            <ul className="list-disc pl-10 my-4">
                              {plato.ingredientes.map((ingrediente, index) => (
                                <li key={index}>{ingrediente}</li>
                              ))}
                            </ul>
                          )}
                        </div>
                        <div className="flex flex-col">
                          <div className="flex items-center justify-center ">
                            <span>S/ {sub_total.toFixed(2)}</span>
                          </div>
                          <div className="flex mt-4">
                            <span className="hover:cursor-pointer text-2xl hover:bg-[#60767db8] rounded-full w-8 flex items-center justify-center" onClick={() => decrementarCantidad(index)}>
                              -
                            </span>
                            <span className="flex items-center justify-center border-2 rounded-lg w-[40px] h-[34px]">
                              {cantidad}
                            </span>
                            <span className="hover:cursor-pointer text-2xl hover:bg-[#60767db8] rounded-full w-8 flex items-center justify-center" onClick={() => incrementarCantidad(index)}>
                              +
                            </span>
                          </div>
                        </div>
                      </div>
                    </li>
                  ))}
                </ul>
                <div className="mt-4 flex justify-between text-lg px-8">
                  <strong>Total: </strong>
                  <strong>S/ {calcularTotal().toFixed(2)}</strong>
                </div>
              </div>
            )}
          </div>
          <div className="flex justify-center items-center  bg-[#586C73] py-4">
            <button className="w-[133px] h-[40px] border-2 rounded-lg hover:bg-slate-500 text-white" onClick={cerrarAnuncio}>
              Pedir
            </button>
          </div>
        </div>
      </div>
    </>
  );
};
