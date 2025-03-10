'use client';

import { motion } from 'framer-motion';
import { Brain, Code, Network, Globe } from 'lucide-react';

const containerVariants = {
  hidden: { opacity: 0, y: 20 },
  visible: { opacity: 1, y: 0, transition: { duration: 1, ease: 'easeOut', staggerChildren: 0.3 } },
};

const cardVariants = {
  hidden: { opacity: 0, scale: 0.9 },
  visible: { opacity: 1, scale: 1, transition: { duration: 0.8, ease: 'easeOut' } },
};

const aiFeatures = [
  { title: 'Neural Networks', description: 'Advanced neural architectures for complex decision making.', icon: Brain },
  { title: 'Deep Learning', description: 'Sophisticated deep learning models for pattern recognition.', icon: Code },
  { title: 'Advanced ML', description: 'Cutting-edge machine learning algorithms.', icon: Network },
  { title: 'Global Scale', description: 'Distributed AI processing across global networks.', icon: Globe }
];

export default function Technology() {
  return (
    <motion.section id="technology" variants={containerVariants} initial="hidden" animate="visible" className="relative flex flex-col items-center justify-center w-full min-h-screen px-6 py-16 text-white text-center">
      <motion.h2 variants={cardVariants} className="text-3xl md:text-5xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-cyan-300">
        Powered by Advanced AI
      </motion.h2>
      <motion.p variants={cardVariants} className="mt-4 text-lg md:text-xl text-gray-300 max-w-3xl">
        Built on cutting-edge neural architectures
      </motion.p>

      {/* AI Features Grid */}
      <div className="mt-12 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-2 gap-8 max-w-5xl mx-auto">
        {aiFeatures.map((feature, index) => (
          <motion.div key={index} variants={cardVariants} className="p-8 rounded-xl border border-zinc-700 bg-zinc-900/50 backdrop-blur-md shadow-lg transition-all duration-500 hover:bg-transparent hover:border-blue-400 hover:shadow-lg hover:scale-105">
            <feature.icon className="w-12 h-12 text-blue-400 mb-4 mx-auto hover:text-orange-700 transition-all duration-500" />
            <h3 className="text-2xl font-semibold text-blue-400">{feature.title}</h3>
            <p className="mt-3 text-gray-300 text-lg">{feature.description}</p>
          </motion.div>
        ))}
      </div>
    </motion.section>
  );
}
