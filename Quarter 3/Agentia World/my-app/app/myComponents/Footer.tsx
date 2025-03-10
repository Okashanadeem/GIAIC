'use client';

import { motion } from 'framer-motion';
import Link from 'next/link';

const footerVariants = {
  hidden: { opacity: 0, y: 20 },
  visible: { opacity: 1, y: 0, transition: { duration: 0.8, ease: 'easeOut', staggerChildren: 0.15 } },
};

const linkVariants = {
  hidden: { opacity: 0, y: 10 },
  visible: { opacity: 1, y: 0, transition: { duration: 0.5, ease: 'easeOut' } },
};

export default function Footer() {
  return (
    <motion.footer
      variants={footerVariants}
      initial="hidden"
      animate="visible"
      className="relative w-full text-white px-6 md:px-20 py-12 mt-8"
    >
      <div className="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-4 gap-10 text-center md:text-left">
        {/* Logo & Description */}
        <motion.div variants={linkVariants} className="space-y-4">
          <div className="flex justify-center md:justify-start items-center space-x-3">
            <a href="/" className="flex items-center space-x-2">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="28"
                height="28"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                strokeWidth="2"
                strokeLinecap="round"
                strokeLinejoin="round"
                className="lucide lucide-bot text-purple-500"
              >
                <path d="M12 8V4H8"></path>
                <rect width="16" height="12" x="4" y="8" rx="2"></rect>
                <path d="M2 14h2"></path>
                <path d="M20 14h2"></path>
                <path d="M15 13v2"></path>
                <path d="M9 13v2"></path>
              </svg>
              <span className="text-2xl font-bold tracking-wide">Agentia World</span>
            </a>
          </div>
          <p className="text-gray-400 text-sm leading-relaxed">
            Next-generation AI agents powering the future of enterprise intelligence.
          </p>
        </motion.div>

        {/* Product Links */}
        <motion.div variants={linkVariants} className="space-y-3">
          <h3 className="text-gray-400 font-semibold text-lg">Product</h3>
          <ul className="space-y-2">
            {['Features', 'Pricing', 'Documentation', 'API'].map((item) => (
              <li key={item}>
                <Link href={`#${item.toLowerCase()}`} className="text-gray-300 hover:text-blue-400 transition">
                  {item}
                </Link>
              </li>
            ))}
          </ul>
        </motion.div>

        {/* Company Links */}
        <motion.div variants={linkVariants} className="space-y-3">
          <h3 className="text-gray-400 font-semibold text-lg">Company</h3>
          <ul className="space-y-2">
            {['About', 'Blog', 'Careers', 'Contact'].map((item) => (
              <li key={item}>
                <Link href={`#${item.toLowerCase()}`} className="text-gray-300 hover:text-blue-400 transition">
                  {item}
                </Link>
              </li>
            ))}
          </ul>
        </motion.div>

        {/* Legal Links */}
        <motion.div variants={linkVariants} className="space-y-3">
          <h3 className="text-gray-400 font-semibold text-lg">Legal</h3>
          <ul className="space-y-2">
            {['Privacy', 'Terms', 'Security', 'Compliance'].map((item) => (
              <li key={item}>
                <Link href={`#${item.toLowerCase()}`} className="text-gray-300 hover:text-blue-400 transition">
                  {item}
                </Link>
              </li>
            ))}
          </ul>
        </motion.div>
      </div>

      {/* Copyright Section */}
      <motion.div
        variants={linkVariants}
        className="mt-10 pt-6 text-center text-gray-400 text-sm"
      >
        © 2025 Agentia World. Powered by <span className="text-blue-400">Panaversity</span>. All rights reserved.
      </motion.div>
    </motion.footer>
  );
}
