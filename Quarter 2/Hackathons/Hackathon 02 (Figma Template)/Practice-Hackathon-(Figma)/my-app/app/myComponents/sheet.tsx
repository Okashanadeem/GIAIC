'use client'
import { useState } from "react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import {
  Sheet,
  SheetClose,
  SheetContent,
  SheetDescription,
  SheetFooter,
  SheetHeader,
  SheetTitle,
  SheetTrigger,
} from "@/components/ui/sheet";
import { Heart, Menu, Search, ShoppingCart } from "lucide-react";
import Link from "next/link";
import { InputDemo } from "./input";

export function SheetDemo() {
  // State for input fields
  const [name, setName] = useState("Pedro Duarte");
  const [username, setUsername] = useState("@peduarte");

  return (
    <Sheet>
      <SheetTrigger asChild>
        <Button variant="outline" className="md:hidden">
          <Menu />
        </Button>
      </SheetTrigger>
      <SheetContent>
        <SheetHeader>
          <SheetTitle>EXCLUSIVE</SheetTitle>
        </SheetHeader>
      <div>
        <nav className="flex flex-col gap-6 mt-6">
            <Link href="/" className="mr-5 hover:text-gray-900">
              Home
            </Link>
            <Link href="/about" className="mr-5 hover:text-gray-900">
              About
            </Link>
            <Link href="/contact" className="mr-5 hover:text-gray-900">
              Contact
            </Link>
            <Link href="/signup" className="mr-5 hover:text-gray-900">
              Sign Up
            </Link>
          </nav>

          {/* Search Bar */}
          <div className="relative mt-4">
            <InputDemo />
            <Search className="absolute top-2 right-2 text-gray-500" />
            
            <div className="space-x-2 mt-1">
              {/* Action Buttons */}
            <Button variant="outline" size="icon" className="border-0">
              <Heart />
            </Button>
            <Button variant="outline" size="icon" className="border-0">
              <ShoppingCart />
            </Button>
            </div>

          </div>
      </div>


        <div className="grid gap-4 py-4">
          <div className="grid grid-cols-4 items-center gap-4">
            <Label htmlFor="name" className="text-right">
              Name
            </Label>
            <Input
              id="name"
              value={name}
              onChange={(e) => setName(e.target.value)}
              className="col-span-3"
            />
          </div>
          <div className="grid grid-cols-4 items-center gap-4">
            <Label htmlFor="username" className="text-right">
              Username
            </Label>
            <Input
              id="username"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              className="col-span-3"
            />
          </div>
        </div>
        <SheetFooter>
          <SheetClose asChild>
            <Button type="submit">Save changes</Button>
          </SheetClose>
        </SheetFooter>
      </SheetContent>
    </Sheet>
  );
}
