import Link from "next/link"
import { Button } from "./button"
import { ModeToggle } from "@/components/ToggleButton";

function Navbar(){


    return(
        <div className="flex items-center justify-between py-5 px-5 bg-transparent border-b-2">
            <Link href='/'>
                <span>Job Board </span> 
            </Link>
            <div className="flex">
                <Button className="mr-2">
                    <Link href='/'>
                        Login
                    </Link>
                </Button>
                <ModeToggle/>
            </div>
 
        </div>
    )
}


export default Navbar