# Game Design Document Template

## Table of Contents

- [What is this Document](#doc-intro)
1. [Document Information](#info)
2. [What is the Game and Why the Game?](#concept)
3. [Genre & Platform](#genre)
4. [Settings: World & Story](#game-world)
5. [Gameplay & Mechanics](#gameplay)
6. [Characters & Entities](#characters)
7. [Art & Sound](#art-sound)
8. [User Interface](#ui)
9. [Extra Content & DLC](#extra-content)

---

## <a name="doc-intro">What is this Document?</a>

*Welcome to this Game Design Document (GDD), which is a comprehensive reference guide and definition document that outlines the core aspects of Rubik's Evo Portaland. The concrete definition helps ensure that all stakeholders are aligned and working towards a cohesive final product, and it can help you to make informed decisions. It is a living dynamic design bible (which you hold one, refer to, but not often open) that will evolve and adapt as the game progresses through various stages of development.*

*There is no "perfect" GDD, but any team member, even newcomers, should be able to use it to answer {what, why, and how} is the game and  to understand their respective resonsibilities, workload, and authorities*

---

## <a name="info">1. Document Information</a>

### LOGO

- [LOGO]

### Title & Version

- **Title**: Rubik's Evo Portaland
- **Version**: 1.0

### Author

- **Author**: Yongcheng Liu

### Original IP or Licensed Property

- **Original IP**: Yes
- **Licensed Property**: N/A

### Document Contents Update

- **Update History**: 4/23/2023 - V1 

---

## <a name="concept"> 2. What is the Game and Why the Game? </a>

### Elevator Pitch

- Rubik's Evo Portaland is an innovative, retro-style game that takes players on a puzzle-solving journey within a 3D Rubik's Cube, experienced through a seemingly 2D viewpoint. The game features various mini-game style levels, exploring different dimensions and utilizing unique gameplay mechanics to uncover a hidden narrative. The game also includes a romantic subplot involving the protagonist and another egg, Xunuo, in the world. The overall experience is designed to be engaging and enjoyable for players who love retro games, puzzles, and exploration.

### Project Goals

- **Expected Player Engagement**: Provide players with a sense of accomplishment as they progress through the game and unveil the hidden story. Keep players engaged and motivated to continue playing through engaging levels with unique core mechanics, dimension-switching, and color-based progression.
- **Project Requirements**: 
  - Develop a captivating and mysterious narrative, intertwined with a romantic subplot.
    - Create various mini-game style levels inspired by classic retro games, such as snake, platformer, brick, pong, and flappy bird.
    - Implement smooth and intuitive gameplay mechanics for dimension-switching and level transitions.
    - Design an immersive retro aesthetic that evolves through the game.
  
- **Project Objectives**: 
  - Objective 1: Create an immersive and evolving experience that encourages exploration and puzzle-solving.
    - Motivation: Provide players with a sense of accomplishment as they progress through the game and unveil the hidden story.
    - Goals: Develop engaging levels with unique core mechanics, dimension-switching, and color-based progression.
    - Key Performance Indicators (KPIs): High player engagement, positive feedback, and completion rates.
  - Objective 2: Develop a captivating and mysterious narrative to keep players engaged and motivated throughout the game.
    - Motivation: Enhance the game's emotional impact by adding depth to the characters and world.
    - Goals: Create relatable characters, an intriguing backstory, and a gradual revelation of the hidden narrative.
    - Key Performance Indicators (KPIs): Player attachment to characters, positive feedback on story elements, and desire for further exploration.

  - Objective 3: Deliver a visually appealing and evolving retro aesthetic that pays homage to classic games and captures players' interest.
    - Motivation: Create a sense of nostalgia and visual progression to maintain player engagement.
    - Goals: Design a distinct visual style that starts in black and white, and evolves through 4-bit, 8-bit, and 16-bit color schemes.
    - Key Performance Indicators (KPIs): Positive feedback on visual style, successful implementation of evolving color schemes, and player appreciation for the retro aesthetic.

  - Objective 4: Ensure a smooth and intuitive user experience by optimizing gameplay mechanics, controls, and level design.
    - Motivation: Offer a seamless and enjoyable experience for players that encourages continued play.
    - Goals: Refine controls, level layouts, and gameplay mechanics to create a polished and accessible game.
    - Key Performance Indicators (KPIs): Low frustration levels, positive feedback on controls and mechanics, and a high level of player satisfaction.


### Target Audience & Rating

- **Target Audience**: 
  - Primary Audience: Retro game lovers, puzzle solvers, and adventure enthusiasts who enjoy **exploration, narrative-driven experiences, and unique gameplay mechanics.**
  - Secondary Audience: Friends and close relatives of the creator, who would appreciate a fun, memorable, and exploration-driven game with a hidden self-narrative.
- **Expected ESRB/PEGI Rating**: E for Everyone

### Design/Project Philosophies and Manifestos

- **Why create this game?**: 
  1. Introduce an innovative approach to express that the digital world is not just 2D but 3D - and we can use the "transition between 2d and 3d" to provide better connection and experience to players. 
  2. Set up a "gate" between "outer public digital space" and "intra personal digital space" for the future, showcasing that digital experiences are not just about the results but also the journey (when travelling from point A to point B, which is only "clicking" in modern games / 2d experiences).
  3. Experiment with the effect of embedding narratives within games in hidden novel ways, exploring the potential of innovative storytelling methods in game design.
  
- **Why the game is different?**: Rubik's Evo Portaland stands out with its dimension-switching mechanics, evolving art style, and color-based progression, which are rarely found in other games. Additionally, the game's unique approach to storytelling and exploration of personal digital space sets it apart from other titles in the genre.

- **Manifestos/Believes**: The core principles guiding this game's development and design include gameplay innovation, visual style progression, captivating storytelling, and an exploration of personal and public digital spaces.

### Production Plan

- **Production Plan Link**: [Link]

---

## <a name="genre">3. Genre & Platform</a>

### Genre & Subgenres

- **Main genre**: Adventure
- **Subgenres** (if applicable): Puzzle, Minigame, Exploration

### Platform & Technical Requirements

- **Platform**: PC
- **Technical Requirements**: Minimal hardware requirements, compatible with most modern PCs.
- **Technical Design Document**: [Link to Technical Design Document if Needed] (This is an overview for the design team, in larger, more complex games there is usually a Technical Design Document (TDD) which gets into details only programmers and software engineers love.)
  - Game Engine: Pyxel engine for Python
  - Camera Implementation: Fixed 2D camera with smooth scrolling between connected levels
  - Game Physics: Basic 2D physics for character movement and object interactions
  - In-house Creation: Level design, character and environment art, core gameplay mechanics
  - Outsourced Assets: Sound effects and music tracks (royalty-free or licensed)
  - Developer Tools: Pyxel editor for level design and asset creation, in-engine debug tools for testing and QA
  - Expected PC Specifications: Low system requirements, compatible with Windows, macOS, and Linux systems with at least 1GB RAM and a 1.2 GHz processor

---

## <a name="game-world">4. Settings: World & Story </a>

### Game World

- **World overview**: The game takes place within a 3D Rubik's Cube. Each face of the 1x1x1 cube represents a 2D mini-game level, with edge adjacency relationships connecting the levels. The Rubik's Cube itself exists within a mysterious, abstract space that serves as a "gate" between "outer public digital space" and "intra personal digital space."

- **The Levels**: The game features multiple mini-game style levels, such as snake, platformer, brick, pong, and flappy bird. Each level is designed with unique core mechanics and visual style that evolves from black and white to 4-bit, 8-bit, and finally 16-bit color schemes. Levels are interconnected through the edge adjacency relationships within the 3D Rubik's Cube structure.

### Story & Narrative

- **Back Story**: The protagonist, an egg-shaped character, embarks on a journey to explore the Rubik's Cube world and uncover its hidden story. Throughout the game, the protagonist encounters another egg-shaped character, Xunuo, who serves as both the goal for the protagonist to chase and as a romantic interest.

- **Player Progression Outline**: The player navigates through the Rubik's Cube by switching dimensions and collecting hidden colors, which grant access to new areas and reveal the missing story. The protagonist's evolution is marked by the acquisition of new colors and the progression through increasingly complex levels. As the player progresses, they will also uncover the hidden romantic subplot between the protagonist and Xunuo.

### Exposition & Cutscenes

- **Cutscenes**: Cutscenes will be used to reveal the hidden story and provide context for the protagonist's journey, as well as develop the romantic subplot between the protagonist and Xunuo. These cutscenes will feature in-game assets and will occur at key moments in the game, such as when the player discovers a new dimension, acquires a new color, or reaches a significant milestone in the relationship with Xunuo.

---

## <a name="gameplay">5. Gameplay & Mechanics</a>

### Design Guidelines

- The game should be engaging and encourage exploration and puzzle-solving through the use of unique mechanics such as dimension-switching and color-based progression.
- The game should integrate various types of puzzles into the game world, seamlessly connecting them to the narrative and the player's progression.
- Challenges and obstacles should be designed to maintain a sense of difficulty and excitement without relying on traditional enemy characters.

### Gameplay Overview

- The game is a retro, puzzle-solving adventure game with unique dimension-switching and color-based progression mechanics. Players explore different levels within a 3D Rubik's Cube, switching between adjacent faces through gates or tunnels that may be color-coded, collecting hidden colors to access new areas and uncover the missing story.

### Game Loops

- **Core Game Loop**: Players explore levels within the Rubik's Cube, solving puzzles, and collecting hidden colors. Dimension-switching through gates or tunnels connects adjacent faces of the cube. As players progress, they unlock new dimensions and areas, revealing more of the hidden story.
- **Secondary Game Loop(s)**: Players can engage with various mini-games and challenges within certain levels, offering additional rewards and enhancing the overall experience. However, the primary focus of the game remains on the narrative, color mechanism, and dimensionality mechanic.

### Player Experience Expectation

- Players should feel intrigued and motivated to explore the Rubik's Cube, uncovering its hidden story through dimension-switching and color-based progression. The unique mechanics and challenging puzzles should provide a sense of accomplishment and satisfaction as players progress through the game. The game's difficulty will be balanced to accommodate different skill levels and playstyles, ensuring an accessible experience for all players.

- Values:
  - Exploration: Players are encouraged to explore the Rubik's Cube and discover new dimensions, levels, and hidden story elements. The game rewards curiosity and a sense of adventure.
  - Fun: The game offers a variety of mini-game-style levels and challenges, providing an enjoyable and engaging experience for players of all skill levels.
  - Growth Curves: As players collect more colors and explore new dimensions, they will uncover additional levels and challenges, allowing for a diverse and evolving gameplay experience.

### Game Mechanics

- **Core Mechanics**: Dimension-switching through color-coded gates or tunnels, and color-based progression, allowing players to access new areas and elements within the game.
- **Game Modes**: Single-player campaign mode, featuring a series of interconnected levels within the Rubik's Cube.
- **Features**: 
  - Unique core mechanics for each level, ranging from platforming to top-down snake gameplay, and various mini-games and challenges.


### Controls & Camera

- **Controls**: The game will utilize keyboard controls, with players using arrow keys to move the protagonist and additional keys for actions such as interacting with objects, switching dimensions, or opening gates and tunnels.
- **Camera**: The game will feature a 2D perspective, with the camera following the protagonist as they navigate through the levels within the Rubik's Cube. The camera will smoothly transition between dimensions and levels, maintaining a clear and consistent view of the gameplay.

---

## 6. Characters & Entities

### Character Matrix

- **Properties**: Name
- **Skills and Abilities**: Movement, Collision
- **Modifiers**: None
- **Common Animation Types**: Idle, movement, interaction, dimension-switching

### Main Characters

- **Character Name**: Protagonist
  - **Character Matrix**: 
    - Name: DANDAN, protagonist
    - Egg-shaped character
    - Color: Evolving throughout the game. Starting from black and then black & white. Each new color will stack up. (total 16, so each new color will stack up 1/16)
    - Abilities: Dimension-switching, color collection
  - **Character Settings**:
    - Background: An egg-shaped character embarking on a journey to explore the Rubik's Cube and uncover its hidden story.
    - Characteristics:
      - Traits: Curious, determined, adventurous
      - Motivations: Uncover the hidden story within the Rubik's Cube and reach the Cute Egg.
    - Behaviors: 
    - Progression:
      - The protagonist makes decisions based on their curiosity and desire to explore the Rubik's Cube. 
      - TO FILL
    - Depth: 
      - TO FILL
  - **Concept Art**: 
    - TO FILL
  - **Creator Notes**:
    - Design Intentions: Create a relatable and engaging protagonist that encourages players to explore the Rubik's Cube and uncover its hidden story.
    - Additional Notes: The protagonist's appearance will evolve as they collect colors throughout the game.

### Non-playable Characters (NPCs)

- **Character Name**: Xunuo
- **Role**: Xunuo serves as a goal for the protagonist throughout the game, driving them to continue exploring the Rubik's Cube. Xunuo also plays a role in the romantic subplot.
  - **Appearance**: Similar to the protagonist, Xunuo is an egg-shaped character, distinguished by a unique color or pattern.
  - **Backstory**: Xunuo's backstory is mysterious and unfolds as the player uncovers the hidden story within the Rubik's Cube.

---

## 7. Art & Sound

### Visual Style

- The visual style of Rubik's Evo Portaland is primarily retro, starting with a black and white color palette and evolving through 4-bit, 8-bit, and 16-bit color schemes. The game's art style is inspired by classic pixel art games, with detailed environments and characters that pay homage to the retro gaming era. The visual style will also incorporate elements of the Rubik's Cube, showcasing the transition between dimensions and the use of colors to unlock new areas and reveal hidden story elements.

### Reference Arts

- [TO FILL]<img> [Explanation]: Examples of retro pixel art games, showcasing the different color schemes and visual styles that will be used in Rubik's Evo Portaland.

### Concept Arts

- [TO FILL]<img> [Explanation]: Early sketches of the protagonist egg character, Xunuo, and various level designs, showcasing the game's retro art style and evolving color schemes.
- [TO FILL]<img> [Explanation]: Concept art of the Rubik's Cube world, including the different dimensions and interconnected levels that players will explore throughout the game.

### Character & Object Design

- **Protagonist Egg Character**
  - Design Style: Retro pixel art, evolving color schemes
  - Visual Themes: Rubik's Cube, exploration, transformation
  - Concept Art: [TO FILL]<img> [Explanation]: Early sketches and concept art of the protagonist egg character, showcasing its progression through the game's color schemes.

- **Xunuo**
  - Design Style: Retro pixel art, evolving color schemes
  - Visual Themes: Rubik's Cube, chase, goal
  - Concept Art: [TO FILL]<img> [Explanation]: Early sketches and concept art of Xunuo, showcasing its progression through the game's color schemes.

### Environment Design

- **Rubik's Cube World**
  - Design Style: Retro pixel art, evolving color schemes
  - Visual Themes: Rubik's Cube, dimensions, interconnected levels
  - Concept Art: [TO FILL]<img> [Explanation]: Concept art of the Rubik's Cube world, showcasing the transition between dimensions and the use of colors to unlock new areas and reveal hidden story elements.

---

## 8. User Interface (UI)

### HUD

- The game's HUD will be minimalistic, focusing on exploration and puzzle-solving. The protagonist's shell will visualize the collected colors, allowing players to easily track their progress. In the majority of the gameplay, the player will be able to see a 16x16 screen, except when certain items or abilities are acquired. The HUD will also evolve along with the game's visual style, transitioning between black and white, 4-bit, 8-bit, and 16-bit color schemes.

### User Flow & Screens

- The user flow will be designed to facilitate a seamless gameplay experience, guiding players through various stages of the game while emphasizing exploration and discovery. Key components of the user flow include:

  - **In-Game**: Players will navigate through levels, solving puzzles and collecting colors. The user interface will be minimalistic, with the protagonist's shell displaying the collected colors. 

  - **Item Collection**: As players progress through the game, they will collect various items, including UI elements that enhance their gameplay experience. These items may unlock new abilities, grant access to new areas, or reveal hidden story elements. The collected items will be displayed in an appropriate section of the HUD, making it easy for players to keep track of their inventory.

  - **Game Start**: The game will begin immediately upon clicking, without a traditional main menu or level selection screen. This design choice emphasizes the focus on exploration and discovery, allowing players to dive right into the game world and start their journey within the Rubik's Cube.

### Controls & Input Feedback

- The game will provide clear and concise feedback for player inputs, with visual and auditory cues for actions such as collecting colors, switching dimensions, and solving puzzles. This feedback will be consistent across the game's evolving visual styles. 

  - **Movement**: Players will use arrow keys or WASD to move the protagonist. The game will provide responsive visual feedback, with the character smoothly moving in the desired direction and animations of four frames (different pose). Auditory feedback and animations will come along, like when hitting the wall.

  - **Pickups**: Many abilities will unlock with pickups, adding more in game shortcut keys.


### Camera & Perspective

- The camera perspective in Rubik's Evo Portaland will primarily be a 2D side-scrolling view, with occasional top-down perspectives for specific levels and puzzles. The camera will smoothly transition between dimensions and levels, maintaining a clear and consistent view of the gameplay.

  - **Camera Transitions**: As players switch dimensions or move to different levels, the camera will smoothly pan or fade between the scenes, ensuring an uninterrupted gameplay experience.
- **Fake 3D**: In some of the scenes, the player will play in fake 3d.

### UI Elements & Visuals

- The game's UI elements will adhere to the retro pixel art style, with buttons and menus that match the current color scheme. Special modes and features, such as dimension-switching and color-based progression, will be visually represented within the UI to provide clear guidance for the player.

  - **Color Representation**: The protagonist's shell will display the collected colors, serving as a visual indicator of player progress. As new colors are collected, the shell will evolve, showcasing the player's achievements.

  - **Dimension Indicator**: TO FILL (Later pickup)

### Controls Mapping & Settings

- The control scheme for Rubik's Evo Portaland will be simple and intuitive, with keyboard and/or gamepad support. Players will be able to customize their controls through an in-game menu, which will be introduced later in the game as a pickup item.

  - **Video Settings**: Once unlocked, the game's settings menu will allow players to adjust the display from 2 bit to 4 bit and finally 8 bit or 16 bit.

### Loading Screens & Transitions

- Loading screens and transitions will feature artwork and animations that showcase the game's evolving visual style and color schemes. Tips and hints may be displayed during these moments to assist players in their journey through the Rubik's Cube world.

  - **Hints and Tips**: Loading screens may occasionally display context-specific hints or tips, providing players with useful information about the current level or puzzle.

  - **Transition Effects**: The game will utilize visually appealing transition effects, such as fading, sliding, or pixelating, to smoothly switch between different dimensions, levels, or game states. These effects will be designed to complement the game's retro aesthetic and maintain a cohesive visual experience.