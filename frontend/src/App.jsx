import { Route, Routes } from 'react-router-dom';
import { Layout } from './components/Layout';
import { Carta } from './pages/Carta';
import { Contacto } from './pages/Contacto';
import { Inicio } from './pages/Inicio';

import { useEffect, useState } from 'react';

function App() {
  const [pedidoId, setPedidoId] = useState(null);

  useEffect(() => {
    const obtenerPedidoExistente = async () => {
      try {
        // Verificar si ya existe un ID de pedido en sessionStorage
        const pedidoIdExistente = sessionStorage.getItem('pedidoId');
        if (pedidoIdExistente) {
          setPedidoId(pedidoIdExistente);
        } else {
          // Si no existe, realizar la solicitud para obtener o crear un nuevo pedido
          const response = await fetch('/pedido', { method: 'POST' });

          if (response.ok) {
            const data = await response.json();
            console.log("Respuesta del servidor: ", data);
            const nuevoPedidoId = data.id;

            sessionStorage.setItem('pedidoId', nuevoPedidoId);
            setPedidoId(nuevoPedidoId);
            console.log('Nuevo pedido creado:', nuevoPedidoId);
          } else {
            console.error('Error al obtener o crear el pedido:', response.statusText);
          }
        }
      } catch (error) {
        console.error('Error al obtener o crear el pedido:', error);
      }
    };

    obtenerPedidoExistente();
  }, []);

  return (
    <>
      <Routes>
        <Route path="/" element={<Layout pedidoId={pedidoId} />}>
          <Route path="/" element={<Inicio  />} />
          <Route path="carta" element={<Carta pedidoId={pedidoId} />} />
          <Route path="contacto" element={<Contacto />} />
          <Route path="*" element={<Inicio />} />
        </Route>
      </Routes>
    </>
  );
}

export default App;
