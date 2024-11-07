'use client';
import Image from 'next/image';
import Link from 'next/link';
import styles from '../styles/About.module.css';
import img from '../../../images/IMG_20241014_104257.jpg';
import { FaHtml5, FaCss3Alt, FaJsSquare, FaReact, FaGithub, FaFileCode } from 'react-icons/fa';

export default function About() {
  return (
    <div className={styles.container}>
      <h1 className={styles.heading}>About Me</h1>
      <section className={styles.aboutWrapper}>
        <div className={styles.aboutContent}>
          <div className={styles.paragraphBox}>
            <p>
              Hi, I'm Okasha Nadeem, an 18-year-old tech enthusiast and a second-year Computer Science student at D.J. Science College in Karachi, Pakistan. With a deep passion for technology and a drive to make a positive impact, I specialize in web development, focusing on front-end technologies like HTML, CSS, JavaScript, TypeScript, and React.js, Next.js. I'm also expanding my skills into Full Stack Development, including Node.js, MongoDb, Express.js.
            </p>

            <p>
              Along with my academic journey, I serve as the Class Representative, where I nurture my leadership skills. My aspirations in tech include becoming a Software Engineer and delving into cutting-edge fields like AI, Cloud Computing, Web 3, and the Metaverse. I'm also on the path to becoming a Certified Cloud Applied Generative AI Engineer.
            </p>

            <p>
              Through my work as an English teacher, I’ve developed strong communication abilities, making complex ideas accessible and clear. I am committed to delivering high-quality work on time, pushing boundaries with creativity and innovation, and fostering collaboration in every project.
            </p>
          </div>
        </div>

        <div className={styles.photoWrapper}>
          <Image src={img} alt="Okasha Nadeem" className={styles.photo} />
        </div>
      </section>

      <section className={styles.skills}>
        <h2>My Skills</h2>
        <div className={styles.skillIcons}>
          <div className={styles.iconContainer}>
            <FaHtml5 className={styles.icon} />
            <span>HTML</span>
          </div>
          <div className={styles.iconContainer}>
            <FaCss3Alt className={styles.icon} />
            <span>CSS</span>
          </div>
          <div className={styles.iconContainer}>
            <FaJsSquare className={styles.icon} />
            <span>JavaScript</span>
          </div>
          <div className={styles.iconContainer}>
            <FaReact className={styles.icon} />
            <span>React.js</span>
          </div>
          <div className={styles.iconContainer}>
            <FaFileCode className={styles.icon} />
            <span>TypeScript</span>
          </div>
          <div className={styles.iconContainer}>
            <FaGithub className={styles.icon} />
            <span>Git/GitHub</span>
          </div>
        </div>
      </section>
      <br />
      <div className={styles.nextButtonContainer}>
        <Link href="/projects" className={styles.nextButton}>View my Projects</Link>
      </div>
    </div>
  );
}
