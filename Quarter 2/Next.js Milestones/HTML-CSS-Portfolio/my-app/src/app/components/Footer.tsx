// src/app/components/Footer.tsx
import { FaGithub } from 'react-icons/fa';
import styles from '../styles/Footer.module.css';

const Footer = () => {
  return (
    <footer className={styles.footer}>
      <div className={styles.footerContent}>
        <p>&copy; 2024 Okasha Nadeem. All rights reserved.</p>
        <div className={styles.socialLinks}>
          <a href="https://github.com/Okashanadeem" target="_blank" rel="noopener noreferrer">
            <FaGithub /> GitHub
          </a>
        </div>
      </div>
    </footer>
  );
}

export default Footer;
