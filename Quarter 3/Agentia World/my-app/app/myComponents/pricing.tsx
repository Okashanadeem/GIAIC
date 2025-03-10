'use client';

import { motion } from 'framer-motion';
import { DollarSign, TrendingUp, Crown } from 'lucide-react';

const containerVariants = {
  hidden: { opacity: 0, y: 20 },
  visible: { opacity: 1, y: 0, transition: { duration: 1, ease: 'easeOut', staggerChildren: 0.3 } },
};

const cardVariants = {
  hidden: { opacity: 0, scale: 0.9 },
  visible: { opacity: 1, scale: 1, transition: { duration: 0.8, ease: 'easeOut' } },
};

const pricingPlans = [
  {
    title: 'Starter',
    price: '$499/month',
    features: [
      '2 AI Agent Instances',
      'Basic Neural Processing',
      '24/7 Support',
      'Weekly Analytics',
      'Basic Integration Support'
    ],
    icon: DollarSign,
    color: 'blue-400',
  },
  {
    title: 'Professional',
    price: '$999/month',
    features: [
      '10 AI Agent Instances',
      'Advanced Neural Networks',
      'Priority Support',
      'Real-time Analytics',
      'Custom Integration',
      'API Access',
      'Advanced Security'
    ],
    icon: TrendingUp,
    color: 'orange-700',
  },
  {
    title: 'Enterprise',
    price: '$Custom',
    features: [
      'Unlimited Agents',
      'Full Neural Suite',
      'Dedicated Support Team',
      'Advanced Analytics Dashboard',
      'Custom Development',
      'Full API Access',
      'Enterprise Security',
      'Custom Training'
    ],
    icon: Crown,
    color: 'blue-400',
  }
];

export default function Pricing() {
  return (
    <motion.section id="pricing" variants={containerVariants} initial="hidden" animate="visible" className="relative flex flex-col items-center justify-center w-full min-h-screen px-6 py-16 text-white text-center">
      <motion.h2 variants={cardVariants} className="text-3xl md:text-5xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-cyan-300">
        Choose Your Plan
      </motion.h2>
      <motion.p variants={cardVariants} className="mt-4 text-lg md:text-xl text-gray-300 max-w-3xl">
        Scale your AI capabilities with our flexible pricing
      </motion.p>

      {/* Pricing Cards */}
      <div className="mt-12 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 max-w-6xl mx-auto">
        {pricingPlans.map((plan, index) => {
          const textColor = plan.color === 'orange-700' ? 'text-orange-700' : 'text-blue-400';
          const borderColor = plan.color === 'orange-700' ? 'border-orange-700' : 'border-blue-400';
          const bgColor = plan.color === 'orange-700' ? 'bg-orange-700' : 'bg-blue-400';
          
          return (
            <motion.div 
              key={index} 
              variants={cardVariants} 
              className={`p-8 rounded-xl border ${borderColor} bg-zinc-900/50 backdrop-blur-md shadow-lg transition-all duration-500 
                hover:bg-transparent hover:${borderColor} hover:shadow-lg hover:scale-105 flex flex-col h-full`}
            >
              {/* Wrapper to ensure even height distribution */}
              <div className="flex flex-col flex-grow">
                <plan.icon className={`w-12 h-12 ${textColor} mb-4 hover:${textColor} transition-all duration-500`} />
                <h3 className={`text-2xl font-semibold ${textColor}`}>{plan.title}</h3>
                <p className="mt-2 text-xl font-bold text-gray-100">{plan.price}</p>
                <ul className="mt-4 text-gray-300 text-lg space-y-2 text-left">
                  {plan.features.map((feature, i) => (
                    <li key={i} className="flex items-center">
                      <span className={`w-2 h-2 ${bgColor} rounded-full mr-2`}></span>
                      {feature}
                    </li>
                  ))}
                </ul>
              </div>

              {/* Button always at the bottom */}
              <div className="mt-auto">
                <button className={`${bgColor} relative px-6 py-3 h-14 rounded-lg text-white font-medium transition-all duration-300 shadow-lg 
      hover:scale-105 hover:shadow-xl active:scale-95 overflow-hidden group`}>
                  Get Started
                    {/* Top-Right to Center Line */}
  <span className="absolute top-0 right-0 w-0 h-0.5 bg-white opacity-0 transition-all duration-500 group-hover:w-full group-hover:opacity-100"></span>

{/* Bottom-Left to Center Line */}
<span className="absolute bottom-0 left-0 w-0 h-0.5 bg-white opacity-0 transition-all duration-500 group-hover:w-full group-hover:opacity-100"></span>

{/* Diagonal Lines Animation */}
<span className="absolute top-0 left-0 h-full border-l-2 border-white opacity-0 transition-all duration-500 group-hover:w-full group-hover:opacity-100"></span>
<span className="absolute bottom-0 right-0 h-full border-r-2 border-white opacity-0 transition-all duration-500 group-hover:w-full group-hover:opacity-100"></span>
                </button>
              </div>
            </motion.div>
          );
        })}
      </div>
    </motion.section>
  );
}
