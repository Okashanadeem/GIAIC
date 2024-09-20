import { IntroStatic } from "./components/IntroStatic";
import { IntroDynamic } from "../app/components/IntroDynamic";

export default function Home() {
  return (
    <>
      <IntroStatic /> 
      <IntroDynamic name="Okasha" age={18} />
      <IntroDynamic name="Ayesha" age={17} />
    </>
  );
}
