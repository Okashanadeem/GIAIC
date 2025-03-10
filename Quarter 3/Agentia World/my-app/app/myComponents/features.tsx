'use client';

import { useState } from 'react';
import { motion } from 'framer-motion';
import { Brain, Code, Network, Globe, Cpu, Zap, ShieldCheck, Layers } from 'lucide-react';

const containerVariants = {
  hidden: { opacity: 0, y: 20 },
  visible: { opacity: 1, y: 0, transition: { duration: 1, ease: 'easeOut', staggerChildren: 0.3 } },
};

const cardVariants = {
  hidden: { opacity: 0, scale: 0.9 },
  visible: { opacity: 1, scale: 1, transition: { duration: 0.8, ease: 'easeOut' } },
};

const features = [
  { title: 'Neural Networks', description: 'AI-driven pattern recognition, predictions, and decision-making for healthcare and automation.', icon: Brain, size: 'md:col-span-1' },
  { title: 'Deep Learning', description: 'Leveraging deep learning, our AI processes vast amounts of unstructured data such as images, videos, and speech.', icon: Code, size: 'md:col-span-2' },
  { title: 'Global Scale', description: 'Our AI runs seamlessly across cloud and edge devices, processing vast datasets in real time.', icon: Globe, size: 'md:col-span-1' },
  { title: 'Autonomous Agents', description: 'Our AI agents make independent decisions based on real-time data, predefined goals, and environmental analytics.', icon: Cpu, size: 'md:col-span-2' },
  { title: 'Real-time Processing', description: 'With near-instant responsiveness, our AI processes data streams in real time.', icon: Zap, size: 'md:col-span-1' },
  { title: 'Secure AI', description: 'Security is at the core of our AI, integrating advanced encryption, strict access controls, and real-time threat detection.', icon: ShieldCheck, size: 'md:col-span-2' },
  { title: 'Advanced ML', description: 'Our cutting-edge machine learning models evolve through self-improvement, optimizing efficiency.', icon: Network, size: 'md:col-span-2' },
  { title: 'Multi-layer AI', description: 'By integrating deep learning, symbolic reasoning, and contextual awareness, our AI achieves high adaptability.', icon: Layers, size: 'md:col-span-1' }
];

export default function Features() {
  const [showAll, setShowAll] = useState(false);

  return (
    <motion.section id="features" variants={containerVariants} initial="hidden" animate="visible" className="relative flex flex-col items-center justify-center w-full min-h-screen px-6 py-16 text-white text-center">
      <motion.h2 variants={cardVariants} className="text-3xl md:text-5xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-cyan-300">
        Powered by Agentic AI
      </motion.h2>
      <motion.p variants={cardVariants} className="mt-4 text-lg md:text-xl text-gray-300 max-w-3xl">
        Experience the future of AI with self-learning, autonomous, and adaptive intelligence that operates at a global scale.
      </motion.p>

      {/* Features Grid */}
      <div className="mt-12 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 max-w-7xl mx-auto">
        {(showAll ? features : features.slice(0, 4)).map((feature, index) => (
          <motion.div key={index} variants={cardVariants} className={`p-8 rounded-xl border border-zinc-700 bg-zinc-900/50 backdrop-blur-md shadow-lg transition-all duration-500 hover:bg-transparent hover:border-blue-400 hover:shadow-lg hover:scale-105 ${feature.size} w-full`}>
            <feature.icon className="w-12 h-12 text-blue-400 mb-4 mx-auto hover:text-orange-700 transition-all duration-500" />
            <h3 className="text-2xl font-semibold text-blue-400">{feature.title}</h3>
            <p className="mt-3 text-gray-300 text-lg">{feature.description}</p>
          </motion.div>
        ))}
      </div>

      {/* Read More Button */}
      <button onClick={() => setShowAll(!showAll)} className="mt-8 px-6 py-3 bg-gradient-to-r from-blue-500 to-orange-700 hover:border-white hover:shadow-lg hover:scale-105 text-white font-semibold rounded-lg shadow-md transition-all">
        {showAll ? 'Show Less' : 'Read More'}
      </button>
    </motion.section>
  );
}
