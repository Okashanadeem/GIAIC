'use client';

import { motion } from 'framer-motion';
import { Building, BrainCircuit, ShieldCheck } from 'lucide-react';

const containerVariants = {
  hidden: { opacity: 0, y: 20 },
  visible: { opacity: 1, y: 0, transition: { duration: 1, ease: 'easeOut', staggerChildren: 0.3 } },
};

const cardVariants = {
  hidden: { opacity: 0, scale: 0.9 },
  visible: { opacity: 1, scale: 1, transition: { duration: 0.8, ease: 'easeOut' } },
};

const aiSolutions = [
  { title: 'Enterprise AI', description: 'Custom AI agents designed for enterprise-scale operations and decision-making.', icon: Building },
  { title: 'Neural Operations', description: 'Automated workflow optimization through distributed neural networks.', icon: BrainCircuit },
  { title: 'Secure Intelligence', description: 'Privacy-first AI solutions with military-grade security protocols.', icon: ShieldCheck }
];

export default function Agents() {
  return (
    <motion.section id="agents" variants={containerVariants} initial="hidden" animate="visible" className="relative flex flex-col items-center justify-center w-full min-h-screen px-6 py-16 text-white text-center">
      <motion.h2 variants={cardVariants} className="text-3xl md:text-5xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-cyan-300">
        AI Solutions
      </motion.h2>
      <motion.p variants={cardVariants} className="mt-4 text-lg md:text-xl text-gray-300 max-w-3xl">
        Transforming industries with intelligent agents
      </motion.p>

      {/* AI Solutions Grid */}
      <div className="mt-12 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 max-w-5xl mx-auto">
        {aiSolutions.map((solution, index) => (
          <motion.div key={index} variants={cardVariants} className="p-8 rounded-xl border border-zinc-700 bg-zinc-900/50 backdrop-blur-md shadow-lg transition-all duration-500 hover:bg-transparent hover:border-blue-400 hover:shadow-lg hover:scale-105">
            <solution.icon className="w-12 h-12 text-blue-400 mb-4 mx-auto hover:text-orange-700 transition-all duration-500" />
            <h3 className="text-2xl font-semibold text-blue-400">{solution.title}</h3>
            <p className="mt-3 text-gray-300 text-lg">{solution.description}</p>
          </motion.div>
        ))}
      </div>
    </motion.section>
  );
}
