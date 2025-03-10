'use client';

import { motion } from 'framer-motion';

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

export default function About() {
  return (
    <motion.section
      id="about"
      variants={containerVariants}
      initial="hidden"
      animate="visible"
      className="relative overflow-hidden flex flex-col items-center justify-center w-full min-h-screen px-6 py-12 text-zinc-300"
    >
      <div className="grid grid-cols-1 md:grid-cols-2 gap-12 max-w-5xl w-full items-center text-center md:text-left mt-12">
        {/* About Me Section */}
        <motion.div variants={cardVariants} className="p-6 rounded-xl border border-zinc-700 bg-zinc-900/50 backdrop-blur-md shadow-lg">
          <p className="text-lg sm:text-xl text-zinc-400 leading-relaxed">
            I'm <span className="text-white font-semibold">Okasha Nadeem</span>, a results-driven Full Stack Developer with expertise in Next.js, React.js, and TypeScript. Passionate about building scalable, high-performance web applications, I focus on optimizing user experience, SEO, and performance to deliver seamless digital solutions.
          </p>
        </motion.div>

        {/* Experience Section */}
        <motion.div variants={cardVariants} className="p-6 rounded-xl border border-zinc-700 bg-zinc-900/50 backdrop-blur-md shadow-lg">
          <h3 className="text-2xl font-semibold text-white">Experience</h3>
          <p className="mt-4 text-lg text-zinc-400 leading-relaxed">
            Over 2 years of experience building scalable web apps and e-commerce platforms with Next.js, React, and TypeScript. I focus on performance, SEO, and seamless user experiences, integrating solutions like Sanity CMS to enhance efficiency.
          </p>
        </motion.div>
      </div>

      {/* Skills & Projects Section */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-12 max-w-5xl w-full items-center text-center md:text-left mt-12">
        {/* Skills Section */}
        <motion.div variants={cardVariants} className="p-6 rounded-xl border border-zinc-700 bg-zinc-900/50 backdrop-blur-md shadow-lg">
          <h3 className="text-2xl font-semibold text-white mb-4">Skills</h3>
          <div className="flex flex-wrap justify-center md:justify-start gap-3">
            {['Next.js', 'React', 'TypeScript', 'Tailwind CSS', 'Node.js', 'Sanity CMS', 'Git', 'Css', 'Html'].map((skill) => (
              <motion.span
                key={skill}
                variants={skillVariants}
                whileHover={{ scale: 1.1 }}
                transition={{ type: 'spring', stiffness: 300 }}
                className="px-4 py-2 rounded-lg bg-zinc-800 shadow-md border border-zinc-600 hover:border-zinc-400 hover:text-indigo-400 text-white  transition duration-300"
              >
                {skill}
              </motion.span>
            ))}
          </div>
        </motion.div>

        {/* Projects Section */}
        <motion.div variants={cardVariants} className="p-6 rounded-xl border border-zinc-700 bg-zinc-900/50 backdrop-blur-md shadow-lg">
          <h3 className="text-2xl font-semibold text-white mb-4">Projects Done</h3>
          <ul className="list-disc list-inside text-lg text-zinc-400 leading-relaxed space-y-2">
            <motion.li variants={skillVariants}>Developed 20+ scalable web applications</motion.li>
            <motion.li variants={skillVariants}>Optimized marketplace platform (improved speed by 35%)</motion.li>
            <motion.li variants={skillVariants}>Integrated CMS for seamless content management</motion.li>
          </ul>
        </motion.div>
      </div>

      {/* Call-to-Action Section */}
      <motion.div variants={cardVariants} className="mt-16 p-6 rounded-xl border border-zinc-700 bg-zinc-900/50 backdrop-blur-md shadow-lg text-center max-w-3xl w-full">
        <h3 className="text-3xl font-semibold text-white">Let's Work Together</h3>
        <p className="mt-2 text-lg text-zinc-400">
          I'm open to collaborations, freelance projects, and new opportunities. Let's create something amazing!
        </p>
        <div className="flex flex-wrap justify-center items-center gap-4 mt-6">
          <a href="https://www.linkedin.com/in/okasha-nadeem" target="_blank" rel="noopener noreferrer" className="px-4 py-2 rounded-lg bg-zinc-800 shadow-md border border-zinc-600 hover:border-zinc-400 hover:text-indigo-400 text-white  transition duration-300">
            Let's Connect
          </a>
          <a href="/resume/resume.pdf" download className="px-4 py-2 rounded-lg bg-zinc-800 shadow-md border border-zinc-600 hover:border-zinc-400 hover:text-indigo-400 text-white  transition duration-300">
            Download Resume
          </a>
          <a href="https://www.upwork.com/freelancers/~01abaa64963c1f56cb" target="_blank" rel="noopener noreferrer" className="px-4 py-2 rounded-lg bg-zinc-800 shadow-md border border-zinc-600 hover:border-zinc-400 hover:text-indigo-400 text-white  transition duration-300">
            Hire Me
          </a>
        </div>
      </motion.div>
    </motion.section>
  );
}
