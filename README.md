# rubik-s-evo-portaland

### About the project
This project is an experiment to use AIGC technologies to automate some parts in game creation. After trying with different open source game engines, I ended up going with retro & pixel games because theoretically any assets or element in the game can be represented by text, and therefore the state-of-the-art AI technologies can better handle them.

The game uses [pyxel](https://github.com/kitao/pyxel) engine, which is an open source retro game engine for python. It worked pretty well. Meanwhile, surprisingly, it used rust to build the core lib.

Regarding the game - the majority of the system & code are generated and tuned (85%+). Some are borrowed from existing open sourced pyxel games.

Regarding assets - some assets are borrowed, some are generated. 

### Folder Structure
```
├─docs
│  ├─project_definition: GDD & Concept Doc (Chat with Intelligent Assistant [Another Ongoing Project] & Created)
│  └─workers: Some typical examples of how I generated assets / code / etc.
│      └─Personas: Worker persona settings
├─python
│  ├─assets: resources
│  ├─build
│  │  └─python
│  ├─levels: simple level files
│  │  └─__pycache__
│  ├─misc
│  ├─modules: modules
│  │  └─__pycache__
│  ├─pseudo_code: The AI coder first generated pseudo code, and then generates actual code 
│  ├─tests: The AI code has to bypass tests (for the first few modules... I didn't have time to ask them to do all)
│  │  └─__pycache__
│  └─__pycache__
├─tools: asset conversion tools
├─wasm: wasm host 
```

### How to play
https://wdandanw.github.io/rubik-s-evo-portaland/wasm/game.html -> Play online
https://wdandanw.github.io/rubik-s-evo-portaland/wasm/editor.html -> Edit assets online

Or:
1. Clone the repo
2. install pyxel, as instructed by https://github.com/kitao/pyxel
3. Install any other missing dependencies (not sure how many... but shouldn't be a lot)
4. go to folder "python" and `pyxel run main.py` or `python main.py`

### Current Game
- The majority are the systems, and lots of the systems are unused.
- 3 levels. 1 ray casting level indicating dropping from 3d to 2d, 1 pickup demo level (also indicating first evolve), and 1 unfishied easter egg lobby level.

### The findings / takeaways from the project
1. AI is capable to perform high-level jobs with decent quality (like system architecture). For more detailed tasks, it needs more speicifc information (domain knowledge)
2. AI can help with reducing lots of development costs and the quality is decent
3. There needs to be unified supports in the future with framework agnostic solutions so they can be reused / open source / shared to others
