'use client';
import styles from '../styles/Projects.module.css';
import Link from 'next/link';
import { FaEye } from 'react-icons/fa'; // Import eye icon from react-icons

export default function Projects() {
  const projects = [
    {
      title: "Job Portal",
      description: "A modern job portal prototype built with React.js and integrated with a back-end API for job listings, allowing users to search and apply for jobs, as well as employers to post opportunities.",
      link: "https://github.com/Saad0095/Job-Portal",
      viewLink: "https://job-portal-website-project.vercel.app/", // Live project link
    },
    {
      title: "CarBaazar",
      description: "An innovative platform designed to give users a virtual showroom experience. CarBaazar lets users explore a wide range of cars and compare features, making car buying easier and more interactive.",
      link: "https://github.com/SameerAhmedBSCE/CarBazaar-React-Project",
      viewLink: "https://car-bazaar-rust.vercel.app/", // Live project link
    },
    {
      title: "Blue Sky Digitals",
      description: "A professional website built for a client in the digital services sector. This project highlights responsive design and modern UI/UX, providing the client with a platform to showcase their digital marketing services.",
      link: "https://github.com/Okashanadeem/blue-sky-digitals",
      viewLink: "https://blue-sky-digitals.vercel.app/", // Live project link
    },
    {
      title: "My Portfolio",
      description: "A professional portfolio website built with pure HTML, CSS and Tailwind, showcasing my skills, projects, and experience in web development.",
      link: "https://github.com/Okashanadeem/GIAIC/tree/main/Quarter%202/Milestones/Portfolio/my-app",
      viewLink: "https://okasha-nadeem-tailwind-portfolio.vercel.app/", // Live project link
    }    
  ];

  return (
    <div className={styles.container}>
      <h1 className={styles.heading}>My Projects</h1>
      <div className={styles.projectList}>
        {projects.map((project, index) => (
          <div key={index} className={styles.projectCard}>
            <h2 className={styles.projectTitle}>{project.title}</h2>
            <p className={styles.projectDescription}>{project.description}</p>
            <div className={styles.eyeIconContainer}>
              <a href={project.viewLink} target="_blank" rel="noopener noreferrer">
                <FaEye className={styles.eyeIcon} />
              </a>
            </div>
          </div>
        ))}
      </div>
      <p className={styles.workingMessage}>I am still working on more exciting projects! Stay tuned for updates!</p>
      <br /><br />
      <div className={styles.nextButtonContainer}>
        <Link href="/" className={styles.nextButton}>Go to Home Page</Link>
      </div>
    </div>
  );
}
