import Link from 'next/link';
import React from 'react';
import { InputDemo } from './input';
import { Heart, Search, ShoppingCart } from 'lucide-react';
import { Button } from '@/components/ui/button';
import { SheetDemo } from './sheet';

const HeaderTop = () => {
  return (
    <>
      {/* Top Banner */}
      <div className="hidden md:flex justify-center bg-black text-white h-12 items-center">
        <div className="mr-40 px-4">
          <p>
            Summer Sale For All Swim Suits And Free Express Delivery - OFF 50%!{' '}
            <span className="underline cursor-pointer ml-1">Shop Now</span>
          </p>
        </div>
        <div className="flex items-center px-4 cursor-pointer">
          English
          <svg
            xmlns="http://www.w3.org/2000/svg"
            className="w-4 h-4 ml-2 transition-transform duration-200"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth="2"
              d="M6 9l6 6 6-6"
            />
          </svg>
        </div>
      </div>

      {/* Header */}
      <header className="text-gray-600 body-font border-b-2">
        <div className="container relative mx-auto flex flex-wrap p-5 flex-col md:flex-row items-center">
          {/* Logo */}
          <Link
            href="/"
            className="flex title-font font-medium items-center text-gray-900 mb-4 md:mb-0 md:mr-0 mr-auto"
          >
            <p className="font-bold text-2xl">Exclusive</p>
          </Link>

          {/* Navigation Links */}
          <nav className="hidden md:flex md:ml-auto md:mr-auto flex-wrap items-center text-base justify-center">
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
          <div className="relative hidden md:flex">
            <InputDemo />
            <Search className="absolute top-2 right-2 text-gray-500" />
          </div>

          {/* Action Buttons */}
          <div className="hidden md:flex space-x-2">
            <Button variant="outline" size="icon" className="border-0">
              <Heart />
            </Button>
            <Button variant="outline" size="icon" className="border-0">
              <ShoppingCart />
            </Button>
          </div>

          {/* Mobile Menu Button */}
          <div className="absolute right-4 top-4">
            <SheetDemo />
          </div>
        </div>
      </header>
    </>
  );
};

export default HeaderTop;
