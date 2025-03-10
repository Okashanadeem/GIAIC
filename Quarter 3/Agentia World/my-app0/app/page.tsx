'use client';

import { motion } from 'framer-motion';
import ChatBubble from './myComponents/Chatbot';
import Features from './myComponents/features';
import Technology from './myComponents/Technology';
import Agents from './myComponents/Agents';
import Pricing from './myComponents/pricing';
import Contact from './myComponents/Contact';
import Footer from './myComponents/Footer';

const containerVariants = {
  hidden: { opacity: 0, y: 20 },
  visible: { opacity: 1, y: 0, transition: { duration: 1, ease: 'easeOut', staggerChildren: 0.3 } },
};

const cardVariants = {
  hidden: { opacity: 0, scale: 0.9 },
  visible: { opacity: 1, scale: 1, transition: { duration: 0.8, ease: 'easeOut' } },
};

const skillVariants = {
  hidden: { opacity: 0, y: 10 },
  visible: { opacity: 1, y: 0, transition: { duration: 0.5, ease: 'easeOut' } },
};

export default function Home() {

  const topLeters = [
    { name: "Autonomy", description: "AI agents that think and act independently." },
    { name: "Intelligence", description: "Harnessing advanced AI for smarter decisions." },
    { name: "Efficiency", description: "Optimizing workflows with AI-driven automation." },
  ];


  return (
    <motion.section
      id="Home"
      variants={containerVariants}
      initial="hidden"
      animate="visible"
      className="relative overflow-hidden flex flex-col items-center justify-center w-full min-h-screen px-6 py-12 text-zinc-300"
    >

      <div className='mt-20'>
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 1, ease: "easeOut" }}
          className="flex flex-col items-center justify-center w-full "
        >
          {/* Navigation Words with Tooltip */}
          <motion.div
            initial={{ opacity: 0, y: -10 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.2, duration: 0.8 }}
            className="flex items-center gap-6 text-zinc-400 text-sm sm:text-xl md:text-sm animate-fade-in"
          >
            {topLeters.map((item) => (
              <div key={item.name} className="hidden  relative group md:flex flex-col items-center">
                <span className="absolute bottom-full mb-2 w-max px-2 py-1 text-sm font-mono text-zinc-200 bg-zinc-800 rounded-lg shadow-lg opacity-0 group-hover:opacity-100 transition-opacity duration-300">
                  {item.description}
                </span>
                <p className="cursor-pointer duration-500 mr-3 text-zinc-500 hover:text-zinc-400">
                  {item.name}
                </p>
              </div>
            ))}
          </motion.div>

          {/* Gradient Divider */}
          <div className=" w-screen h-px animate-glow md:block animate-fade-left bg-gradient-to-r from-zinc-300/0 via-zinc-300/50 to-zinc-300/0 mt-10" />

          {/* Animated Heading */}
          <motion.h1
            initial={{ opacity: 0, scale: 0.8 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ delay: 0.4, duration: 1, ease: "easeOut" }}
            className="z-10 py-4 text-2xl sm:text-4xlxl md:text-7xl font-extrabold text-transparent bg-clip-text  bg-gradient-to-r from-purple-400 to-blue-500 animate-fade-in"
          >
            Autonomous Intelligence
          </motion.h1>

          {/* Gradient Divider */}
          <div className=" w-screen h-px animate-glow md:block animate-fade-left bg-gradient-to-r from-zinc-300/0 via-zinc-300/50 to-zinc-300/0 mb-10" />

          {/* Animated Tagline */}
          <motion.div
            initial={{ opacity: 0, y: 10 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.6, duration: 1 }}
            className="text-center animate-fade-in"
          >
            <h2 className="text-sm text-zinc-500">
              <p>Shaping the Future of AI Agents</p>
            </h2>
          </motion.div>
        </motion.div>
      </div>


      {/* ChatBubble Section */}
      <ChatBubble />

      <Features/>

      <Technology/>

      <Agents/>

      <Pricing/>

      <Contact/>

      <Footer/>
    </motion.section>
  );
}
