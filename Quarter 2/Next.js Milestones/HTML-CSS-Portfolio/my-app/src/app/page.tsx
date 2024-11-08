'use client';
import { FaGithub, FaLinkedin, FaEnvelope } from 'react-icons/fa';
import { useState, useEffect } from 'react';
import styles from './styles/Home.module.css';
import Link from 'next/link';

export default function Home() {
  const words = ["Hello!", "Salam!", "Konnichiwa!", "Hola!", "Namaste!"];
  const [currentWordIndex, setCurrentWordIndex] = useState(0);
  const [displayedText, setDisplayedText] = useState('');
  const [isDeleting, setIsDeleting] = useState(false);

  useEffect(() => {
    const typingSpeed = isDeleting ? 50 : 100; // Faster speed when deleting
    const currentWord = words[currentWordIndex];

    const handleTyping = setTimeout(() => {
      if (!isDeleting) {
        // Typing forward
        setDisplayedText((prevText) => currentWord.slice(0, prevText.length + 1));
        if (displayedText === currentWord) {
          setTimeout(() => setIsDeleting(true), 1000); // Pause before deleting
        }
      } else {
        // Deleting backward
        setDisplayedText((prevText) => prevText.slice(0, -1));
        if (displayedText === '') {
          setIsDeleting(false);
          setCurrentWordIndex((prevIndex) => (prevIndex + 1) % words.length); // Move to next word
        }
      }
    }, typingSpeed);

    return () => clearTimeout(handleTyping);
  }, [displayedText, isDeleting, currentWordIndex, words]);

  return (
    <div className={styles.container}>
      <section className={styles.hero}>
        <div className={styles.nameDiv}>
          <h1>Okasha Nadeem</h1>
          <p><br /><br /></p>
          <p>Passionate about technology and innovation.</p>
        </div>
      </section>
      
      <section className={styles.mainContent}>
        <div className={styles.about}>
          <h2 className={styles.typingEffect}>{displayedText}</h2>
          <p className={styles.aboutParagraph}>I&apos;m a developer who loves building applications that improve lives. With a strong foundation in front-end and back-end technologies, I&apos;m always exploring new challenges and ways to innovate.</p>
        </div>
        
        <div className={styles.contact}>
          <h2>Contact</h2>
          <br />
          <div className={styles.socialLinks}>
            <a href="https://github.com/Okashanadeem" target="_blank" rel="noopener noreferrer">
              <FaGithub /> GitHub
            </a>
            <a href="https://www.linkedin.com/in/okasha-nadeem/" target="_blank" rel="noopener noreferrer">
              <FaLinkedin /> LinkedIn
            </a>
            <a href="mailto:okashanadeem0101@gmail.com">
              <FaEnvelope /> Email
            </a>
          </div>
        </div>
      </section>

      <div className={styles.nextButtonContainer}>
        <Link href="/about" className={styles.nextButton}>Go to About Page</Link>
      </div>
    </div>
  );
}
