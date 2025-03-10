'use client';

import Link from 'next/link';
import { useState } from 'react';
import { Menu, X } from 'lucide-react';

export default function Navbar() {
  const [isOpen, setIsOpen] = useState(false);

  const navLinks = [
    { name: 'Features', path: '/features' },
    { name: 'Technology', path: '/technology' },
    { name: 'Agents', path: '/agents' },
    { name: 'Pricing', path: '/pricing' },
    { name: 'Contact', path: '/contact' }
  ];

  return (
    <nav className="fixed top-0 left-0 w-full bg-black/10 backdrop-blur-md shadow-md z-[100]">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between items-center h-16">
          {/* Logo */}
          <div className="flex items-center">
            <a href="/" className="flex items-center space-x-2">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="24"
                height="24"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                strokeWidth="2"
                strokeLinecap="round"
                strokeLinejoin="round"
                className="lucide lucide-bot w-8 h-8 text-purple-500"
              >
                <path d="M12 8V4H8"></path>
                <rect width="16" height="12" x="4" y="8" rx="2"></rect>
                <path d="M2 14h2"></path>
                <path d="M20 14h2"></path>
                <path d="M15 13v2"></path>
                <path d="M9 13v2"></path>
              </svg>
              <span className="text-xl font-bold">Agentia World</span>
            </a>
          </div>

          {/* Desktop Menu */}
          <div className="hidden md:flex space-x-6 items-center">
            {navLinks.map(({ name, path }) => (
              <Link
                key={name}
                href={path}
                className="relative text-white hover:text-indigo-400 transition duration-300 
                after:content-[''] after:absolute after:bottom-0 after:left-0 after:w-0 after:h-0.5 
                after:bg-white after:transition-all after:duration-500 hover:after:w-full"
              >
                {name}
              </Link>
            ))}
            <Link
              href="/launch-console"
              className="px-4 py-2 rounded-lg bg-zinc-800 shadow-md border border-zinc-600 hover:border-zinc-400 hover:text-indigo-400 text-white transition duration-300"
            >
              Launch Console
            </Link>
          </div>

          {/* Mobile Menu Button */}
          <button
            onClick={() => setIsOpen(!isOpen)}
            aria-label="Toggle menu"
            aria-expanded={isOpen}
            className="md:hidden text-white p-2 rounded-md focus:outline-none focus:ring-2 focus:ring-gray-400"
          >
            {isOpen ? <X size={28} /> : <Menu size={28} />}
          </button>
        </div>
      </div>

      {/* Mobile Menu */}
      <div
        className={`md:hidden flex flex-col items-center gap-4 py-4 bg-black/80 transition-all duration-300 ${
          isOpen ? "opacity-100 max-h-screen" : "opacity-0 max-h-0 overflow-hidden"
        }`}
      >
        {navLinks.map(({ name, path }) => (
          <Link
            key={name}
            href={path}
            className="block text-white hover:text-gray-300 transition duration-300"
            onClick={() => setIsOpen(false)}
          >
            {name}
          </Link>
        ))}
        <Link
          href="/launch-console"
          className="px-4 py-2 rounded-lg bg-zinc-800 shadow-md border border-zinc-600 hover:border-zinc-400 hover:text-indigo-400 text-white transition duration-300"
          onClick={() => setIsOpen(false)}
        >
          Launch Console
        </Link>
      </div>
    </nav>
  );
}
