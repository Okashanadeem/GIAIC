'use client';

import { motion } from 'framer-motion';

const containerVariants = {
  hidden: { opacity: 0, y: 20 },
  visible: { opacity: 1, y: 0, transition: { duration: 1, ease: 'easeOut', staggerChildren: 0.3 } },
};

const inputVariants = {
  hidden: { opacity: 0, y: 10 },
  visible: { opacity: 1, y: 0, transition: { duration: 0.5, ease: 'easeOut' } },
};

export default function Contact() {
  return (
    <motion.section
      id="contact"
      variants={containerVariants}
      initial="hidden"
      animate="visible"
      className="relative flex flex-col items-center justify-center w-full min-h-screen px-6 py-16 text-white text-center  overflow-hidden"
    >
      {/* Parallax Background Effect */}
      <div className="absolute inset-0 z-0 bg-[radial-gradient(circle,_rgba(29,78,216,0.2)_0%,_rgba(0,0,0,0)_60%)]" />


      {/* Heading */}
      <motion.h2 variants={inputVariants} className="text-4xl md:text-6xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-cyan-300 drop-shadow-lg">
        Get in Touch
      </motion.h2>
      <motion.p variants={inputVariants} className="mt-4 text-lg md:text-xl text-gray-300 max-w-2xl">
        Ready to transform your business with AI?
      </motion.p>

      {/* Contact Info */}
      <div className="mt-6 text-gray-300 space-y-2 text-lg">
        <motion.p variants={inputVariants} className="hover:text-blue-400 transition duration-300">📧 contact@agentiaworld.com</motion.p>
        <motion.p variants={inputVariants} className="hover:text-cyan-400 transition duration-300">🌍 www.agentiaworld.com</motion.p>
      </div>

      {/* Contact Form */}
      <motion.form
        variants={containerVariants}
        className="relative mt-10 w-full max-w-3xl bg-opacity-20 bg-zinc-800 p-8 rounded-xl shadow-lg backdrop-blur-lg border border-zinc-700/50"
      >
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <motion.input
            variants={inputVariants}
            type="text"
            placeholder="First Name"
            className="w-full p-3 bg-zinc-700/50 text-white rounded-lg border border-zinc-600 focus:outline-none focus:ring-2 focus:ring-blue-400 focus:shadow-lg transition-all"
          />
          <motion.input
            variants={inputVariants}
            type="text"
            placeholder="Last Name"
            className="w-full p-3 bg-zinc-700/50 text-white rounded-lg border border-zinc-600 focus:outline-none focus:ring-2 focus:ring-blue-400 focus:shadow-lg transition-all"
          />
        </div>

        <motion.input
          variants={inputVariants}
          type="email"
          placeholder="Email Address"
          className="mt-4 w-full p-3 bg-zinc-700/50 text-white rounded-lg border border-zinc-600 focus:outline-none focus:ring-2 focus:ring-cyan-400 focus:shadow-lg transition-all"
        />

        <motion.textarea
          variants={inputVariants}
          placeholder="Your Message"
          rows={5}
          className="mt-4 w-full p-3 bg-zinc-700/50 text-white rounded-lg border border-zinc-600 focus:outline-none focus:ring-2 focus:ring-blue-400 focus:shadow-lg transition-all"
        />

        {/* Send Message Button */}
        <motion.button
          variants={inputVariants}
          type="submit"
          whileHover={{ scale: 1.05 }}
          whileTap={{ scale: 0.95 }}
          className="mt-6 w-full p-3 bg-gradient-to-r from-purple-600 to-blue-500 
      hover:scale-105 hover:shadow-xl active:scale-95 text-white font-semibold rounded-lg shadow-md transition-all duration-300"
        >
          Send Message
        </motion.button>
      </motion.form>
    </motion.section>
  );
}
