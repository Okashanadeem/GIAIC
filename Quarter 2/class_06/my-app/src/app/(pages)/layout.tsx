export default function RootLayout({children}: any) {
  return (
    <div>
      {children}
      <h2>Hello Layout.tsx</h2>
      <p>This is this route own layout.tsx</p>
    </div>
  );
}
