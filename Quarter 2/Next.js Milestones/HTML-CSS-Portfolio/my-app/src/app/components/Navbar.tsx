'use client';
import Link from 'next/link';
import { FaBars, FaTimes } from 'react-icons/fa';
import { useState } from 'react';
import styles from '../styles/Navbar.module.css';

export default function Navbar() {
  const [isOpen, setIsOpen] = useState(false);

  const toggleMenu = () => setIsOpen(!isOpen);

  const handleMenuClick = () => {
    if (isOpen) {
      setIsOpen(false);  // Close the menu when a menu item is clicked
    }
  };

  return (
    <nav className={styles.navbar}>
      <div className={styles.logo}>
        <h2><span>&lt;Okasha. /&gt;</span></h2>
      </div>
      <div className={`${styles.menu} ${isOpen ? styles.open : ''}`}>
        <ul>
          <li>
            <Link href="/" onClick={handleMenuClick}>Home</Link>
          </li>
          <li>
            <Link href="/about" onClick={handleMenuClick}>About</Link>
          </li>
          <li>
            <Link href="/projects" onClick={handleMenuClick}>Projects</Link>
          </li>
        </ul>
      </div>
      <div className={styles.toggle} onClick={toggleMenu}>
        {isOpen ? <FaTimes /> : <FaBars />}
      </div>
    </nav>
  );
}
