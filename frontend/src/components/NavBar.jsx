import { Link } from 'react-router-dom'
import menu from '../assets/menu.png'

export const NavBar = () => {
  return (
    <>
        <nav>
        <ul className="hidden text-2xl sm:flex sm:place-content-around sm:w-[500px] tracking-tight">
            <li>
                <Link to="/">I N I C I O</Link>
            </li>
            <li>
                <Link to="/carta">C A R T A</Link>
            </li>
            <li>
                <Link to="/contacto">C O N T A C T O</Link>
            </li>
        </ul>
        </nav>
    <img className='w-8 block sm:hidden' src={menu} alt="" />
    </>
  )
}

