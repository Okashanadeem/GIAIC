import { Heart, Search, ShoppingCart, UserX } from 'lucide-react';
import React from 'react';
import MobileNavbar from './mobileMenu';
import Link from 'next/link';

const Navbar = () => {
  return (
    <>
      {/* Mobile Navbar */}
      <MobileNavbar />

      {/* Desktop Navbar */}
      <div className="hidden md:flex h-[100px] w-auto justify-center items-center md:justify-end text-black">
        <div className="flex justify-between w-auto">
          {/* Links Section */}
          <div>
            <ul className="flex gap-10 md:mr-48">
            <Link href="/" className="text-lg font-medium hover:underline">Home</Link>
            <Link href="/shop" className="text-lg font-medium hover:underline">Shop</Link>
            <Link href="/about" className="text-lg font-medium hover:underline">About</Link>
            <Link href="/contact" className="text-lg font-medium hover:underline">Contact</Link>
            </ul>
          </div>

          {/* Icons Section */}
          <div className="flex gap-16 h-[28px] mr-16">
          <Link href="/account" className="text-lg font-medium hover:underline"><UserX /></Link>
            <Search />
            <Heart />
            <Link href="/cart" className="text-lg font-medium hover:underline"><ShoppingCart /></Link>
          </div>
        </div>
      </div>
    </>
  );
};

export default Navbar;
