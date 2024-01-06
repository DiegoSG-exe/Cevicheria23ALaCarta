import { MenuCarta } from "../components/MenuCarta"
import { TituloCarta } from "../components/TituloCarta"

export const Carta = ({pedidoId}) => {
  return (
    <>
        <TituloCarta/>
        <MenuCarta pedidoId={pedidoId}/>
    </>
  )
}
