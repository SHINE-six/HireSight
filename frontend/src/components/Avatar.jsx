import { useAnimations, useFBX, useGLTF } from "@react-three/drei";
import { useFrame, useLoader } from "@react-three/fiber";
import React, { useEffect, useMemo, useRef } from "react";


const corresponding = {
  A: "viseme_PP",
  B: "viseme_kk",
  C: "viseme_I",
  D: "viseme_AA",
  E: "viseme_O",
  F: "viseme_U",
  G: "viseme_FF",
  H: "viseme_TH",
  X: "viseme_PP",
};

export function Avatar(props) {
	const voice = ["fromAI.wav", "fromAI(1).wav", "fromAI(2).wav", "fromAI(3).wav", "fromAI(4).wav", "fromAI(5).wav", "fromAI(6).wav", "fromAI(7).wav", "fromAI(8).wav"]
	const mouth = ["fromAI.json", "fromAI(1).json", "fromAI(2).json", "fromAI(3).json", "fromAI(4).json", "fromAI(5).json", "fromAI(6).json", "fromAI(7).json", "fromAI(8).json"]
	const currentVoiceRef = useRef(voice[-1])
	const currentVoiceIndex = useRef(-1)
	
    const audio = useRef(new Audio(`/audios/${currentVoiceRef.current}`));
    const lipsync = props.newJsonData;
    // const jsonFile = useLoader(THREE.FileLoader, props.newJsonData);
    // const lipsync = JSON.parse(jsonFile);

    console.log(audio, "from AVATAR");

	useEffect(() => {
		const handleKeyPress = (e) => {
			console.log(e.key);
			e.preventDefault();
			if (e.key === "a") {
				currentVoiceIndex.current = (currentVoiceIndex.current + 1) % voice.length;
				currentVoiceRef.current = voice[currentVoiceIndex.current];
				audio.current = new Audio(`/audios/${currentVoiceRef.current}`);
				console.log(currentVoiceRef.current);

				nodes.Wolf3D_Head.morphTargetInfluences[
				nodes.Wolf3D_Head.morphTargetDictionary["viseme_I"]
				] = 1;
				nodes.Wolf3D_Teeth.morphTargetInfluences[
				nodes.Wolf3D_Teeth.morphTargetDictionary["viseme_I"]
				] = 1;
				audio.current.play();
			}
		};

		window.addEventListener("keypress", handleKeyPress);

		// Cleanup function to remove the event listener when the component unmounts
		return () => {
			audio.pause();
			window.removeEventListener("keypress", handleKeyPress);
		};
	}, [audio]); // Empty dependency array means this effect runs once on mount and cleanup on unmount


    useFrame(() => {
        const currentAudioTime = audio.current.currentTime;
        if (audio.current.paused || audio.current.ended) {
        // setAnimation("Idle");
        return;
        }

        Object.values(corresponding).forEach((value) => {
            nodes.Wolf3D_Head.morphTargetInfluences[
                nodes.Wolf3D_Head.morphTargetDictionary[value]
            ] = 0;
            nodes.Wolf3D_Teeth.morphTargetInfluences[
                nodes.Wolf3D_Teeth.morphTargetDictionary[value]
            ] = 0;
        
        });

        for (let i = 0; i < lipsync.mouthCues.length; i++) {
        const mouthCue = lipsync.mouthCues[i];
        if (
            currentAudioTime >= mouthCue.start &&
            currentAudioTime <= mouthCue.end
        ) {
            nodes.Wolf3D_Head.morphTargetInfluences[
                nodes.Wolf3D_Head.morphTargetDictionary[
                corresponding[mouthCue.value]
                ]
            ] = 1.3;
            nodes.Wolf3D_Teeth.morphTargetInfluences[
                nodes.Wolf3D_Teeth.morphTargetDictionary[
                corresponding[mouthCue.value]
                ]
            ] = 1;
            break;
        }
        }
    });

    // useEffect(() => {
    //     nodes.Wolf3D_Head.morphTargetInfluences[
    //     nodes.Wolf3D_Head.morphTargetDictionary["viseme_I"]
    //     ] = 1;
    //     nodes.Wolf3D_Teeth.morphTargetInfluences[
    //     nodes.Wolf3D_Teeth.morphTargetDictionary["viseme_I"]
    //     ] = 1;

    //     audio.play();

    //     return () => {
    //       audio.pause();
    //     };

    // }, [currentVoiceRef.current]);

    const { nodes, materials } = useGLTF("/models/660ad1058d2d6c082659cc71.glb");
    // const { animations: idleAnimation } = useGLTF("/animations/Cover To Stand.fbx");
    // idleAnimation[0].tracks.forEach((track) => {
    //   track.name = track.name.replace('mixamorig', '');
    // });
    // console.log(idleAnimation, "from AVATAR");
    const group = useRef();

    // idleAnimation[0].name = "Talking";


    // const [animation, setAnimation] = useState("Talking");

    // const { actions } = useAnimations(
    //     [idleAnimation[0]],
    //     group
    // );

    // useEffect(() => {
    //     actions[animation].play();

    //     return () => {
    //       actions[animation].stop();
    //     };
    // }, []);


  return (
    <group {...props} dispose={null} ref={group}>
      <primitive object={nodes.Hips} />
      <skinnedMesh
        geometry={nodes.Wolf3D_Body.geometry}
        material={materials.Wolf3D_Body}
        skeleton={nodes.Wolf3D_Body.skeleton}
      />
      <skinnedMesh
        geometry={nodes.Wolf3D_Outfit_Bottom.geometry}
        material={materials.Wolf3D_Outfit_Bottom}
        skeleton={nodes.Wolf3D_Outfit_Bottom.skeleton}
      />
      <skinnedMesh
        geometry={nodes.Wolf3D_Outfit_Footwear.geometry}
        material={materials.Wolf3D_Outfit_Footwear}
        skeleton={nodes.Wolf3D_Outfit_Footwear.skeleton}
      />
      <skinnedMesh
        geometry={nodes.Wolf3D_Outfit_Top.geometry}
        material={materials.Wolf3D_Outfit_Top}
        skeleton={nodes.Wolf3D_Outfit_Top.skeleton}
      />
      <skinnedMesh
        geometry={nodes.Wolf3D_Hair.geometry}
        material={materials.Wolf3D_Hair}
        skeleton={nodes.Wolf3D_Hair.skeleton}
      />
      <skinnedMesh
        name="EyeLeft"
        geometry={nodes.EyeLeft.geometry}
        material={materials.Wolf3D_Eye}
        skeleton={nodes.EyeLeft.skeleton}
        morphTargetDictionary={nodes.EyeLeft.morphTargetDictionary}
        morphTargetInfluences={nodes.EyeLeft.morphTargetInfluences}
      />
      <skinnedMesh
        name="EyeRight"
        geometry={nodes.EyeRight.geometry}
        material={materials.Wolf3D_Eye}
        skeleton={nodes.EyeRight.skeleton}
        morphTargetDictionary={nodes.EyeRight.morphTargetDictionary}
        morphTargetInfluences={nodes.EyeRight.morphTargetInfluences}
      />
      <skinnedMesh
        name="Wolf3D_Head"
        geometry={nodes.Wolf3D_Head.geometry}
        material={materials.Wolf3D_Skin}
        skeleton={nodes.Wolf3D_Head.skeleton}
        morphTargetDictionary={nodes.Wolf3D_Head.morphTargetDictionary}
        morphTargetInfluences={nodes.Wolf3D_Head.morphTargetInfluences}
      />
      <skinnedMesh
        name="Wolf3D_Teeth"
        geometry={nodes.Wolf3D_Teeth.geometry}
        material={materials.Wolf3D_Teeth}
        skeleton={nodes.Wolf3D_Teeth.skeleton}
        morphTargetDictionary={nodes.Wolf3D_Teeth.morphTargetDictionary}
        morphTargetInfluences={nodes.Wolf3D_Teeth.morphTargetInfluences}
      />
    </group>
  );
}

// useGLTF.preload("/models/660ad1058d2d6c082659cc71.glb");
