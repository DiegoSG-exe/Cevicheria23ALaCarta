import { NavBar } from "./NavBar"

export const Header = () => {
  return (
    <>
    <header className=" flex place-content-between font-lato h-32 items-center px-4 sm:px-[5%]" >
        <h1 className="text-2xl sm:text-3xl font-bold tracking-tight">C E V I C H E R I A 2 3</h1>
        <NavBar/>
    </header>
    </>
  )
}
