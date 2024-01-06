import { useState } from "react"
import { Outlet } from "react-router-dom"
import { Footer } from "./Footer"
import { IconCarrito } from "./Icon_Carrito"
import { Header } from "./header"

export const Layout = (props) => {
  const [anuncioAbierto, setAnuncioAbierto] = useState(false)

  const abrirAnuncio = () => {
    setAnuncioAbierto(true)
  }

  const cerrarAnuncio = () => {
    setAnuncioAbierto(false)
  }



  return (
    <>
    <div className={`min-h-[100vh] flex flex-col font-lato ${anuncioAbierto ? "blur-md" : "" }`}>
        <Header/>
        <Outlet/>
        <Footer/>
    </div>
    <IconCarrito onAnuncio={abrirAnuncio} onCerrar={cerrarAnuncio} anuncioAbiertoL={anuncioAbierto} pedidoId={props.pedidoId}/>
    </>
  )
}