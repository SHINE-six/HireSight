import { Environment, OrbitControls, useTexture } from "@react-three/drei";
import { useThree } from "@react-three/fiber";
import { Avatar } from "./Avatar";
import { memo } from "react";

interface ExperienceProps {
  newAudioURL: string | null;
  newJsonData: any;
}

const Experience: React.FC<ExperienceProps> = memo(({ newAudioURL, newJsonData }) => {
  const texture = useTexture("models/offic.png");
  const viewport = useThree((state) => state.viewport);

  return (
    <>
      <Avatar position={[0, -3, 2]} scale={2} newAudioURL={newAudioURL} newJsonData={newJsonData}/>
      <Environment preset="sunset" />
      <mesh>
        <planeGeometry args={[viewport.width, viewport.height]} />
        <meshBasicMaterial map={texture} />
      </mesh>
    </>
  );
}, (prev, next) => {
  return prev.newAudioURL === next.newAudioURL && prev.newJsonData === next.newJsonData;
});

export default Experience;

// import { Environment, OrbitControls, useTexture } from "@react-three/drei";
// import { useThree } from "@react-three/fiber";
// import { Avatar } from "./Avatar";
// import { memo } from "react";

// interface ExperienceProps {
//   newAudioURL: string | null;
//   newJsonData: any;
// }

// const Experience: React.FC<ExperienceProps> = memo(({ newAudioURL, newJsonData }) => {
// //   const texture = useTexture("textures/youtubeBackground.jpg");
//   const viewport = useThree((state) => state.viewport);

//   return (
//     <>
//       <Avatar position={[0, -3, 2]} scale={2} newAudioURL={newAudioURL} newJsonData={newJsonData}/>
//       <Environment preset="sunset" />
//       <mesh>
//         <planeGeometry args={[viewport.width, viewport.height]} />
//         {/* <meshBasicMaterial map={texture} /> */}
//       </mesh>
//     </>
//   );
// }, (prev, next) => {
//   return prev.newAudioURL === next.newAudioURL && prev.newJsonData === next.newJsonData;
// });

// export default Experience;

