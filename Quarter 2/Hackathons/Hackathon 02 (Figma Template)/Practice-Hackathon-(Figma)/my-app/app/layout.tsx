import "./globals.css";
import Footer from "./myComponents/footer";
import HeaderTop from "./myComponents/headerTop";
export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className="bg-background">
        <HeaderTop/>
        {children}
        <Footer/>
      </body>
    </html>
  );
}
