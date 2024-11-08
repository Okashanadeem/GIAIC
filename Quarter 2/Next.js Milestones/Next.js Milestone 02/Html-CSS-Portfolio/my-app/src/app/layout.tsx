// app/layout.tsx
import Navbar from '../app/components/Navbar';
import Footer from './components/Footer';
import '../app/globals.css'

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <head>
        <title>My Portfolio</title>
        <meta name="description" content="Welcome to my personal portfolio" />
      </head>
      <body>
        <Navbar />
        <main>{children}</main>
        <Footer />
      </body>
    </html>
  );
}
