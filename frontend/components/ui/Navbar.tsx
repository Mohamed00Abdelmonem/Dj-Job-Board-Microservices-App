import Link from "next/link"
import { Button } from "./button"
import { ModeToggle } from "@/components/ToggleButton";
import { BriefcaseBusiness } from "lucide-react";
import { CircleUser } from "lucide-react";
import {
    DropdownMenu,
    DropdownMenuContent,
    DropdownMenuItem,
    DropdownMenuLabel,
    DropdownMenuSeparator,
    DropdownMenuTrigger,
  } from "@/components/ui/dropdown-menu"

    
function Navbar(){


    return(
        <div className="flex items-center justify-between py-5 px-5 bg-transparent border-b-2">
            <div className="flex items-center">
                <Link href='/' className="flex gap-2 items-center">
                    <BriefcaseBusiness className="w-8 h-8"/>
                    <span>JobBoard </span> 
                </Link>
                <Link className="mx-3 pl-3" href='/jobs'>jobs</Link>
                <Link className="mx-3" href="/blog">blog</Link>
            </div>
            
            <div className="flex">
                <Button className="mr-2">
                    <Link href='/'>
                        Login
                    </Link>
                </Button>
                <ModeToggle/>
                <div className="ml-2 pl-3 flex gap-2 items-center">  
                <DropdownMenu>
                    <DropdownMenuTrigger>  <CircleUser /></DropdownMenuTrigger>
                    <DropdownMenuContent>
                        <DropdownMenuLabel>My Account</DropdownMenuLabel>
                        <DropdownMenuSeparator />
                        <DropdownMenuItem>Profile</DropdownMenuItem>
                        <DropdownMenuItem>Billing</DropdownMenuItem>
                        <DropdownMenuItem>Team</DropdownMenuItem>
                        <DropdownMenuItem>Subscription</DropdownMenuItem>
                    </DropdownMenuContent>
                </DropdownMenu>

                  
                </div>




            </div>
 
        </div>
    )
}


export default Navbar