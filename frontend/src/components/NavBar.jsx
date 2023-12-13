import menu from '../assets/menu.png'

export const NavBar = () => {
  return (
    <>
    <ul className="hidden text-2xl sm:flex sm:place-content-around sm:w-[500px] tracking-tight">
        <li>
            <a href="#">I N I C I O</a>
        </li>
        <li>
            <a href="#">C A R T A</a>
        </li>
        <li>
            <a href="#">C O N T A C T O</a>
        </li>
    </ul>
    <img className='w-8 block sm:hidden' src={menu} alt="" />
    </>
  )
}

